exec(open('newslides.py').read().split('# ---------- 11 Design System ----------')[0])
steps=[('01','사용성 테스트','다음 버전 전',['참가자 3명 · 1인 30분 · Think-aloud','과업 4개: 기록하기 · 홈 이해 · 돌아보기 · 작품 만들기']),
       ('02','반복 문제 개선','테스트 직후',['2명 이상 반복된 문제부터 수정','행동 → 발언 → 원인 → UI 개선 → 다시 확인']),
       ('03','출시 후 측정','공개 이후',['작품을 만든 사용자와 만들지 않은 사용자의','다시 기록하는 비율 비교'])]
st=''.join(f'<div class="st"><div class="sh"><span class="chip">{a}</span><small>{c}</small></div><b>{b}</b>'+''.join(f'<p>{x}</p>' for x in d)+'</div>'+('<i class="ar">›</i>' if a!='03' else '') for a,b,c,d in steps)
mets=[('사용성','2 / 3명','과업 1 · 4를 도움 없이 완료','기록 3단계와 작품 만들기를 혼자 끝내는가'),
      ('핵심 가치','2 / 3명','"기존 일기 앱과 다르다"고 답함','기록이 작품으로 남는 경험이 차이로 느껴지는가'),
      ('지속','3.3% ↑','30일 뒤에도 기록하는 사용자','02장의 업계 중앙값보다 높이는 것이 목표')]
mt=''.join(f'<div class="m"><small>{a}</small><b>{b}</b><p>{c}</p><span>{d}</span></div>' for a,b,c,d in mets)
css='''.lb{margin-top:28px;font-size:12.5px;font-weight:700;color:#5a4ab3;letter-spacing:.04em}
.steps{margin-top:10px;display:grid;grid-template-columns:1fr 24px 1fr 24px 1fr;align-items:center}
.st{border-radius:18px;background:#fff;box-shadow:0 16px 36px -26px rgba(60,40,90,.3),0 0 0 1px rgba(0,0,0,.035);padding:22px 24px;height:182px}
.sh{display:flex;justify-content:space-between;align-items:center}.sh small{font-size:12px;color:var(--ink3);font-weight:600;letter-spacing:0}
.st b{display:block;margin:10px 0 6px;font-size:17px;font-weight:700;letter-spacing:-.04em}.st p{font-size:13px;line-height:1.55;color:var(--ink2);font-weight:500}
.ar{font-style:normal;text-align:center;color:#b3a8e8;font-size:22px;font-weight:700}
.ms{margin-top:10px;display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.m{border-radius:18px;background:#f8f7fc;border:1px solid #ebe7f6;padding:22px 24px;height:216px}
.m small{font-size:12px;font-weight:700;color:var(--ink3);letter-spacing:0}.m b{display:block;margin-top:6px;font-size:38px;font-weight:700;color:#5a4ab3;letter-spacing:-.04em;line-height:1.1}
.m p{margin-top:8px;font-size:15px;font-weight:700;color:var(--ink)}.m span{display:block;margin-top:4px;font-size:12.5px;color:var(--ink2);font-weight:500}'''
body=f'<div class="lb">검증 단계</div><div class="steps">{st}</div><div class="lb" style="margin-top:28px">성공 지표</div><div class="ms">{mt}</div>'
s=slide('감정로그 · Next Step','Deliver · Validation Plan &amp; Next Step','다음 단계는, 작품이 돌아올 때 사용자가 <em>다시 기록하는지</em> 확인하는 것입니다.',
 '아직 사용자 테스트 전입니다. <b>3명 사용성 테스트로 흐름을 다듬고</b>, 출시 후에는 지표로 "계속 기록하는가"를 검증합니다.',body,
 '이 프로젝트의 질문은 하나입니다 — <b>기록이 작품으로 돌아오면, 사람들은 다시 기록하는가.</b>',css)
open('s13v.html','w').write(s);print('ok')
