// Ícones do site. Dois papéis, duas bibliotecas (ver scripts/gerar_icones.mjs):
//  - Solar "Bold Duotone": lugares, categorias e estados (duas camadas, a de trás a 50%).
//  - Phosphor "Fill/Bold": ações dentro de botões (play, +, ✓, fechar, setas).
// A moeda é desenho próprio: um disco com o "play" no meio, a marca da moeda da plataforma.
import type { SVGProps } from "react";
import { ICONES, type NomeIcone } from "./icones.gerado";

type IconProps = Omit<SVGProps<SVGSVGElement>, "children" | "dangerouslySetInnerHTML"> & { size?: number };

function Icone({ nome, size = 24, ...rest }: IconProps & { nome: NomeIcone }) {
  const { body, v } = ICONES[nome];
  return (
    <svg
      width={size}
      height={size}
      viewBox={`0 0 ${v} ${v}`}
      aria-hidden="true"
      focusable="false"
      {...rest}
      // corpo estático, gerado das bibliotecas no build (nenhum dado do usuário)
      dangerouslySetInnerHTML={{ __html: body }}
    />
  );
}

/* ---------- lugares, categorias e estados (Solar) ---------- */
export const IconHome = (p: IconProps) => <Icone nome="inicio" {...p} />;
export const IconFeed = (p: IconProps) => <Icone nome="paraVoce" {...p} />;
export const IconFlame = (p: IconProps) => <Icone nome="emAlta" {...p} />;
export const IconBookmark = (p: IconProps) => <Icone nome="lista" {...p} />;
export const IconBookmarkCheck = (p: IconProps) => <Icone nome="listaSalvo" {...p} />;
export const IconSearch = (p: IconProps) => <Icone nome="buscar" {...p} />;
export const IconUser = (p: IconProps) => <Icone nome="perfil" {...p} />;
export const IconHelp = (p: IconProps) => <Icone nome="ajuda" {...p} />;
export const IconInfo = (p: IconProps) => <Icone nome="info" {...p} />;
export const IconLock = (p: IconProps) => <Icone nome="cadeado" {...p} />;
export const IconUnlock = (p: IconProps) => <Icone nome="cadeadoAberto" {...p} />;
export const IconGift = (p: IconProps) => <Icone nome="presente" {...p} />;
export const IconCrown = (p: IconProps) => <Icone nome="coroa" {...p} />;
export const IconClock = (p: IconProps) => <Icone nome="relogio" {...p} />;
export const IconMic = (p: IconProps) => <Icone nome="microfone" {...p} />;
export const IconTranslate = (p: IconProps) => <Icone nome="idioma" {...p} />;
export const IconEpisodios = (p: IconProps) => <Icone nome="episodios" {...p} />;
export const IconHistory = (p: IconProps) => <Icone nome="historico" {...p} />;
export const IconStars = (p: IconProps) => <Icone nome="estrelas" {...p} />;
export const IconMoneyBag = (p: IconProps) => <Icone nome="dinheiro" {...p} />;
export const IconBolt = (p: IconProps) => <Icone nome="raio" {...p} />;
export const IconGhost = (p: IconProps) => <Icone nome="fantasma" {...p} />;
export const IconRomance = (p: IconProps) => <Icone nome="romance" {...p} />;
export const IconLaugh = (p: IconProps) => <Icone nome="risada" {...p} />;
export const IconSun = (p: IconProps) => <Icone nome="sol" {...p} />;
export const IconMoon = (p: IconProps) => <Icone nome="lua" {...p} />;
export const IconTv = (p: IconProps) => <Icone nome="tv" {...p} />;
export const IconRanking = (p: IconProps) => <Icone nome="ranking" {...p} />;
export const IconWallet = (p: IconProps) => <Icone nome="carteira" {...p} />;

/* ---------- ações (Phosphor) ---------- */
export const IconPlay = (p: IconProps) => <Icone nome="play" {...p} />;
export const IconPause = (p: IconProps) => <Icone nome="pausa" {...p} />;
export const IconPlus = (p: IconProps) => <Icone nome="mais" {...p} />;
export const IconCheck = (p: IconProps) => <Icone nome="check" {...p} />;
export const IconClose = (p: IconProps) => <Icone nome="fechar" {...p} />;
export const IconChevronLeft = (p: IconProps) => <Icone nome="esquerda" {...p} />;
export const IconChevronRight = (p: IconProps) => <Icone nome="direita" {...p} />;
export const IconChevronUp = (p: IconProps) => <Icone nome="cima" {...p} />;
export const IconChevronDown = (p: IconProps) => <Icone nome="baixo" {...p} />;
export const IconArrowLeft = (p: IconProps) => <Icone nome="voltar" {...p} />;
export const IconShare = (p: IconProps) => <Icone nome="enviar" {...p} />;
export const IconThumb = (p: IconProps) => <Icone nome="gostei" {...p} />;
export const IconList = (p: IconProps) => <Icone nome="grade" {...p} />;
export const IconHeart = ({ cheio, ...p }: IconProps & { cheio?: boolean }) => <Icone nome={cheio ? "coracaoCheio" : "coracao"} {...p} />;

/* ---------- player (Phosphor) ---------- */
export const IconVolume = ({ mudo, ...p }: IconProps & { mudo?: boolean }) => <Icone nome={mudo ? "somDesligado" : "somLigado"} {...p} />;
export const IconTelaCheia = ({ sair, ...p }: IconProps & { sair?: boolean }) => <Icone nome={sair ? "sairTelaCheia" : "telaCheia"} {...p} />;
export const IconVelocidade = (p: IconProps) => <Icone nome="velocidade" {...p} />;
export const IconAcelerar = (p: IconProps) => <Icone nome="acelerar" {...p} />;
export const IconRepetir = (p: IconProps) => <Icone nome="repetir" {...p} />;
export const IconProximo = (p: IconProps) => <Icone nome="proximo" {...p} />;

/* ---------- moeda (desenho próprio, no mesmo duotone do Solar) ---------- */
export const IconCoin = ({ size = 24, ...p }: IconProps) => (
  <svg width={size} height={size} viewBox="0 0 24 24" aria-hidden="true" focusable="false" {...p}>
    <circle cx="12" cy="12" r="10" fill="currentColor" opacity=".5" />
    <circle cx="12" cy="12" r="7.1" fill="none" stroke="currentColor" strokeWidth="1.5" />
    <path fill="currentColor" d="M10.3 9.06v5.88c0 .52.57.84 1.01.56l4.55-2.94a.66.66 0 0 0 0-1.12L11.3 8.5a.66.66 0 0 0-1.01.56Z" />
  </svg>
);
