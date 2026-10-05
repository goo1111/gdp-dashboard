import type { ButtonHTMLAttributes } from 'react';
import './Button.css';

/**
 * Button — Figma: Components/Button
 *
 * | Figma 프로퍼티        | props                          |
 * | --------------------- | ------------------------------ |
 * | Style=Primary         | variant="primary"              |
 * | Style=Secondary       | variant="secondary"            |
 * | Size=Large / Medium   | size="lg" / size="md"          |
 * | State=Disabled        | disabled                       |
 * | Label (Text)          | label                          |
 *
 * 색·크기·모서리·글자는 design-tokens.css의 Semantic 토큰만 쓴다.
 */
export type ButtonVariant = 'primary' | 'secondary';
export type ButtonSize = 'lg' | 'md';

export interface ButtonProps extends Omit<ButtonHTMLAttributes<HTMLButtonElement>, 'children'> {
  label: string;
  variant?: ButtonVariant;
  size?: ButtonSize;
  fullWidth?: boolean;
}

export function Button({
  label,
  variant = 'primary',
  size = 'lg',
  fullWidth = false,
  type = 'button',
  className,
  ...rest
}: ButtonProps) {
  const classes = ['ds-button', `ds-button--${variant}`, `ds-button--${size}`, fullWidth && 'ds-button--full', className]
    .filter(Boolean)
    .join(' ');
  return (
    <button type={type} className={classes} {...rest}>
      {label}
    </button>
  );
}

export default Button;
