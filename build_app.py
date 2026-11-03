# Hesaplayıcı sayfasından telefon uygulaması (PWA) index.html üretir.
import re
s=open('src/briganti-nomogram.html').read()
te=s.index('</title>')+len('</title>')
head='''
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0e8a97">
<meta name="description" content="Briganti 2012 ve 2019 nomogramları ile prostat kanserinde lenf nodu invazyonu riski">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-192.png" type="image/png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Briganti">
<meta name="apple-mobile-web-app-status-bar-style" content="default">'''
rest=s[te:].replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
se=rest.index('</style>')+len('</style>')
hp=rest[:se].replace('<style>','<style>\n:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}\nbody{margin:0}\n[hidden]{display:none!important}',1)
sw='\n<script>\nif ("serviceWorker" in navigator) window.addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(()=>{}));\n</script>\n'
ver=re.search(r'version: "([^"]+)"',s).group(1)
open('index.html','w').write('<!doctype html>\n<html lang="tr">\n<head>\n'+s[:te]+head+hp+'\n</head>\n<body>\n'+rest[se:].strip()+'\n'+sw+'</body>\n</html>\n')
sj=open('sw.js').read(); sj=re.sub(r'const CACHE = "briganti-v[^"]+";',f'const CACHE = "briganti-v{ver}";',sj); open('sw.js','w').write(sj)
print('built',ver)
