"""v72 → v73: 키보드로 기록하기(P0) + 문구 정리(브랜드명·해요체·띄어쓰기)
사용법: python3 tools/build_v73.py <출력.html> <v72.html>"""
import sys
OUT, SRC = sys.argv[1], sys.argv[2]
t = open(SRC, encoding='utf-8').read()
def rep(old, new, count):
    global t
    n = t.count(old); assert n == count, (old[:70], n, count); t = t.replace(old, new)

rep('<title>감정일기 v72</title>', '<title>감정일기 v73</title>', 1)

# ---------- P0: 키보드로 감정 고르기 ----------
HELPER = '''<script id="a11y-helpers">
/* 키보드·스크린리더 보조: 시트(대화상자) 열릴 때 첫 버튼으로 포커스, Tab은 시트 안에서만, Esc로 닫고 마음 지도로 복귀 */
window.APP_A11Y={
  focusable:function(root){return [].slice.call(root.querySelectorAll('button:not([disabled]),input,textarea,select,[href],[tabindex]:not([tabindex="-1"])')).filter(function(e){return e.offsetParent!==null})},
  focusFirst:function(el,key){if(!el||el.dataset.focusKey===String(key))return;el.dataset.focusKey=String(key);setTimeout(function(){var f=APP_A11Y.focusable(el);if(f[0])f[0].focus({preventScroll:true})},0)},
  sheetKeys:function(ev,close){
    if(ev.key==='Escape'){ev.preventDefault();close();setTimeout(function(){var c=document.querySelector('.app-home-compass-v43');if(c)c.focus()},0);return}
    if(ev.key!=='Tab')return;var s=ev.currentTarget.querySelector('[role=dialog]');if(!s)return;var f=APP_A11Y.focusable(s);if(!f.length)return;
    var first=f[0],last=f[f.length-1];
    if(ev.shiftKey&&(document.activeElement===first||!s.contains(document.activeElement))){ev.preventDefault();last.focus()}
    else if(!ev.shiftKey&&(document.activeElement===last||!s.contains(document.activeElement))){ev.preventDefault();first.focus()}
  }
};
</script>
'''
rep('<script id="emotion-tokens">', HELPER + '<script id="emotion-tokens">', 1)

# 마음 지도: Tab으로 도달, Enter/Space로 목록 시트 열기
rep("h('div',{className:'app-home-compass-v43',onPointerUp:compassPick},",
    "h('div',{className:'app-home-compass-v43',onPointerUp:compassPick,tabIndex:0,role:'button','aria-haspopup':'dialog',"
    "'aria-label':step===1?'마음 지도. Enter를 눌러 감정 목록에서 고르기':'세부 감정 지도. Enter를 눌러 목록에서 고르기',"
    "onKeyDown:function(ev){if(ev.key==='Enter'||ev.key===' '){ev.preventDefault();setModal(true)}}},", 2)

# 감정 시트: 대화상자 + 포커스 이동 + Esc + 포커스 가두기
rep("h('div',{className:'app-home-modal-v43',onPointerUp:function(){setModal(false)}},h('section',{onPointerUp:function(ev){ev.stopPropagation()}},",
    "h('div',{className:'app-home-modal-v43',onPointerUp:function(){setModal(false)},onKeyDown:function(ev){APP_A11Y.sheetKeys(ev,function(){setModal(false)})}},"
    "h('section',{role:'dialog','aria-modal':'true','aria-label':step===1?'감정 고르기':'세부 감정 고르기',ref:function(el){APP_A11Y.focusFirst(el,step)},onPointerUp:function(ev){ev.stopPropagation()}},", 2)

# 3단계: 본문 입력칸으로 바로 포커스
rep("h('textarea',{'aria-label':'오늘의 한 문장',value:journal,", "h('textarea',{'aria-label':'오늘의 한 문장',autoFocus:true,value:journal,", 2)

# ---------- 문구 ----------
rep('감정 로그 이용 원칙', '감정일기 이용 원칙', 2)
rep('"감정 로그 모바일 프로토타입"', '"감정일기 모바일 프로토타입"', 1)
rep('감정 로그는 감정을 진단하거나 기록을 강요하지 않습니다. 선택한 감정을 문장과 창작물로 표현하고, 날짜별로 다시 볼 수 있도록 연결합니다.',
    '감정일기는 감정을 진단하거나 기록을 강요하지 않아요. 고른 감정을 문장과 창작물로 표현하고, 날짜별로 다시 볼 수 있게 이어 줘요.', 1)
rep('감정 로그는 기록을 강요하거나 감정을 진단하지 않아요. 사용자가 남긴 감정을 작품과 캐릭터로 표현하고 안전하게 보관하는 데 집중합니다.',
    '감정일기는 기록을 강요하거나 감정을 진단하지 않아요. 남긴 감정을 작품과 캐릭터로 표현하고 안전하게 보관하는 데 집중해요.', 1)
rep('변경한 설정은 이 기기에 바로 저장됩니다.', '바꾼 설정은 이 기기에 바로 저장돼요.', 1)
rep('저장 방식만 관리하며 기록 자체를 삭제하지 않습니다.', '저장 방식만 바꾸고, 남긴 기록은 지우지 않아요.', 1)
rep('기록은 현재 기기에 저장됩니다', '기록은 이 기기에만 저장돼요', 1)
rep('이 프로토타입은 입력한 감정 기록과 창작물을 브라우저의 로컬 저장소에 보관합니다. 외부 전송이나 계정 간 동기화는 아직 포함하지 않았습니다.',
    '이 프로토타입은 남긴 감정 기록과 창작물을 브라우저 저장소에 보관해요. 외부로 보내거나 다른 기기와 동기화하는 기능은 아직 없어요.', 1)
rep('공통 흐름을 확인합니다.', '공통 흐름을 확인해요.', 1)
rep('다음 작업에서 색상\\xB7제목\\xB7레이아웃 편집을 연결합니다.', '다음 작업에서 색상\\xB7제목\\xB7레이아웃 편집을 연결해요.', 1)
rep('연결된 화면을 확인하는 프로토타입입니다.', '연결된 화면을 확인하는 프로토타입이에요.', 1)
rep('비어있어요', '비어 있어요', 2)

open(OUT, 'w', encoding='utf-8').write(t)
print('ok')
