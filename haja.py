_a = {}

_a['globals'] = globals()
from sys import stdin
_a['stdin'] = stdin
del stdin

a = {}

a['_EXTERNAL'] = '_a'

a['_SELF'] = a

# A REGISTER: ARIADNE IS REQUESTING FULL ATTENTION OF THE PROCESSOR
a['_ATTN'] = [False]

a['_BACK_STACK'] = [] # USED BY { BACK } AND { FORTH }

a['_DATA'] = {} # DATA FIELDS FOR WORDS HAVING DATA

a['_DICTIONARY'] = {}

a['_INPUTS'] = [lambda x: eval(x['_EXTERNAL'])['stdin']]
a['_INPUT_FILES'] = [None]

a['_Python'] = {}

a['_Python']['_DEFAULT'] = ''

a['_Python']['_RDEFAULT'] = ('QUERY',)

a['_WORD_UNDER_CONSTRUCTION'] = [None]

from collections import deque
a['_INPUT_BUFFER'] = deque()
del deque

#ALIASES
a['in'] = a['_INPUT_BUFFER']
a[ 'd'] = a['_DICTIONARY']



def _include(x, obj, name=None):
    name = getattr(obj, '__name__') if name is None else name
    x['_Python'][name] = obj

a['_include'] = _include
del _include



def expand(x, NAME, name=None):
    name = NAME.lower() if name is None else name
    x['_DICTIONARY'].update({ NAME: lambda y: y['_Python'][name](y) })

a['_include'](a, expand)
a['_expand'] = expand
del expand



def echo(*args, prompt='1>>'):
    '''for debugging.
    '''
    print(prompt, *args)

a['_include'](a, echo)
del echo



def nop(x): # FOR TESTING, ETC.
    pass

a['_include'](a, nop)
a['_expand'](a, 'NOP')
del nop



def if_(x):
    PY = x['_Python']
    if not bool(PY['drop'](x)):
        PY['rdrop'](x) # DROP { IF } ITSELF
        PY['rdrop'](x) # DROP THE CALLER OF { IF }

a['_include'](a, if_, 'if')
a['_expand'](a, 'IF')
del if_



def ebb(x):
    x['_Python']['rdrop'](x) # DROP { EBB } ITSELF
    R = x['_RETURN_STACK']
    R['TOP'][0] = len(R['SUB'])

a['_include'](a, ebb)
a['_expand'](a, 'EBB')
del ebb



def _populatereturnstack(x):
    y = x['_Python']['_RDEFAULT']
    R = x['_RETURN_STACK']
    R['TOP'][0] = len(y)
    R['SUB'][0] = y

a['_include'](a, _populatereturnstack)

del _populatereturnstack



def _rclear(x):
    x['_RETURN_STACK'] = {
        'TOP': [None], 'SUB': [None], 'REST': [] }
    x['_Python']['_populatereturnstack'](x)

a['_include'](a, _rclear)

del _rclear



def rest(x):
    PY = x['_Python']
    PY['push'](x, PY['drop'](x)[1:])

a['_include'](a, rest)
a['_expand'](a, 'REST')
del rest



def _cold(x):
    PY = x['_Python']
    PY['_clear'](x)
    PY['_rclear'](x)
    x.update({
        'py': x['_Python'],
        'r': x['_RETURN_STACK'],
        's': x['_DATA_STACK'] })

a['_include'](a, _cold)

del _cold



def push(x, obj):
    S = x['_DATA_STACK']
    S['REST'].append(S['SUB'][0])
    S['SUB'][0] = S['TOP'][0]
    S['TOP'][0] = obj

a['_include'](a, push)

del push



def drop(x):
    S = x['_DATA_STACK']
    y = S['TOP'][0]
    S['TOP'][0] = S['SUB'][0]
    S['SUB'][0] = \
        x['_Python']['_DEFAULT'] \
        if not S['REST'] else \
        S['REST'].pop()
    return y

a['_Python'].update({ 'drop': drop })
a['_expand'](a, 'DROP')
del drop


def self(x):
    PY = x['_Python']
    PY['push'](x, x['_SELF'])

a['_include'](a, self)
a['_expand'](a, 'SELF')
del self




def pry(x):
    PY = x['_Python']
    index = PY['drop'](x)
    container = PY['drop'](x)
    PY['push'](x, container[index])

a['_include'](a, pry)
a['_expand'](a, ']', 'pry')
del pry



def dropn(x, n):
    from collections import deque
    d = deque()
    for k in range(n):
        d.appendleft(x['_Python']['drop'](x))
    return list(d)

a['_include'](a, dropn)

del dropn



def fimport(x, function=None, as_=''):
    PY = x['_Python']
    if function is None:
        #ASSUMPTION: CALLING FROM FORTH
        function = PY['drop'](x)
        name = PY['drop'](x)
    name = getattr(function, '__name__') if not as_ else as_
    def inner(y):
        PY = y['_Python']
        tuple_, dict_ = PY['drop'](y)
        PY['push'](y, function(*tuple_, **dict_))
    x['_include'](x, inner, name)
    PY['expand'](x, name)

a['_include'](a, fimport)
a['_expand'](a, 'FIMPORT')
del fimport



def eval_(x):
    PY =x['_Python']
    PY['push'](x, eval(
        PY['drop'](x),
        eval(x['_EXTERNAL'])['globals'],
        PY))

a['_include'](a, eval_)
a['_expand'](a, 'EVAL', 'eval_')
del eval_



def exec_(x):
    exec(
        x['_Python']['drop'](x),
        eval(x['_EXTERNAL'])['globals'],
        x['_Python'])

a['_include'](a, exec_)
a['_expand'](a, 'EXEC', 'exec_')
del exec_



def rpush(x, words):
    R = x['_RETURN_STACK']
    R['REST'].append( (R['SUB'][0], R['TOP'][0]) )
    R['SUB'][0] = words
    R['TOP'][0] = len(words)

a['_include'](a, rpush)
del rpush



def rdrop(x):
    R = x['_RETURN_STACK']
    if R['REST']:
        item = R['REST'].pop()
        R['TOP'][0] = item[1]
        R['SUB'][0] = item[0]
    else:
        x['_Python']['_populatereturnstack'](x)

a['_include'](a, rdrop)
del rdrop



def step(x):
    Top = x['_RETURN_STACK']['TOP']
    while Top[0] <= 0:
        x['_Python']['rdrop'](x)
    Top[0] -= 1

a['_include'](a, step)
del step



def opera(x):
    R = x['_RETURN_STACK']
    return R['SUB'][0][R['TOP'][0] - 0]

a['_include'](a, opera)
del opera




def _execute(x):
    '''Not to be confused with Forth { EXECUTE }.
    '''
    PY = x['_Python']
    PY['step'](x)
    WORD = PY['opera'](x)
    D = x['_DICTIONARY']
    if WORD in D:
        D[WORD](x)
    else:
        PY['push'](x, WORD)

a['_include'](a, _execute)
del _execute



def execute(x):
    '''Forth { EXECUTE }.
    '''
    PY = x['_Python']
    WORD = PY['drop'](x)
    D = x['_DICTIONARY']
    if WORD in D:
        PY['rpush'](x, (WORD,))
    else:
        PY['push'](x, WORD)

a['_include'](a, execute)
a['_expand'](a, 'EXECUTE')
del execute



def ddrop(x):
    D = x['_DICTIONARY']
    PY = x['_Python']
    PY['rest'](x)
    K = PY['drop'](x)
    if K in D:
        D.pop(K)
        DA = x['_DATA']
        if K in DA:
            DA.pop(K)

a['_include'](a, ddrop)
a['_expand'](a, 'DDROP')
del ddrop



def defaultlist(x):
    return [x['_Python']['_DEFAULT']]

a['_include'](a, defaultlist)
del defaultlist



def _clear(x):
    x['_DATA_STACK'] = dict(map(
        lambda name: (name, x['_Python']['defaultlist'](x)),
        'TOP SUB REST'.split()))

a['_include'](a, _clear)
a['_expand'](a, 'CLEAR', '_clear')
del _clear



def top4(x):
    '''Return (copies of) the top four elments on the stack.
    '''
    S = x['_DATA_STACK']
    return S['REST'][-2:] + S['SUB'] + S['TOP']

a['_include'](a, top4)
del top4



def _dup(stack):
    stack['REST'].append(stack['SUB'][0])
    stack['SUB'].pop()
    stack['SUB'].append(stack['TOP'][0])

a['_include'](a, _dup)
del _dup



def dup(x):
    x['_Python']['_dup'](x['_DATA_STACK'])

a['_include'](a, dup)
a['_expand'](a, 'DUP')
del dup



def top(x):
    return x['_DATA_STACK']['TOP'][0]

a['_include'](a, top)
del top



def sub(x):
    return x['_DATA_STACK']['SUB'][0]

a['_include'](a, sub)
del sub



def over(x):
    PY = x['_Python']
    S = x['_DATA_STACK']
    PY['dup'](x)
    S['TOP'][0] = S['REST'][-1]

a['_include'](a, over)
a['_expand'](a, 'OVER')
del over



def back(x):
    x['_BACK_STACK'].append( x['_Python']['drop'](x) )

a['_include'](a, back)
a['_expand'](a, 'BACK')
del back



def forth(x):
    PY = x['_Python']
    PY['push'](x,
        PY['_DEFAULT']
        if not x['_BACK_STACK'] else
        x['_BACK_STACK'].pop() )

a['_include'](a, forth)
a['_expand'](a, 'FORTH')
del forth


def readline(x):
    return x['_Python']['push'](x, input())

a['_include'](a, readline)
a['_expand'](a, 'READ')
del readline



def _input(x):
    '''Push a line scanned from stdin.
    '''
    PY = x['_Python']
    PY['echo'](*map(repr, PY['top4'](x)), prompt='S>>')
    PY['push'](x, input('OK> ') + '\n')

a['_include'](a, _input)
del _input



def finput(x, file):
    '''Push a line scanned from file.
    '''
    x['_Python']['push'](x, file.readline())

a['_Python'].update({ 'finput': finput })
del finput



def load(x):
    PY = x['_Python']
    file = open(PY['drop'](x))
    x['_INPUT_FILES'].append(file)
    x['_INPUTS'].append(lambda x: x['_INPUT_FILES'][-1])

a['_include'](a, load)
a['_expand'](a, 'LOAD')
del load



def read(x):
    PY = x['_Python']
    inn = x['_INPUTS']
    file = inn[-1](x)
    if len(inn) < 2: # inn[0] SHOULD BE stdin
        PY['_input'](x)
    else:
        PY['finput'](x, file)
        if not PY['top'](x):
            file.close()
            x['_INPUT_FILES'].pop()
            inn.pop()

a['_Python']['read'] = read
del read



def readRest(x):
    PY = x['_Python']
    file = PY['drop'](x)
    PY['push'](x, ''.join(file))

a['_Python']['readRest'] = readRest
a['_expand'](a, 'READREST', 'readRest')
del readRest



def preprocess(string):
    def whitespaceToSpace(string):
        return ''.join(map(lambda s: ' ' if s.isspace() else s, string))
    def collapseSpaces(string):
        a, b = string, object()
        while a != b:
            b = a
            a = b.replace('  ', ' ')
        return a
    def splitIgnoringGraphicSpace(string):
        _ = '\ue000' # U+E000: FIRST PRIVATE USE CHARACTER
        return tuple(map(
            lambda s: s.replace(_, ' '),
            string.replace('\\ ', _).split()))
    return splitIgnoringGraphicSpace(collapseSpaces(whitespaceToSpace(string)))

a['_include'](a, preprocess)
del preprocess



def query(x):
    PY = x['_Python']
    inn = x['_INPUT_BUFFER']
    while not inn:
        PY['read'](x)
        inn.extend(  PY['preprocess'](PY['drop'](x))   )
    PY['rpush'](x, (inn.popleft(),))

a['_include'](a, query)
a['_expand'](a, 'QUERY')
del query



def sail(x):
    x['_ATTN'][0] = True
    while x['_ATTN'][0]:
        x['_Python']['_execute'](x)

a['_include'](a, sail)
a['sail'] = a['_Python']['sail']
del sail



def zz(x):
    x['_ATTN'][0] = False

a['_include'](a, zz)
a['_expand'](a, 'ZZ')
del zz



def call(x):
    PY = x['_Python']
    PY['push'](x, PY['drop'](x)())

a['_include'](a, call)
a['_expand'](a, '()', 'call')
del call



def call1(x):
    PY = x['_Python']
    FUNCTION = PY['drop'](x)
    ARG = PY['drop'](x)
    PY['push'](x, FUNCTION(ARG))

a['_include'](a, call1)
a['_expand'](a, '(1)', 'call1')
del call1



def callstar(x):
    PY = x['_Python']
    FUNCTION = PY['drop'](x)
    ARGS = PY['drop'](x)
    PY['push'](x, FUNCTION(*ARGS))

a['_include'](a, callstar)
a['_expand'](a, '(*)', 'callstar')
del callstar



def callstarstar(x):
    PY = x['_Python']
    FUNCTION = PY['drop'](x)
    ARGS, KWARGS = PY['drop'](x)
    PY['push'](x, FUNCTION(*ARGS, **KWARGS))

a['_include'](a, callstarstar)
a['_expand'](a, '(**)', 'callstarstar')
del callstarstar



def append(x):
    PY = x['_Python']
    Obj = PY['drop'](x)
    ITEM = PY['drop'](x)
    Obj.append(ITEM)
    PY['push'](x, Obj)

a['_include'](a, append)
a['_expand'](a, 'APPEND')
del append



def split(x):
    PY = x['_Python']
    PY['push'](x, PY['drop'](x).split())

a['_include'](a, split)
a['_expand'](a, 'SPLIT')
del split



def docolon(x):
    '''Push current WORD's definition onto the Return Stack.
    '''
    PY = x['_Python']
    OP = PY['opera'](x)
    PY['rpush'](x, x['_DATA'][OP])

a['_include'](a, docolon)
del docolon



def colon(x):
    '''Start a new Dictionary entry.
    '''
    PY = x['_Python']
    WORD = PY['drop'](x)
    x['_WORD_UNDER_CONSTRUCTION'][0] = WORD
    x['_DICTIONARY'].update({ WORD: PY['docolon'] })
    x['_DATA'].update({ WORD: [] })

a['_include'](a, colon, ':')
a['_expand'](a, ':')
del colon



def backtick(x):
    PY = x['_Python']
    PY['rest'](x)
    TOKEN = PY['drop'](x)
    WORD = x['_WORD_UNDER_CONSTRUCTION'][0]
    x['_DATA'][WORD].append(TOKEN)

a['_include'](a, backtick, '`')
a['_expand'](a, '`')
del backtick



def semicolon(x):
    WORD = x['_WORD_UNDER_CONSTRUCTION'][0]
    x['_DATA'].update({
        WORD:
        tuple(reversed( x['_DATA'][WORD] )) })

a['_include'](a, semicolon, ';')
a['_expand'](a, ';')
del semicolon



def colonsemicolon(x):
    PY = x['_Python']
    WORD = PY['drop'](x)
    x['_DICTIONARY'].update({ WORD: PY['docolon'] })
    PY['split'](x)
    LIST = tuple(reversed(PY['drop'](x)))
    x['_DATA'].update({ WORD: LIST })

a['_include'](a, colonsemicolon, ':;')
a['_expand'](a, ':;')
del colonsemicolon



def docode(x):
    x['_DATA'][x['_Python']['opera'](x)](x)

a['_include'](a, docode)
del docode



def code(x):
    '''Define a word in terms of Python.
    '''
    PY = x['_Python']
    WORD = PY['drop'](x)
    STRING = PY['drop'](x)
    x['_DICTIONARY'].update({ WORD: PY['docode'] })
    x['_DATA'].update({ WORD: eval(STRING) })

a['_include'](a, code)
a['_expand'](a, 'CODE')
del code



def dot(x):
    '''Analogous to DOT or { . } in Ting.
    We use { . } in a manner more consistent with Python.
    '''
    print(x['_Python']['drop'](x))

a['_include'](a, dot, '?')
a['_expand'](a, '?')
del dot



def docon(x):
    '''
    '''
    PY = x['_Python']
    OP = PY['opera'](x)
    PY['push'](x, x['_DATA'][OP])

a['_include'](a, docon)
del docon



def constant(x):
    PY = x['_Python']
    WORD = PY['drop'](x)
    x['_DICTIONARY'].update({ WORD: PY['docon'] })
    x['_DATA'][WORD] = PY['drop'](x)

a['_include'](a, constant, '=')
a['_expand'](a, '=')
del constant



a['_Python']['_cold'](a)
