#coding=utf8
import re
import pandas as pda
import csv

print("please input the file_name:", end="")
file_name = input()
fileName = "D:\\job_data" + "\\" + str(file_name) + ".csv"


def get_word_from_html(html):
    parttern = re.compile('<td.*?>.*?</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>', re.S)
    items = re.findall(parttern, html)
    number = 1
    words = []
    for item in items:
        yield {
            "a_word": item[0],
            "b_alphabet": item[1],
            "c_meaning": item[2]
        }
        words.append(item)
        data = pda.DataFrame(words)
        # print(words)

    try:
        if number == 1:
            csv_headers = ['a_word', 'b_alphabet', 'c_meaning']
            data.to_csv(fileName, header=csv_headers, index=False, mode='a+', encoding='utf-8')
        else:
            data.to_csv(fileName, header=False, index=False, mode='a+', encoding='utf-8')
            number = number + 1
    except UnicodeEncodeError:
        print("编码错误, 该数据无法写到文件中, 直接忽略该数据")
def main():
    html ="""  <tr>
                <td class="export-td">1</td>
                <td class="export-td">alright</td>
                <td class="export-td">英:/ɔːl'raɪt/ 美:/ɔlˈraɪt/ </td>
                <td class="export-td">1. adj. 没问题的
2. adv. 好吧（等于all right）</td>
            </tr>
            
             <tr>
                <td class="export-td">2</td>
                <td class="export-td">already</td>
                <td class="export-td">英:/ɔːl'redɪ/ 美:/ɔl'rɛdi/ </td>
                <td class="export-td">adv. 已经，早已；先前</td>
            </tr>
            
             <tr>
                <td class="export-td">3</td>
                <td class="export-td">alpine</td>
                <td class="export-td">英:/'ælpain/ 美:/ˈælˌpaɪn/ </td>
                <td class="export-td">adj. 阿尔卑斯山的，高山的</td>
            </tr>
            
             <tr>
                <td class="export-td">4</td>
                <td class="export-td">alpha particle</td>
                <td class="export-td"></td>
                <td class="export-td">n. [核物理]阿尔法粒子</td>
            </tr>
            
             <tr>
                <td class="export-td">5</td>
                <td class="export-td">alphabetical</td>
                <td class="export-td">英:/ælfə'betɪk(ə)l/ 美:/ˌælfə'bɛtɪkl/ </td>
                <td class="export-td">按字母表顺序的</td>
            </tr>
            
             <tr>
                <td class="export-td">6</td>
                <td class="export-td">alphabet</td>
                <td class="export-td">英:/'ælfəbet/ 美:/'ælfə'bɛt/ </td>
                <td class="export-td">n. 字母表，字母系统；入门，初步</td>
            </tr>
            
             <tr>
                <td class="export-td">7</td>
                <td class="export-td">alpha</td>
                <td class="export-td">英:/'ælfə/ 美:/'ælfə/ </td>
                <td class="export-td">n. 希腊字母的第一个字母；开端；最初</td>
            </tr>
            
             <tr>
                <td class="export-td">8</td>
                <td class="export-td">alpaca</td>
                <td class="export-td">英:/æl'pækə/ 美:/æl'pækə/ </td>
                <td class="export-td">n. 羊驼；羊驼呢；羊驼毛棉混纺织物；德国银（等于alpacca）</td>
            </tr>
            
             <tr>
                <td class="export-td">9</td>
                <td class="export-td">aloud</td>
                <td class="export-td">英:/ə'laʊd/ 美:/ə'laʊd/ </td>
                <td class="export-td">adv. 大声地；出声地</td>
            </tr>
            
             <tr>
                <td class="export-td">10</td>
                <td class="export-td">aloof</td>
                <td class="export-td">英:/ə'luːf/ 美:/ə'luf/ </td>
                <td class="export-td">1. adj. 冷淡的；远离的；冷漠的
2. adv. 远离；避开地</td>
            </tr>
            
             <tr>
                <td class="export-td">11</td>
                <td class="export-td">alongside</td>
                <td class="export-td">英:/əlɒŋ'saɪd/ 美:/ə'lɔŋ'saɪd/ </td>
                <td class="export-td">在旁边</td>
            </tr>
            
             <tr>
                <td class="export-td">12</td>
                <td class="export-td">along</td>
                <td class="export-td">英:/ə'lɒŋ/ 美:/ə'lɔŋ/ </td>
                <td class="export-td">1. adv. 向前；一起；来到
2. prep. 沿着；顺着</td>
            </tr>
            
             <tr>
                <td class="export-td">13</td>
                <td class="export-td">alone</td>
                <td class="export-td">英:/ə'ləʊn/ 美:/ə'lon/ </td>
                <td class="export-td">1. adj. 单独的；孤独的；独自的
2. adv. 独自地；单独地</td>
            </tr>
            
             <tr>
                <td class="export-td">14</td>
                <td class="export-td">aloft</td>
                <td class="export-td">英:/ə'lɒft/ 美:/ə'lɔft/ </td>
                <td class="export-td">1. adv. 在高处；在上面；在空中
2. prep. 在…之上；在…顶上</td>
            </tr>
            
             <tr>
                <td class="export-td">15</td>
                <td class="export-td">almost</td>
                <td class="export-td">英:/'ɔːlməʊst/ 美:/'ɔlmost/ </td>
                <td class="export-td">adv. 差不多，几乎</td>
            </tr>
            
             <tr>
                <td class="export-td">16</td>
                <td class="export-td">almond</td>
                <td class="export-td">英:/'ɑːmənd/ 美:/'ɑmənd/ </td>
                <td class="export-td">n. 杏仁，杏树；杏仁状的东西</td>
            </tr>
            
             <tr>
                <td class="export-td">17</td>
                <td class="export-td">almighty</td>
                <td class="export-td">英:/ɔːl'maɪtɪ/ 美:/ɔl'maɪti/ </td>
                <td class="export-td">1. adj. 全能的；有无限权力的
2. adv. 非常</td>
            </tr>
            
             <tr>
                <td class="export-td">18</td>
                <td class="export-td">almanac</td>
                <td class="export-td">英:/'ɔːlmənæk/ 美:/'ɔlmənæk/ </td>
                <td class="export-td">n. 年鉴；历书；年历</td>
            </tr>
            
             <tr>
                <td class="export-td">19</td>
                <td class="export-td">ally</td>
                <td class="export-td">英:/'ælaɪ/ 美:/ə'laɪ/ </td>
                <td class="export-td">1. n. 同盟国；同盟者；助手；伙伴
2. vt. 使联盟；使联合</td>
            </tr>
            
             <tr>
                <td class="export-td">20</td>
                <td class="export-td">alluvium</td>
                <td class="export-td">英:/ə'l(j)uːvɪəm/ 美:/ə'lʊvɪəm/ </td>
                <td class="export-td">n. [地]冲积层，冲积土</td>
            </tr>
            
             <tr>
                <td class="export-td">21</td>
                <td class="export-td">alluvial</td>
                <td class="export-td">英:/ə'l(j)uːvɪəl/ 美:/ə'lʊvɪəl/ </td>
                <td class="export-td">adj. 冲积的</td>
            </tr>
            
             <tr>
                <td class="export-td">22</td>
                <td class="export-td">alluring</td>
                <td class="export-td">/ə'l(j)ʊərɪŋ/ </td>
                <td class="export-td">adj. 迷人的，吸引人的；诱惑的，诱人的</td>
            </tr>
            
             <tr>
                <td class="export-td">23</td>
                <td class="export-td">allure</td>
                <td class="export-td">英:/ə'ljʊə/ 美:/ə'lɪʊr/ </td>
                <td class="export-td">1. vt. 吸引；引诱，诱惑
2. n. 诱惑力</td>
            </tr>
            
             <tr>
                <td class="export-td">24</td>
                <td class="export-td">allude</td>
                <td class="export-td">英:/ə'l(j)uːd/ 美:/ə'lʊd/ </td>
                <td class="export-td">vi. 暗指，转弯抹角地说到；略为提及，顺便提到</td>
            </tr>
            
             <tr>
                <td class="export-td">25</td>
                <td class="export-td">all-time</td>
                <td class="export-td">英:/'ɔ:ltaim/ 美:/ˈɔlˈtaɪm/ </td>
                <td class="export-td">空前的</td>
            </tr>
            
             <tr>
                <td class="export-td">26</td>
                <td class="export-td">allspice</td>
                <td class="export-td">英:/'ɔːlspaɪs/ 美:/'ɔl'spaɪs/ </td>
                <td class="export-td">n. 甜胡椒；用甜胡椒制成的香味料</td>
            </tr>
            
             <tr>
                <td class="export-td">27</td>
                <td class="export-td">all-rounder</td>
                <td class="export-td">英:/'ɔ:lraundə/ 美:/ˈ ɔlˈraʊndɚ/ </td>
                <td class="export-td">多面手</td>
            </tr>
            
             <tr>
                <td class="export-td">28</td>
                <td class="export-td">allround</td>
                <td class="export-td"></td>
                <td class="export-td">全能</td>
            </tr>
            
             <tr>
                <td class="export-td">29</td>
                <td class="export-td">all right</td>
                <td class="export-td"></td>
                <td class="export-td">好；顺利；正确的</td>
            </tr>
            
             <tr>
                <td class="export-td">30</td>
                <td class="export-td">alloy</td>
                <td class="export-td">英:/'ælɒɪ/ 美:/'ælɔɪ/ </td>
                <td class="export-td">1. vt. 使减低成色；使成合金
2. n. 合金</td>
            </tr>
            
             <tr>
                <td class="export-td">31</td>
                <td class="export-td">allowance</td>
                <td class="export-td">英:/ə'laʊəns/ 美:/ə'laʊəns/ </td>
                <td class="export-td">津贴</td>
            </tr>
            
             <tr>
                <td class="export-td">32</td>
                <td class="export-td">allowable</td>
                <td class="export-td">英:/ə'laʊəbl/ 美:/ə'laʊəbl/ </td>
                <td class="export-td">容许的, 承认的</td>
            </tr>
            
             <tr>
                <td class="export-td">33</td>
                <td class="export-td">allow</td>
                <td class="export-td">英:/ə'laʊ/ 美:/ə'laʊ/ </td>
                <td class="export-td">1. vt. 允许；认可；给予
2. vi. 容许；考虑</td>
            </tr>
            
             <tr>
                <td class="export-td">34</td>
                <td class="export-td">all out</td>
                <td class="export-td"></td>
                <td class="export-td">全力以赴, 竭尽全力</td>
            </tr>
            
             <tr>
                <td class="export-td">35</td>
                <td class="export-td">allotropy</td>
                <td class="export-td">英:/ə'lɒtrəpɪ/ 美:/ə'lɑtrəpi/ </td>
                <td class="export-td">同素异形体</td>
            </tr>
            
             <tr>
                <td class="export-td">36</td>
                <td class="export-td">allotment</td>
                <td class="export-td">英:/ə'lɒtm(ə)nt/ 美:/ə'lɑtmənt/ </td>
                <td class="export-td">配发</td>
            </tr>
            
             <tr>
                <td class="export-td">37</td>
                <td class="export-td">allot</td>
                <td class="export-td">英:/ə'lɒt/ 美:/ə'lɑt/ </td>
                <td class="export-td">vt. 分配；拨给；分派</td>
            </tr>
            
             <tr>
                <td class="export-td">38</td>
                <td class="export-td">allocate</td>
                <td class="export-td">英:/'æləkeɪt/ 美:/'æləket/ </td>
                <td class="export-td">1. vt. 分配；拨出；使坐落于
2. vi. 分配；指定</td>
            </tr>
            
             <tr>
                <td class="export-td">39</td>
                <td class="export-td">all-in</td>
                <td class="export-td">/'ɔ:l'in/ </td>
                <td class="export-td">所有功能于</td>
            </tr>
            
             <tr>
                <td class="export-td">40</td>
                <td class="export-td">alliteration</td>
                <td class="export-td">英:/əlɪtə'reɪʃ(ə)n/ 美:/ə,lɪtə'reʃən/ </td>
                <td class="export-td">头韵</td>
            </tr>
            
             <tr>
                <td class="export-td">41</td>
                <td class="export-td">allin</td>
                <td class="export-td"></td>
                <td class="export-td">n. [生]大蒜素原</td>
            </tr>
            
             <tr>
                <td class="export-td">42</td>
                <td class="export-td">alligator</td>
                <td class="export-td">英:/'ælɪgeɪtə/ 美:/'ælɪɡetɚ/ </td>
                <td class="export-td">产于美洲的鳄鱼</td>
            </tr>
            
             <tr>
                <td class="export-td">43</td>
                <td class="export-td">allied</td>
                <td class="export-td">英:/'ælaɪd/ 美:/ə'laɪd/ </td>
                <td class="export-td">1. adj. 同盟的；联合的；与…同属一系
2. v. 联合（ally的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">44</td>
                <td class="export-td">alliance</td>
                <td class="export-td">英:/ə'laɪəns/ 美:/ə'laɪəns/ </td>
                <td class="export-td">n. 联盟，联合；联姻</td>
            </tr>
            
             <tr>
                <td class="export-td">45</td>
                <td class="export-td">alley</td>
                <td class="export-td">英:/'ælɪ/ 美:/'æli/ </td>
                <td class="export-td">n. 小径；小巷；小路</td>
            </tr>
            
             <tr>
                <td class="export-td">46</td>
                <td class="export-td">alleviate</td>
                <td class="export-td">英:/ə'liːvɪeɪt/ 美:/ə'livɪ'et/ </td>
                <td class="export-td">减轻,使...缓和</td>
            </tr>
            
             <tr>
                <td class="export-td">47</td>
                <td class="export-td">allergy</td>
                <td class="export-td">英:/'ælədʒɪ/ 美:/'ælɚdʒi/ </td>
                <td class="export-td">n. 过敏症；[口]反感；厌恶</td>
            </tr>
            
             <tr>
                <td class="export-td">48</td>
                <td class="export-td">allergic</td>
                <td class="export-td">英:/ə'lɜːdʒɪk/ 美:/ə'lɝdʒɪk/ </td>
                <td class="export-td">adj. 对…过敏的；对…极讨厌的</td>
            </tr>
            
             <tr>
                <td class="export-td">49</td>
                <td class="export-td">allergenic</td>
                <td class="export-td">/ˌælə'dʒenik/ </td>
                <td class="export-td">过敏</td>
            </tr>
            
             <tr>
                <td class="export-td">50</td>
                <td class="export-td">allergen</td>
                <td class="export-td">英:/'ælədʒ(ə)n/ 美:/'ælɚdʒən/ </td>
                <td class="export-td">n. 过敏原</td>
            </tr>
            
             <tr>
                <td class="export-td">51</td>
                <td class="export-td">allele</td>
                <td class="export-td">英:/'æliːl/ 美:/ə'lil/ </td>
                <td class="export-td">n. 等位基因</td>
            </tr>
            
             <tr>
                <td class="export-td">52</td>
                <td class="export-td">allegro</td>
                <td class="export-td">英:/ə'legrəʊ/ 美:/ə'lɛgro/ </td>
                <td class="export-td">1. n. 急速的乐章；快板
2. adj. 快速的</td>
            </tr>
            
             <tr>
                <td class="export-td">53</td>
                <td class="export-td">allegory</td>
                <td class="export-td">英:/'ælɪg(ə)rɪ/ 美:/'æləɡɔri/ </td>
                <td class="export-td">n. 寓言</td>
            </tr>
            
             <tr>
                <td class="export-td">54</td>
                <td class="export-td">allegiance</td>
                <td class="export-td">英:/ə'liːdʒ(ə)ns/ 美:/ə'lidʒəns/ </td>
                <td class="export-td">忠诚</td>
            </tr>
            
             <tr>
                <td class="export-td">55</td>
                <td class="export-td">allege</td>
                <td class="export-td">英:/ə'ledʒ/ 美:/ə'lɛdʒ/ </td>
                <td class="export-td">vt. 宣称，断言；提出…作为理由</td>
            </tr>
            
             <tr>
                <td class="export-td">56</td>
                <td class="export-td">allay</td>
                <td class="export-td">英:/ə'leɪ/ 美:/ə'le/ </td>
                <td class="export-td">vt. 减轻；使缓和；使平静</td>
            </tr>
            
             <tr>
                <td class="export-td">57</td>
                <td class="export-td">Allah</td>
                <td class="export-td">/'ælə/ </td>
                <td class="export-td">n. 阿拉；真主</td>
            </tr>
            
             <tr>
                <td class="export-td">58</td>
                <td class="export-td">all</td>
                <td class="export-td">英:/ɔːl/ 美:/ɔl/ </td>
                <td class="export-td">1. adj. 全部的
2. adv. 越发；全然地</td>
            </tr>
            
             <tr>
                <td class="export-td">59</td>
                <td class="export-td">alkene</td>
                <td class="export-td">英:/'ælkiːn/ 美:/'ælkin/ </td>
                <td class="export-td">n. [化]烯烃；链烯烃</td>
            </tr>
            
             <tr>
                <td class="export-td">60</td>
                <td class="export-td">alkane</td>
                <td class="export-td">英:/'ælkeɪn/ 美:/'æl,ken/ </td>
                <td class="export-td">n. 链烷；烷属烃</td>
            </tr>
            
             <tr>
                <td class="export-td">61</td>
                <td class="export-td">alkaloid</td>
                <td class="export-td">英:/'ælkəlɒɪd/ 美:/'ælkə'lɔɪd/ </td>
                <td class="export-td">n. 生物碱；植物碱基</td>
            </tr>
            
             <tr>
                <td class="export-td">62</td>
                <td class="export-td">alkali</td>
                <td class="export-td">英:/'ælkəlaɪ/ 美:/'ælkə'lai/ </td>
                <td class="export-td">1. n. 碱；可溶性无机盐
2. adj. 碱性的</td>
            </tr>
            
             <tr>
                <td class="export-td">63</td>
                <td class="export-td">alive</td>
                <td class="export-td">英:/ə'laɪv/ 美:/ə'laɪv/ </td>
                <td class="export-td">adj. 活着的；活泼的；有生气的</td>
            </tr>
            
             <tr>
                <td class="export-td">64</td>
                <td class="export-td">alist</td>
                <td class="export-td">/ə'lɪst/ </td>
                <td class="export-td">1. adj. 船向一边倾斜的
2. adv. 船向一边倾斜地</td>
            </tr>
            
             <tr>
                <td class="export-td">65</td>
                <td class="export-td">alimony</td>
                <td class="export-td">英:/'ælɪmənɪ/ 美:/'ælɪmoni/ </td>
                <td class="export-td">n. 赡养费；生活费</td>
            </tr>
            
             <tr>
                <td class="export-td">66</td>
                <td class="export-td">alimentary canal</td>
                <td class="export-td"></td>
                <td class="export-td">消化道</td>
            </tr>
            
             <tr>
                <td class="export-td">67</td>
                <td class="export-td">alike</td>
                <td class="export-td">英:/ə'laɪk/ 美:/ə'laɪk/ </td>
                <td class="export-td">1. adj. 相同的；相似的
2. adv. 以同样的方式；类似于</td>
            </tr>
            
             <tr>
                <td class="export-td">68</td>
                <td class="export-td">alignment</td>
                <td class="export-td">英:/ə'laɪnm(ə)nt/ 美:/ə'laɪnmənt/ </td>
                <td class="export-td">校准</td>
            </tr>
            
             <tr>
                <td class="export-td">69</td>
                <td class="export-td">align</td>
                <td class="export-td">英:/ə'laɪn/ 美:/ə'laɪn/ </td>
                <td class="export-td">1. vt. 使结盟；使成一行；匹配
2. vi. 排列；排成一行</td>
            </tr>
            
             <tr>
                <td class="export-td">70</td>
                <td class="export-td">alight</td>
                <td class="export-td">英:/ə'laɪt/ 美:/ə'laɪt/ </td>
                <td class="export-td">1. vi. 下来；飞落
2. adj. 烧着的；点亮着的</td>
            </tr>
            
             <tr>
                <td class="export-td">71</td>
                <td class="export-td">alienate</td>
                <td class="export-td">英:/'eɪlɪəneɪt/ 美:/ˈeljəˌnet/ </td>
                <td class="export-td">vt. 使疏远，离间；让与</td>
            </tr>
            
             <tr>
                <td class="export-td">72</td>
                <td class="export-td">alien</td>
                <td class="export-td">英:/'eɪlɪən/ 美:/'elɪən/ </td>
                <td class="export-td">1. adj. 外国的；相异的，性质不同的；不相容的
2. n. 外星人；外国人，外侨</td>
            </tr>
            
             <tr>
                <td class="export-td">73</td>
                <td class="export-td">alibi</td>
                <td class="export-td">英:/'ælɪbaɪ/ 美:/'æləbaɪ/ </td>
                <td class="export-td">1. n. 托辞；犯罪现场；辩解
2. vi. 辩解；找借口</td>
            </tr>
            
             <tr>
                <td class="export-td">74</td>
                <td class="export-td">alias</td>
                <td class="export-td">英:/'eɪlɪəs/ 美:/'elɪəs/ </td>
                <td class="export-td">1. n. 别名，化名
2. adv. 别名叫；化名为</td>
            </tr>
            
             <tr>
                <td class="export-td">75</td>
                <td class="export-td">algorithm</td>
                <td class="export-td">英:/'ælgərɪð(ə)m/ 美:/'ælgə'rɪðəm/ </td>
                <td class="export-td">算法</td>
            </tr>
            
             <tr>
                <td class="export-td">76</td>
                <td class="export-td">algebra</td>
                <td class="export-td">英:/'ældʒɪbrə/ 美:/'ældʒɪbrə/ </td>
                <td class="export-td">n. 代数学</td>
            </tr>
            
             <tr>
                <td class="export-td">77</td>
                <td class="export-td">algae</td>
                <td class="export-td">英:/'ælɡədʒiː/ 美:/'ældʒi/ </td>
                <td class="export-td">n. 藻类；海藻</td>
            </tr>
            
             <tr>
                <td class="export-td">78</td>
                <td class="export-td">alfalfa</td>
                <td class="export-td">英:/æl'fælfə/ 美:/æl'fælfə/ </td>
                <td class="export-td">n. 紫花苜蓿；苜蓿</td>
            </tr>
            
             <tr>
                <td class="export-td">79</td>
                <td class="export-td">alert</td>
                <td class="export-td">英:/ə'lɜːt/ 美:/ə'lɝt/ </td>
                <td class="export-td">1. vt. 使警觉，使意识到；警告
2. adj. 警惕的，警觉的；留心的</td>
            </tr>
            
             <tr>
                <td class="export-td">80</td>
                <td class="export-td">ale</td>
                <td class="export-td">英:/eɪl/ 美:/el/ </td>
                <td class="export-td">n. 麦芽酒</td>
            </tr>
            
             <tr>
                <td class="export-td">81</td>
                <td class="export-td">alderman</td>
                <td class="export-td">英:/'ɔːldəmən/ 美:/'ɔldɚmən/ </td>
                <td class="export-td">n. 总督；市议员；市府参事；高级市政官</td>
            </tr>
            
             <tr>
                <td class="export-td">82</td>
                <td class="export-td">alcove</td>
                <td class="export-td">英:/'ælkəʊv/ 美:/'ælkov/ </td>
                <td class="export-td">n. 凹室；壁龛</td>
            </tr>
            
             <tr>
                <td class="export-td">83</td>
                <td class="export-td">alcoholism</td>
                <td class="export-td">英:/'ælkəhɒlɪz(ə)m/ 美:/'ælkəhɔlɪzəm/ </td>
                <td class="export-td">酒精中毒, 酗酒</td>
            </tr>
            
             <tr>
                <td class="export-td">84</td>
                <td class="export-td">alcoholic</td>
                <td class="export-td">英:/ælkə'hɒlɪk/ 美:/ˌælkə'hɔlɪk/ </td>
                <td class="export-td">酒精</td>
            </tr>
            
             <tr>
                <td class="export-td">85</td>
                <td class="export-td">alcohol</td>
                <td class="export-td">英:/'ælkəhɒl/ 美:/'ælkəhɔl/ </td>
                <td class="export-td">n. 酒精，乙醇</td>
            </tr>
            
             <tr>
                <td class="export-td">86</td>
                <td class="export-td">alchemy</td>
                <td class="export-td">英:/'ælkɪmɪ/ 美:/'ælkəmi/ </td>
                <td class="export-td">n. 点金术；魔力</td>
            </tr>
            
             <tr>
                <td class="export-td">87</td>
                <td class="export-td">alchemist</td>
                <td class="export-td">英:/'ælkɪmɪst/ 美:/'ælkəmɪst/ </td>
                <td class="export-td">炼丹术士</td>
            </tr>
            
             <tr>
                <td class="export-td">88</td>
                <td class="export-td">albumen</td>
                <td class="export-td">英:/'ælbjʊmɪn/ 美:/æl'bjʊmən/ </td>
                <td class="export-td">n. 蛋白；[植]胚乳</td>
            </tr>
            
             <tr>
                <td class="export-td">89</td>
                <td class="export-td">album</td>
                <td class="export-td">英:/'ælbəm/ 美:/'ælbəm/ </td>
                <td class="export-td">n. 相簿；唱片集；集邮簿；签名纪念册</td>
            </tr>
            
             <tr>
                <td class="export-td">90</td>
                <td class="export-td">albino</td>
                <td class="export-td">英:/æl'biːnəʊ/ 美:/æl'baɪno/ </td>
                <td class="export-td">n. 白化病者；白化体；白化现象</td>
            </tr>
            
             <tr>
                <td class="export-td">91</td>
                <td class="export-td">albeit</td>
                <td class="export-td">英:/ɔːl'biːɪt/ 美:/ˌɔl'biɪt/ </td>
                <td class="export-td">conj. 即使；虽然</td>
            </tr>
            
             <tr>
                <td class="export-td">92</td>
                <td class="export-td">albatross</td>
                <td class="export-td">英:/'ælbətrɒs/ 美:/'ælbətrɔs/ </td>
                <td class="export-td">信天翁</td>
            </tr>
            
             <tr>
                <td class="export-td">93</td>
                <td class="export-td">alas</td>
                <td class="export-td">英:/ə'læs/ 美:/ə'læs/ </td>
                <td class="export-td">int. 唉（表悲伤、遗憾、恐惧、关切等等）</td>
            </tr>
            
             <tr>
                <td class="export-td">94</td>
                <td class="export-td">alarmist</td>
                <td class="export-td">英:/ə'lɑːmɪst/ 美:/ə'lɑrmɪst/ </td>
                <td class="export-td">1. n. 杞人忧天者；大惊小怪者
2. adj. 忧虑的；危言耸听的</td>
            </tr>
            
             <tr>
                <td class="export-td">95</td>
                <td class="export-td">alarming</td>
                <td class="export-td">英:/ə'lɑːmɪŋ/ 美:/ə'lɑrmɪŋ/ </td>
                <td class="export-td">1. adj. 令人担忧的；使人惊恐的
2. v. 使惊恐（alarm的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">96</td>
                <td class="export-td">alarmed</td>
                <td class="export-td">英:/əˈlɑ:md/ 美:/ə'lɑrmd/ </td>
                <td class="export-td">1. adj. 受惊的；焦虑的；惊恐的
2. v. 报警（alarm的过去式及过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">97</td>
                <td class="export-td">alarm</td>
                <td class="export-td">英:/ə'lɑːm/ 美:/ə'lɑrm/ </td>
                <td class="export-td">1. n. 警报，警告器；惊慌
2. vt. 警告；使惊恐</td>
            </tr>
            
             <tr>
                <td class="export-td">98</td>
                <td class="export-td">alabaster</td>
                <td class="export-td">英:/'æləbɑːstə/ 美:/'æləbæstɚ/ </td>
                <td class="export-td">雪花石膏</td>
            </tr>
            
             <tr>
                <td class="export-td">99</td>
                <td class="export-td">akin</td>
                <td class="export-td">英:/ə'kɪn/ 美:/ə'kɪn/ </td>
                <td class="export-td">adj. 同族的；同类的；类似的</td>
            </tr>
            
             <tr>
                <td class="export-td">100</td>
                <td class="export-td">ajar</td>
                <td class="export-td">英:/ə'dʒɑː/ 美:/ə'dʒɑr/ </td>
                <td class="export-td">1. adj. 微开的；半开的；不和谐的
2. adv. 微开地；半开地；不协调地</td>
            </tr>
            
             <tr>
                <td class="export-td">101</td>
                <td class="export-td">aisle</td>
                <td class="export-td">英:/aɪl/ 美:/aɪl/ </td>
                <td class="export-td">n. 通道，走道；侧廊</td>
            </tr>
            
             <tr>
                <td class="export-td">102</td>
                <td class="export-td">airy</td>
                <td class="export-td">英:/'eərɪ/ 美:/'ɛri/ </td>
                <td class="export-td">adj. 通风的；空气的；空中的；幻想的；轻快的</td>
            </tr>
            
             <tr>
                <td class="export-td">103</td>
                <td class="export-td">airworthy</td>
                <td class="export-td">英:/'eəwɜːðɪ/ 美:/'ɛrwɝði/ </td>
                <td class="export-td">适航</td>
            </tr>
            
             <tr>
                <td class="export-td">104</td>
                <td class="export-td">airway</td>
                <td class="export-td">英:/'eəweɪ/ 美:/'ɛrwe/ </td>
                <td class="export-td">n. 导气管；空中航线；通风孔</td>
            </tr>
            
             <tr>
                <td class="export-td">105</td>
                <td class="export-td">airwaves</td>
                <td class="export-td">/'eəweɪvz/ </td>
                <td class="export-td">n. 电视广播</td>
            </tr>
            
             <tr>
                <td class="export-td">106</td>
                <td class="export-td">air-to-air</td>
                <td class="export-td">英:/'εətə'εə/ 美:/ˌɛrtəˈɛr/ </td>
                <td class="export-td">空气 - 空气</td>
            </tr>
            
             <tr>
                <td class="export-td">107</td>
                <td class="export-td">airtime</td>
                <td class="export-td">英:/'eətaɪm/ 美:/ˈɛrˌtaɪm/ </td>
                <td class="export-td">n. 电影或电视节目开始的时间</td>
            </tr>
            
             <tr>
                <td class="export-td">108</td>
                <td class="export-td">airtight</td>
                <td class="export-td">英:/'eətaɪt/ 美:/'ɛrtaɪt/ </td>
                <td class="export-td">adj. 无懈可击的；密闭的，密封的</td>
            </tr>
            
             <tr>
                <td class="export-td">109</td>
                <td class="export-td">airstrip</td>
                <td class="export-td">英:/'eəstrɪp/ 美:/'ɛr'strɪp/ </td>
                <td class="export-td">n. 飞机跑道</td>
            </tr>
            
             <tr>
                <td class="export-td">110</td>
                <td class="export-td">airspace</td>
                <td class="export-td">英:/'eəspeɪs/ 美:/'ɛr'spes/ </td>
                <td class="export-td">n. 空域；领空；空间</td>
            </tr>
            
             <tr>
                <td class="export-td">111</td>
                <td class="export-td">airsick</td>
                <td class="export-td">英:/'eəsɪk/ 美:/'ɛr'sɪk/ </td>
                <td class="export-td">adj. 晕机的；患航空病的</td>
            </tr>
            
             <tr>
                <td class="export-td">112</td>
                <td class="export-td">airship</td>
                <td class="export-td">英:/'eəʃɪp/ 美:/'ɛr'ʃɪp/ </td>
                <td class="export-td">n. 飞艇</td>
            </tr>
            
             <tr>
                <td class="export-td">113</td>
                <td class="export-td">airport</td>
                <td class="export-td">英:/'eəpɔːt/ 美:/'ɛr'pɔrt/ </td>
                <td class="export-td">n. 机场；航空站</td>
            </tr>
            
             <tr>
                <td class="export-td">114</td>
                <td class="export-td">air pocket</td>
                <td class="export-td"></td>
                <td class="export-td">气穴；（大气中使汽机突然下跌的）气陷</td>
            </tr>
            
             <tr>
                <td class="export-td">115</td>
                <td class="export-td">airplane</td>
                <td class="export-td">英:/'eəpleɪn/ 美:/'ɛr'plen/ </td>
                <td class="export-td">n. 飞机</td>
            </tr>
            
             <tr>
                <td class="export-td">116</td>
                <td class="export-td">airmail</td>
                <td class="export-td">英:/'eəmeɪl/ 美:/'ɛrmel/ </td>
                <td class="export-td">航空邮件，航空邮政</td>
            </tr>
            
             <tr>
                <td class="export-td">117</td>
                <td class="export-td">airlock</td>
                <td class="export-td">/'ɛrlɑk/ </td>
                <td class="export-td">n. 气塞；气闸</td>
            </tr>
            
             <tr>
                <td class="export-td">118</td>
                <td class="export-td">airliner</td>
                <td class="export-td">英:/'eəlaɪnə/ 美:/'ɛrlaɪnɚ/ </td>
                <td class="export-td">n. 班机；大型客机</td>
            </tr>
            
             <tr>
                <td class="export-td">119</td>
                <td class="export-td">airline</td>
                <td class="export-td">英:/'eəlaɪn/ 美:/'ɛrlaɪn/ </td>
                <td class="export-td">1. n. 航空公司；航线
2. adj. 航线的</td>
            </tr>
            
             <tr>
                <td class="export-td">120</td>
                <td class="export-td">airlift</td>
                <td class="export-td">英:/'eəlɪft/ 美:/'ɛrlɪft/ </td>
                <td class="export-td">1. n. 空运物资；空运
2. vt. 空运</td>
            </tr>
            
             <tr>
                <td class="export-td">121</td>
                <td class="export-td">airless</td>
                <td class="export-td">英:/'eəlɪs/ 美:/'ɛrləs/ </td>
                <td class="export-td">adj. 没有风的；不通风的；缺少空气的</td>
            </tr>
            
             <tr>
                <td class="export-td">122</td>
                <td class="export-td">airing cupboard</td>
                <td class="export-td"></td>
                <td class="export-td">晾衣橱</td>
            </tr>
            
             <tr>
                <td class="export-td">123</td>
                <td class="export-td">air hostess</td>
                <td class="export-td"></td>
                <td class="export-td">空中小姐</td>
            </tr>
            
             <tr>
                <td class="export-td">124</td>
                <td class="export-td">air force</td>
                <td class="export-td"></td>
                <td class="export-td">空军</td>
            </tr>
            
             <tr>
                <td class="export-td">125</td>
                <td class="export-td">airfield</td>
                <td class="export-td">英:/'eəfiːld/ 美:/'ɛrfild/ </td>
                <td class="export-td">n. 飞机场</td>
            </tr>
            
             <tr>
                <td class="export-td">126</td>
                <td class="export-td">airdrop</td>
                <td class="export-td">英:/'eədrɒp/ 美:/'ɛrdrɑp/ </td>
                <td class="export-td">1. vt. 空投
2. n. 空投</td>
            </tr>
            
             <tr>
                <td class="export-td">127</td>
                <td class="export-td">aircrew</td>
                <td class="export-td">英:/ˈeəkru:/ 美:/'ɛrkru/ </td>
                <td class="export-td">n. 全体机组人员</td>
            </tr>
            
             <tr>
                <td class="export-td">128</td>
                <td class="export-td">aircraft carrier</td>
                <td class="export-td"></td>
                <td class="export-td">n. 航空母舰；全能篮球中锋</td>
            </tr>
            
             <tr>
                <td class="export-td">129</td>
                <td class="export-td">aircraft</td>
                <td class="export-td">英:/'eəkrɑːft/ 美:/'ɛr'kræft/ </td>
                <td class="export-td">n. 飞机，航空器</td>
            </tr>
            
             <tr>
                <td class="export-td">130</td>
                <td class="export-td">air conditioning</td>
                <td class="export-td"></td>
                <td class="export-td">空调；空气调节</td>
            </tr>
            
             <tr>
                <td class="export-td">131</td>
                <td class="export-td">air conditioner</td>
                <td class="export-td"></td>
                <td class="export-td">n. 空调设备；空气调节机</td>
            </tr>
            
             <tr>
                <td class="export-td">132</td>
                <td class="export-td">airbus</td>
                <td class="export-td">英:/'e(ə)r,bəs/ 美:/'ɛr,bʌs/ </td>
                <td class="export-td">n. 空中巴士（指大型中短程喷气客机）</td>
            </tr>
            
             <tr>
                <td class="export-td">133</td>
                <td class="export-td">airbrush</td>
                <td class="export-td">英:/'eəbrʌʃ/ 美:/'ɛr'brʌʃ/ </td>
                <td class="export-td">1. n. 喷枪；气笔
2. vt. 用气笔修（照片等）；用喷枪喷；粉饰</td>
            </tr>
            
             <tr>
                <td class="export-td">134</td>
                <td class="export-td">airborne</td>
                <td class="export-td">英:/'eəbɔːn/ 美:/'ɛr'bɔrn/ </td>
                <td class="export-td">adj. 空运的；空气传播的；风媒的</td>
            </tr>
            
             <tr>
                <td class="export-td">135</td>
                <td class="export-td">airbase</td>
                <td class="export-td">/'ɛrbes/ </td>
                <td class="export-td">空军基地</td>
            </tr>
            
             <tr>
                <td class="export-td">136</td>
                <td class="export-td">airbag</td>
                <td class="export-td">/'ɛrbæɡ/ </td>
                <td class="export-td">n. 安全气袋（一种在汽车受冲撞时自动充气以免乘客撞伤的安全装置）</td>
            </tr>
            
             <tr>
                <td class="export-td">137</td>
                <td class="export-td">air</td>
                <td class="export-td">英:/eə/ 美:/ɛr/ </td>
                <td class="export-td">1. n. 空气，大气；曲调；天空；样子
2. vt. 使通风，晾干；夸耀</td>
            </tr>
            
             <tr>
                <td class="export-td">138</td>
                <td class="export-td">ain't</td>
                <td class="export-td">英:/eint/ 美:/ent/ </td>
                <td class="export-td">不</td>
            </tr>
            
             <tr>
                <td class="export-td">139</td>
                <td class="export-td">aimless</td>
                <td class="export-td">英:/'eɪmlɪs/ 美:/'emləs/ </td>
                <td class="export-td">adj. 没有目标的，无目的的</td>
            </tr>
            
             <tr>
                <td class="export-td">140</td>
                <td class="export-td">aim</td>
                <td class="export-td">英:/eɪm/ 美:/em/ </td>
                <td class="export-td">1. vt. 把…对准；目的在于；引导
2. vi. 对准目标；打算</td>
            </tr>
            
             <tr>
                <td class="export-td">141</td>
                <td class="export-td">ailment</td>
                <td class="export-td">英:/'eɪlm(ə)nt/ 美:/'elmənt/ </td>
                <td class="export-td">n. 小病；不安</td>
            </tr>
            
             <tr>
                <td class="export-td">142</td>
                <td class="export-td">ailing</td>
                <td class="export-td">英:/'eɪlɪŋ/ 美:/'elɪŋ/ </td>
                <td class="export-td">1. adj. 生病的，身体不舒服的；体衰的
2. v. 生病；苦恼（ail的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">143</td>
                <td class="export-td">aileron</td>
                <td class="export-td">英:/'eɪlərɒn/ 美:/'elərɑn/ </td>
                <td class="export-td">n. 副翼</td>
            </tr>
            
             <tr>
                <td class="export-td">144</td>
                <td class="export-td">AIDS</td>
                <td class="export-td">/edz/ </td>
                <td class="export-td">abbr. 获得性免疫缺乏综合症；爱滋病（Acquired Immure Deficiency Syndrome）</td>
            </tr>
            
             <tr>
                <td class="export-td">145</td>
                <td class="export-td">aide</td>
                <td class="export-td">英:/eɪd/ 美:/ed/ </td>
                <td class="export-td">n. 副官；助手；侍从武官</td>
            </tr>
            
             <tr>
                <td class="export-td">146</td>
                <td class="export-td">Aida</td>
                <td class="export-td">/'eɪdə/ </td>
                <td class="export-td">阿依达</td>
            </tr>
            
             <tr>
                <td class="export-td">147</td>
                <td class="export-td">aid</td>
                <td class="export-td">英:/eɪd/ 美:/ed/ </td>
                <td class="export-td">1. n. 帮助；援助；助手；帮助者
2. vt. 帮助；援助；有助于</td>
            </tr>
            
             <tr>
                <td class="export-td">148</td>
                <td class="export-td">ahead</td>
                <td class="export-td">英:/ə'hed/ 美:/ə'hɛd/ </td>
                <td class="export-td">1. adv. 向前；预先；领先
2. adj. 向前的；领先的</td>
            </tr>
            
             <tr>
                <td class="export-td">149</td>
                <td class="export-td">aha</td>
                <td class="export-td">英:/ə'hɑː/ 美:/ɑ'hɑ/ </td>
                <td class="export-td">int. 啊哈（表示喜悦、轻蔑、惊讶等）</td>
            </tr>
            
             <tr>
                <td class="export-td">150</td>
                <td class="export-td">ah</td>
                <td class="export-td">英:/ɑː/ 美:/'e 'etʃ/ </td>
                <td class="export-td">int. 啊；呀</td>
            </tr>
            
             <tr>
                <td class="export-td">151</td>
                <td class="export-td">aground</td>
                <td class="export-td">英:/ə'graʊnd/ 美:/ə'ɡraʊnd/ </td>
                <td class="export-td">1. adv. 搁浅地；地面上
2. adj. 搁浅的；地面上的</td>
            </tr>
            
             <tr>
                <td class="export-td">152</td>
                <td class="export-td">agronomist</td>
                <td class="export-td">英:/əˈ gr ɔnəmɪst/ 美:/ə'ɡrɑnəmɪst/ </td>
                <td class="export-td">农学家</td>
            </tr>
            
             <tr>
                <td class="export-td">153</td>
                <td class="export-td">agrochemical</td>
                <td class="export-td">英:/ægrəʊ'kemɪk(ə)l/ 美:/ˌæɡrokɛmɪkl/ </td>
                <td class="export-td">农用化学品</td>
            </tr>
            
             <tr>
                <td class="export-td">154</td>
                <td class="export-td">agritourism</td>
                <td class="export-td">英:/ˌægrɪˈtʊəˌɪzəm/ 美:/ˌæɡrɪˈtʊrˌɪzəm/ </td>
                <td class="export-td">农业旅游</td>
            </tr>
            
             <tr>
                <td class="export-td">155</td>
                <td class="export-td">agriculture</td>
                <td class="export-td">英:/'ægrɪkʌltʃə/ 美:/'æɡrɪkʌltʃɚ/ </td>
                <td class="export-td">农业</td>
            </tr>
            
             <tr>
                <td class="export-td">156</td>
                <td class="export-td">agribusiness</td>
                <td class="export-td">英:/'ægrɪbɪznɪs/ 美:/'æɡrɪbɪznəs/ </td>
                <td class="export-td">农业综合企业</td>
            </tr>
            
             <tr>
                <td class="export-td">157</td>
                <td class="export-td">agreement</td>
                <td class="export-td">英:/ə'griːm(ə)nt/ 美:/ə'grimənt/ </td>
                <td class="export-td">同意, 一致, 协议</td>
            </tr>
            
             <tr>
                <td class="export-td">158</td>
                <td class="export-td">agreeable</td>
                <td class="export-td">英:/ə'griːəb(ə)l/ 美:/ə'ɡriəbl/ </td>
                <td class="export-td">合适的</td>
            </tr>
            
             <tr>
                <td class="export-td">159</td>
                <td class="export-td">agree</td>
                <td class="export-td">英:/ə'griː/ 美:/ə'ɡri/ </td>
                <td class="export-td">1. vt. 同意；赞成；承认
2. vi. 同意；意见一致</td>
            </tr>
            
             <tr>
                <td class="export-td">160</td>
                <td class="export-td">agrarian</td>
                <td class="export-td">英:/ə'greərɪən/ 美:/ə'ɡrɛrɪən/ </td>
                <td class="export-td">adj. 土地的；耕地的；有关土地的</td>
            </tr>
            
             <tr>
                <td class="export-td">161</td>
                <td class="export-td">agoraphobia</td>
                <td class="export-td">英:/ˌæg(ə)rə'fəʊbɪə/ 美:/ˌæɡərə'fobɪə/ </td>
                <td class="export-td">广场恐怖症</td>
            </tr>
            
             <tr>
                <td class="export-td">162</td>
                <td class="export-td">agony</td>
                <td class="export-td">英:/'ægənɪ/ 美:/'æɡəni/ </td>
                <td class="export-td">n. 极大的痛苦；苦恼；临死的挣扎</td>
            </tr>
            
             <tr>
                <td class="export-td">163</td>
                <td class="export-td">agonizing</td>
                <td class="export-td">英:/ˈæ gənaɪzɪŋ/ 美:/'ægə'naɪzɪŋ/ </td>
                <td class="export-td">惨痛</td>
            </tr>
            
             <tr>
                <td class="export-td">164</td>
                <td class="export-td">agonized</td>
                <td class="export-td">/'æɡənaɪzd/ </td>
                <td class="export-td">1. adj. 感到极度痛苦的，苦闷的
2. v. 使极度痛苦（agonize的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">165</td>
                <td class="export-td">agonize</td>
                <td class="export-td">英:/ˈægəˌnaɪz/ 美:/'æɡənaɪz/ </td>
                <td class="export-td">1. vi. 感到极度痛苦；挣扎
2. vt. 使极度痛苦；折磨</td>
            </tr>
            
             <tr>
                <td class="export-td">166</td>
                <td class="export-td">agog</td>
                <td class="export-td">英:/ə'gɒg/ 美:/əˈɡɑɡ/ </td>
                <td class="export-td">1. adj. 兴奋的；有强烈兴趣的
2. adv. 热切地；渴望地</td>
            </tr>
            
             <tr>
                <td class="export-td">167</td>
                <td class="export-td">ago</td>
                <td class="export-td">英:/ə'gəʊ/ 美:/ə'ɡo/ </td>
                <td class="export-td">1. adv. 以前，以往
2. adj. 过去的；以前的</td>
            </tr>
            
             <tr>
                <td class="export-td">168</td>
                <td class="export-td">agnostic</td>
                <td class="export-td">英:/æg'nɒstɪk/ 美:/æg'nɑstɪk/ </td>
                <td class="export-td">1. n. [哲]不可知论者
2. adj. [哲]不可知论的</td>
            </tr>
            
             <tr>
                <td class="export-td">169</td>
                <td class="export-td">AGM</td>
                <td class="export-td">/ˌei dʒi: 'em/ </td>
                <td class="export-td">abbr. 空对地导弹（Air-to-Ground Missile）；美国音乐家协会（American Guild of Musicians）</td>
            </tr>
            
             <tr>
                <td class="export-td">170</td>
                <td class="export-td">aglow</td>
                <td class="export-td">英:/ə'gləʊ/ 美:/ə'ɡlo/ </td>
                <td class="export-td">1. adj. 通红的；发红的
2. adv. 发光地</td>
            </tr>
            
             <tr>
                <td class="export-td">171</td>
                <td class="export-td">agitator</td>
                <td class="export-td">英:/'ædʒɪteɪtə/ 美:/'ædʒɪtetɚ/ </td>
                <td class="export-td">n. 煽动者；搅拌器；鼓动者</td>
            </tr>
            
             <tr>
                <td class="export-td">172</td>
                <td class="export-td">agitated</td>
                <td class="export-td">英:/'ædʒɪteɪtɪd/ 美:/'ædʒɪtetɪd/ </td>
                <td class="export-td">1. adj. 激动的；焦虑的；表现不安的
2. v. 焦虑；鼓动（agitate的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">173</td>
                <td class="export-td">agitate</td>
                <td class="export-td">英:/'ædʒɪteɪt/ 美:/'ædʒə'tet/ </td>
                <td class="export-td">1. vt. 摇动；骚动；使…激动
2. vi. 煽动</td>
            </tr>
            
             <tr>
                <td class="export-td">174</td>
                <td class="export-td">agism</td>
                <td class="export-td">英:/'eidʒizəm/ 美:/ˈeˌdʒɪzəm/ </td>
                <td class="export-td">n. 歧视老年人（尤指在就业和住房方面）</td>
            </tr>
            
             <tr>
                <td class="export-td">175</td>
                <td class="export-td">agile</td>
                <td class="export-td">英:/'ædʒaɪl/ 美:/'ædʒl/ </td>
                <td class="export-td">adj. 敏捷的；机敏的；活泼的</td>
            </tr>
            
             <tr>
                <td class="export-td">176</td>
                <td class="export-td">aghast</td>
                <td class="export-td">英:/ə'gɑːst/ 美:/ə'ɡæst/ </td>
                <td class="export-td">adj. 吓呆的，惊骇的；吃惊的</td>
            </tr>
            
             <tr>
                <td class="export-td">177</td>
                <td class="export-td">aggrieved</td>
                <td class="export-td">英:/ə'griːvd/ 美:/ə'ɡrivd/ </td>
                <td class="export-td">委屈</td>
            </tr>
            
             <tr>
                <td class="export-td">178</td>
                <td class="export-td">aggressor</td>
                <td class="export-td">英:/ə'gresə/ 美:/ə'ɡrɛsɚ/ </td>
                <td class="export-td">侵略者</td>
            </tr>
            
             <tr>
                <td class="export-td">179</td>
                <td class="export-td">aggressive</td>
                <td class="export-td">英:/ə'gresɪv/ 美:/ə'ɡrɛsɪv/ </td>
                <td class="export-td">积极</td>
            </tr>
            
             <tr>
                <td class="export-td">180</td>
                <td class="export-td">aggression</td>
                <td class="export-td">英:/ə'greʃ(ə)n/ 美:/ə'ɡrɛʃən/ </td>
                <td class="export-td">侵略</td>
            </tr>
            
             <tr>
                <td class="export-td">181</td>
                <td class="export-td">aggregate</td>
                <td class="export-td">英:/'ægrɪgət/ 美:/'æɡrɪɡət/ </td>
                <td class="export-td">合计</td>
            </tr>
            
             <tr>
                <td class="export-td">182</td>
                <td class="export-td">aggravate</td>
                <td class="export-td">英:/'ægrəveɪt/ 美:/'æɡrəvet/ </td>
                <td class="export-td">加剧</td>
            </tr>
            
             <tr>
                <td class="export-td">183</td>
                <td class="export-td">agglomeration</td>
                <td class="export-td">英:/əglɒmə'reɪʃ(ə)n/ 美:/ə,ɡlɑmə'reʃən/ </td>
                <td class="export-td">n. 结块；凝聚；[化]附聚</td>
            </tr>
            
             <tr>
                <td class="export-td">184</td>
                <td class="export-td">age-old</td>
                <td class="export-td">英:/'eidʒəuld/ 美:/ˈedʒˈold/ </td>
                <td class="export-td">古老</td>
            </tr>
            
             <tr>
                <td class="export-td">185</td>
                <td class="export-td">agent</td>
                <td class="export-td">英:/'eɪdʒ(ə)nt/ 美:/'edʒənt/ </td>
                <td class="export-td">1. n. 代理人，代理商；药剂；特工
2. vt. 由…作中介；由…代理</td>
            </tr>
            
             <tr>
                <td class="export-td">186</td>
                <td class="export-td">agenda</td>
                <td class="export-td">英:/ə'dʒendə/ 美:/ə'dʒɛndə/ </td>
                <td class="export-td">n. 议程；日常工作事项</td>
            </tr>
            
             <tr>
                <td class="export-td">187</td>
                <td class="export-td">agency</td>
                <td class="export-td">英:/'eɪdʒ(ə)nsɪ/ 美:/'edʒənsi/ </td>
                <td class="export-td">n. 代理，中介；代理处，经销处</td>
            </tr>
            
             <tr>
                <td class="export-td">188</td>
                <td class="export-td">age limit</td>
                <td class="export-td"></td>
                <td class="export-td">年龄限制</td>
            </tr>
            
             <tr>
                <td class="export-td">189</td>
                <td class="export-td">ageless</td>
                <td class="export-td">英:/'eɪdʒlɪs/ 美:/'edʒləs/ </td>
                <td class="export-td">adj. 永恒的；不老的</td>
            </tr>
            
             <tr>
                <td class="export-td">190</td>
                <td class="export-td">ageism</td>
                <td class="export-td">英:/'eɪdʒɪz(ə)m/ 美:/'edʒ'ɪzəm/ </td>
                <td class="export-td">n. 对老年人的歧视</td>
            </tr>
            
             <tr>
                <td class="export-td">191</td>
                <td class="export-td">aged</td>
                <td class="export-td">英:/'eidʒid/ 美:/ˈedʒɪd/ </td>
                <td class="export-td">1. adj. 年老的；…岁的；老年人特有的
2. v. 变老；成熟；老化（age的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">192</td>
                <td class="export-td">age</td>
                <td class="export-td">英:/eɪdʒ/ 美:/edʒ/ </td>
                <td class="export-td">1. n. 年龄；时代；阶段；寿命，使用年限
2. vi. 变老；成熟</td>
            </tr>
            
             <tr>
                <td class="export-td">193</td>
                <td class="export-td">agate</td>
                <td class="export-td">英:/ˈeiɡət/ 美:/ˈæɡɪt/ </td>
                <td class="export-td">n. 玛瑙；玛瑙制工具</td>
            </tr>
            
             <tr>
                <td class="export-td">194</td>
                <td class="export-td">agar</td>
                <td class="export-td">英:/'eiɡə/ 美:/ˈeˌɡɑr/ </td>
                <td class="export-td">n. 琼脂（一种植物胶）</td>
            </tr>
            
             <tr>
                <td class="export-td">195</td>
                <td class="export-td">against</td>
                <td class="export-td">英:/ə'genst/ 美:/ə'ɡɛnst/ </td>
                <td class="export-td">1. prep. 反对，违反；靠；倚；防备
2. adj. 对立的；不利的</td>
            </tr>
            
             <tr>
                <td class="export-td">196</td>
                <td class="export-td">again</td>
                <td class="export-td">英:/ə'gen/ 美:/ə'ɡɛn/ </td>
                <td class="export-td">adv. 再一次；又，此外</td>
            </tr>
            
             <tr>
                <td class="export-td">197</td>
                <td class="export-td">afterwards</td>
                <td class="export-td">/'æftɚwɚdz/ </td>
                <td class="export-td">以后, 后来</td>
            </tr>
            
             <tr>
                <td class="export-td">198</td>
                <td class="export-td">afterthought</td>
                <td class="export-td">英:/'ɑːftəθɔːt/ 美:/'æftəθɔt/ </td>
                <td class="export-td">事后</td>
            </tr>
            
             <tr>
                <td class="export-td">199</td>
                <td class="export-td">aftertaste</td>
                <td class="export-td">英:/'ɑːftəteɪst/ 美:/'æftɚtest/ </td>
                <td class="export-td">回味</td>
            </tr>
            
             <tr>
                <td class="export-td">200</td>
                <td class="export-td">aftershock</td>
                <td class="export-td">英:/'ɑːftəʃɒk/ 美:/'æftəʃɑk/ </td>
                <td class="export-td">余震</td>
            </tr>
            
             <tr>
                <td class="export-td">201</td>
                <td class="export-td">aftershave</td>
                <td class="export-td">英:/'ɑːftəʃeɪv/ 美:/'æftə,ʃev/ </td>
                <td class="export-td">擦面液</td>
            </tr>
            
             <tr>
                <td class="export-td">202</td>
                <td class="export-td">afternoon</td>
                <td class="export-td">英:/ɑːftə'nuːn/ 美:/ˌæftɚ'nun/ </td>
                <td class="export-td">下午;下午好</td>
            </tr>
            
             <tr>
                <td class="export-td">203</td>
                <td class="export-td">aftermath</td>
                <td class="export-td">英:/'ɑːftəmæθ/ 美:/'æftəmæθ/ </td>
                <td class="export-td">后果</td>
            </tr>
            
             <tr>
                <td class="export-td">204</td>
                <td class="export-td">afterlife</td>
                <td class="export-td">英:/'ɑːftəlaɪf/ 美:/'æftəlaɪf/ </td>
                <td class="export-td">来世</td>
            </tr>
            
             <tr>
                <td class="export-td">205</td>
                <td class="export-td">aftereffect</td>
                <td class="export-td">英:/'ɑːftəɪ,fekt/ 美:/'æftəɪ,fɛkt/ </td>
                <td class="export-td">后效</td>
            </tr>
            
             <tr>
                <td class="export-td">206</td>
                <td class="export-td">afterbirth</td>
                <td class="export-td">英:/'ɑːftəbɜːθ/ 美:/'æftɚbɝθ/ </td>
                <td class="export-td">胞衣</td>
            </tr>
            
             <tr>
                <td class="export-td">207</td>
                <td class="export-td">after</td>
                <td class="export-td">英:/'ɑːftə/ 美:/'æftɚ/ </td>
                <td class="export-td">1. adv. 后来，以后
2. prep. 在……之后</td>
            </tr>
            
             <tr>
                <td class="export-td">208</td>
                <td class="export-td">aft</td>
                <td class="export-td">英:/ɑːft/ 美:/æft/ </td>
                <td class="export-td">1. adv. 在船尾；近船尾
2. n. [计]自动存款取款</td>
            </tr>
            
             <tr>
                <td class="export-td">209</td>
                <td class="export-td">Afro-Caribbean</td>
                <td class="export-td">英:/ˌæfrəʊˌkærəˈbi:ən/ 美:/ˌæfroˌkærəˈbiən/ </td>
                <td class="export-td">加勒比黑人</td>
            </tr>
            
             <tr>
                <td class="export-td">210</td>
                <td class="export-td">African American</td>
                <td class="export-td"></td>
                <td class="export-td">非裔美国人（指美国黑人）；非裔美籍（等于African American）</td>
            </tr>
            
             <tr>
                <td class="export-td">211</td>
                <td class="export-td">afresh</td>
                <td class="export-td">英:/ə'freʃ/ 美:/ə'frɛʃ/ </td>
                <td class="export-td">adv. 重新；再度</td>
            </tr>
            
             <tr>
                <td class="export-td">212</td>
                <td class="export-td">afraid</td>
                <td class="export-td">英:/ə'freɪd/ 美:/ə'fred/ </td>
                <td class="export-td">adj. 害怕的；担心的；恐怕</td>
            </tr>
            
             <tr>
                <td class="export-td">213</td>
                <td class="export-td">aforementioned</td>
                <td class="export-td">英:/əfɔː'menʃənd/ 美:/ə,fɔr'mɛnʃənd/ </td>
                <td class="export-td">上述的, 前述的</td>
            </tr>
            
             <tr>
                <td class="export-td">214</td>
                <td class="export-td">afoot</td>
                <td class="export-td">英:/ə'fʊt/ 美:/ə'fʊt/ </td>
                <td class="export-td">1. adj. 在进行中的；徒步的；准备中
2. adv. 在进行中，在准备中</td>
            </tr>
            
             <tr>
                <td class="export-td">215</td>
                <td class="export-td">afloat</td>
                <td class="export-td">英:/ə'fləʊt/ 美:/ə'flot/ </td>
                <td class="export-td">1. adj. 飘浮的；在海上的；浸满水的；在传播的
2. adv. 在海上；飘浮著；浸满水</td>
            </tr>
            
             <tr>
                <td class="export-td">216</td>
                <td class="export-td">afield</td>
                <td class="export-td">英:/ə'fiːld/ 美:/ə'fild/ </td>
                <td class="export-td">adv. 在战场上；去野外；在远处；远离著</td>
            </tr>
            
             <tr>
                <td class="export-td">217</td>
                <td class="export-td">affront</td>
                <td class="export-td">英:/ə'frʌnt/ 美:/ə'frʌnt/ </td>
                <td class="export-td">1. vt. 公开侮辱；冒犯，有意冒犯；面对
2. n. 轻蔑；公开侮辱</td>
            </tr>
            
             <tr>
                <td class="export-td">218</td>
                <td class="export-td">afforestation</td>
                <td class="export-td">/ə'fɔrəs'teʃən/ </td>
                <td class="export-td">造林</td>
            </tr>
            
             <tr>
                <td class="export-td">219</td>
                <td class="export-td">afford</td>
                <td class="export-td">英:/ə'fɔːd/ 美:/ə'fɔrd/ </td>
                <td class="export-td">vt. 给予，提供；买得起</td>
            </tr>
            
             <tr>
                <td class="export-td">220</td>
                <td class="export-td">affluent</td>
                <td class="export-td">英:/'æflʊənt/ 美:/'æfluənt/ </td>
                <td class="export-td">1. adj. 富裕的；丰富的；流畅的
2. n. 支流；富人</td>
            </tr>
            
             <tr>
                <td class="export-td">221</td>
                <td class="export-td">afflict</td>
                <td class="export-td">英:/ə'flɪkt/ 美:/ə'flɪkt/ </td>
                <td class="export-td">vt. 折磨；使痛苦；使苦恼</td>
            </tr>
            
             <tr>
                <td class="export-td">222</td>
                <td class="export-td">affix</td>
                <td class="export-td">英:/ə'fɪks/ 美:/ə'fɪks/ </td>
                <td class="export-td">1. vt. 粘上；署名；将罪责加之于
2. n. [语]词缀；附加物</td>
            </tr>
            
             <tr>
                <td class="export-td">223</td>
                <td class="export-td">affirmative</td>
                <td class="export-td">英:/ə'fɜːmətɪv/ 美:/ə'fɝmətɪv/ </td>
                <td class="export-td">肯定的, 正面的</td>
            </tr>
            
             <tr>
                <td class="export-td">224</td>
                <td class="export-td">affirm</td>
                <td class="export-td">英:/ə'fɜːm/ 美:/ə'fɝm/ </td>
                <td class="export-td">1. vt. 断言；肯定
2. vi. 断言；确认</td>
            </tr>
            
             <tr>
                <td class="export-td">225</td>
                <td class="export-td">affinity</td>
                <td class="export-td">英:/ə'fɪnɪtɪ/ 美:/ə'fɪnəti/ </td>
                <td class="export-td">n. 吸引力；姻亲关系；密切关系；类同</td>
            </tr>
            
             <tr>
                <td class="export-td">226</td>
                <td class="export-td">affiliate</td>
                <td class="export-td">英:/ə'fɪlɪeɪt/ 美:/ə'fɪlɪet/ </td>
                <td class="export-td">联盟</td>
            </tr>
            
             <tr>
                <td class="export-td">227</td>
                <td class="export-td">affidavit</td>
                <td class="export-td">英:/ˌæfɪ'deɪvɪt/ 美:/ˌæfə'devɪt/ </td>
                <td class="export-td">宣誓书</td>
            </tr>
            
             <tr>
                <td class="export-td">228</td>
                <td class="export-td">affective</td>
                <td class="export-td">英:/ə'fektɪv/ 美:/ə'fɛktɪv/ </td>
                <td class="export-td">情感</td>
            </tr>
            
             <tr>
                <td class="export-td">229</td>
                <td class="export-td">affectionate</td>
                <td class="export-td">英:/ə'fekʃ(ə)nət/ 美:/ə'fɛkʃənət/ </td>
                <td class="export-td">情深的,充满情爱的</td>
            </tr>
            
             <tr>
                <td class="export-td">230</td>
                <td class="export-td">affection</td>
                <td class="export-td">英:/ə'fekʃ(ə)n/ 美:/ə'fɛkʃən/ </td>
                <td class="export-td">感情</td>
            </tr>
            
             <tr>
                <td class="export-td">231</td>
                <td class="export-td">affected</td>
                <td class="export-td">英:/ə'fektɪd/ 美:/ə'fɛktɪd/ </td>
                <td class="export-td">1. adj. 假装的；做作的；受到影响的
2. vt. 影响；假装；使…感动（affect的过去式和过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">232</td>
                <td class="export-td">affect</td>
                <td class="export-td">英:/ə'fekt/ 美:/ə'fɛkt/ </td>
                <td class="export-td">1. vt. 影响；假装；感动；感染
2. vi. 倾向；喜欢</td>
            </tr>
            
             <tr>
                <td class="export-td">233</td>
                <td class="export-td">affair</td>
                <td class="export-td">英:/ə'feə/ 美:/ə'fɛr/ </td>
                <td class="export-td">n. 事情；事务；私事；（尤指关系不长久的）风流韵事</td>
            </tr>
            
             <tr>
                <td class="export-td">234</td>
                <td class="export-td">affable</td>
                <td class="export-td">英:/'æfəb(ə)l/ 美:/'æfəbl/ </td>
                <td class="export-td">adj. 和蔼可亲的；友善的</td>
            </tr>
            
             <tr>
                <td class="export-td">235</td>
                <td class="export-td">afar</td>
                <td class="export-td">英:/ə'fɑː/ 美:/əˈfɑr/ </td>
                <td class="export-td">adv. 遥远地；在远处</td>
            </tr>
            
             <tr>
                <td class="export-td">236</td>
                <td class="export-td">aetiology</td>
                <td class="export-td">英:/ˌiːtɪ'ɒlədʒɪ/ 美:/ˌitɪ'ɑlədʒi/ </td>
                <td class="export-td">病因</td>
            </tr>
            
             <tr>
                <td class="export-td">237</td>
                <td class="export-td">aesthetics</td>
                <td class="export-td">英:/iːs'θetɪks/ 美:/ɛs'θɛtɪks/ </td>
                <td class="export-td">美学，审美学</td>
            </tr>
            
             <tr>
                <td class="export-td">238</td>
                <td class="export-td">aesthete</td>
                <td class="export-td">英:/'iːsθiːt/ 美:/'ɛsθit/ </td>
                <td class="export-td">n. 唯美主义者；审美家</td>
            </tr>
            
             <tr>
                <td class="export-td">239</td>
                <td class="export-td">aesthetic</td>
                <td class="export-td">英:/iːs'θetɪk/ 美:/ɛs'θɛtɪk/ </td>
                <td class="export-td">审美的</td>
            </tr>
            
             <tr>
                <td class="export-td">240</td>
                <td class="export-td">aerospace</td>
                <td class="export-td">英:/'eərəspeɪs/ 美:/'ɛrospes/ </td>
                <td class="export-td">航天</td>
            </tr>
            
             <tr>
                <td class="export-td">241</td>
                <td class="export-td">aerosol</td>
                <td class="export-td">英:/'eərəsɒl/ 美:/'ɛrəsɔl/ </td>
                <td class="export-td">1. n. 喷雾器；气雾剂；浮质；气溶胶
2. adj. 喷雾器的；喷雾的</td>
            </tr>
            
             <tr>
                <td class="export-td">242</td>
                <td class="export-td">aeroplane</td>
                <td class="export-td">英:/'eərəpleɪn/ 美:/'ɛrə'plen/ </td>
                <td class="export-td">飞机</td>
            </tr>
            
             <tr>
                <td class="export-td">243</td>
                <td class="export-td">aeronautics</td>
                <td class="export-td">英:/eərə'nɔːtɪks/ 美:/ˌɛrə'nɔtɪks/ </td>
                <td class="export-td">航空学</td>
            </tr>
            
             <tr>
                <td class="export-td">244</td>
                <td class="export-td">aerodynamics</td>
                <td class="export-td">英:/ˌeərə(ʊ)daɪ'næmɪks/ 美:/'ɛrodaɪ'næmɪks/ </td>
                <td class="export-td">空气动力学</td>
            </tr>
            
             <tr>
                <td class="export-td">245</td>
                <td class="export-td">aerodrome</td>
                <td class="export-td">英:/'eərədrəʊm/ 美:/'ɛrə'drom/ </td>
                <td class="export-td">n. 飞机场；航空站</td>
            </tr>
            
             <tr>
                <td class="export-td">246</td>
                <td class="export-td">aerobics</td>
                <td class="export-td">英:/eəˈrəʊbɪks/ 美:/ɛ'robɪks/ </td>
                <td class="export-td">n. 有氧运动法；增氧健身法</td>
            </tr>
            
             <tr>
                <td class="export-td">247</td>
                <td class="export-td">aerobic</td>
                <td class="export-td">英:/eə'rəʊbɪk/ 美:/ɛ'robɪk/ </td>
                <td class="export-td">adj. 需氧的；增氧健身法的</td>
            </tr>
            
             <tr>
                <td class="export-td">248</td>
                <td class="export-td">aerial</td>
                <td class="export-td">英:/'eərɪəl/ 美:/'ɛrɪəl/ </td>
                <td class="export-td">1. adj. 空气的；空中的，航空的；空想的
2. n. 天线</td>
            </tr>
            
             <tr>
                <td class="export-td">249</td>
                <td class="export-td">aerate</td>
                <td class="export-td">英:/'eəreɪt/ 美:/'ɛret/ </td>
                <td class="export-td">vt. 充气；让空气进入；使暴露于空气中</td>
            </tr>
            
             <tr>
                <td class="export-td">250</td>
                <td class="export-td">aeon</td>
                <td class="export-td">英:/'iːən/ 美:/'iən/ </td>
                <td class="export-td">n. 万古，永世</td>
            </tr>
            
             <tr>
                <td class="export-td">251</td>
                <td class="export-td">Aeolian</td>
                <td class="export-td">英:/i:'əuliən/ 美:/iˈoliən/ </td>
                <td class="export-td">1. adj. 伊奥利亚（人）的；风神的
2. n. 伊奥利亚人（居住于希腊中部）；伊奥利亚语</td>
            </tr>
            
             <tr>
                <td class="export-td">252</td>
                <td class="export-td">adze</td>
                <td class="export-td">英:/ædz/ 美:/ædz/ </td>
                <td class="export-td">1. v. 以扁斧劈
2. n. 扁斧（等于adz）</td>
            </tr>
            
             <tr>
                <td class="export-td">253</td>
                <td class="export-td">advocate</td>
                <td class="export-td">英:/'ædvəkət/ 美:/'ædvəkət/ </td>
                <td class="export-td">1. vt. 提倡，主张，拥护
2. n. 提倡者；支持者；律师</td>
            </tr>
            
             <tr>
                <td class="export-td">254</td>
                <td class="export-td">advocacy</td>
                <td class="export-td">英:/'ædvəkəsɪ/ 美:/'ædvəkəsi/ </td>
                <td class="export-td">n. 拥护；主张；辩护</td>
            </tr>
            
             <tr>
                <td class="export-td">255</td>
                <td class="export-td">advisory</td>
                <td class="export-td">英:/əd'vaɪz(ə)rɪ/ 美:/əd'vaɪzəri/ </td>
                <td class="export-td">1. adj. 顾问的；咨询的；劝告的
2. n. 报告；公告</td>
            </tr>
            
             <tr>
                <td class="export-td">256</td>
                <td class="export-td">adviser</td>
                <td class="export-td">英:/ædˈvaɪzə/ 美:/əd'vaɪzɚ/ </td>
                <td class="export-td">n. 顾问；劝告者；指导教师（等于advisor）</td>
            </tr>
            
             <tr>
                <td class="export-td">257</td>
                <td class="export-td">advise</td>
                <td class="export-td">英:/əd'vaɪz/ 美:/əd'vaɪz/ </td>
                <td class="export-td">1. vt. 劝告，忠告；通知；警告；建议
2. vi. 建议；与…商量</td>
            </tr>
            
             <tr>
                <td class="export-td">258</td>
                <td class="export-td">advisable</td>
                <td class="export-td">英:/əd'vaɪzəb(ə)l/ 美:/əd'vaɪzəbl/ </td>
                <td class="export-td">明智的,可取的</td>
            </tr>
            
             <tr>
                <td class="export-td">259</td>
                <td class="export-td">advice</td>
                <td class="export-td">英:/əd'vaɪs/ 美:/əd'vaɪs/ </td>
                <td class="export-td">n. 通知；忠告；建议；劝告</td>
            </tr>
            
             <tr>
                <td class="export-td">260</td>
                <td class="export-td">advertorial</td>
                <td class="export-td">英:/ˌædvɜː'tɔːrɪəl/ 美:/ˌædvɚ'tɔrɪəl/ </td>
                <td class="export-td">软文广告</td>
            </tr>
            
             <tr>
                <td class="export-td">261</td>
                <td class="export-td">advertising</td>
                <td class="export-td">英:/'ædvətaɪzɪŋ/ 美:/'ædvɚ'taɪzɪŋ/ </td>
                <td class="export-td">广告业,广告</td>
            </tr>
            
             <tr>
                <td class="export-td">262</td>
                <td class="export-td">advertisement</td>
                <td class="export-td">英:/əd'vɜːtɪzm(ə)nt/ 美:/ˌædvɚ'taɪzmənt/ </td>
                <td class="export-td">广告</td>
            </tr>
            
             <tr>
                <td class="export-td">263</td>
                <td class="export-td">advertise</td>
                <td class="export-td">英:/'ædvətaɪz/ 美:/'ædvɚtaɪz/ </td>
                <td class="export-td">登广告</td>
            </tr>
            
             <tr>
                <td class="export-td">264</td>
                <td class="export-td">adversity</td>
                <td class="export-td">英:/əd'vɜːsɪtɪ/ 美:/əd'vɝsəti/ </td>
                <td class="export-td">不幸, 灾难</td>
            </tr>
            
             <tr>
                <td class="export-td">265</td>
                <td class="export-td">adverse</td>
                <td class="export-td">英:/'ædvɜːs/ 美:/'ædvɝs/ </td>
                <td class="export-td">adj. 不利的；相反的；敌对的（名词adverseness，副词adversely）</td>
            </tr>
            
             <tr>
                <td class="export-td">266</td>
                <td class="export-td">adversary</td>
                <td class="export-td">英:/'ædvəs(ə)rɪ/ 美:/'ædvɚsɛri/ </td>
                <td class="export-td">敌手, 对手</td>
            </tr>
            
             <tr>
                <td class="export-td">267</td>
                <td class="export-td">adverb</td>
                <td class="export-td">英:/'ædvɜːb/ 美:/'ædvɝb/ </td>
                <td class="export-td">1. n. 副词
2. adj. 副词的</td>
            </tr>
            
             <tr>
                <td class="export-td">268</td>
                <td class="export-td">adventurous</td>
                <td class="export-td">英:/əd'ventʃ(ə)rəs/ 美:/əd'vɛntʃərəs/ </td>
                <td class="export-td">爱冒险的</td>
            </tr>
            
             <tr>
                <td class="export-td">269</td>
                <td class="export-td">adventure</td>
                <td class="export-td">英:/əd'ventʃə/ 美:/əd'vɛntʃɚ/ </td>
                <td class="export-td">冒险,奇遇</td>
            </tr>
            
             <tr>
                <td class="export-td">270</td>
                <td class="export-td">advent</td>
                <td class="export-td">英:/'ædvənt/ 美:/ˈædˌvɛnt/ </td>
                <td class="export-td">n. 到来；出现；基督降临；基督降临节</td>
            </tr>
            
             <tr>
                <td class="export-td">271</td>
                <td class="export-td">advantageous</td>
                <td class="export-td">英:/ædvən'teɪdʒəs/ 美:/'ædvən'tedʒəs/ </td>
                <td class="export-td">有利</td>
            </tr>
            
             <tr>
                <td class="export-td">272</td>
                <td class="export-td">advantage</td>
                <td class="export-td">英:/əd'vɑːntɪdʒ/ 美:/əd'væntɪdʒ/ </td>
                <td class="export-td">优势,有利条件</td>
            </tr>
            
             <tr>
                <td class="export-td">273</td>
                <td class="export-td">advancement</td>
                <td class="export-td">英:/əd'vɑːnsm(ə)nt/ 美:/əd'vænsmənt/ </td>
                <td class="export-td">前进, 进步</td>
            </tr>
            
             <tr>
                <td class="export-td">274</td>
                <td class="export-td">advanced</td>
                <td class="export-td">英:/æd'vɑːnst/ 美:/əd'vænst/ </td>
                <td class="export-td">1. adj. 高级的；先进的；晚期的；年老的
2. v. 前进；增加；上涨（advance的过去式和过去分词形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">275</td>
                <td class="export-td">advance</td>
                <td class="export-td">英:/əd'vɑːns/ 美:/əd'væns/ </td>
                <td class="export-td">1. n. 前进；预付款；发展；增长
2. vt. 预付；提出；使……前进；将……提前</td>
            </tr>
            
             <tr>
                <td class="export-td">276</td>
                <td class="export-td">adulthood</td>
                <td class="export-td">/'ædʌlthʊd/ </td>
                <td class="export-td">成年</td>
            </tr>
            
             <tr>
                <td class="export-td">277</td>
                <td class="export-td">adultery</td>
                <td class="export-td">英:/ə'dʌlt(ə)rɪ/ 美:/ə'dʌltəri/ </td>
                <td class="export-td">n. 通奸，通奸行为</td>
            </tr>
            
             <tr>
                <td class="export-td">278</td>
                <td class="export-td">adulterate</td>
                <td class="export-td">英:/ə'dʌltəreɪt/ 美:/ə'dʌltəret/ </td>
                <td class="export-td">搀...使品质变劣</td>
            </tr>
            
             <tr>
                <td class="export-td">279</td>
                <td class="export-td">adult</td>
                <td class="export-td">英:/'ædʌlt/ 美:/'ædʌlt/ </td>
                <td class="export-td">成人</td>
            </tr>
            
             <tr>
                <td class="export-td">280</td>
                <td class="export-td">adulation</td>
                <td class="export-td">英:/ˌædʒəˈleɪʃən/ 美:/ˌædʒə'leʃən/ </td>
                <td class="export-td">n. 谄媚；奉承</td>
            </tr>
            
             <tr>
                <td class="export-td">281</td>
                <td class="export-td">ADSL</td>
                <td class="export-td"></td>
                <td class="export-td">abbr. 非对称数字用户环线（Asymmetrical Digital Subscriber Loop）</td>
            </tr>
            
             <tr>
                <td class="export-td">282</td>
                <td class="export-td">adroit</td>
                <td class="export-td">英:/ə'drɒɪt/ 美:/ə'drɔɪt/ </td>
                <td class="export-td">adj. 敏捷的，灵巧的；熟练的</td>
            </tr>
            
             <tr>
                <td class="export-td">283</td>
                <td class="export-td">adrift</td>
                <td class="export-td">英:/ə'drɪft/ 美:/ə'drɪft/ </td>
                <td class="export-td">1. adj. 漂浮着的；漂泊的
2. adv. 随波逐流地；漂浮着</td>
            </tr>
            
             <tr>
                <td class="export-td">284</td>
                <td class="export-td">adrenalin</td>
                <td class="export-td">英:/əˈdrenəlin/ 美:/ə'drɛnlən/ </td>
                <td class="export-td">肾上腺素</td>
            </tr>
            
             <tr>
                <td class="export-td">285</td>
                <td class="export-td">adrenal</td>
                <td class="export-td">英:/ə'driːn(ə)l/ 美:/æd'rinl/ </td>
                <td class="export-td">1. adj. 肾上腺的
2. n. 肾上腺</td>
            </tr>
            
             <tr>
                <td class="export-td">286</td>
                <td class="export-td">adorn</td>
                <td class="export-td">英:/ə'dɔːn/ 美:/ə'dɔrn/ </td>
                <td class="export-td">vt. 装饰；使生色</td>
            </tr>
            
             <tr>
                <td class="export-td">287</td>
                <td class="export-td">adore</td>
                <td class="export-td">英:/ə'dɔː/ 美:/ə'dɔr/ </td>
                <td class="export-td">1. vt. 爱慕；崇拜；喜爱；[口]极喜欢
2. vi. 爱慕；崇拜</td>
            </tr>
            
             <tr>
                <td class="export-td">288</td>
                <td class="export-td">adorable</td>
                <td class="export-td">英:/ə'dɔːrəb(ə)l/ 美:/ə'dɔrəbl/ </td>
                <td class="export-td">adj. 可爱的；可敬重的，值得崇拜的</td>
            </tr>
            
             <tr>
                <td class="export-td">289</td>
                <td class="export-td">adoptive</td>
                <td class="export-td">英:/ə'dɒptɪv/ 美:/ə'dɑptɪv/ </td>
                <td class="export-td">adj. 有收养关系的；采用的</td>
            </tr>
            
             <tr>
                <td class="export-td">290</td>
                <td class="export-td">adopt</td>
                <td class="export-td">英:/ə'dɒpt/ 美:/ə'dɑpt/ </td>
                <td class="export-td">1. vt. 收养；采取；接受；正式通过
2. vi. 过继；采取</td>
            </tr>
            
             <tr>
                <td class="export-td">291</td>
                <td class="export-td">adolescent</td>
                <td class="export-td">英:/ædə'les(ə)nt/ 美:/ˌædə'lɛsnt/ </td>
                <td class="export-td">青少年</td>
            </tr>
            
             <tr>
                <td class="export-td">292</td>
                <td class="export-td">adobe</td>
                <td class="export-td">英:/əˈdəubi/ 美:/əˈdobi/ </td>
                <td class="export-td">n. 土砖，砖坯</td>
            </tr>
            
             <tr>
                <td class="export-td">293</td>
                <td class="export-td">ado</td>
                <td class="export-td">英:/ə'duː/ 美:/ə'du/ </td>
                <td class="export-td">n. 忙乱，纷扰，麻烦</td>
            </tr>
            
             <tr>
                <td class="export-td">294</td>
                <td class="export-td">admittedly</td>
                <td class="export-td">英:/əd'mɪtɪdlɪ/ 美:/əd'mɪtɪdli/ </td>
                <td class="export-td">不可否认的，公认地</td>
            </tr>
            
             <tr>
                <td class="export-td">295</td>
                <td class="export-td">admittance</td>
                <td class="export-td">英:/əd'mɪt(ə)ns/ 美:/əd'mɪtns/ </td>
                <td class="export-td">入场权, 准入</td>
            </tr>
            
             <tr>
                <td class="export-td">296</td>
                <td class="export-td">admit</td>
                <td class="export-td">英:/əd'mɪt/ 美:/əd'mɪt/ </td>
                <td class="export-td">1. vt. 承认；准许进入；可容纳
2. vi. 承认；容许</td>
            </tr>
            
             <tr>
                <td class="export-td">297</td>
                <td class="export-td">admission</td>
                <td class="export-td">英:/əd'mɪʃ(ə)n/ 美:/əd'mɪʃən/ </td>
                <td class="export-td">承认</td>
            </tr>
            
             <tr>
                <td class="export-td">298</td>
                <td class="export-td">admissible</td>
                <td class="export-td">英:/əd'mɪsɪb(ə)l/ 美:/əd'mɪsəbl/ </td>
                <td class="export-td">受理</td>
            </tr>
            
             <tr>
                <td class="export-td">299</td>
                <td class="export-td">admiring</td>
                <td class="export-td">/əd'maɪrɪŋ/ </td>
                <td class="export-td">adj. 赞赏的，羡慕的</td>
            </tr>
            
             <tr>
                <td class="export-td">300</td>
                <td class="export-td">admirer</td>
                <td class="export-td">英:/ədˈmaɪərə/ 美:/əd'maɪərɚ/ </td>
                <td class="export-td">n. 赞赏者；钦佩者；爱慕者</td>
            </tr>
            
             <tr>
                <td class="export-td">301</td>
                <td class="export-td">admire</td>
                <td class="export-td">英:/əd'maɪə/ 美:/əd'maɪɚ/ </td>
                <td class="export-td">1. vt. 钦佩；赞美
2. vi. 钦佩；称赞</td>
            </tr>
            
             <tr>
                <td class="export-td">302</td>
                <td class="export-td">admiration</td>
                <td class="export-td">英:/ædmə'reɪʃ(ə)n/ 美:/ˌædmə'reʃən/ </td>
                <td class="export-td">钦佩, 赞赏</td>
            </tr>
            
             <tr>
                <td class="export-td">303</td>
                <td class="export-td">admiral</td>
                <td class="export-td">英:/'ædm(ə)r(ə)l/ 美:/'ædmərəl/ </td>
                <td class="export-td">n. 舰队司令；海军上将；旗舰</td>
            </tr>
            
             <tr>
                <td class="export-td">304</td>
                <td class="export-td">admirable</td>
                <td class="export-td">英:/'ædm(ə)rəb(ə)l/ 美:/'ædmərəbl/ </td>
                <td class="export-td">令人钦佩</td>
            </tr>
            
             <tr>
                <td class="export-td">305</td>
                <td class="export-td">administrator</td>
                <td class="export-td">英:/əd'mɪnɪstreɪtə/ 美:/əd'mɪnɪstretɚ/ </td>
                <td class="export-td">管理人,行政官</td>
            </tr>
            
             <tr>
                <td class="export-td">306</td>
                <td class="export-td">administrative</td>
                <td class="export-td">英:/əd'mɪnɪstrətɪv/ 美:/əd'mɪnɪstretɪv/ </td>
                <td class="export-td">行政的,管理的</td>
            </tr>
            
             <tr>
                <td class="export-td">307</td>
                <td class="export-td">administration</td>
                <td class="export-td">英:/ədmɪnɪ'streɪʃ(ə)n/ 美:/əd,mɪnɪ'streʃən/ </td>
                <td class="export-td">行政,管理,行政部门</td>
            </tr>
            
             <tr>
                <td class="export-td">308</td>
                <td class="export-td">administer</td>
                <td class="export-td">英:/əd'mɪnɪstə/ 美:/əd'mɪnɪstɚ/ </td>
                <td class="export-td">管理,执行,给与</td>
            </tr>
            
             <tr>
                <td class="export-td">309</td>
                <td class="export-td">adjustable spanner</td>
                <td class="export-td"></td>
                <td class="export-td">可调扳手；活络扳子</td>
            </tr>
            
             <tr>
                <td class="export-td">310</td>
                <td class="export-td">adjustable</td>
                <td class="export-td">英:/əˈdʒʌstəbl/ 美:/ə'dʒʌstəbl/ </td>
                <td class="export-td">可调整的</td>
            </tr>
            
             <tr>
                <td class="export-td">311</td>
                <td class="export-td">adjust</td>
                <td class="export-td">英:/ə'dʒʌst/ 美:/ə'dʒʌst/ </td>
                <td class="export-td">1. vt. 校准；调整，使…适合
2. vi. 调整，校准；适应</td>
            </tr>
            
             <tr>
                <td class="export-td">312</td>
                <td class="export-td">adjunct</td>
                <td class="export-td">英:/'ædʒʌŋ(k)t/ 美:/'ædʒʌŋkt/ </td>
                <td class="export-td">1. n. 修饰语；附属物；助手
2. adj. 附属的</td>
            </tr>
            
             <tr>
                <td class="export-td">313</td>
                <td class="export-td">adjudicator</td>
                <td class="export-td">/ə'dʒu:dikeitə/ </td>
                <td class="export-td">评判员</td>
            </tr>
            
             <tr>
                <td class="export-td">314</td>
                <td class="export-td">adjudicate</td>
                <td class="export-td">英:/ə'dʒuːdɪkeɪt/ 美:/ə'dʒudɪket/ </td>
                <td class="export-td">判决，裁定</td>
            </tr>
            
             <tr>
                <td class="export-td">315</td>
                <td class="export-td">adjourn</td>
                <td class="export-td">英:/ə'dʒɜːn/ 美:/ə'dʒɝn/ </td>
                <td class="export-td">1. vi. 休会；延期；换地方
2. vt. 推迟；使…中止；使…延期</td>
            </tr>
            
             <tr>
                <td class="export-td">316</td>
                <td class="export-td">adjoining</td>
                <td class="export-td">英:/ə'dʒɒɪnɪŋ/ 美:/ə'dʒɔɪnɪŋ/ </td>
                <td class="export-td">隔壁的</td>
            </tr>
            
             <tr>
                <td class="export-td">317</td>
                <td class="export-td">adjective</td>
                <td class="export-td">英:/'ædʒɪktɪv/ 美:/'ædʒɪktɪv/ </td>
                <td class="export-td">形容词</td>
            </tr>
            
             <tr>
                <td class="export-td">318</td>
                <td class="export-td">adjectival</td>
                <td class="export-td">英:/ˌædʒek'taɪvəl/ 美:/ˌædʒɪk'taɪvl/ </td>
                <td class="export-td">形容词</td>
            </tr>
            
             <tr>
                <td class="export-td">319</td>
                <td class="export-td">adjacent</td>
                <td class="export-td">英:/ə'dʒeɪs(ə)nt/ 美:/ə'dʒesnt/ </td>
                <td class="export-td">adj. 邻近的，毗连的</td>
            </tr>
            
             <tr>
                <td class="export-td">320</td>
                <td class="export-td">adipose</td>
                <td class="export-td">英:/'ædɪpəʊs/ 美:/'ædə'pos/ </td>
                <td class="export-td">1. adj. 脂肪的；肥胖的
2. n. 动物脂肪</td>
            </tr>
            
             <tr>
                <td class="export-td">321</td>
                <td class="export-td">ad infinitum</td>
                <td class="export-td">英:/ˏædˏɪnfɪˈnaɪtəm/ 美:/æd ˌɪnfəˈnaɪtəm/ </td>
                <td class="export-td">无限地；永久地；无止境地</td>
            </tr>
            
             <tr>
                <td class="export-td">322</td>
                <td class="export-td">adhesive</td>
                <td class="export-td">英:/əd'hiːsɪv/ 美:/əd'hisɪv/ </td>
                <td class="export-td">1. n. 粘合剂；胶黏剂
2. adj. 带粘性的；粘着的</td>
            </tr>
            
             <tr>
                <td class="export-td">323</td>
                <td class="export-td">adherent</td>
                <td class="export-td">英:/əd'hɪər(ə)nt/ 美:/əd'hɪrənt/ </td>
                <td class="export-td">1. n. 信徒；追随者
2. adj. 附着的；粘着的</td>
            </tr>
            
             <tr>
                <td class="export-td">324</td>
                <td class="export-td">adhere</td>
                <td class="export-td">英:/əd'hɪə/ 美:/əd'hɪr/ </td>
                <td class="export-td">1. vi. 坚持；粘着；依附；追随
2. vt. 使粘附</td>
            </tr>
            
             <tr>
                <td class="export-td">325</td>
                <td class="export-td">adequate</td>
                <td class="export-td">英:/'ædɪkwət/ 美:/ˈædɪkwɪt/ </td>
                <td class="export-td">adj. 适当的；胜任的；充足的</td>
            </tr>
            
             <tr>
                <td class="export-td">326</td>
                <td class="export-td">adept</td>
                <td class="export-td">英:/ə'dept/ 美:/ə'dɛpt/ </td>
                <td class="export-td">1. adj. 熟练的；擅长…的
2. n. 内行；能手</td>
            </tr>
            
             <tr>
                <td class="export-td">327</td>
                <td class="export-td">adenoids</td>
                <td class="export-td">英:/'ædɪnɒɪdz/ 美:/'ædn'ɔɪdz/ </td>
                <td class="export-td">n. [医]扁桃腺肥大；腺状肿大</td>
            </tr>
            
             <tr>
                <td class="export-td">328</td>
                <td class="export-td">adenine</td>
                <td class="export-td">英:/'ædɪniːn/ 美:/'ædənɪn/ </td>
                <td class="export-td">n. 腺嘌呤</td>
            </tr>
            
             <tr>
                <td class="export-td">329</td>
                <td class="export-td">address</td>
                <td class="export-td">英:/ə'dres/ 美:/ə'drɛs/ </td>
                <td class="export-td">1. vt. 写姓名地址；向…致辞；演说；从事；忙于
2. n. 地址；致辞；演讲；说话的技巧</td>
            </tr>
            
             <tr>
                <td class="export-td">330</td>
                <td class="export-td">additive</td>
                <td class="export-td">英:/'ædɪtɪv/ 美:/'ædətɪv/ </td>
                <td class="export-td">1. n. 添加剂，添加物
2. adj. 附加的；加法的</td>
            </tr>
            
             <tr>
                <td class="export-td">331</td>
                <td class="export-td">additional</td>
                <td class="export-td">英:/ə'dɪʃ(ə)n(ə)l/ 美:/ə'dɪʃənl/ </td>
                <td class="export-td">附加的, 另外的</td>
            </tr>
            
             <tr>
                <td class="export-td">332</td>
                <td class="export-td">addition</td>
                <td class="export-td">英:/ə'dɪʃ(ə)n/ 美:/ə'dɪʃən/ </td>
                <td class="export-td">n. 添加；增加物；加法</td>
            </tr>
            
             <tr>
                <td class="export-td">333</td>
                <td class="export-td">addictive</td>
                <td class="export-td">英:/ə'dɪktɪv/ 美:/ə'dɪktɪv/ </td>
                <td class="export-td">使人上瘾的</td>
            </tr>
            
             <tr>
                <td class="export-td">334</td>
                <td class="export-td">addict</td>
                <td class="export-td">英:/'ædɪkt/ 美:/'ædɪkt/ </td>
                <td class="export-td">1. n. 有瘾的人；入迷的人
2. vt. 使沉溺；使上瘾</td>
            </tr>
            
             <tr>
                <td class="export-td">335</td>
                <td class="export-td">adder</td>
                <td class="export-td">英:/'ædə/ 美:/'ædɚ/ </td>
                <td class="export-td">n. 加算器；蝰蛇（欧洲产的小毒蛇）；猪鼻蛇（北美产无毒的）</td>
            </tr>
            
             <tr>
                <td class="export-td">336</td>
                <td class="export-td">addendum</td>
                <td class="export-td">英:/ə'dendəm/ 美:/ə'dɛndəm/ </td>
                <td class="export-td">n. 附录，附件；补遗；附加物</td>
            </tr>
            
             <tr>
                <td class="export-td">337</td>
                <td class="export-td">added</td>
                <td class="export-td">/'ædɪd/ </td>
                <td class="export-td">1. adj. 额外的；更多的
2. v. 增加（add的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">338</td>
                <td class="export-td">add</td>
                <td class="export-td">英:/æd/ 美:/æd/ </td>
                <td class="export-td">1. vi. 加；增加；加起来；做加法
2. vt. 增加，添加；补充说；计算…总和</td>
            </tr>
            
             <tr>
                <td class="export-td">339</td>
                <td class="export-td">adaptor</td>
                <td class="export-td">英:/əˈdæptə/ 美:/ə'dæptɚ/ </td>
                <td class="export-td">n. （美）改编者；适配器；转接器（等于adapter）</td>
            </tr>
            
             <tr>
                <td class="export-td">340</td>
                <td class="export-td">adaptive</td>
                <td class="export-td">英:/ə'dæptɪv/ 美:/ə'dæptɪv/ </td>
                <td class="export-td">adj. 适应的，适合的</td>
            </tr>
            
             <tr>
                <td class="export-td">341</td>
                <td class="export-td">adapted</td>
                <td class="export-td">/ə'dæptɪd/ </td>
                <td class="export-td">1. adj. 适合的
2. v. 使适应，改编（adapt的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">342</td>
                <td class="export-td">adaptation</td>
                <td class="export-td">英:/ædəp'teɪʃ(ə)n/ 美:/ˌædæp'teʃən/ </td>
                <td class="export-td">适应</td>
            </tr>
            
             <tr>
                <td class="export-td">343</td>
                <td class="export-td">adaptable</td>
                <td class="export-td">英:/ə'dæptəb(ə)l/ 美:/ə'dæptəbl/ </td>
                <td class="export-td">适应能力强</td>
            </tr>
            
             <tr>
                <td class="export-td">344</td>
                <td class="export-td">adapt</td>
                <td class="export-td">英:/ə'dæpt/ 美:/ə'dæpt/ </td>
                <td class="export-td">1. vt. 改编；使适应
2. vi. 适应</td>
            </tr>
            
             <tr>
                <td class="export-td">345</td>
                <td class="export-td">adamant</td>
                <td class="export-td">英:/'ædəm(ə)nt/ 美:/'ædəmənt/ </td>
                <td class="export-td">1. adj. 坚定不移的；坚硬无比的；固执的，坚强的
2. n. 坚硬的东西；坚石</td>
            </tr>
            
             <tr>
                <td class="export-td">346</td>
                <td class="export-td">adagio</td>
                <td class="export-td">英:/ə'dɑː(d)ʒɪəʊ/ 美:/ə'dɑdʒɪo/ </td>
                <td class="export-td">1. n. 柔板；慢板乐章
2. adj. 缓慢的</td>
            </tr>
            
             <tr>
                <td class="export-td">347</td>
                <td class="export-td">adage</td>
                <td class="export-td">英:/'ædɪdʒ/ 美:/'ædɪdʒ/ </td>
                <td class="export-td">n. 格言，谚语；箴言</td>
            </tr>
            
             <tr>
                <td class="export-td">348</td>
                <td class="export-td">AD</td>
                <td class="export-td">英:/æd/ 美:/'e 'di/ </td>
                <td class="export-td">n. 公元</td>
            </tr>
            
             <tr>
                <td class="export-td">349</td>
                <td class="export-td">acute</td>
                <td class="export-td">英:/ə'kjuːt/ 美:/ə'kjut/ </td>
                <td class="export-td">adj. 严重的，急性的；激烈的；敏锐的；尖声的</td>
            </tr>
            
             <tr>
                <td class="export-td">350</td>
                <td class="export-td">acupuncturist</td>
                <td class="export-td">/'ækjupʌŋktʃərɪst/ </td>
                <td class="export-td">针灸师</td>
            </tr>
            
             <tr>
                <td class="export-td">351</td>
                <td class="export-td">acupuncture</td>
                <td class="export-td">英:/'ækjʊ,pʌŋ(k)tʃə/ 美:/'ækjupʌŋktʃɚ/ </td>
                <td class="export-td">针灸,针治</td>
            </tr>
            
             <tr>
                <td class="export-td">352</td>
                <td class="export-td">acumen</td>
                <td class="export-td">英:/'ækjʊmən/ 美:/əˈkjumən/ </td>
                <td class="export-td">n. 聪明，敏锐</td>
            </tr>
            
             <tr>
                <td class="export-td">353</td>
                <td class="export-td">actuary</td>
                <td class="export-td">英:/'æktʃʊərɪ/ 美:/'æktʃuɛri/ </td>
                <td class="export-td">n. 保险计算员；保险精算师</td>
            </tr>
            
             <tr>
                <td class="export-td">354</td>
                <td class="export-td">actually</td>
                <td class="export-td">英:/'æktjʊəlɪ/ 美:/'æktʃuəli/ </td>
                <td class="export-td">adv. 实际上；事实上</td>
            </tr>
            
             <tr>
                <td class="export-td">355</td>
                <td class="export-td">actual</td>
                <td class="export-td">英:/'æktʃʊəl/ 美:/'æktʃuəl/ </td>
                <td class="export-td">adj. 真实的，实际的；现行的，目前的</td>
            </tr>
            
             <tr>
                <td class="export-td">356</td>
                <td class="export-td">actress</td>
                <td class="export-td">英:/'æktrɪs/ 美:/'æktrəs/ </td>
                <td class="export-td">n. 女演员</td>
            </tr>
            
             <tr>
                <td class="export-td">357</td>
                <td class="export-td">actor</td>
                <td class="export-td">英:/'æktə/ 美:/'æktɚ/ </td>
                <td class="export-td">n. 行动者；男演员；作用物</td>
            </tr>
            
             <tr>
                <td class="export-td">358</td>
                <td class="export-td">activity</td>
                <td class="export-td">英:/æk'tɪvɪtɪ/ 美:/æk'tɪvəti/ </td>
                <td class="export-td">n. 活动；活跃；行动</td>
            </tr>
            
             <tr>
                <td class="export-td">359</td>
                <td class="export-td">activist</td>
                <td class="export-td">英:/ˈæktivist/ 美:/'æktɪvɪst/ </td>
                <td class="export-td">n. 积极分子；激进主义分子</td>
            </tr>
            
             <tr>
                <td class="export-td">360</td>
                <td class="export-td">active</td>
                <td class="export-td">英:/'æktɪv/ 美:/'æktɪv/ </td>
                <td class="export-td">1. adj. 主动的；有效的；积极的；活跃的；现役的
2. n. 主动语态；积极分子</td>
            </tr>
            
             <tr>
                <td class="export-td">361</td>
                <td class="export-td">activation</td>
                <td class="export-td">/ˌæktə'veʃən/ </td>
                <td class="export-td">激活，催化作用</td>
            </tr>
            
             <tr>
                <td class="export-td">362</td>
                <td class="export-td">activate</td>
                <td class="export-td">英:/'æktɪveɪt/ 美:/'æktə'vet/ </td>
                <td class="export-td">1. vt. 刺激；使活泼；使活动；使产生放射性
2. vi. 有活力；激活</td>
            </tr>
            
             <tr>
                <td class="export-td">363</td>
                <td class="export-td">action painting</td>
                <td class="export-td"></td>
                <td class="export-td">行动绘画；行为绘画；行动画派；动作画</td>
            </tr>
            
             <tr>
                <td class="export-td">364</td>
                <td class="export-td">action</td>
                <td class="export-td">英:/'ækʃ(ə)n/ 美:/'ækʃən/ </td>
                <td class="export-td">n. 行动；活动；功能；情节；战斗</td>
            </tr>
            
             <tr>
                <td class="export-td">365</td>
                <td class="export-td">actinium</td>
                <td class="export-td">英:/æk'tɪnɪəm/ 美:/æk'tɪnɪəm/ </td>
                <td class="export-td">n. 锕（元素符号Ac）</td>
            </tr>
            
             <tr>
                <td class="export-td">366</td>
                <td class="export-td">acting</td>
                <td class="export-td">英:/'æktɪŋ/ 美:/'æktɪŋ/ </td>
                <td class="export-td">1. adj. 代理的；装腔作势的
2. n. 演戏；演技；假装</td>
            </tr>
            
             <tr>
                <td class="export-td">367</td>
                <td class="export-td">act</td>
                <td class="export-td">英:/ækt/ 美:/ækt/ </td>
                <td class="export-td">1. vt. 扮演；装作，举动像
2. vi. 行动；扮演，充当；起作用，见效；假装，演戏；表现，举止</td>
            </tr>
            
             <tr>
                <td class="export-td">368</td>
                <td class="export-td">acrylic</td>
                <td class="export-td">英:/ə'krɪlɪk/ 美:/ə'krɪlɪk/ </td>
                <td class="export-td">adj. [化]丙烯酸的</td>
            </tr>
            
             <tr>
                <td class="export-td">369</td>
                <td class="export-td">across</td>
                <td class="export-td">英:/ə'krɒs/ 美:/ə'krɔs/ </td>
                <td class="export-td">1. prep. 穿过；横穿
2. adv. 在对面；横过</td>
            </tr>
            
             <tr>
                <td class="export-td">370</td>
                <td class="export-td">acropolis</td>
                <td class="export-td">英:/ə'krɔpəlis/ 美:/əˈkrɑpəlɪs/ </td>
                <td class="export-td">城堡, 雅典的卫城</td>
            </tr>
            
             <tr>
                <td class="export-td">371</td>
                <td class="export-td">acronym</td>
                <td class="export-td">英:/'ækrənɪm/ 美:/'ækrənɪm/ </td>
                <td class="export-td">n. 首字母缩略词</td>
            </tr>
            
             <tr>
                <td class="export-td">372</td>
                <td class="export-td">acrobatics</td>
                <td class="export-td">英:/ækrə'bætɪks/ 美:/ˌækrə'bætɪks/ </td>
                <td class="export-td">杂技，技巧</td>
            </tr>
            
             <tr>
                <td class="export-td">373</td>
                <td class="export-td">acrobatic</td>
                <td class="export-td">英:/ˌækrəˈbætɪk/ 美:/ˌækrə'bætɪk/ </td>
                <td class="export-td">杂技的</td>
            </tr>
            
             <tr>
                <td class="export-td">374</td>
                <td class="export-td">acrobat</td>
                <td class="export-td">英:/'ækrəbæt/ 美:/'ækrəbæt/ </td>
                <td class="export-td">n. 杂技演员，特技演员；随机应变者；翻云覆雨者，善变者</td>
            </tr>
            
             <tr>
                <td class="export-td">375</td>
                <td class="export-td">acrimony</td>
                <td class="export-td">英:/'ækrɪmənɪ/ 美:/ækrɪmoni/ </td>
                <td class="export-td">n. 辛辣；尖刻；严厉</td>
            </tr>
            
             <tr>
                <td class="export-td">376</td>
                <td class="export-td">acrimonious</td>
                <td class="export-td">英:/ˌækrɪ'məʊnɪəs/ 美:/ˌækrəˈmoniəs/ </td>
                <td class="export-td">尖刻的</td>
            </tr>
            
             <tr>
                <td class="export-td">377</td>
                <td class="export-td">acrid</td>
                <td class="export-td">英:/'ækrɪd/ 美:/'ækrɪd/ </td>
                <td class="export-td">adj. 刻薄的；辛辣的；苦的</td>
            </tr>
            
             <tr>
                <td class="export-td">378</td>
                <td class="export-td">acre</td>
                <td class="export-td">英:/ˈɑ:krə/ 美:/ˈekɚ/ </td>
                <td class="export-td">n. 英亩；土地，地产</td>
            </tr>
            
             <tr>
                <td class="export-td">379</td>
                <td class="export-td">acquittal</td>
                <td class="export-td">英:/ə'kwɪtəl/ 美:/ə'kwɪtl/ </td>
                <td class="export-td">开释, 宣告无罪</td>
            </tr>
            
             <tr>
                <td class="export-td">380</td>
                <td class="export-td">acquit</td>
                <td class="export-td">英:/ə'kwɪt/ 美:/ə'kwɪt/ </td>
                <td class="export-td">vt. 无罪释放；表现；脱卸义务和责任；清偿</td>
            </tr>
            
             <tr>
                <td class="export-td">381</td>
                <td class="export-td">acquisition</td>
                <td class="export-td">英:/ˌækwɪ'zɪʃ(ə)n/ 美:/ˌækwɪ'zɪʃən/ </td>
                <td class="export-td">获得, 所获之物</td>
            </tr>
            
             <tr>
                <td class="export-td">382</td>
                <td class="export-td">acquire</td>
                <td class="export-td">英:/ə'kwaɪə/ 美:/ə'kwaɪr/ </td>
                <td class="export-td">vt. 获得；学到；取得；捕获</td>
            </tr>
            
             <tr>
                <td class="export-td">383</td>
                <td class="export-td">acquiesce</td>
                <td class="export-td">英:/ˌækwɪ'es/ 美:/ˌækwiˈɛs/ </td>
                <td class="export-td">默许, 勉强同意</td>
            </tr>
            
             <tr>
                <td class="export-td">384</td>
                <td class="export-td">acquainted</td>
                <td class="export-td">英:/əˈkweɪntɪd/ 美:/ə'kwentɪd/ </td>
                <td class="export-td">熟悉</td>
            </tr>
            
             <tr>
                <td class="export-td">385</td>
                <td class="export-td">acquaintance</td>
                <td class="export-td">英:/ə'kweɪnt(ə)ns/ 美:/ə'kwentəns/ </td>
                <td class="export-td">熟人,相识,了解</td>
            </tr>
            
             <tr>
                <td class="export-td">386</td>
                <td class="export-td">acoustics</td>
                <td class="export-td">英:/ə'kuːstɪks/ 美:/ə'kustɪks/ </td>
                <td class="export-td">声学</td>
            </tr>
            
             <tr>
                <td class="export-td">387</td>
                <td class="export-td">acoustic</td>
                <td class="export-td">英:/ə'kuːstɪk/ 美:/ə'kʊstɪk/ </td>
                <td class="export-td">1. adj. 声学的；听觉的；音响的
2. n. 原声乐器；不用电传音的乐器</td>
            </tr>
            
             <tr>
                <td class="export-td">388</td>
                <td class="export-td">acorn</td>
                <td class="export-td">英:/'eɪkɔːn/ 美:/'ekɔrn/ </td>
                <td class="export-td">n. 橡子；橡实</td>
            </tr>
            
             <tr>
                <td class="export-td">389</td>
                <td class="export-td">acne</td>
                <td class="export-td">英:/'æknɪ/ 美:/'ækni/ </td>
                <td class="export-td">n. [医]痤疮，粉刺</td>
            </tr>
            
             <tr>
                <td class="export-td">390</td>
                <td class="export-td">acknowledgement</td>
                <td class="export-td">/ək'nɑlɪdʒmənt/ </td>
                <td class="export-td">承认, 确认</td>
            </tr>
            
             <tr>
                <td class="export-td">391</td>
                <td class="export-td">acknowledge</td>
                <td class="export-td">英:/ək'nɒlɪdʒ/ 美:/ək'nɑlɪdʒ/ </td>
                <td class="export-td">承认</td>
            </tr>
            
             <tr>
                <td class="export-td">392</td>
                <td class="export-td">acid test</td>
                <td class="export-td"></td>
                <td class="export-td">酸性试验；严峻的考验；决定性考验</td>
            </tr>
            
             <tr>
                <td class="export-td">393</td>
                <td class="export-td">acidity</td>
                <td class="export-td">英:/ə'sɪdɪtɪ/ 美:/ə'sɪdəti/ </td>
                <td class="export-td">n. 酸度；酸性；酸过多；胃酸过多</td>
            </tr>
            
             <tr>
                <td class="export-td">394</td>
                <td class="export-td">acidify</td>
                <td class="export-td">英:/ə'sɪdɪfaɪ/ 美:/ə'sɪdə'fai/ </td>
                <td class="export-td">1. vi. 酸化；变酸
2. vt. 使……成酸；使……酸化</td>
            </tr>
            
             <tr>
                <td class="export-td">395</td>
                <td class="export-td">acid</td>
                <td class="export-td">英:/'æsɪd/ 美:/'æsɪd/ </td>
                <td class="export-td">1. n. 酸，迷幻药
2. adj. 酸的，讽刺的，刻薄的</td>
            </tr>
            
             <tr>
                <td class="export-td">396</td>
                <td class="export-td">achilles tendon</td>
                <td class="export-td"></td>
                <td class="export-td">跟腱</td>
            </tr>
            
             <tr>
                <td class="export-td">397</td>
                <td class="export-td">acid rain</td>
                <td class="export-td"></td>
                <td class="export-td">酸雨</td>
            </tr>
            
             <tr>
                <td class="export-td">398</td>
                <td class="export-td">achievement</td>
                <td class="export-td">英:/ə'tʃiːvm(ə)nt/ 美:/ə'tʃivmənt/ </td>
                <td class="export-td">成就</td>
            </tr>
            
             <tr>
                <td class="export-td">399</td>
                <td class="export-td">achieve</td>
                <td class="export-td">英:/ə'tʃiːv/ 美:/ə'tʃiv/ </td>
                <td class="export-td">1. vt. 完成；达到
2. vi. 达到目的；如愿以偿</td>
            </tr>
            
             <tr>
                <td class="export-td">400</td>
                <td class="export-td">ache</td>
                <td class="export-td">英:/eɪk/ 美:/ek/ </td>
                <td class="export-td">1. vi. 疼痛；渴望
2. n. 疼痛</td>
            </tr>
            
             <tr>
                <td class="export-td">401</td>
                <td class="export-td">acetylene</td>
                <td class="export-td">英:/ə'setɪliːn/ 美:/ə'sɛtəlin/ </td>
                <td class="export-td">乙炔, 电石气</td>
            </tr>
            
             <tr>
                <td class="export-td">402</td>
                <td class="export-td">acetone</td>
                <td class="export-td">英:/'æsɪtəʊn/ 美:/'æsɪton/ </td>
                <td class="export-td">n. [化]丙酮</td>
            </tr>
            
             <tr>
                <td class="export-td">403</td>
                <td class="export-td">acetic acid</td>
                <td class="export-td"></td>
                <td class="export-td">[化]醋酸，乙酸</td>
            </tr>
            
             <tr>
                <td class="export-td">404</td>
                <td class="export-td">acetate</td>
                <td class="export-td">英:/'æsɪteɪt/ 美:/'æsɪtet/ </td>
                <td class="export-td">n. 醋酸盐；醋酸纤维素及其制成的产品</td>
            </tr>
            
             <tr>
                <td class="export-td">405</td>
                <td class="export-td">ace</td>
                <td class="export-td">英:/eɪs/ 美:/es/ </td>
                <td class="export-td">1. n. 幺点；直接得分的发球；佼佼者；（俚）最好的朋友
2. adj. 一流的，突出的</td>
            </tr>
            
             <tr>
                <td class="export-td">406</td>
                <td class="export-td">accustomed</td>
                <td class="export-td">英:/ə'kʌstəmd/ 美:/ə'kʌstəmd/ </td>
                <td class="export-td">习惯了的,通常的</td>
            </tr>
            
             <tr>
                <td class="export-td">407</td>
                <td class="export-td">accustom</td>
                <td class="export-td">英:/ə'kʌstəm/ 美:/ə'kʌstəm/ </td>
                <td class="export-td">vt. 使习惯于</td>
            </tr>
            
             <tr>
                <td class="export-td">408</td>
                <td class="export-td">accusing</td>
                <td class="export-td">/ə'kjuzɪŋ/ </td>
                <td class="export-td">1. adj. 指责的；非难的；归咎的
2. v. 指责；指控（accuse的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">409</td>
                <td class="export-td">the accused</td>
                <td class="export-td"></td>
                <td class="export-td">被告</td>
            </tr>
            
             <tr>
                <td class="export-td">410</td>
                <td class="export-td">accuse</td>
                <td class="export-td">英:/ə'kjuːz/ 美:/ə'kjuz/ </td>
                <td class="export-td">1. vt. 控告，指控；谴责；归咎于
2. vi. 控告；指责</td>
            </tr>
            
             <tr>
                <td class="export-td">411</td>
                <td class="export-td">accusatory</td>
                <td class="export-td">英:/ə'kjuːzət(ə)rɪ/ 美:/ə'kjuzətɔri/ </td>
                <td class="export-td">非难的</td>
            </tr>
            
             <tr>
                <td class="export-td">412</td>
                <td class="export-td">accusative</td>
                <td class="export-td">英:/ə'kjuːzətɪv/ 美:/ə'kjuzətɪv/ </td>
                <td class="export-td">宾格</td>
            </tr>
            
             <tr>
                <td class="export-td">413</td>
                <td class="export-td">accusation</td>
                <td class="export-td">英:/ækjʊ'zeɪʃ(ə)n/ 美:/ˌækju'zeʃən/ </td>
                <td class="export-td">控告,指控,非难</td>
            </tr>
            
             <tr>
                <td class="export-td">414</td>
                <td class="export-td">accurate</td>
                <td class="export-td">英:/'ækjʊrət/ 美:/'ækjərət/ </td>
                <td class="export-td">adj. 精确的</td>
            </tr>
            
             <tr>
                <td class="export-td">415</td>
                <td class="export-td">accumulate</td>
                <td class="export-td">英:/ə'kjuːmjʊleɪt/ 美:/ə'kjumjəlet/ </td>
                <td class="export-td">积聚,累加,堆积</td>
            </tr>
            
             <tr>
                <td class="export-td">416</td>
                <td class="export-td">accrue</td>
                <td class="export-td">英:/ə'kruː/ 美:/ə'kru/ </td>
                <td class="export-td">1. vi. 自然增长或利益增加；产生
2. vt. 积累；获得</td>
            </tr>
            
             <tr>
                <td class="export-td">417</td>
                <td class="export-td">accredited</td>
                <td class="export-td">/ə'kreditid/ </td>
                <td class="export-td">认证</td>
            </tr>
            
             <tr>
                <td class="export-td">418</td>
                <td class="export-td">accounts payable</td>
                <td class="export-td"></td>
                <td class="export-td">应付帐款</td>
            </tr>
            
             <tr>
                <td class="export-td">419</td>
                <td class="export-td">accounting</td>
                <td class="export-td">英:/ə'kaʊntɪŋ/ 美:/ə'kaʊntɪŋ/ </td>
                <td class="export-td">会计</td>
            </tr>
            
             <tr>
                <td class="export-td">420</td>
                <td class="export-td">accountant</td>
                <td class="export-td">英:/ə'kaʊnt(ə)nt/ 美:/ə'kaʊntənt/ </td>
                <td class="export-td">会计人员</td>
            </tr>
            
             <tr>
                <td class="export-td">421</td>
                <td class="export-td">accountancy</td>
                <td class="export-td">英:/ə'kaʊnt(ə)nsɪ/ 美:/ə'kaʊntənsi/ </td>
                <td class="export-td">会计</td>
            </tr>
            
             <tr>
                <td class="export-td">422</td>
                <td class="export-td">accountable</td>
                <td class="export-td">英:/ə'kaʊntəb(ə)l/ 美:/ə'kaʊntəbl/ </td>
                <td class="export-td">负有责任的</td>
            </tr>
            
             <tr>
                <td class="export-td">423</td>
                <td class="export-td">account</td>
                <td class="export-td">英:/ə'kaʊnt/ 美:/ə'kaʊnt/ </td>
                <td class="export-td">1. n. 帐目，帐单；理由；帐户；解释
2. vi. 报帐；解释；导致</td>
            </tr>
            
             <tr>
                <td class="export-td">424</td>
                <td class="export-td">accost</td>
                <td class="export-td">英:/ə'kɒst/ 美:/ə'kɔst/ </td>
                <td class="export-td">vt. 勾引；引诱；对…说话；搭讪</td>
            </tr>
            
             <tr>
                <td class="export-td">425</td>
                <td class="export-td">accordion</td>
                <td class="export-td">英:/ə'kɔːdɪən/ 美:/ə'kɔrdɪən/ </td>
                <td class="export-td">手风琴</td>
            </tr>
            
             <tr>
                <td class="export-td">426</td>
                <td class="export-td">according to</td>
                <td class="export-td"></td>
                <td class="export-td">根据，按照；取决于；据…所说</td>
            </tr>
            
             <tr>
                <td class="export-td">427</td>
                <td class="export-td">accordingly</td>
                <td class="export-td">英:/ə'kɔːdɪŋlɪ/ 美:/ə'kɔrdɪŋli/ </td>
                <td class="export-td">从而</td>
            </tr>
            
             <tr>
                <td class="export-td">428</td>
                <td class="export-td">accordance</td>
                <td class="export-td">英:/ə'kɔːd(ə)ns/ 美:/ə'kɔrdns/ </td>
                <td class="export-td">符合,同意</td>
            </tr>
            
             <tr>
                <td class="export-td">429</td>
                <td class="export-td">accord</td>
                <td class="export-td">英:/ə'kɔːd/ 美:/ə'kɔrd/ </td>
                <td class="export-td">1. n. 一致；符合；协议；自愿
2. vt. 使一致；给予</td>
            </tr>
            
             <tr>
                <td class="export-td">430</td>
                <td class="export-td">accomplishment</td>
                <td class="export-td">英:/ə'kʌmplɪʃm(ə)nt/ 美:/ə'kɑmplɪʃmənt/ </td>
                <td class="export-td">成就,完成</td>
            </tr>
            
             <tr>
                <td class="export-td">431</td>
                <td class="export-td">accomplished</td>
                <td class="export-td">英:/ə'kʌmplɪʃt/ 美:/ə'kɑmplɪʃt/ </td>
                <td class="export-td">完成</td>
            </tr>
            
             <tr>
                <td class="export-td">432</td>
                <td class="export-td">accomplish</td>
                <td class="export-td">英:/ə'kʌmplɪʃ/ 美:/ə'kɑmplɪʃ/ </td>
                <td class="export-td">完成</td>
            </tr>
            
             <tr>
                <td class="export-td">433</td>
                <td class="export-td">accomplice</td>
                <td class="export-td">英:/ə'kʌmplɪs/ 美:/ə'kɑmplɪs/ </td>
                <td class="export-td">共犯, 同谋，帮凶</td>
            </tr>
            
             <tr>
                <td class="export-td">434</td>
                <td class="export-td">accompany</td>
                <td class="export-td">英:/ə'kʌmpənɪ/ 美:/ə'kʌmpəni/ </td>
                <td class="export-td">陪</td>
            </tr>
            
             <tr>
                <td class="export-td">435</td>
                <td class="export-td">accompanist</td>
                <td class="export-td">英:/ə'kʌmpənɪst/ 美:/ə'kʌmpənɪst/ </td>
                <td class="export-td">伴奏</td>
            </tr>
            
             <tr>
                <td class="export-td">436</td>
                <td class="export-td">accompaniment</td>
                <td class="export-td">英:/ə'kʌmp(ə)nɪm(ə)nt/ 美:/ə'kʌmpənɪmənt/ </td>
                <td class="export-td">伴奏</td>
            </tr>
            
             <tr>
                <td class="export-td">437</td>
                <td class="export-td">accommodation</td>
                <td class="export-td">英:/əkɒmə'deɪʃ(ə)n/ 美:/ə,kɑmə'deʃən/ </td>
                <td class="export-td">住处,膳宿</td>
            </tr>
            
             <tr>
                <td class="export-td">438</td>
                <td class="export-td">accommodating</td>
                <td class="export-td">英:/ə'kɒmədeɪtɪŋ/ 美:/ə'kɑmədetɪŋ/ </td>
                <td class="export-td">包容</td>
            </tr>
            
             <tr>
                <td class="export-td">439</td>
                <td class="export-td">accommodate</td>
                <td class="export-td">英:/ə'kɒmədeɪt/ 美:/ə'kɑmədet/ </td>
                <td class="export-td">使自己适应</td>
            </tr>
            
             <tr>
                <td class="export-td">440</td>
                <td class="export-td">accolade</td>
                <td class="export-td">英:/'ækəleɪd/ 美:/'ækəled/ </td>
                <td class="export-td">n. 荣誉称号授予仪式；荣誉；连谱号；称赞</td>
            </tr>
            
             <tr>
                <td class="export-td">441</td>
                <td class="export-td">acclimatize</td>
                <td class="export-td">英:/əˈklaɪməˌtaɪz/ 美:/ə'klaɪmətaɪz/ </td>
                <td class="export-td">适应新环境</td>
            </tr>
            
             <tr>
                <td class="export-td">442</td>
                <td class="export-td">acclamation</td>
                <td class="export-td">英:/ˌæklə'meɪʃ(ə)n/ 美:/ˌæklə'meʃən/ </td>
                <td class="export-td">n. 欢呼，喝彩；鼓掌欢呼表示通过</td>
            </tr>
            
             <tr>
                <td class="export-td">443</td>
                <td class="export-td">acclaim</td>
                <td class="export-td">英:/ə'kleɪm/ 美:/ə'klem/ </td>
                <td class="export-td">1. vt. 称赞；为…喝采，向…欢呼
2. n. 称赞；欢呼，喝彩</td>
            </tr>
            
             <tr>
                <td class="export-td">444</td>
                <td class="export-td">accident-prone</td>
                <td class="export-td">英:/'æksidənt,prəun/ 美:/ˈæksɪdəntˌpron/ </td>
                <td class="export-td">事故多发</td>
            </tr>
            
             <tr>
                <td class="export-td">445</td>
                <td class="export-td">accidental</td>
                <td class="export-td">英:/æksɪ'dent(ə)l/ 美:/ˌæksɪ'dɛntl/ </td>
                <td class="export-td">偶然</td>
            </tr>
            
             <tr>
                <td class="export-td">446</td>
                <td class="export-td">accident</td>
                <td class="export-td">英:/'æksɪdənt/ 美:/'æksədənt/ </td>
                <td class="export-td">n. 事故；机遇；意外事件；意外</td>
            </tr>
            
             <tr>
                <td class="export-td">447</td>
                <td class="export-td">accessory</td>
                <td class="export-td">英:/ək'ses(ə)rɪ/ 美:/ək'sɛsəri/ </td>
                <td class="export-td">附属的</td>
            </tr>
            
             <tr>
                <td class="export-td">448</td>
                <td class="export-td">accession</td>
                <td class="export-td">英:/ək'seʃ(ə)n/ 美:/æk'sɛʃən/ </td>
                <td class="export-td">到达, 即位, 加入</td>
            </tr>
            
             <tr>
                <td class="export-td">449</td>
                <td class="export-td">accessible</td>
                <td class="export-td">英:/ək'sesɪb(ə)l/ 美:/ək'sɛsəbl/ </td>
                <td class="export-td">访问</td>
            </tr>
            
             <tr>
                <td class="export-td">450</td>
                <td class="export-td">assess</td>
                <td class="export-td">英:/ə'ses/ 美:/ə'sɛs/ </td>
                <td class="export-td">vt. 评定；估价；对…征税</td>
            </tr>
            
             <tr>
                <td class="export-td">451</td>
                <td class="export-td">acceptance</td>
                <td class="export-td">英:/ək'sept(ə)ns/ 美:/ək'sɛptəns/ </td>
                <td class="export-td">接受 ，同意，认可</td>
            </tr>
            
             <tr>
                <td class="export-td">452</td>
                <td class="export-td">acceptable</td>
                <td class="export-td">英:/ək'septəb(ə)l/ 美:/ək'sɛptəbl/ </td>
                <td class="export-td">接受</td>
            </tr>
            
             <tr>
                <td class="export-td">453</td>
                <td class="export-td">accept</td>
                <td class="export-td">英:/ək'sept/ 美:/ək'sɛpt/ </td>
                <td class="export-td">1. vt. 接受；承认；承担；承兑；容纳
2. vi. 同意；承认；承兑</td>
            </tr>
            
             <tr>
                <td class="export-td">454</td>
                <td class="export-td">accentuate</td>
                <td class="export-td">英:/ək'sentʃʊeɪt/ 美:/ək'sɛntʃuet/ </td>
                <td class="export-td">强调</td>
            </tr>
            
             <tr>
                <td class="export-td">455</td>
                <td class="export-td">accent</td>
                <td class="export-td">英:/'æks(ə)nt/ 美:/'æksɛnt/ </td>
                <td class="export-td">1. n. 口音；重音；重音符号；强调；特点
2. vt. 重读；强调；带…口音讲话</td>
            </tr>
            
             <tr>
                <td class="export-td">456</td>
                <td class="export-td">accelerator</td>
                <td class="export-td">英:/ək'seləreɪtə/ 美:/ək'sɛlə'retɚ/ </td>
                <td class="export-td">加速器</td>
            </tr>
            
             <tr>
                <td class="export-td">457</td>
                <td class="export-td">accelerate</td>
                <td class="export-td">英:/ək'seləreɪt/ 美:/ək'sɛləret/ </td>
                <td class="export-td">加速,提前,跳级</td>
            </tr>
            
             <tr>
                <td class="export-td">458</td>
                <td class="export-td">accelerando</td>
                <td class="export-td">英:/ək,selə'rændəʊ/ 美:/æk,sɛlə'rændo/ </td>
                <td class="export-td">渐快</td>
            </tr>
            
             <tr>
                <td class="export-td">459</td>
                <td class="export-td">academy</td>
                <td class="export-td">英:/ə'kædəmɪ/ 美:/ə'kædəmi/ </td>
                <td class="export-td">n. 学会；学院；研究院；专科院校</td>
            </tr>
            
             <tr>
                <td class="export-td">460</td>
                <td class="export-td">academician</td>
                <td class="export-td">英:/ə,kædə'mɪʃ(ə)n/ 美:/ˌækədə'mɪʃən/ </td>
                <td class="export-td">院士</td>
            </tr>
            
             <tr>
                <td class="export-td">461</td>
                <td class="export-td">academic</td>
                <td class="export-td">英:/ækə'demɪk/ 美:/ˌækə'dɛmɪk/ </td>
                <td class="export-td">1. adj. 学院的；学术的；理论的
2. n. 大学生，大学教师；学者</td>
            </tr>
            
             <tr>
                <td class="export-td">462</td>
                <td class="export-td">acacia</td>
                <td class="export-td">英:/ə'keɪʃə/ 美:/ə'keʃə/ </td>
                <td class="export-td">n. [植]阿拉伯树胶；刺槐；金合欢属植物</td>
            </tr>
            
             <tr>
                <td class="export-td">463</td>
                <td class="export-td">abyssal</td>
                <td class="export-td">英:/ə'bisəl/ 美:/əˈbɪsəl/ </td>
                <td class="export-td">adj. 深不可测的；深渊的，深海的</td>
            </tr>
            
             <tr>
                <td class="export-td">464</td>
                <td class="export-td">abyss</td>
                <td class="export-td">英:/ə'bɪs/ 美:/ə'bɪs/ </td>
                <td class="export-td">n. 深渊；深邃，无底洞</td>
            </tr>
            
             <tr>
                <td class="export-td">465</td>
                <td class="export-td">abysmal</td>
                <td class="export-td">英:/ə'bɪzm(ə)l/ 美:/ə'bɪzməl/ </td>
                <td class="export-td">adj. 深不可测的；极度的；糟透的</td>
            </tr>
            
             <tr>
                <td class="export-td">466</td>
                <td class="export-td">abusive</td>
                <td class="export-td">英:/ə'bjuːsɪv/ 美:/ə'bjʊsɪv/ </td>
                <td class="export-td">adj. 辱骂的；滥用的；虐待的</td>
            </tr>
            
             <tr>
                <td class="export-td">467</td>
                <td class="export-td">abuse</td>
                <td class="export-td">英:/ə'bjuːz/ 美:/ə'bjus/ </td>
                <td class="export-td">1. n. 滥用；辱骂；虐待；弊端；恶习，陋习
2. vt. 滥用；辱骂；虐待</td>
            </tr>
            
             <tr>
                <td class="export-td">468</td>
                <td class="export-td">abundant</td>
                <td class="export-td">英:/ə'bʌnd(ə)nt/ 美:/ə'bʌndənt/ </td>
                <td class="export-td">adj. 充裕的；丰富的；盛产</td>
            </tr>
            
             <tr>
                <td class="export-td">469</td>
                <td class="export-td">abundance</td>
                <td class="export-td">英:/ə'bʌnd(ə)ns/ 美:/ə'bʌndəns/ </td>
                <td class="export-td">丰富,充裕</td>
            </tr>
            
             <tr>
                <td class="export-td">470</td>
                <td class="export-td">abstract expressionism</td>
                <td class="export-td"></td>
                <td class="export-td">n. 抽象表现主义</td>
            </tr>
            
             <tr>
                <td class="export-td">471</td>
                <td class="export-td">absurd</td>
                <td class="export-td">英:/əb'sɜːd/ 美:/əb'sɝd/ </td>
                <td class="export-td">1. adj. 荒谬的；可笑的
2. n. 荒诞；荒诞作品</td>
            </tr>
            
             <tr>
                <td class="export-td">472</td>
                <td class="export-td">abstraction</td>
                <td class="export-td">英:/əb'strækʃ(ə)n/ 美:/æb'strækʃən/ </td>
                <td class="export-td">抽象化</td>
            </tr>
            
             <tr>
                <td class="export-td">473</td>
                <td class="export-td">abstract art</td>
                <td class="export-td"></td>
                <td class="export-td">n. 抽象主义；抽象派</td>
            </tr>
            
             <tr>
                <td class="export-td">474</td>
                <td class="export-td">abstinence</td>
                <td class="export-td">英:/'æbstɪnəns/ 美:/'æbstɪnəns/ </td>
                <td class="export-td">节制, 禁食, 戒酒</td>
            </tr>
            
             <tr>
                <td class="export-td">475</td>
                <td class="export-td">abstention</td>
                <td class="export-td">英:/əb'stenʃ(ə)n/ 美:/əb'stɛnʃən/ </td>
                <td class="export-td">弃权</td>
            </tr>
            
             <tr>
                <td class="export-td">476</td>
                <td class="export-td">abstainer</td>
                <td class="export-td">/əb'steinə/ </td>
                <td class="export-td">戒酒</td>
            </tr>
            
             <tr>
                <td class="export-td">477</td>
                <td class="export-td">abstain</td>
                <td class="export-td">英:/əb'steɪn/ 美:/əb'sten/ </td>
                <td class="export-td">vi. 放弃；自制；避免</td>
            </tr>
            
             <tr>
                <td class="export-td">478</td>
                <td class="export-td">absorption</td>
                <td class="export-td">英:/əb'zɔːpʃ(ə)n/ 美:/əb'sɔrpʃən/ </td>
                <td class="export-td">吸收,全神贯注</td>
            </tr>
            
             <tr>
                <td class="export-td">479</td>
                <td class="export-td">absorbing</td>
                <td class="export-td">英:/əb'zɔːbɪŋ/ 美:/əb'sɔrbɪŋ/ </td>
                <td class="export-td">吸收</td>
            </tr>
            
             <tr>
                <td class="export-td">480</td>
                <td class="export-td">absorbent</td>
                <td class="export-td">英:/əb'zɔːb(ə)nt/ 美:/əb'sɔrbənt/ </td>
                <td class="export-td">能吸收的</td>
            </tr>
            
             <tr>
                <td class="export-td">481</td>
                <td class="export-td">absorbed</td>
                <td class="export-td">英:/əb'sɔːbd/ 美:/əb'sɔrbd/ </td>
                <td class="export-td">1. adj. 一心一意的；被吸收的
2. v. 吸收；使全神贯注（absorb的过去分词形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">482</td>
                <td class="export-td">absorb</td>
                <td class="export-td">英:/əb'sɔ:b/ 美:/əbˈsɔrb/ </td>
                <td class="export-td">vt. 吸收；吸引；承受；理解；使…全神贯注</td>
            </tr>
            
             <tr>
                <td class="export-td">483</td>
                <td class="export-td">absolve</td>
                <td class="export-td">英:/əb'zɒlv/ 美:/əb'zɑlv/ </td>
                <td class="export-td">vt. 宣告…无罪；赦免；免除</td>
            </tr>
            
             <tr>
                <td class="export-td">484</td>
                <td class="export-td">absolution</td>
                <td class="export-td">英:/æbsə'luːʃ(ə)n/ 美:/ˌæbsə'luʃən/ </td>
                <td class="export-td">免罪, 赦罪</td>
            </tr>
            
             <tr>
                <td class="export-td">485</td>
                <td class="export-td">absolute majority</td>
                <td class="export-td"></td>
                <td class="export-td">绝对多数</td>
            </tr>
            
             <tr>
                <td class="export-td">486</td>
                <td class="export-td">absolute zero</td>
                <td class="export-td"></td>
                <td class="export-td">绝对零度</td>
            </tr>
            
             <tr>
                <td class="export-td">487</td>
                <td class="export-td">absolutely</td>
                <td class="export-td">英:/'æbsəlju:tli/ 美:/ˈæbsəˌlutli/ </td>
                <td class="export-td">绝对地,完全地</td>
            </tr>
            
             <tr>
                <td class="export-td">488</td>
                <td class="export-td">absolute</td>
                <td class="export-td">英:/'æbsəluːt/ 美:/'æbsəlut/ </td>
                <td class="export-td">1. adj. 绝对的；完全的；专制的
2. n. 绝对事物；绝对</td>
            </tr>
            
             <tr>
                <td class="export-td">489</td>
                <td class="export-td">absentminded</td>
                <td class="export-td">/'æbsənt'maindid/ </td>
                <td class="export-td">恍惚</td>
            </tr>
            
             <tr>
                <td class="export-td">490</td>
                <td class="export-td">absenteeism</td>
                <td class="export-td">英:/æbs(ə)n'tiːɪz(ə)m/ 美:/ˌæbsən'tiɪzəm/ </td>
                <td class="export-td">旷工</td>
            </tr>
            
             <tr>
                <td class="export-td">491</td>
                <td class="export-td">absentee</td>
                <td class="export-td">英:/ˌæbs(ə)n'tiː/ 美:/ˌæbsən'ti/ </td>
                <td class="export-td">n. 缺席者</td>
            </tr>
            
             <tr>
                <td class="export-td">492</td>
                <td class="export-td">absent</td>
                <td class="export-td">英:/'æbs(ə)nt/ 美:/æb'sɛnt/ </td>
                <td class="export-td">1. adj. 缺席的；缺少的；心不在焉的；茫然的
2. vt. 使缺席</td>
            </tr>
            
             <tr>
                <td class="export-td">493</td>
                <td class="export-td">absence</td>
                <td class="export-td">英:/'æbs(ə)ns/ 美:/'æbsns/ </td>
                <td class="export-td">n. 缺席；缺乏；没有；不注意</td>
            </tr>
            
             <tr>
                <td class="export-td">494</td>
                <td class="export-td">abseil</td>
                <td class="export-td">英:/'æbseɪl/ 美:/'æzaɪl/ </td>
                <td class="export-td">n. 沿绳滑下法</td>
            </tr>
            
             <tr>
                <td class="export-td">495</td>
                <td class="export-td">abscond</td>
                <td class="export-td">英:/əb'skɒnd/ 美:/əb'skɑnd/ </td>
                <td class="export-td">vi. 逃匿，潜逃；避债</td>
            </tr>
            
             <tr>
                <td class="export-td">496</td>
                <td class="export-td">abscess</td>
                <td class="export-td">英:/'æbsɪs/ 美:/'æb'sɛs/ </td>
                <td class="export-td">1. n. 脓肿；脓疮
2. vi. 形成脓肿</td>
            </tr>
            
             <tr>
                <td class="export-td">497</td>
                <td class="export-td">ABS</td>
                <td class="export-td">/æbz/ </td>
                <td class="export-td">abbr. 美国圣经协会（American Bible Society）；防滑煞车系统（Anti-skid Brake System）；美国标准局（American Bureau of Standards）；丙烯腈-丁二烯-苯乙烯（Acrylonitrile Butadiene StyreneAcrylonitrile Butadiene Styrene）</td>
            </tr>
            
             <tr>
                <td class="export-td">498</td>
                <td class="export-td">abrupt</td>
                <td class="export-td">英:/ə'brʌpt/ 美:/ə'brʌpt/ </td>
                <td class="export-td">adj. 突然的；唐突的；陡峭的；生硬的</td>
            </tr>
            
             <tr>
                <td class="export-td">499</td>
                <td class="export-td">abroad</td>
                <td class="export-td">英:/ə'brɔːd/ 美:/ə'brɔd/ </td>
                <td class="export-td">1. adv. 到海外；在国外
2. adj. 往国外的</td>
            </tr>
            
             <tr>
                <td class="export-td">500</td>
                <td class="export-td">abridge</td>
                <td class="export-td">英:/ə'brɪdʒ/ 美:/ə'brɪdʒ/ </td>
                <td class="export-td">vt. 删节；缩短；节略</td>
            </tr>
            
             <tr>
                <td class="export-td">501</td>
                <td class="export-td">abreast</td>
                <td class="export-td">英:/ə'brest/ 美:/ə'brɛst/ </td>
                <td class="export-td">1. adv. 并肩地；并列
2. adj. 并排的；肩并肩的</td>
            </tr>
            
             <tr>
                <td class="export-td">502</td>
                <td class="export-td">abrasive</td>
                <td class="export-td">英:/ə'breɪsɪv/ 美:/ə'bresɪv/ </td>
                <td class="export-td">1. adj. 有研磨作用的；粗糙的；伤人感情的
2. n. 研磨料</td>
            </tr>
            
             <tr>
                <td class="export-td">503</td>
                <td class="export-td">abrasion</td>
                <td class="export-td">英:/ə'breɪʒ(ə)n/ 美:/ə'breʒən/ </td>
                <td class="export-td">n. 磨损；擦伤；磨耗</td>
            </tr>
            
             <tr>
                <td class="export-td">504</td>
                <td class="export-td">above-the-line</td>
                <td class="export-td">/ə'bʌvðə,lain/ </td>
                <td class="export-td">上面的线</td>
            </tr>
            
             <tr>
                <td class="export-td">505</td>
                <td class="export-td">above-mentioned</td>
                <td class="export-td">英:/ə,bʌv'menʃənd/ 美:/əˈbʌvˌmɛnʃənd/ </td>
                <td class="export-td">上述</td>
            </tr>
            
             <tr>
                <td class="export-td">506</td>
                <td class="export-td">above</td>
                <td class="export-td">英:/ə'bʌv/ 美:/ə'bʌv/ </td>
                <td class="export-td">1. prep. 在……上面；在……之上；超过
2. adv. 在上面；在上文</td>
            </tr>
            
             <tr>
                <td class="export-td">507</td>
                <td class="export-td">about-turn</td>
                <td class="export-td">/ə'baut,tə:n/ </td>
                <td class="export-td">关于转</td>
            </tr>
            
             <tr>
                <td class="export-td">508</td>
                <td class="export-td">about</td>
                <td class="export-td">英:/ə'baʊt/ 美:/ə'baʊt/ </td>
                <td class="export-td">1. prep. 关于；大约
2. adj. 四处走动的；在起作用的；在附近的</td>
            </tr>
            
             <tr>
                <td class="export-td">509</td>
                <td class="export-td">abound</td>
                <td class="export-td">英:/ə'baʊnd/ 美:/ə'baʊnd/ </td>
                <td class="export-td">vi. 充满；富于</td>
            </tr>
            
             <tr>
                <td class="export-td">510</td>
                <td class="export-td">abortive</td>
                <td class="export-td">英:/ə'bɔːtɪv/ 美:/ə'bɔrtɪv/ </td>
                <td class="export-td">adj. 失败的；流产的；堕胎的</td>
            </tr>
            
             <tr>
                <td class="export-td">511</td>
                <td class="export-td">abortionist</td>
                <td class="export-td">英:/ə'bɔːʃ(ə)nɪst/ 美:/ə'bɔrʃənɪst/ </td>
                <td class="export-td">堕胎</td>
            </tr>
            
             <tr>
                <td class="export-td">512</td>
                <td class="export-td">abortion</td>
                <td class="export-td">英:/ə'bɔːʃ(ə)n/ 美:/ə'bɔrʃən/ </td>
                <td class="export-td">n. 流产，小产；流产的胎儿</td>
            </tr>
            
             <tr>
                <td class="export-td">513</td>
                <td class="export-td">abort</td>
                <td class="export-td">英:/ə'bɔːt/ 美:/ə'bɔrt/ </td>
                <td class="export-td">1. vi. 流产；夭折；发育不全；堕胎
2. vt. 使流产；使中止</td>
            </tr>
            
             <tr>
                <td class="export-td">514</td>
                <td class="export-td">aborigine</td>
                <td class="export-td">英:/æbə'rɪdʒɪniː/ 美:/'æbə'rɪdʒəni/ </td>
                <td class="export-td">原住民</td>
            </tr>
            
             <tr>
                <td class="export-td">515</td>
                <td class="export-td">aboriginal</td>
                <td class="export-td">英:/æbə'rɪdʒɪn(ə)l/ 美:/ˌæbə'rɪdʒənl/ </td>
                <td class="export-td">原始的, 土著的</td>
            </tr>
            
             <tr>
                <td class="export-td">516</td>
                <td class="export-td">abominable</td>
                <td class="export-td">英:/ə'bɒm(ə)nəb(ə)l/ 美:/ə'bɑmɪnəbl/ </td>
                <td class="export-td">讨厌的, 令人憎恶的</td>
            </tr>
            
             <tr>
                <td class="export-td">517</td>
                <td class="export-td">abolition</td>
                <td class="export-td">英:/æbə'lɪʃ(ə)n/ 美:/ˌæbə'lɪʃən/ </td>
                <td class="export-td">废除, 废止</td>
            </tr>
            
             <tr>
                <td class="export-td">518</td>
                <td class="export-td">abolish</td>
                <td class="export-td">英:/ə'bɒlɪʃ/ 美:/ə'bɑlɪʃ/ </td>
                <td class="export-td">vt. 废除，废止；取消，革除</td>
            </tr>
            
             <tr>
                <td class="export-td">519</td>
                <td class="export-td">abode</td>
                <td class="export-td">英:/ə'bəʊd/ 美:/ə'bod/ </td>
                <td class="export-td">1. n. 住处；营业所
2. v. 遵守；停留；忍受（abide的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">520</td>
                <td class="export-td">aboard</td>
                <td class="export-td">英:/ə'bɔːd/ 美:/ə'bɔrd/ </td>
                <td class="export-td">1. adv. 在火车上；在飞机上；在船上
2. prep. 在…上</td>
            </tr>
            
             <tr>
                <td class="export-td">521</td>
                <td class="export-td">abnormality</td>
                <td class="export-td">英:/æbnɔː'mælɪtɪ/ 美:/ˌæbnɔr'mæləti/ </td>
                <td class="export-td">异常</td>
            </tr>
            
             <tr>
                <td class="export-td">522</td>
                <td class="export-td">abnormal</td>
                <td class="export-td">英:/əb'nɔːm(ə)l/ 美:/æb'nɔrml/ </td>
                <td class="export-td">adj. 反常的，不规则的；变态的</td>
            </tr>
            
             <tr>
                <td class="export-td">523</td>
                <td class="export-td">able-bodied</td>
                <td class="export-td">英:/'eibl'bɔdid/ 美:/ˈebəlˈbɑdid/ </td>
                <td class="export-td">健全</td>
            </tr>
            
             <tr>
                <td class="export-td">524</td>
                <td class="export-td">able</td>
                <td class="export-td">英:/'eɪb(ə)l/ 美:/'ebl/ </td>
                <td class="export-td">adj. 能干的；有能力的；能</td>
            </tr>
            
             <tr>
                <td class="export-td">525</td>
                <td class="export-td">ablaze</td>
                <td class="export-td">英:/ə'bleɪz/ 美:/ə'blez/ </td>
                <td class="export-td">1. adj. 着火的；闪耀的；激昂的
2. adv. 着火；闪耀</td>
            </tr>
            
             <tr>
                <td class="export-td">526</td>
                <td class="export-td">ablation</td>
                <td class="export-td">英:/æbˈleiʃən/ 美:/ə'bleʃən/ </td>
                <td class="export-td">n. 切除；消融</td>
            </tr>
            
             <tr>
                <td class="export-td">527</td>
                <td class="export-td">abject</td>
                <td class="export-td">英:/'æbdʒekt/ 美:/'æbdʒɛkt/ </td>
                <td class="export-td">adj. 不幸的；卑鄙的；可怜的</td>
            </tr>
            
             <tr>
                <td class="export-td">528</td>
                <td class="export-td">abide</td>
                <td class="export-td">英:/ə'baɪd/ 美:/ə'baɪd/ </td>
                <td class="export-td">1. vt. 忍受，容忍；停留
2. vi. 持续；停留；忍受</td>
            </tr>
            
             <tr>
                <td class="export-td">529</td>
                <td class="export-td">abhorrent</td>
                <td class="export-td">英:/əb'hɒr(ə)nt/ 美:/əb'hɔrənt/ </td>
                <td class="export-td">可恶</td>
            </tr>
            
             <tr>
                <td class="export-td">530</td>
                <td class="export-td">abhorrence</td>
                <td class="export-td">英:/əb'hɒr(ə)ns/ 美:/əb'hɔrəns/ </td>
                <td class="export-td">可憎恶的人 , 憎恶</td>
            </tr>
            
             <tr>
                <td class="export-td">531</td>
                <td class="export-td">abhor</td>
                <td class="export-td">英:/əb'hɔː/ 美:/əb'hɔr/ </td>
                <td class="export-td">vt. 痛恨，憎恶</td>
            </tr>
            
             <tr>
                <td class="export-td">532</td>
                <td class="export-td">abet</td>
                <td class="export-td">英:/ə'bet/ 美:/ə'bɛt/ </td>
                <td class="export-td">vt. 煽动，教唆；支持</td>
            </tr>
            
             <tr>
                <td class="export-td">533</td>
                <td class="export-td">aberration</td>
                <td class="export-td">英:/ˌæbə'reɪʃ(ə)n/ 美:/'æbə'reʃən/ </td>
                <td class="export-td">越轨，误差，偏差</td>
            </tr>
            
             <tr>
                <td class="export-td">534</td>
                <td class="export-td">abduct</td>
                <td class="export-td">英:/əb'dʌkt/ 美:/æb'dʌkt/ </td>
                <td class="export-td">vt. 诱拐；绑架；[生]使外展</td>
            </tr>
            
             <tr>
                <td class="export-td">535</td>
                <td class="export-td">abdomen</td>
                <td class="export-td">英:/'æbdəmən/ 美:/'æbdəmən/ </td>
                <td class="export-td">n. 腹部；下腹；腹腔</td>
            </tr>
            
             <tr>
                <td class="export-td">536</td>
                <td class="export-td">abdicate</td>
                <td class="export-td">英:/'æbdɪkeɪt/ 美:/'æbdɪket/ </td>
                <td class="export-td">1. vi. 退位；放弃
2. vt. 退位；放弃</td>
            </tr>
            
             <tr>
                <td class="export-td">537</td>
                <td class="export-td">ABC</td>
                <td class="export-td">/'e 'bi 'si/ </td>
                <td class="export-td">1. n. 基础知识；字母表
2. abbr. 美国广播公司（American Broadcasting Company）；澳大利亚广播公司（Australian Broadcasting Corporation）；出生在美国的华人（American - born Chinese）</td>
            </tr>
            
             <tr>
                <td class="export-td">538</td>
                <td class="export-td">abbr</td>
                <td class="export-td"></td>
                <td class="export-td">缩写</td>
            </tr>
            
             <tr>
                <td class="export-td">539</td>
                <td class="export-td">abbot</td>
                <td class="export-td">英:/'æbət/ 美:/'æbət/ </td>
                <td class="export-td">n. 男修道院院长；大寺院男住持</td>
            </tr>
            
             <tr>
                <td class="export-td">540</td>
                <td class="export-td">abbess</td>
                <td class="export-td">英:/'æbes/ 美:/'æbɛs/ </td>
                <td class="export-td">n. 女修道院院长；女庵主持</td>
            </tr>
            
             <tr>
                <td class="export-td">541</td>
                <td class="export-td">abstract</td>
                <td class="export-td">英:/'æbstrækt/ 美:/'æbstrækt/ </td>
                <td class="export-td">1. n. 抽象；摘要；抽象的概念
2. adj. 抽象的；深奥的</td>
            </tr>
            
             <tr>
                <td class="export-td">542</td>
                <td class="export-td">ability</td>
                <td class="export-td">英:/ə'bɪlɪtɪ/ 美:/ə'bɪləti/ </td>
                <td class="export-td">n. 能力，能耐；才能</td>
            </tr>
            
             <tr>
                <td class="export-td">543</td>
                <td class="export-td">abandoned</td>
                <td class="export-td">英:/ə'bænd(ə)nd/ 美:/ə'bændənd/ </td>
                <td class="export-td">弃</td>
            </tr>
            
             <tr>
                <td class="export-td">544</td>
                <td class="export-td">abbreviation</td>
                <td class="export-td">英:/əbriːvɪ'eɪʃ(ə)n/ 美:/ə'brivɪ'eʃən/ </td>
                <td class="export-td">缩写</td>
            </tr>
            
             <tr>
                <td class="export-td">545</td>
                <td class="export-td">abbreviate</td>
                <td class="export-td">英:/ə'briːvɪeɪt/ 美:/ə'brivɪ'et/ </td>
                <td class="export-td">简略</td>
            </tr>
            
             <tr>
                <td class="export-td">546</td>
                <td class="export-td">abbey</td>
                <td class="export-td">英:/ˈæbi/ 美:/ˈæbi/ </td>
                <td class="export-td">n. 大修道院，大寺院；修道院中全体修士或修女</td>
            </tr>
            
             <tr>
                <td class="export-td">547</td>
                <td class="export-td">abattoir</td>
                <td class="export-td">英:/'æbətwɑː/ 美:/ˈæbəˌtwɑr/ </td>
                <td class="export-td">n. 角斗场；屠宰场</td>
            </tr>
            
             <tr>
                <td class="export-td">548</td>
                <td class="export-td">abashed</td>
                <td class="export-td">/ə'bæʃt/ </td>
                <td class="export-td">adj. 不安的；窘迫的；尴尬的</td>
            </tr>
            
             <tr>
                <td class="export-td">549</td>
                <td class="export-td">abate</td>
                <td class="export-td">英:/ə'beɪt/ 美:/ə'bet/ </td>
                <td class="export-td">1. vt. 减少；减轻；废除
2. vi. 减轻；失效</td>
            </tr>
            
             <tr>
                <td class="export-td">550</td>
                <td class="export-td">abacus</td>
                <td class="export-td">英:/'æbəkəs/ 美:/'æbəkəs/ </td>
                <td class="export-td">n. 算盘</td>
            </tr>
            
             <tr>
                <td class="export-td">551</td>
                <td class="export-td">aback</td>
                <td class="export-td">英:/ə'bæk/ 美:/ə'bæk/ </td>
                <td class="export-td">adv. 向后；处于顶风位置；向后地</td>
            </tr>
            
             <tr>
                <td class="export-td">552</td>
                <td class="export-td">abalone</td>
                <td class="export-td">英:/ˌæbə'ləʊnɪ/ 美:/ˌæbə'loni/ </td>
                <td class="export-td">n. 鲍鱼</td>
            </tr>
            
             <tr>
                <td class="export-td">553</td>
                <td class="export-td">abandon</td>
                <td class="export-td">英:/ə'bænd(ə)n/ 美:/ə'bændən/ </td>
                <td class="export-td">1. n. 狂热，放任
2. vt. 遗弃，放弃</td>
            </tr>"""
    items = get_word_from_html(html)
    for item in items:
        print(item)


if __name__ == "__main__":
    main()