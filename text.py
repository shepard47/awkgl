import bpy
import sys
import struct

d = bpy.context.object.data

"""
    print('vert {}'.format(len(d.vertices)))
    for v in d.vertices:
       print('{} {} {} {} {} {}'.format(v.co.x, v.co.y, v.co.z, v.normal.x, v.normal.y, v.normal.z))

    print('ind {}'.format(len(d.polygons)))
    for f in d.polygons:
        for v in f.vertices:
            print('{} '.format(v), end='')
        print()
"""
with open("C:/Users/Admin/Downloads/obj.txt", 'w') as o:
    sys.stdout = o

    #print('vert {}'.format(len(d.vertices)))
    for f in d.polygons:
        for v in f.vertices:
            for i in d.vertices[v].co:
                print(i,end=' ')
            for i in d.uv_layers.active.data[v].uv:
                print(i,end=' ')
            for i in d.vertices[v].normal:
                print(i,end=' ')
            print()
