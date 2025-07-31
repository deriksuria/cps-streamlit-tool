# variable_aliases.py

# Paste your entire codebook here, exactly as received (space- or tab-separated)
_raw_vars = """
hrhhid2 HUFINAL OCCURNUM HUINTTYP HURESPLI HUPRSCNT HUTYPEA HUTYPB HUTYPC 
HUBUS HUBUSL1 HUBUSL2 HUBUSL3 HUBUSL4 HRMIS HRMONTH HRYEAR4 HRLONGLK qstnum 
gereg gestfips gediv hehousut hxhousut hephoneo hxphoneo hetelavl hxtelavl 
hetelhhd hxtelhhd hrhtype hrintsta hrnumhou hefaminc hxfaminc hwhhwgt hwhhwtln 
PULINENO PUCHINHH PUWK PUBUS1 PUDIS PULAY PUHROFF1 PUHROFF2 PUHROT1 PUHROT2 
PUABSOT PUBUSCK1 PUBUSCK2 PUBUSCK3 PUBUSCK4 PURETOT PUHRCK1 PUHRCK2 PUHRCK3 
PUHRCK4 PUHRCK5 PUHRCK6 PUHRCK7 PUHRCK12 PULAYDT PULAY6M PULAYAVR PULK PULKAVR 
PULAYCK1 PULAYCK2 PULAYCK3 PUDWCK1 PUDWCK2 PUDWCK3 PUDWCK4 PUDWCK5 PUJHCK1 
PUJHCK2 PUJHDP1O PUJHCK3 PUJHCK4 PUJHCK5 PULKM2 PULKM3 PULKM4 PULKM5 PULKM6 
PULKDK1 PULKDK2 PULKDK3 PULKDK4 PULKDK5 PULKDK6 PULKPS1 PULKPS2 PULKPS3 PULKPS4 
PULKPS5 PULKPS6 PUIOCK1 PUIOCK2 PUIOCK3 PUIODP1 PUIODP2 PUIODP3 PUIO1MFG PUIO2MFG 
PUNLFCK1 PUNLFCK2 PUSLFPRX PUDIS1 PUDIS2 PUBUS2OT perrp pxrrp pxage peafnow pxafnow 
pesex pxsex pemaritl pxmaritl pxrace1 pehspnon pxhspnon peeduca pxeduca peafever pxafever 
peafwhn1 pxafwhn1 peafwhn2 peafwhn3 peafwhn4 pespouse pxspouse penatvty pxnatvty 
pemntvty pxmntvty pefntvty pxfntvty pxinusyr pedipged pxdipged pehgcomp pxhgcomp 
pecyc pxcyc pepar1 pxpar1 pepar2 pxpar2 pepar1typ pxpar1typ pepar2typ pxpar2typ prdasian 
prmarsta ptdtrace prdthsp prpertyp prfamnum prfamtyp prfamrel prnmchld prchld prcitflg 
prcitshp prinuyer prtage prtfage pecohab pxcohab peabspdo peabsrsn pedwavl pedwavr 
pedwlko pedwlkwk pedwrsn pedwwk pedwwnto pedw4wk pehractt pehract1 pehract2 pehravl 
pehrftpt pehrrsn1 pehrrsn2 pehrrsn3 pehruslt pehrusl1 pehrusl2 pehrwant pejhrsn pejhwant 
pejhwko pelayavl pelaydur pelayfto pelaylk pelkavl pelkdur pelkfto pelkll1o pelkll2o 
pelklwo pelkm1 pemjnum pemjot pemlr penlfact penlfjh penlfret peret1 pxabspdo pxabsrsn 
pxdwavl pxdwavr pxdwlko pxdwlkwk pxdwrsn pxdwwk pxdwwnto pxdw4wk pxhractt pxhract1 
pxhract2 pxhravl pxhrftpt pxhrrsn1 pxhrrsn2 pxhrrsn3 pxhruslt pxhrusl1 pxhrusl2 
pxhrwant pxjhrsn pxjhwant pxjhwko pxlayavl pxlaydur pxlayfto pxlaylk pxlkavl pxlkdur 
pxlkfto pxlkll1o pxlkll2o pxlklwo pxlkm1 pxmjnum pxmjot pxmlr pxnlfact pxnlfjh pxnlfret 
pxret1 prabsrea prcivlf prdisc premphrs prempnot prexplf prftlf prhrusl prjobsea prpthrs 
prptrea prunedur pruntype prwksch prwkstat prwntjob peio1icd peio2icd peio1cow peio2cow 
pepdemp1 pepdemp2 pxio1icd pxio2icd pxio1ocd pxio2ocd pxio1cow pxio2cow pxpdemp1 pxpdemp2 
pxnmemp1 pxnmemp2 prioelg premp prcow1 prcow2 prnagws prnagpws prdtcow1 prdtcow2 prmjind1 
prmjind2 primind1 primind2 prmjocc1 prmjocc2 prdtind1 prdtind2 prdtocc1 prdtocc2 pragna 
prsjmj prcowpg prmjocgr peernper peernhry peernuot peernwkp peernrt peernhro peernlab peerncov 
pxernper pxernhry pxernuot pxernwkp pxernrt pxernh2 pxernh1o pxernhro pxern pxernlab pxerncov 
prerelg prwernal prhernal peschlvl peschenr peschft pxschlvl pxschenr pxschft prnlfsch pedisear 
pediseye pedisrem pedisphy pedisdrs pedisout pxdisear pxdiseye pxdisrem pxdisphy pxdisdrs 
pxdisout prdisflg pecert1 pecert2 pecert3 pxcert1 pxcert2 pxcert3 pxtlwk pxtlwkhr pwsswgt pwlgwgt 
pwvetwgt pworwgt pwfmwgt pwcmpwgt pttlwk pttlwkhr prernmin pternhly pternh1o pternh2 pternh1c 
pternwa ptern ptern2 ptio1ocd ptio2ocd ptnmemp1 ptnmemp2 hrhhid ptot ptwk pthr gtcbsa gtco 
gtcbsast gtcbsasz gtcsa gtmetsta gtindvpc
"""

# Build the dict dynamically
VARIABLE_ALIASES = {var.upper(): [var.upper()] for var in _raw_vars.split()}
