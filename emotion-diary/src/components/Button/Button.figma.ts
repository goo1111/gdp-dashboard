// url=https://www.figma.com/design/mxyAXz6tmrsxaYbRRwXTUu?node-id=4-19
// source=emotion-diary/src/components/Button/Button.tsx
// component=Button
// Code Connect는 Figma Organization/Enterprise 플랜 + 라이브러리 게시가 필요하다 (현재 L&P 팀은 Professional).
import figma from 'figma'
const instance = figma.selectedInstance

const label = instance.getString('Label')
const variant = instance.getEnum('Style', {
  'Primary': 'primary',
  'Secondary': 'secondary',
})
const size = instance.getEnum('Size', {
  'Large': 'lg',
  'Medium': 'md',
})
const disabled = instance.getEnum('State', {
  'Default': false,
  'Disabled': true,
})

export default {
  example: figma.code`<Button
  label="${label}"
  variant="${variant}"
  size="${size}"
  ${disabled ? 'disabled' : ''}
/>`,
  imports: ['import { Button } from "./components/Button"'],
  id: 'button',
  metadata: { nestable: true },
}
