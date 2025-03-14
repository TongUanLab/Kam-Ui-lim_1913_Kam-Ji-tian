import pandas as pd
from thokit import ThoKit
import re

df = pd.read_csv('dict.csv')

df['page'] = df['page'].astype('string').fillna('')
df['page'] = df['page'].apply(lambda x: str(int(float(x))) if x else x)

df['word'] = df['word'].apply(lambda x: x.strip())
df['chinese'] = df['chinese'].apply(lambda x: x.strip())
df['exp'] = df['exp'].apply(lambda x: x.strip())
df['example'] = df['example'].astype('string').fillna('')
df['example'] = df['example'].apply(lambda x: x.strip())

df2 = df[['id', 'word', 'chinese', 'exp', 'example', 'page']]

df2['ji'] = df2['chinese'].apply(lambda x: ''.join(re.findall(r'[^a-zA-Z\(\)\[\]\d]+', x)).strip())
df2['bunim'] = df2['chinese'].apply(lambda x: ''.join(re.findall(r'[a-zA-Z\[\]]+\d?', x)).strip())
df2['bunim'] = df2['bunim'].apply(lambda x: x if not x else x[0].upper()+x[1:])

df3 = df2[['id', 'word', 'ji', 'bunim', 'exp', 'example', 'page']]

df3['word'] = df3['word'].apply(lambda x: ThoKit().pojAscii2Unicode(x, standard='campbell', support_N=True))
df3['bunim'] = df3['bunim'].apply(lambda x: ThoKit().pojAscii2Unicode(x, standard='campbell', support_N=True))
df3['exp'] = df3['exp'].apply(lambda x: ThoKit().pojAscii2Unicode(ThoKit().pojUnicode2Ascii(x), standard='campbell', support_N=True).replace('\r\n', ' ').replace('  ', ' '))
df3['example'] = df3['example'].apply(lambda x: ThoKit().pojAscii2Unicode(ThoKit().pojUnicode2Ascii(x), standard='campbell', support_N=True).replace('\r\n', ' ').replace('  ', ' '))
df3['tailo'] = df3['word'].apply(lambda x: ThoKit().tailoUnicode2Ascii(ThoKit().pojUnicode2TailoUnicode(x.lower(), poj_standard='campbell')))

df3 = df3[['id', 'word', 'ji', 'bunim', 'exp', 'example', 'tailo', 'page']]

df3 = df3.rename(columns={'word': 'poj_unicode', 'bunim': 'poj_bunim_unicode', 'exp': 'comment', 'example': 'hanlo_comment', 'page': 'page_number'})

df3 = df3.set_index('id')


'''
統一格式[TODO]：

1. 訂[原]

'''

df3.loc[315, 'comment'] = 'bán-(=boán-) thian-kong, chiū-sī ū kúi-nā ki sòe-sim tūi-teh ê tông.'
df3.loc[315, 'hanlo_comment'] = '滿天光, 就是 有 幾若 枝 細心 墜 teh ê 燈.'
df3.loc[840, 'comment'] = 'ka(=kā)-boa̍h-chhài, chiū-sī chhiⁿ-chhài, á-sī chhài-thâu.'
df3.loc[1222, 'comment'] = 'oe-khoeh, sak, ni̍h-oá, tūi-lo̍h, pâi-lia̍t, chhia-tó, chhia-sak.'
df3.loc[1247, 'comment'] = 'hù-sû ê oē; sih-chheh[sih-cheh]=sih chi̍t-ē sio-siāng; kiu-cheh lun-cheh=kiaⁿ ê ì-sù.'
df3.loc[1247, 'comment'] = '副詞 ê 話; sih-cheh=sih 一下 相像; 勼cheh, 縮cheh=驚 ê 意思.'
df3.loc[1251, 'poj_bunim_unicode'] = 'Tsoa̍t'
df3.loc[1730, 'comment'] = 'oa̍t-tńg, sóa-ūi; àm-chīⁿ, siu-khǹg, tè i kiâⁿ, kiâⁿ bōe chìn.'
df3.loc[2122, 'comment'] = 'chúi[chiú]-tsóaⁿ, niû mi̍h ê khì-kū, tsū-chi̍p, siúⁿ-sù, tí-tng, tāng-tāng.'
df3.loc[2624, 'comment'] = 'm̄-ti̍hⁿ ê chhù; pàng-sang; chhiong-móa; chio, tōa, bô-lō͘-ēng.'
df3.loc[2992, 'hanlo_comment'] = '嗤chhn̍gh哮, 嗤chhn̍gh 叫, 就是 哮 ê 聲.'
df3.loc[3127, 'hanlo_comment'] = '藥 ê 名, 親像 石菖pô͘ⁿ, 抑是 石菖婆.'
df3.loc[3646, 'poj_unicode'] = 'Chhù'
df3.loc[3646, 'tailo'] = 'tshu3'
df3.loc[4143, 'comment'] = 'léng-gē sī léng-chhiò ê ì-sù; gē-tòaⁿ, gē-pîⁿ, tsng-gē[tosng-gē].'
df3.loc[4881, 'comment'] = 'chhùi kā-mi̍h, bé kā-kiuⁿ; kám-kek, niá-siúⁿ, chhùi kâm-teh, koaⁿ-hâm.'
df3.loc[6552, 'ji'] = '㕼'
df3.loc[6552, 'comment'] = 'chhut tōa-siaⁿ; oh-tit chiâⁿ kong-lô.' # 'kap téng-bīn jī sio-siāng.'
df3.loc[7370, 'hanlo_comment'] = '依偎[因為], 有 所靠, 偏邊, 歪; 依oá, oá靠, oá重.'
df3.loc[7438, 'ji'] = '圯[圮]'
df3.loc[7438, 'poj_bunim_unicode'] = ''
df3.loc[8481, 'comment'] = 'ûn-á-sio, hé-to̍h, jia̍t; ìn-hó; chhin-chhiūⁿ, àn-ni; nā-sī; gú-tsō͘-sû, sui-jiân.'
df3.loc[8524, 'comment'] = 'jiáuⁿ-súi, chiū-sī toh-piⁿ chhâ khek ê hoe; jiáuⁿ-súi-teng, chiū-sī thih-teng lâi tèng hit ê hoe.'
df3.loc[9060, 'poj_bunim_unicode'] = 'Te̍k[Tek]'
df3.loc[9349, 'ji'] = '假'
df3.loc[9349, 'poj_bunim_unicode'] = 'Kà[Ká]'
df3.loc[9631, 'comment'] = 'ki-ki kê-kê, chiū-sī siông-siông khê-tio̍h ê ì-sù.'
df3.loc[10696, 'ji'] = '綰'
df3.loc[10901, 'comment'] = 'koat-tsoa̍t, chiū-sī tsoa̍t-tn̄g kap-lâng óng-lâi ê ì-sù.'
df3.loc[10903, 'comment'] = 'khī-koe, hé-koe[hí-koe]; tsàu-koe; koe-bú, koe-kak, koe-mn̂g, koe-nn̄g.'
df3.loc[10903, 'hanlo_comment'] = '雉雞, 火雞; 灶雞; 雞母, 雞角, 雞毛, 雞卵.'
df3.loc[11067, 'comment'] = 'chho͘-ku̍t bē kè-hé ê tâng thih, chho͘-ku̍t ê kim-ge̍k, tâng, thih.'
df3.loc[11067, 'hanlo_comment'] = '粗掘 未 過火 ê 銅 鐵, 粗掘 ê 金玉, 銅, 鐵.'
df3.loc[11068, 'comment'] = 'chho͘-ku̍t bē kè-hé ê tâng thih, chho͘-ku̍t ê kim-ge̍k, tâng, thih.'
df3.loc[11068, 'hanlo_comment'] = '粗掘 未 過火 ê 銅 鐵, 粗掘 ê 金玉, 銅, 鐵.'
df3.loc[15130, 'ji'] = '玫[玟]'
df3.loc[15130, 'poj_bunim_unicode'] = ''
df3.loc[16498, 'ji'] = '䀣'
df3.loc[16499, 'ji'] = '箅'
df3.loc[16499, 'poj_bunim_unicode'] = ''
df3.loc[16500, 'ji'] = '䪐'
df3.loc[16501, 'ji'] = '𢲾'
df3.loc[17435, 'ji'] = '礟'
df3.loc[17436, 'poj_bunim_unicode'] = ''
df3.loc[17807, 'hanlo_comment'] = 'phn̍gh-phn̍gh哮, 就是 蛇 跳oá beh 咬 ê 聲; 人 哄頭 ê 款式.'
df3.loc[19284, 'comment'] = 'Ûn-sio[Un-sio], siâⁿ ê miâ, chiū-sī tī Chiuⁿ-phó͘[Chiu-phó͘] kap Chiau-an ê tiong-kan.'
df3.loc[19284, 'hanlo_comment'] = '雲霄, 城 ê 名, 就是 tī 漳浦 kap 詔安 ê 中間.'
df3.loc[19812, 'poj_unicode'] = 'soaihⁿ'
df3.loc[19812, 'comment'] = 'sihⁿ-si̍hⁿ sa̍uhⁿ-sa̍uhⁿ, sa̍uhⁿ-sa̍uhⁿ háu ê siaⁿ.'
df3.loc[19812, 'tailo'] = 'suainnh4'
df3.loc[20447, 'comment'] = 'ta-po͘, ta-po͘-kiáⁿ, ta-po͘-sun; ta-po͘-lâng, ta-po͘-hàn.'
df3.loc[21855, 'ji'] = '朵[呆]'
df3.loc[21855, 'poj_bunim_unicode'] = ''
df3.loc[21968, 'comment'] = 'chiū-sī bô chhiú-ńg ê saⁿ ê ì-sù.'
df3.loc[22494, 'comment'] = 'chháu ê miâ, hio̍h chhin-chhiūⁿ sng-chiong-hoa, sòe koh pe̍h, tiong-sim n̂g.'
df3.loc[24243, 'poj_unicode'] = 'tsoàn'
df3.loc[24243, 'tailo'] = 'tsuan3'
df3.loc[24270, 'poj_unicode'] = 'Tsoat'
df3.loc[24270, 'tailo'] = 'tsuat4'
df3.loc[24780, 'ji'] = '圩[𱖇]'
df3.loc[24780, 'poj_bunim_unicode'] = ''
df3.loc[24785, 'ji'] = '盱[盰]'
df3 = df3.drop(index=[25213, 25214, 25215])

df3['comment'] = df3['comment'].apply(lambda x: re.sub('\[([\u4e00-\u9fff][^,\]]*)\]', '{\\1}', x))
df3['hanlo_comment'] = df3['hanlo_comment'].apply(lambda x: re.sub('\[([\u4e00-\u9fff][^,\]]*)\]', '{\\1}', x))

df3.to_csv('dict-new.csv')