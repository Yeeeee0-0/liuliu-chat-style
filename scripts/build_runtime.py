"""Build one startup prompt from the maintained role rules and adapter block."""
import argparse
from pathlib import Path

def render(root):
    role=(root/'references'/'口吻规则.md').read_text(encoding='utf-8').strip()
    adapter=(root/'references'/'QQ接入约定.md').read_text(encoding='utf-8')
    start='<!-- RUNTIME_START -->';end='<!-- RUNTIME_END -->'
    if adapter.count(start)!=1 or adapter.count(end)!=1:
        raise ValueError('Expected exactly one runtime block')
    block=adapter.split(start,1)[1].split(end,1)[0].strip()
    return '六六完整运行提示词 v1.0｜启动时加载，当前规则优先于旧聊天示范\n\n'+role+'\n\n'+block+'\n'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[1]
    target=root/'assets'/'六六系统提示词.txt'
    expected=render(root)
    if args.check:
        if not target.exists() or target.read_text(encoding='utf-8')!=expected:
            parser.exit(1,'Runtime prompt is missing or stale\n')
        print('Runtime prompt is consistent')
    else:
        target.parent.mkdir(exist_ok=True)
        target.write_text(expected,encoding='utf-8')
        print('Built runtime prompt: '+str(target))

if __name__=='__main__':main()
