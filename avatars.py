import random


template: str = '''
<svg width="80" height="80" xmlns="http://www.w3.org/2000/svg">
    {circle}
    {face}
</svg>
'''

circle: str = '<circle r="40" cx="40" cy="40" fill="#{bgColor}"/>'
face: str = '''
    <g transform="translate({faceX}, {faceY}) scale(2)">
        <path d="M4 10c{bezier}" stroke="#{faceColor}" fill="none" stroke-linecap="round"></path>
        <rect x="{leX}" y="{leY}" width="1.5" height="2" rx="1" stroke="none" fill="#{faceColor}"></rect>
        <rect x="{reX}" y="{reY}" width="1.5" height="2" rx="1" stroke="none" fill="#{faceColor}"></rect>
    </g>
'''

colors: list[tuple[int, int, int]] = [
    (255, 212, 120),
    (255, 125, 122),
    (122, 164, 255),
    (122, 209, 255),
    (122, 255, 213),
    (213, 122, 255),
    (164, 255, 122),
    (122, 164, 255),
    (213, 122, 255),
    (122, 255, 147),
    (122, 164, 255),
    (255, 122, 231),
]

TRIGGER: int = 200

def isDark(color: tuple[int, int, int]) -> bool:
    luminance = 0.2126*color[0] + 0.7152*color[1] + 0.0722*color[2]
    return luminance <= 190

def genAvatar(bgColor: str, faceColor: str, eyesSpace: int, eyesY: int, faceX: int, faceY: int, mouthBezier: str = '2 1 4 1 6 0') -> str:
    avatarCircle = circle.format(bgColor=bgColor)
    
    eyesCenter = (eyesSpace * 8 + 4) / 2

    avatarFace = face.format(
        faceX = faceX * 39 + 7,
        faceY = faceY * 40 + 7,
        leX = 6 - eyesCenter,
        leY = 2 + eyesY * 4,
        reX = 6 + eyesCenter,
        reY = 2 + eyesY * 4,
        faceColor = faceColor,
        bezier=mouthBezier
    )

    return template.format(circle=avatarCircle, face=avatarFace)

def changeColor(v: int) -> int:
    v = v + random.random() * 30 - 15
    if v > 255:
        v = 255
    elif v < 0:
        v = 0
    return v

def randAvatar() -> str:
    color: tuple[int, int, int] = random.choice(colors)
    color: tuple[int, int, int] = (
        int(changeColor(color[0])),
        int(changeColor(color[1])),
        int(changeColor(color[2])),
    )

    dark: bool = isDark(color)
    color: str = ''.join(hex(int(n))[2] for n in color)

    firstPoint: str = f'{random.randint(0, 3)} {random.randint(1, 2)}'
    secondPoint: str = f'{random.randint(3, 6)} {random.randint(1, 2)}'

    return genAvatar(
        bgColor=color,
        faceColor='EFEFEF' if dark else '010101',
        eyesSpace=random.random(),
        eyesY=random.random(),
        faceX=random.random(),
        faceY=random.random(),
        mouthBezier=f'{firstPoint} {secondPoint} 6 0'
    )

if __name__ == '__main__':
    with open("face.svg", 'w') as f:
        f.write(randAvatar())
