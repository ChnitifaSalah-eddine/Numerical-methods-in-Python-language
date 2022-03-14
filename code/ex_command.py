import sys

print('Nombre de Params: {}'.format(len(sys.argv)))
for i,param in enumerate(sys.argv):
    print('Param. {}: {}'.format(i,param))