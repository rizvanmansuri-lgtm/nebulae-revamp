# -*- coding: utf-8 -*-
"""Helpers for writing tools/products/<slug>.json files (import with: from mkjson import *)."""
import json, os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'products')+os.sep
def J(d):
    json.dump(d,open(OUT+d['slug']+'.json','w',encoding='utf-8'),indent=1,ensure_ascii=False)
def G(f,a,l): return dict(file=f,alt=a,label=l)
def Q(i,l,v): return dict(icon=i,label=l,value=v)
def ST(n,l): return dict(num=n,label=l)
def W(t,d): return dict(t=t,d=d)
def F(i,c,b,t,d): return dict(icon=i,color=c,bg=b,t=t,d=d)
def A(i,t,d): return dict(icon=i,t=t,d=d)
def SP(g,rows): return dict(group=g,rows=[list(r) for r in rows])
def SC(f,a,c): return dict(file=f,alt=a,cap=c)
COL=[('#2563eb','rgba(37,99,235,.1)'),('#059669','rgba(16,185,129,.1)'),('#d97706','rgba(251,191,36,.12)'),('#4f46e5','rgba(79,70,229,.1)'),('#ea580c','rgba(234,88,12,.1)'),('#7c3aed','rgba(124,58,237,.1)'),('#0d9488','rgba(13,148,136,.1)'),('#dc2626','rgba(220,38,38,.1)')]
def FS(items): return [F(i,COL[k%8][0],COL[k%8][1],t,d) for k,(i,t,d) in enumerate(items)]
def DOC(name,path,sub): return dict(name=name,path='./assets/docs/'+path,sub=sub)

