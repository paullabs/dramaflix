// Nome PROVISÓRIO da plataforma — trocar quando a marca for definida.
export const MARCA = {
  nome: "DRAMA",
  provisoria: true,
} as const;

export const cx = (...classes: Array<string | false | null | undefined>) =>
  classes.filter(Boolean).join(" ");
