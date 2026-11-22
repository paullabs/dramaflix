"use client";

import { createContext, useCallback, useContext, useEffect, useMemo, useRef, useState } from "react";
import { destaques } from "@/data/catalogo";
import { alternarLista as alternarListaArmazenada } from "@/lib/estado";

type Modal = { id: string; episodio?: number } | null;

/** O ícone do aviso diz o que aconteceu antes mesmo de ler o texto. */
export type TipoToast = "lista" | "listaFora" | "curtida" | "moedas" | "vip" | "desbloqueio" | "link" | "emBreve" | "info";
export interface Aviso {
  id: number;
  msg: string;
  tipo: TipoToast;
}

interface AppContextValue {
  /** título que pinta o fundo ambiente */
  ambienteId: string;
  setDestaqueId: (id: string) => void;

  modal: Modal;
  abrirModal: (id: string, episodio?: number) => void;
  fecharModal: () => void;

  toast: Aviso | null;
  mostrarToast: (msg: string, tipo?: TipoToast) => void;

  /** adiciona/remove da Minha lista e avisa */
  alternarLista: (id: string) => void;
}

// Valor padrão inofensivo: permite que um trecho seja renderizado isolado (ex.: na validação
// de navegação instantânea do Next em desenvolvimento) sem quebrar.
const nada = () => {};
const padrao: AppContextValue = {
  ambienteId: destaques[0],
  setDestaqueId: nada,
  modal: null,
  abrirModal: nada,
  fecharModal: nada,
  toast: null,
  mostrarToast: nada,
  alternarLista: nada,
};

const AppContext = createContext<AppContextValue>(padrao);

export function useApp() {
  return useContext(AppContext);
}

export function AppProvider({ children }: { children: React.ReactNode }) {
  const [destaqueId, setDestaqueId] = useState(destaques[0]);
  const [modal, setModal] = useState<Modal>(null);
  const [toast, setToast] = useState<Aviso | null>(null);
  const toastTimer = useRef<number | undefined>(undefined);

  const mostrarToast = useCallback((msg: string, tipo: TipoToast = "info") => {
    setToast({ id: Date.now(), msg, tipo });
    window.clearTimeout(toastTimer.current);
    toastTimer.current = window.setTimeout(() => setToast(null), 2600);
  }, []);

  const alternarLista = useCallback(
    (id: string) => {
      const ficou = alternarListaArmazenada(id);
      mostrarToast(ficou ? "Na Minha lista" : "Fora da lista", ficou ? "lista" : "listaFora");
    },
    [mostrarToast],
  );

  const abrirModal = useCallback((id: string, episodio?: number) => setModal({ id, episodio }), []);
  const fecharModal = useCallback(() => setModal(null), []);

  useEffect(() => () => window.clearTimeout(toastTimer.current), []);

  const value = useMemo<AppContextValue>(
    () => ({
      ambienteId: modal?.id ?? destaqueId,
      setDestaqueId,
      modal,
      abrirModal,
      fecharModal,
      toast,
      mostrarToast,
      alternarLista,
    }),
    [destaqueId, modal, abrirModal, fecharModal, toast, mostrarToast, alternarLista],
  );

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
}
