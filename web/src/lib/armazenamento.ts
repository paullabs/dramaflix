"use client";

import { useSyncExternalStore } from "react";

/**
 * Pequeno armazenamento local (localStorage) com assinatura para o React.
 * Serve para o protótipo funcionar sem backend: Minha lista, carteira de moedas, VIP e curtidas.
 * Se o navegador bloquear o localStorage, os dados ficam só na memória da aba.
 */
/** Funções que zeram cada armazenamento criado (usado por "Recomeçar"). */
const zeradores = new Set<() => void>();

/** Apaga tudo o que o app guardou neste aparelho e avisa as telas na hora. */
export function apagarTudo() {
  zeradores.forEach((zerar) => zerar());
}

export function criarArmazenamento<T extends object>(chave: string, padrao: T) {
  const ouvintes = new Set<() => void>();
  let cacheBruto: string | null | undefined;
  let cacheValor: T = padrao;
  let memoria: T | null = null;

  function ler(): T {
    if (memoria) return memoria;
    let bruto: string | null = null;
    try {
      bruto = window.localStorage.getItem(chave);
    } catch {
      /* armazenamento indisponível */
    }
    if (bruto !== cacheBruto) {
      cacheBruto = bruto;
      try {
        cacheValor = bruto ? { ...padrao, ...(JSON.parse(bruto) as Partial<T>) } : padrao;
      } catch {
        cacheValor = padrao;
      }
    }
    return cacheValor;
  }

  function gravar(novo: T) {
    try {
      window.localStorage.setItem(chave, JSON.stringify(novo));
    } catch {
      memoria = novo;
    }
    ouvintes.forEach((avisar) => avisar());
  }

  function assinar(avisar: () => void) {
    ouvintes.add(avisar);
    const aoMudarEmOutraAba = (e: StorageEvent) => {
      if (e.key === chave) avisar();
    };
    window.addEventListener("storage", aoMudarEmOutraAba);
    return () => {
      ouvintes.delete(avisar);
      window.removeEventListener("storage", aoMudarEmOutraAba);
    };
  }

  function zerar() {
    try {
      window.localStorage.removeItem(chave);
    } catch {
      /* armazenamento indisponível */
    }
    memoria = null;
    ouvintes.forEach((avisar) => avisar());
  }
  zeradores.add(zerar);

  function useValor(): T {
    return useSyncExternalStore(assinar, ler, () => padrao);
  }

  return { ler, gravar, useValor };
}
