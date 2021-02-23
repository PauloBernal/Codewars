import os

def initFile(name, fname, fvar = 'args'):
    f = open(f'./kata/{name}.py', 'w')
    f.write(f'# Solution by PauloBA\n\ndef {fname}({fvar}):\n pass\n\narg = None\n\nprint({fname}(arg))')

initFile('maxSubarraySum', 'max_sequence', 'arr')