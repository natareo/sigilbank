import argparse

parser = argparse.ArgumentParser(description='Produce Azimuth sigil images.')
parser.add_argument('--pixelsize', type=int, nargs=1,
                    default=[32],
                    help='the file containing the list of planets')

args = parser.parse_args()

import numpy as np

from imageio import imread,imwrite
import matplotlib.pyplot as plt
pixelsize = args.pixelsize[0]

prefix='dozmarbinwansamlitsighidfidlissogdirwacsabwissibrigsoldopmodfoglidhopdardorlorhodfolrintogsilmirholpaslacrovlivdalsatlibtabhanticpidtorbolfosdotlosdilforpilramtirwintadbicdifrocwidbisdasmidloprilnardapmolsanlocnovsitnidtipsicropwitnatpanminritpodmottamtolsavposnapnopsomfinfonbanmorworsipronnorbotwicsocwatdolmagpicdavbidbaltimtasmalligsivtagpadsaldivdactansidfabtarmonranniswolmispallasdismaprabtobrollatlonnodnavfignomnibpagsopralbilhaddocridmocpacravripfaltodtiltinhapmicfanpattaclabmogsimsonpinlomrictapfirhasbosbatpochactidhavsaplindibhosdabbitbarracparloddosbortochilmactomdigfilfasmithobharmighinradmashalraglagfadtopmophabnilnosmilfopfamdatnoldinhatnacrisfotribhocnimlarfitwalrapsarnalmoslandondanladdovrivbacpollaptalpitnambonrostonfodponsovnocsorlavmatmipfip'
suffix='zodnecbudwessevpersutletfulpensytdurwepserwylsunrypsyxdyrnuphebpeglupdepdysputlughecryttyvsydnexlunmeplutseppesdelsulpedtemledtulmetwenbynhexfebpyldulhetmevruttylwydtepbesdexsefwycburderneppurrysrebdennutsubpetrulsynregtydsupsemwynrecmegnetsecmulnymtevwebsummutnyxrextebfushepbenmuswyxsymselrucdecwexsyrwetdylmynmesdetbetbeltuxtugmyrpelsyptermebsetdutdegtexsurfeltudnuxruxrenwytnubmedlytdusnebrumtynseglyxpunresredfunrevrefmectedrusbexlebduxrynnumpyxrygryxfeptyrtustyclegnemfermertenlusnussyltecmexpubrymtucfyllepdebbermughuttunbylsudpemdevlurdefbusbeprunmelpexdytbyttyplevmylwedducfurfexnulluclennerlexrupnedlecrydlydfenwelnydhusrelrudneshesfetdesretdunlernyrsebhulrylludremlysfynwerrycsugnysnyllyndyndemluxfedsedbecmunlyrtesmudnytbyrsenwegfyrmurtelreptegpecnelnevfes'

prefixes = [ prefix[ 3*i:3*i+3 ] for i in range( len( prefix ) // 3 ) ]
suffixes = [ suffix[ 3*i:3*i+3 ] for i in range( len( prefix ) // 3 ) ]

################################################################################

js_preamble = '''
const { sigil, stringRenderer } = require('urbit-sigil-js')
function svgString(inpatp,incolor) {
  return sigil({
  patp: inpatp,
  renderer: stringRenderer,
  size: %i,
  colors: ['white', incolor],
});
}
var form0 = '<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>'
var form1 = '<svg width=\"%i\" height=\"%i\" version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\">'
var form2 = '</svg>';
const fs = require('fs');
''' % (pixelsize,pixelsize,pixelsize)

js_load = '''
var http = require('http');
var uc = require('upper-case');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write('<style>div { white-space: nowrap; overflow: hidden; }</style>');
'''

js_end = '''
  res.end();
}).listen(8080);
'''

planets = prefixes + suffixes

js_middle = ''
for index,planet in enumerate(planets):
    planet = planet.strip()
    rgb = (0,0,0,0)
    html = f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
    svg_string = (f'form0+form1+svgString("{planet}","{html}")+form2')
    js_middle += f'''
    console.log('{planet}','svg{index}.svg');
    fs.writeFileSync('working/{planet}.svg', {svg_string});
    '''

print( 'Source JS generated.' )

with open('out.js','w') as destfile:
    destfile.write(js_preamble)
    #destfile.write(js_header)
    destfile.write(js_load)
    destfile.write(js_middle)
    destfile.write(js_end)

print( 'Now run `node out.js` and visit `localhost:8080` to render them.' )

#import subprocess
#subprocess.run(['node','out.js'],timeout=5)#,shell=True)