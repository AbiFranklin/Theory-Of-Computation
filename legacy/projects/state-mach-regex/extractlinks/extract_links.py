import re # module for processing regular expressions https://docs.python.org/3/library/re.html
import sys
import csv
if __name__ == '__main__':
  # Exit if command line args entered incorrectly
  if len(sys.argv) != 2:
    print("usage: extract_links.py [input_file]")
    sys.exit(0)

# Filename is 2nd command line arg
filename = sys.argv[1]


HtmlFile = open(filename, 'r', encoding='utf-8')
source_code = HtmlFile.read() 

link_regex = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

answer_data = re.findall(link_regex, source_code)

i = 1

for x in answer_data:
  print(i, " ", x)
  i+=1




# Check matches, print results
# TODO Read in links from answers.txt (hint...this is a CSV file), 
# save in list called 'answer_data'

# with open('answers.txt', 'r') as csvfile:
#     matches = [row[0] for row in csv.reader(csvfile, delimiter=',')]
 
matches= ["https://cdn.sstatic.net/Sites/stackoverflow/img/favicon.ico?v=4f32ecc8f43d","https://cdn.sstatic.net/Sites/stackoverflow/img/apple-touch-icon.png?v=c78bd457575a","https://stackoverflow.com/","https://cdn.sstatic.net/Sites/stackoverflow/img/apple-touch-icon@2.png?v=73d79a89bded","https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js","https://cdn.sstatic.net/Js/stub.en.js?v=000b2a920ae6","https://cdn.sstatic.net/Sites/stackoverflow/all.css?v=abaeac34fef4","http://www.w3.org/2000/svg","https://cdn-prom.sstatic.net/WinterBash/js/wb-core-incl.js?v=8","https://cdn-prom.sstatic.net/WinterBash/","https://stackauth.com","https://meta.stackoverflow.com","https://js-sec.indexww.com/ht/p/185901-159836282584097.js","https://stackoverflow.com","https://stackoverflow.com","https://stackoverflow.com/help","https://chat.stackoverflow.com","https://stackoverflow.com","https://meta.stackoverflow.com","https://stackoverflow.com/users/signup?ssrc=site_switcher&amp;returnurl=%2fusers%2fstory%2fcurrent&amp;amp;utm_source=stackoverflow.com&amp;amp;utm_medium=dev-story&amp;amp;utm_campaign=signup-redirect","https://stackoverflow.com/users/login?ssrc=site_switcher&amp;returnurl=https%3a%2f%2fstackoverflow.com%2f","https://stackexchange.com/sites","https://stackoverflow.blog","https://meta.stackoverflow.com","https://stackoverflow.com/company/about","https://www.stackoverflowbusiness.com/?ref=topbar_help","https://stackexchange.com/users/?tab=inbox","https://stackexchange.com/users/?tab=reputation","https://stackexchange.com","https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f","https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent&amp;utm_source=stackoverflow.com&amp;utm_medium=dev-story&amp;utm_campaign=signup-redirect","https://accounts.google.com/o/oauth2/auth","https://www.facebook.com/v2.0/dialog/oauth","https://stackexchange.com/legal/privacy-policy","https://stackexchange.com/legal/terms-of-service","https://www.stackoverflowbusiness.com/?utm_source=so-homepage&utm_medium=referral&utm_campaign=brand-activation&utm_term=sotob2b-hero-learn-more","https://www.googletagservices.com/tag/js/gpt.js","https://cdn.sstatic.net/clc/clc.min.js?v=b0e6e728032a","https://cdn.sstatic.net/clc/styles/clc.min.css?v=b18b3a2258df","https://clc.stackoverflow.com/markup.js","https://stackexchange.com/questions?tab=hot","https://electronics.stackexchange.com/questions/347172/why-do-devices-stop-operating-properly-in-extreme-cold","https://security.stackexchange.com/questions/176373/can-phone-apps-read-my-clipboard","https://biology.stackexchange.com/questions/69162/black-insect-with-antennas-and-large-abdomen","https://bitcoin.stackexchange.com/questions/67009/can-someone-explain-this-weird-mining-activity","https://codegolf.stackexchange.com/questions/152099/ternary-triangles","https://travel.stackexchange.com/questions/107407/i-need-to-fly-between-two-european-countries-once-a-month-what-is-the-cheapest","https://stackoverflow.com/questions/48033944/how-are-coroutines-implemented-in-jvm-langs-without-jvm-support","https://worldbuilding.stackexchange.com/questions/100995/how-much-of-a-modern-day-tank-can-the-14th-century-replicate","https://skeptics.stackexchange.com/questions/40298/did-jodie-foster-say-all-men-over-30-are-full-blown-rapists","https://superuser.com/questions/1280827/why-does-the-registered-domain-name-localtest-me-resolve-to-127-0-0-1","https://bicycles.stackexchange.com/questions/51575/do-bike-frames-actually-break-so-easily","https://superuser.com/questions/1281215/how-to-mount-read-write-with-pmount","https://unix.stackexchange.com/questions/413756/bash-changes-its-behavior-depending-on-the-value-of-the-ifs-variable","https://interpersonal.stackexchange.com/questions/8448/how-do-i-tell-my-parents-i-dont-want-to-go-to-church-over-the-holidays","https://opensource.stackexchange.com/questions/6382/guidelines-for-licensing-and-attribution-for-code-from-an-article-blog-post","https://academia.stackexchange.com/questions/101119/why-do-some-researchers-need-to-be-professors-at-universities","https://retrocomputing.stackexchange.com/questions/5313/how-much-faster-is-the-z80h","https://stackoverflow.com/questions/48030393/is-there-a-performance-degradation-penalty-in-using-pure-c-library-in-c-code","https://math.stackexchange.com/questions/2585328/what-is-the-essence-of-kernel-or-null-space","https://chess.stackexchange.com/questions/19553/carlsen-inarkiev-game-illegal-moves","https://interpersonal.stackexchange.com/questions/8574/how-to-tell-friends-that-they-are-welcome-without-their-kids","https://opensource.stackexchange.com/questions/6385/streaming-coding-sessions-on-twitch-is-it-possible-to-license-the-code-as-open","https://stackoverflow.com/questions/48033760/cast-taskt-to-taskobject-in-c-sharp","https://aviation.stackexchange.com/questions/47046/is-there-any-work-on-improving-fuel-tanks-so-they-could-store-hydrogen","https://stackoverflow.com","https://stackoverflow.com","https://stackoverflow.com/jobs","https://stackoverflow.com/jobs/directory/developer-jobs","https://stackoverflow.com/jobs/salary","https://www.stackoverflowbusiness.com/?utm_source=so-footer&utm_medium=referral&utm_campaign=brand-activation&utm_term=sotob2b-footer-business-category","https://www.stackoverflowbusiness.com/talent?utm_source=so-footer&utm_medium=referral&utm_campaign=brand-activation&utm_term=sotob2b-footer-talent","https://www.stackoverflowbusiness.com/advertise?utm_source=so-footer&utm_medium=referral&utm_campaign=brand-activation&utm_term=sotob2b-footer-advertise","https://www.stackoverflowbusiness.com/enterprise?utm_source=so-footer&utm_medium=referral&utm_campaign=brand-activation&utm_term=sotob2b-footer-enterprise","https://stackoverflow.com/company/about","https://stackoverflow.com/company/about","https://stackoverflow.com/company/press","https://stackoverflow.com/company/work-here","https://stackexchange.com/legal","https://stackexchange.com/legal/privacy-policy","https://stackoverflow.com/company/contact","https://stackexchange.com","https://stackoverflow.com","https://serverfault.com","https://superuser.com","https://webapps.stackexchange.com","https://askubuntu.com","https://webmasters.stackexchange.com","https://gamedev.stackexchange.com","https://tex.stackexchange.com","https://softwareengineering.stackexchange.com","https://unix.stackexchange.com","https://apple.stackexchange.com","https://wordpress.stackexchange.com","https://gis.stackexchange.com","https://electronics.stackexchange.com","https://android.stackexchange.com","https://security.stackexchange.com","https://dba.stackexchange.com","https://drupal.stackexchange.com","https://sharepoint.stackexchange.com","https://ux.stackexchange.com","https://mathematica.stackexchange.com","https://salesforce.stackexchange.com","https://expressionengine.stackexchange.com","https://pt.stackoverflow.com","https://blender.stackexchange.com","https://networkengineering.stackexchange.com","https://crypto.stackexchange.com","https://codereview.stackexchange.com","https://magento.stackexchange.com","https://softwarerecs.stackexchange.com","https://dsp.stackexchange.com","https://emacs.stackexchange.com","https://raspberrypi.stackexchange.com","https://ru.stackoverflow.com","https://codegolf.stackexchange.com","https://es.stackoverflow.com","https://ethereum.stackexchange.com","https://datascience.stackexchange.com","https://arduino.stackexchange.com","https://bitcoin.stackexchange.com","https://stackexchange.com/sites#technology","https://photo.stackexchange.com","https://scifi.stackexchange.com","https://graphicdesign.stackexchange.com","https://movies.stackexchange.com","https://music.stackexchange.com","https://worldbuilding.stackexchange.com","https://cooking.stackexchange.com","https://diy.stackexchange.com","https://money.stackexchange.com","https://academia.stackexchange.com","https://law.stackexchange.com","https://stackexchange.com/sites#lifearts","https://english.stackexchange.com","https://skeptics.stackexchange.com","https://judaism.stackexchange.com","https://travel.stackexchange.com","https://christianity.stackexchange.com","https://ell.stackexchange.com","https://japanese.stackexchange.com","https://gaming.stackexchange.com","https://bicycles.stackexchange.com","https://rpg.stackexchange.com","https://anime.stackexchange.com","https://puzzling.stackexchange.com","https://mechanics.stackexchange.com","https://stackexchange.com/sites#culturerecreation","https://mathoverflow.net","https://math.stackexchange.com","https://stats.stackexchange.com","https://cstheory.stackexchange.com","https://physics.stackexchange.com","https://chemistry.stackexchange.com","https://biology.stackexchange.com","https://cs.stackexchange.com","https://philosophy.stackexchange.com","https://stackexchange.com/sites#science","https://meta.stackexchange.com","https://stackapps.com","https://api.stackexchange.com","https://data.stackexchange.com","https://area51.stackexchange.com","https://stackoverflow.blog?blb=1","https://www.facebook.com/officialstackoverflow/","https://twitter.com/stackoverflow","https://linkedin.com/company/stack-overflow","https://creativecommons.org/licenses/by-sa/3.0/","https://stackoverflow.blog/2009/06/25/attribution-required/","https://pixel.quantserve.com/pixel/p-c1rF4kxgLUzNc.gif","https://www.google-analytics.com/analytics.js"]


y=0
for x in matches:
  print(y, " ", x)
  y+=1

# Compare answers with matches found using regex, print out any mismatches
# UNCOMMENT BELOW WHEN READY TO CHECK IF YOUR REGEX IS FINDING ALL THE LINKS
result = "All links matched!"
# if len( matches ) != len( answer_data ):
#   result = "Your regex found %i matches. There should be %i matches" %(len( matches ), len( answer_data ) )
# else:
for i in range( len(answer_data) ):
  if( matches[i] != answer_data[i] ):
    result = "%s Mismatched link. Got %s but expected %s at" % ( i, matches[i], answer_data[i] )
    break
print( result )

