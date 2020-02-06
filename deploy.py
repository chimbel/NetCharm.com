import os

sites = [

"Responciv.com",
"YogiPreneurs.com",
    "BizGlide.com",
    "BusinessHarbour.com",
"CoderTrove.com",
"Efficiento.com",
"MeetYourTribe.com",
"Rethrill.com",
"VintageLabs.com",
]
for website in sites:
    print(website)
    os.popen('rm -rf ./deploy/').read()
    os.popen('git clone https://github.com/chimbel/' + website + '.git ./deploy').read()
    os.popen('cp -a ./website/* ./deploy/').read()
    with open('./deploy/CNAME', 'w') as f:
        f.write(website)
    os.popen('cd ./deploy && git add --all').read()
    os.popen('cd ./deploy && git commit -m "first commit"').read()
    os.popen('cd ./deploy && git push').read()