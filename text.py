import bpy
import sys
import struct

d = bpy.context.object.data

with open("C:/Users/Admin/Downloads/obj.txt", 'w') as o:
    sys.stdout = o

    print('{} {}'.format(len(d.vertices), len(d.polygons)))
    vb = []
    
    for f in d.polygons:
        for v in f.vertices:
            vert = []
            for i in d.vertices[v].co:
                vert.append(i)
            for i in d.uv_layers.active.data[v].uv:
                vert.append(i)
            for i in d.vertices[v].normal:
                vert.append(i)
            vb.append(vert)

    vert = [float] * 8
    va = [vert] * len(d.vertices)

    i = 0
    for f in d.polygons:
        for v in f.vertices:
            va[v] = vb[i]
            i += 1
    i = 0
    for v in d.vertices:
        for j in va[i]:
            print(j,end=' ')
        i += 1
        print()
    
    for f in d.polygons:
        for v in f.vertices:
            print('{} '.format(v), end='')
        print()