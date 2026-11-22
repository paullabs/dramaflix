"use client";

import { useSyncExternalStore } from "react";

const nada = () => () => {};

/** true só no navegador (depois da hidratação) — para portais. */
export function useNoNavegador() {
  return useSyncExternalStore(
    nada,
    () => true,
    () => false,
  );
}

function useMediaQuery(query: string) {
  return useSyncExternalStore(
    (avisar) => {
      const mq = window.matchMedia(query);
      mq.addEventListener("change", avisar);
      return () => mq.removeEventListener("change", avisar);
    },
    () => window.matchMedia(query).matches,
    () => false,
  );
}

export function useReducedMotion() {
  return useMediaQuery("(prefers-reduced-motion: reduce)");
}

/** true quando o aparelho tem mouse de verdade (hover + ponteiro fino) e tela larga. */
export function usePodeHover() {
  return useMediaQuery("(hover: hover) and (pointer: fine) and (min-width: 960px)");
}

/** true depois que a página rolou além de `limite` px. */
export function useRolou(limite = 24) {
  return useSyncExternalStore(
    (avisar) => {
      window.addEventListener("scroll", avisar, { passive: true });
      return () => window.removeEventListener("scroll", avisar);
    },
    () => window.scrollY > limite,
    () => false,
  );
}
