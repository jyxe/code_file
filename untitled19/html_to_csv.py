import re
import pandas as pda
import csv

print("please input the file_name:",end="")
file_name = input()
fileName="D:\\job_data"+"\\"+str(file_name)+".csv"

def get_word_from_html(html):
    parttern = re.compile('<td.*?>.*?</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>',re.S)
    items = re.findall(parttern,html)
    number = 1
    words = []
    for item in items:
        yield {
            "a_word":item[0],
            "b_alphabet":item[1],
            "c_meaning":item[2]
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
    html="""<tr>
                <td class="export-td">1</td>
                <td class="export-td">inappropriate</td>
                <td class="export-td">英:/ɪnə'prəʊprɪət/ 美:/'ɪnə'proprɪət/ </td>
                <td class="export-td">不适当的,不相称的</td>
            </tr>
            
             <tr>
                <td class="export-td">2</td>
                <td class="export-td">inadequate</td>
                <td class="export-td">英:/ɪn'ædɪkwət/ 美:/ɪn'ædɪkwət/ </td>
                <td class="export-td">不充分的,不适当的</td>
            </tr>
            
             <tr>
                <td class="export-td">3</td>
                <td class="export-td">inaccurate</td>
                <td class="export-td">英:/ɪn'ækjʊrət/ 美:/ɪn'ækjərət/ </td>
                <td class="export-td">不准确的，错误的</td>
            </tr>
            
             <tr>
                <td class="export-td">4</td>
                <td class="export-td">inability</td>
                <td class="export-td">英:/ɪnə'bɪlɪtɪ/ 美:/ˌɪnə'bɪləti/ </td>
                <td class="export-td">无能,无力</td>
            </tr>
            
             <tr>
                <td class="export-td">5</td>
                <td class="export-td">impulsive</td>
                <td class="export-td">英:/ɪm'pʌlsɪv/ 美:/ɪm'pʌlsɪv/ </td>
                <td class="export-td">浮躁</td>
            </tr>
            
             <tr>
                <td class="export-td">6</td>
                <td class="export-td">improbable</td>
                <td class="export-td">英:/ɪm'prɒbəb(ə)l/ 美:/ɪm'prɑbəbl/ </td>
                <td class="export-td">adj. 不可信的；未必会发生的；不大可能的，未必确实的</td>
            </tr>
            
             <tr>
                <td class="export-td">7</td>
                <td class="export-td">imprisonable</td>
                <td class="export-td">/ɪm'prɪznəbl/ </td>
                <td class="export-td">坐牢</td>
            </tr>
            
             <tr>
                <td class="export-td">8</td>
                <td class="export-td">impractical</td>
                <td class="export-td">英:/ɪm'præktɪk(ə)l/ 美:/ɪm'præktɪkl/ </td>
                <td class="export-td">不切实际</td>
            </tr>
            
             <tr>
                <td class="export-td">9</td>
                <td class="export-td">impolite</td>
                <td class="export-td">英:/ɪmpə'laɪt/ 美:/ˌɪmpəˈlaɪt/ </td>
                <td class="export-td">adj. 粗鲁的；无礼的</td>
            </tr>
            
             <tr>
                <td class="export-td">10</td>
                <td class="export-td">impertinent</td>
                <td class="export-td">英:/ɪm'pɜːtɪnənt/ 美:/ɪm'pɝtnənt/ </td>
                <td class="export-td">adj. 粗鲁的；不恰当的；不相干的；无礼的</td>
            </tr>
            
             <tr>
                <td class="export-td">11</td>
                <td class="export-td">immoral</td>
                <td class="export-td">英:/ɪ'mɒr(ə)l/ 美:/ɪ'mɔrəl/ </td>
                <td class="export-td">adj. 不道德的；邪恶的；淫荡的</td>
            </tr>
            
             <tr>
                <td class="export-td">12</td>
                <td class="export-td">immigration</td>
                <td class="export-td">英:/ɪmɪ'ɡreɪʃn/ 美:/ˌɪmɪ'ɡreʃən/ </td>
                <td class="export-td">移居, 移民</td>
            </tr>
            
             <tr>
                <td class="export-td">13</td>
                <td class="export-td">immensely</td>
                <td class="export-td">/i'mensli/ </td>
                <td class="export-td">非常</td>
            </tr>
            
             <tr>
                <td class="export-td">14</td>
                <td class="export-td">imam</td>
                <td class="export-td">英:/ɪ'mɑːm/ 美:/ɪ'mɑm/ </td>
                <td class="export-td">n. （伊斯兰的）阿訇；伊玛目</td>
            </tr>
            
             <tr>
                <td class="export-td">15</td>
                <td class="export-td">imaginatively</td>
                <td class="export-td">/ɪ'mædʒə,netɪvli/ </td>
                <td class="export-td">想象力</td>
            </tr>
            
             <tr>
                <td class="export-td">16</td>
                <td class="export-td">image</td>
                <td class="export-td">英:/'ɪmɪdʒ/ 美:/'ɪmɪdʒ/ </td>
                <td class="export-td">1. n. 影像；肖像；想象；偶像
2. vt. 反映；象征；想象；作…的像</td>
            </tr>
            
             <tr>
                <td class="export-td">17</td>
                <td class="export-td">illustrated</td>
                <td class="export-td">英:/'ɪləstreɪtɪd/ 美:/'ɪləstret/ </td>
                <td class="export-td">插图</td>
            </tr>
            
             <tr>
                <td class="export-td">18</td>
                <td class="export-td">igloo</td>
                <td class="export-td">英:/'ɪgluː/ 美:/'ɪglʊ/ </td>
                <td class="export-td">n. 圆顶建筑</td>
            </tr>
            
             <tr>
                <td class="export-td">19</td>
                <td class="export-td">idiot</td>
                <td class="export-td">英:/'ɪdɪət/ 美:/'ɪdɪət/ </td>
                <td class="export-td">n. 白痴；笨蛋，傻瓜</td>
            </tr>
            
             <tr>
                <td class="export-td">20</td>
                <td class="export-td">idiomatic</td>
                <td class="export-td">英:/ˌɪdɪə'mætɪk/ 美:/ˌɪdɪə'mætɪk/ </td>
                <td class="export-td">惯用的</td>
            </tr>
            
             <tr>
                <td class="export-td">21</td>
                <td class="export-td">identifying</td>
                <td class="export-td"></td>
                <td class="export-td">确定</td>
            </tr>
            
             <tr>
                <td class="export-td">22</td>
                <td class="export-td">identic</td>
                <td class="export-td">英:/aɪ'dentɪk/ 美:/aɪˈdɛntɪk/ </td>
                <td class="export-td">adj. 形式相同的；措辞相同的；同文的</td>
            </tr>
            
             <tr>
                <td class="export-td">23</td>
                <td class="export-td">identically</td>
                <td class="export-td">/ai'dentikli/ </td>
                <td class="export-td">同一地，相等地</td>
            </tr>
            
             <tr>
                <td class="export-td">24</td>
                <td class="export-td">icy</td>
                <td class="export-td">英:/'aɪsɪ/ 美:/'aɪsi/ </td>
                <td class="export-td">adj. 冰冷的；结满冰的；冷淡的</td>
            </tr>
            
             <tr>
                <td class="export-td">25</td>
                <td class="export-td">Iceland</td>
                <td class="export-td">英:/ˈaislənd/ 美:/ˈaɪslənd/ </td>
                <td class="export-td">n. 冰岛（欧洲岛名，在大西洋北部，近北极圈）</td>
            </tr>
            
             <tr>
                <td class="export-td">26</td>
                <td class="export-td">Icelandic</td>
                <td class="export-td">英:/aisˈlændik/ 美:/aɪsˈlændɪk/ </td>
                <td class="export-td">冰岛的, 冰岛人的</td>
            </tr>
            
             <tr>
                <td class="export-td">27</td>
                <td class="export-td">iceberg</td>
                <td class="export-td">英:/'aɪsbɜːg/ 美:/'aɪs'bɝg/ </td>
                <td class="export-td">n. 冰山；显露部分</td>
            </tr>
            
             <tr>
                <td class="export-td">28</td>
                <td class="export-td">icebox</td>
                <td class="export-td">英:/'aɪsbɒks/ 美:/'aɪsbɑks/ </td>
                <td class="export-td">n. 冷藏库；冰箱</td>
            </tr>
            
             <tr>
                <td class="export-td">29</td>
                <td class="export-td">hysterical</td>
                <td class="export-td">英:/hɪ'sterɪk(ə)l/ 美:/hɪ'stɛrɪkl/ </td>
                <td class="export-td">狂乱</td>
            </tr>
            
             <tr>
                <td class="export-td">30</td>
                <td class="export-td">hypnosis</td>
                <td class="export-td">英:/hɪp'nəʊsɪs/ 美:/hɪp'nosɪs/ </td>
                <td class="export-td">n. 催眠状态；催眠</td>
            </tr>
            
             <tr>
                <td class="export-td">31</td>
                <td class="export-td">hype</td>
                <td class="export-td">英:/haɪp/ 美:/haɪp/ </td>
                <td class="export-td">1. n. 大肆宣传；皮下注射
2. vt. 大肆宣传；使…兴奋</td>
            </tr>
            
             <tr>
                <td class="export-td">32</td>
                <td class="export-td">hygienically</td>
                <td class="export-td">/ˌhai'dʒi:nikəli/ </td>
                <td class="export-td">卫生</td>
            </tr>
            
             <tr>
                <td class="export-td">33</td>
                <td class="export-td">hydraulic</td>
                <td class="export-td">英:/haɪ'drɔːlɪk/ 美:/haɪ'drɔlɪk/ </td>
                <td class="export-td">水力的, 水压的</td>
            </tr>
            
             <tr>
                <td class="export-td">34</td>
                <td class="export-td">hurtful</td>
                <td class="export-td">英:/'hɜːtfʊl/ 美:/'hɝtfl/ </td>
                <td class="export-td">adj. 造成损害的</td>
            </tr>
            
             <tr>
                <td class="export-td">35</td>
                <td class="export-td">hurried</td>
                <td class="export-td">英:/'hʌrɪd/ 美:/'hɝɪd/ </td>
                <td class="export-td">1. adj. 匆忙的；草率的
2. v. 催促；匆忙进行；急派（hurry的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">36</td>
                <td class="export-td">hunter</td>
                <td class="export-td">英:/'hʌntə/ 美:/'hʌntɚ/ </td>
                <td class="export-td">n. 猎人；猎犬；搜寻者</td>
            </tr>
            
             <tr>
                <td class="export-td">37</td>
                <td class="export-td">hunting</td>
                <td class="export-td">英:/'hʌntɪŋ/ 美:/'hʌntɪŋ/ </td>
                <td class="export-td">1. n. 打猎；追逐；搜索
2. adj. 打猎的；振荡的</td>
            </tr>
            
             <tr>
                <td class="export-td">38</td>
                <td class="export-td">hunted</td>
                <td class="export-td">/'hʌntid/ </td>
                <td class="export-td">1. adj. 被捕猎的；受迫害的
2. v. 狩猎；追捕（hunt的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">39</td>
                <td class="export-td">hung</td>
                <td class="export-td">英:/hʌŋ/ 美:/hʌŋ/ </td>
                <td class="export-td">v. 悬挂；垂落（hang的过去式和过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">40</td>
                <td class="export-td">hundredth</td>
                <td class="export-td">英:/'hʌndrədθ/ 美:/'hʌndrədθ/ </td>
                <td class="export-td">第一百，百分之一</td>
            </tr>
            
             <tr>
                <td class="export-td">41</td>
                <td class="export-td">hump</td>
                <td class="export-td">英:/hʌmp/ 美:/hʌmp/ </td>
                <td class="export-td">1. n. 圆形隆起物；驼背；驼峰
2. vi. 隆起；弓起；努力；急速行进</td>
            </tr>
            
             <tr>
                <td class="export-td">42</td>
                <td class="export-td">humorless</td>
                <td class="export-td">英:/'hjuːməlɪs/ 美:/'hjʊməlɪs/ </td>
                <td class="export-td">幽默感</td>
            </tr>
            
             <tr>
                <td class="export-td">43</td>
                <td class="export-td">hum</td>
                <td class="export-td">英:/hʌm/ 美:/hʌm/ </td>
                <td class="export-td">1. vi. 发低哼声
2. vt. 用哼声表示</td>
            </tr>
            
             <tr>
                <td class="export-td">44</td>
                <td class="export-td">hug</td>
                <td class="export-td">英:/hʌg/ 美:/hʌɡ/ </td>
                <td class="export-td">1. vt. 紧抱；拥抱；抱有，坚持
2. vi. 拥抱；紧抱在一起；挤在一起</td>
            </tr>
            
             <tr>
                <td class="export-td">45</td>
                <td class="export-td">hovercraft</td>
                <td class="export-td">英:/'hɔvəkrɑ:ft/ 美:/ˈhʌvɚˌkræft/ </td>
                <td class="export-td">气垫船</td>
            </tr>
            
             <tr>
                <td class="export-td">46</td>
                <td class="export-td">housing</td>
                <td class="export-td">英:/haʊzɪŋ/ 美:/'haʊzɪŋ/ </td>
                <td class="export-td">n. 房屋；外壳；住房供给；遮盖物；机器等的防护外壳或外罩</td>
            </tr>
            
             <tr>
                <td class="export-td">47</td>
                <td class="export-td">housekeeper</td>
                <td class="export-td">英:/'haʊskiːpə/ 美:/'haʊskipɚ/ </td>
                <td class="export-td">主妇, 女管家</td>
            </tr>
            
             <tr>
                <td class="export-td">48</td>
                <td class="export-td">housework</td>
                <td class="export-td">英:/'haʊswɜːk/ 美:/'haʊs'wɝk/ </td>
                <td class="export-td">家务劳动</td>
            </tr>
            
             <tr>
                <td class="export-td">49</td>
                <td class="export-td">hourly</td>
                <td class="export-td">英:/'aʊəlɪ/ 美:/'aʊɚli/ </td>
                <td class="export-td">1. adv. 频繁地，随时；每小时地
2. adj. 每小时的，以钟点计算的；频繁的</td>
            </tr>
            
             <tr>
                <td class="export-td">50</td>
                <td class="export-td">hotline</td>
                <td class="export-td">英:/ˈhɔtˌlaɪn/ 美:/'hɑtlaɪn/ </td>
                <td class="export-td">热线</td>
            </tr>
            
             <tr>
                <td class="export-td">51</td>
                <td class="export-td">hostel</td>
                <td class="export-td">英:/'hɒst(ə)l/ 美:/'hɑstl/ </td>
                <td class="export-td">n. 旅社，招待所（尤指青年旅社）</td>
            </tr>
            
             <tr>
                <td class="export-td">52</td>
                <td class="export-td">hostelry</td>
                <td class="export-td">英:/'hɒst(ə)lrɪ/ 美:/ˈhɑstəlri/ </td>
                <td class="export-td">n. 客栈；旅店</td>
            </tr>
            
             <tr>
                <td class="export-td">53</td>
                <td class="export-td">horseshoe</td>
                <td class="export-td">英:/'hɔːsʃuː/ 美:/'hɔrʃʃu/ </td>
                <td class="export-td">马蹄铁, U形物</td>
            </tr>
            
             <tr>
                <td class="export-td">54</td>
                <td class="export-td">horseradish</td>
                <td class="export-td">英:/'hɔːsrædɪʃ/ 美:/'hɔrs'rædɪʃ/ </td>
                <td class="export-td">辣根</td>
            </tr>
            
             <tr>
                <td class="export-td">55</td>
                <td class="export-td">horseback</td>
                <td class="export-td">英:/'hɔːsbæk/ 美:/'hɔrsbæk/ </td>
                <td class="export-td">马背</td>
            </tr>
            
             <tr>
                <td class="export-td">56</td>
                <td class="export-td">horridly</td>
                <td class="export-td">/'hɔridli/ </td>
                <td class="export-td">adv. 可怕地；讨厌地</td>
            </tr>
            
             <tr>
                <td class="export-td">57</td>
                <td class="export-td">horrified</td>
                <td class="export-td">英:/'hɔrifaid/ 美:/ ˈhɔrəˌfaɪd/ </td>
                <td class="export-td">吓坏了</td>
            </tr>
            
             <tr>
                <td class="export-td">58</td>
                <td class="export-td">horrid</td>
                <td class="export-td">英:/'hɒrɪd/ 美:/'hɔrɪd/ </td>
                <td class="export-td">adj. 可怕的；恐怖的；极讨厌的</td>
            </tr>
            
             <tr>
                <td class="export-td">59</td>
                <td class="export-td">horoscope</td>
                <td class="export-td">英:/'hɒrəskəʊp/ 美:/'hɔrəskop/ </td>
                <td class="export-td">n. 占星术；星象；十二宫图</td>
            </tr>
            
             <tr>
                <td class="export-td">60</td>
                <td class="export-td">hopelessly</td>
                <td class="export-td">英:/ˈhəʊplɪslɪ/ 美:/'hoplɪsli/ </td>
                <td class="export-td">绝望地</td>
            </tr>
            
             <tr>
                <td class="export-td">61</td>
                <td class="export-td">hopefully</td>
                <td class="export-td">英:/'həʊpfʊlɪ/ 美:/'hopfəli/ </td>
                <td class="export-td">怀着希望地, 但愿</td>
            </tr>
            
             <tr>
                <td class="export-td">62</td>
                <td class="export-td">hoping</td>
                <td class="export-td"></td>
                <td class="export-td">v. 希望（hope的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">63</td>
                <td class="export-td">hop</td>
                <td class="export-td">英:/hɒp/ 美:/hɑp/ </td>
                <td class="export-td">1. vt. 跳跃；跳过
2. n. 跳跃；舞会；短途旅行</td>
            </tr>
            
             <tr>
                <td class="export-td">64</td>
                <td class="export-td">Hoover</td>
                <td class="export-td">英:/'huːvə/ 美:/'huvɚ/ </td>
                <td class="export-td">1. vi. 胡佛电动吸尘
2. n. 胡佛电动吸尘器</td>
            </tr>
            
             <tr>
                <td class="export-td">65</td>
                <td class="export-td">hoot</td>
                <td class="export-td">英:/huːt/ 美:/hut/ </td>
                <td class="export-td">1. n. 鸣响；嘲骂声；汽笛响声
2. vi. 鸣响；大声叫嚣</td>
            </tr>
            
             <tr>
                <td class="export-td">66</td>
                <td class="export-td">hooray</td>
                <td class="export-td">英:/hʊ'reɪ/ 美:/hu're/ </td>
                <td class="export-td">1. vi. 呼万岁
2. vt. 呼万岁</td>
            </tr>
            
             <tr>
                <td class="export-td">67</td>
                <td class="export-td">hooligan</td>
                <td class="export-td">英:/'huːlɪg(ə)n/ 美:/'hulɪɡən/ </td>
                <td class="export-td">n. [俚]小流氓；阿飞</td>
            </tr>
            
             <tr>
                <td class="export-td">68</td>
                <td class="export-td">hoody</td>
                <td class="export-td">/'hʊdi/ </td>
                <td class="export-td">n. 套头衫；年轻小混混</td>
            </tr>
            
             <tr>
                <td class="export-td">69</td>
                <td class="export-td">homosexual</td>
                <td class="export-td">英:/ˌhɒmə(ʊ)'sekʃʊəl/ 美:/ˌhomə'sɛkʃuəl/ </td>
                <td class="export-td">同性恋的; 同性恋</td>
            </tr>
            
             <tr>
                <td class="export-td">70</td>
                <td class="export-td">homework</td>
                <td class="export-td">英:/'həʊmwɜːk/ 美:/'hom'wɝk/ </td>
                <td class="export-td">n. 家庭作业，课外作业</td>
            </tr>
            
             <tr>
                <td class="export-td">71</td>
                <td class="export-td">homesick</td>
                <td class="export-td">英:/'həʊmsɪk/ 美:/'homsɪk/ </td>
                <td class="export-td">adj. 想家的；思乡病的</td>
            </tr>
            
             <tr>
                <td class="export-td">72</td>
                <td class="export-td">homeless</td>
                <td class="export-td">英:/'həʊmlɪs/ 美:/'homləs/ </td>
                <td class="export-td">adj. 无家可归的</td>
            </tr>
            
             <tr>
                <td class="export-td">73</td>
                <td class="export-td">holly</td>
                <td class="export-td">英:/'hɒlɪ/ 美:/'hɑli/ </td>
                <td class="export-td">1. n. 冬青树（等于holm oak）
2. adj. 冬青属植物的</td>
            </tr>
            
             <tr>
                <td class="export-td">74</td>
                <td class="export-td">hockey</td>
                <td class="export-td">英:/'hɒkɪ/ 美:/'hɑki/ </td>
                <td class="export-td">n. 冰球；曲棍球</td>
            </tr>
            
             <tr>
                <td class="export-td">75</td>
                <td class="export-td">hoarding</td>
                <td class="export-td">英:/'hɔːdɪŋ/ 美:/'hɔrdɪŋ/ </td>
                <td class="export-td">1. n. 贮藏；囤积；临时围墙
2. v. 贮藏（hoard的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">76</td>
                <td class="export-td">hitchhike</td>
                <td class="export-td">英:/'hɪtʃhaɪk/ 美:/'hɪtʃ,haɪk/ </td>
                <td class="export-td">搭便车</td>
            </tr>
            
             <tr>
                <td class="export-td">77</td>
                <td class="export-td">historic</td>
                <td class="export-td">英:/hɪ'stɒrɪk/ 美:/hɪ'stɔrɪk/ </td>
                <td class="export-td">adj. 历史上著名的；有历史意义的</td>
            </tr>
            
             <tr>
                <td class="export-td">78</td>
                <td class="export-td">historian</td>
                <td class="export-td">英:/hɪ'stɔːrɪən/ 美:/hɪ'stɔrɪən/ </td>
                <td class="export-td">历史学家，编史者</td>
            </tr>
            
             <tr>
                <td class="export-td">79</td>
                <td class="export-td">hippie</td>
                <td class="export-td">英:/'hɪpɪ/ 美:/'hɪpi/ </td>
                <td class="export-td">1. n. 嬉皮士；嬉皮模样的年青人
2. adj. 嬉皮的</td>
            </tr>
            
             <tr>
                <td class="export-td">80</td>
                <td class="export-td">hip</td>
                <td class="export-td">英:/hɪp/ 美:/hɪp/ </td>
                <td class="export-td">1. n. 臀部；蔷薇果；忧郁
2. adj. 熟悉内情的；非常时尚的</td>
            </tr>
            
             <tr>
                <td class="export-td">81</td>
                <td class="export-td">Hinduism</td>
                <td class="export-td">英:/ˈhɪndu:ˌɪzəm/ 美:/ˈhɪnduˌɪzəm/ </td>
                <td class="export-td">n. 印度教</td>
            </tr>
            
             <tr>
                <td class="export-td">82</td>
                <td class="export-td">Hindu</td>
                <td class="export-td">英:/ˈhɪndu:/ 美:/ˈhɪndu/ </td>
                <td class="export-td">1. adj. 印度教的；印度的
2. n. 印度人；印度教教徒</td>
            </tr>
            
             <tr>
                <td class="export-td">83</td>
                <td class="export-td">highness</td>
                <td class="export-td">英:/'hainis/ 美:/ˈhaɪnɪs/ </td>
                <td class="export-td">n. 殿下，阁下；高度，高位；高尚，高贵</td>
            </tr>
            
             <tr>
                <td class="export-td">84</td>
                <td class="export-td">hiding</td>
                <td class="export-td">英:/'haɪdɪŋ/ 美:/'haɪdɪŋ/ </td>
                <td class="export-td">n. 隐匿；躲藏处；[口]殴打</td>
            </tr>
            
             <tr>
                <td class="export-td">85</td>
                <td class="export-td">hiccup</td>
                <td class="export-td">英:/'hɪkʌp/ 美:/'hɪkəp/ </td>
                <td class="export-td">1. n. 打嗝
2. vi. 打嗝</td>
            </tr>
            
             <tr>
                <td class="export-td">86</td>
                <td class="export-td">hibernation</td>
                <td class="export-td">英:/ˌhaibə'neiʃən/ 美:/ˌhaɪbɚˈneʃən/ </td>
                <td class="export-td">n. 冬眠；避寒；过冬</td>
            </tr>
            
             <tr>
                <td class="export-td">87</td>
                <td class="export-td">helpless</td>
                <td class="export-td">英:/'helplɪs/ 美:/'hɛlpləs/ </td>
                <td class="export-td">adj. 无助的；没用的；无能的</td>
            </tr>
            
             <tr>
                <td class="export-td">88</td>
                <td class="export-td">hectares</td>
                <td class="export-td">/'hektɑ:/ </td>
                <td class="export-td">n. 公顷（hectare的复数）</td>
            </tr>
            
             <tr>
                <td class="export-td">89</td>
                <td class="export-td">heartbreak</td>
                <td class="export-td">英:/'hɑːtbreɪk/ 美:/'hɑrtbrek/ </td>
                <td class="export-td">心碎</td>
            </tr>
            
             <tr>
                <td class="export-td">90</td>
                <td class="export-td">headquarter</td>
                <td class="export-td">英:/'hɛd'kwɔrtɚ/ 美:/ˈhɛdˈkwɔrtɚ/ </td>
                <td class="export-td">总部设于</td>
            </tr>
            
             <tr>
                <td class="export-td">91</td>
                <td class="export-td">headmistress</td>
                <td class="export-td">英:/hed'mɪstrəs/ 美:/'hɛd'mæstɚ/ </td>
                <td class="export-td">女校长</td>
            </tr>
            
             <tr>
                <td class="export-td">92</td>
                <td class="export-td">he</td>
                <td class="export-td">英:/hiː/ 美:/hi/ </td>
                <td class="export-td">他</td>
            </tr>
            
             <tr>
                <td class="export-td">93</td>
                <td class="export-td">hazelnut</td>
                <td class="export-td">英:/'heɪz(ə)lnʌt/ 美:/'hezlnʌt/ </td>
                <td class="export-td">n. 榛树；榛子</td>
            </tr>
            
             <tr>
                <td class="export-td">94</td>
                <td class="export-td">hazard</td>
                <td class="export-td">英:/ˈhæzəd/ 美:/ˈhæzəd/ </td>
                <td class="export-td">1. vt. 赌运气；冒…的危险，使遭受危险
2. n. 危险，冒险；冒险的事</td>
            </tr>
            
             <tr>
                <td class="export-td">95</td>
                <td class="export-td">haunted</td>
                <td class="export-td">英:/'hɔːntɪd/ 美:/'hɔntɪd/ </td>
                <td class="export-td">1. adj. 闹鬼的；反复出现的；受到困扰的
2. v. 常去；缠住；使担忧（haunt的过去式和过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">96</td>
                <td class="export-td">hastily</td>
                <td class="export-td">英:/'heistili/ 美:/ˈhestɪlɪ/ </td>
                <td class="export-td">adv. 匆忙地；急速地；慌忙地</td>
            </tr>
            
             <tr>
                <td class="export-td">97</td>
                <td class="export-td">hashtag</td>
                <td class="export-td"></td>
                <td class="export-td"></td>
            </tr>
            
             <tr>
                <td class="export-td">98</td>
                <td class="export-td">hash</td>
                <td class="export-td">英:/hæʃ/ 美:/hæʃ/ </td>
                <td class="export-td">1. n. 剁碎的食物；混杂，拼凑；重新表述
2. vt. 搞糟，把…弄乱；切细；推敲</td>
            </tr>
            
             <tr>
                <td class="export-td">99</td>
                <td class="export-td">harvesting</td>
                <td class="export-td">/'hɑrvɪst/ </td>
                <td class="export-td">收获</td>
            </tr>
            
             <tr>
                <td class="export-td">100</td>
                <td class="export-td">harmless</td>
                <td class="export-td">英:/'hɑːmlɪs/ 美:/'hɑrmləs/ </td>
                <td class="export-td">adj. 无害的；无恶意的</td>
            </tr>
            
             <tr>
                <td class="export-td">101</td>
                <td class="export-td">harmonic</td>
                <td class="export-td">英:/hɑː'mɒnɪk/ 美:/hɑr'mɑnɪk/ </td>
                <td class="export-td">1. adj. 和声的；谐和的；音乐般的
2. n. 谐波；和声</td>
            </tr>
            
             <tr>
                <td class="export-td">102</td>
                <td class="export-td">hardback</td>
                <td class="export-td">英:/'hɑːdbæk/ 美:/'hɑrd'bæk/ </td>
                <td class="export-td">1. n. 精装本；硬封面的书
2. adj. 硬封面的；精装的</td>
            </tr>
            
             <tr>
                <td class="export-td">103</td>
                <td class="export-td">happiness</td>
                <td class="export-td">英:/ˈhæpɪnɪs/ 美:/'hæpɪnɪs/ </td>
                <td class="export-td">快乐,幸福,适当</td>
            </tr>
            
             <tr>
                <td class="export-td">104</td>
                <td class="export-td">happily</td>
                <td class="export-td">英:/ˈhæpili/ 美:/'hæpɪli/ </td>
                <td class="export-td">adv. 幸福地；快乐地；幸运地；恰当地</td>
            </tr>
            
             <tr>
                <td class="export-td">105</td>
                <td class="export-td">hanky</td>
                <td class="export-td">英:/ˈhæŋkɪ/ 美:/'hæŋki/ </td>
                <td class="export-td">n. 手帕</td>
            </tr>
            
             <tr>
                <td class="export-td">106</td>
                <td class="export-td">handset</td>
                <td class="export-td">英:/'hæn(d)set/ 美:/'hænd'sɛt/ </td>
                <td class="export-td">n. 手机，电话听筒</td>
            </tr>
            
             <tr>
                <td class="export-td">107</td>
                <td class="export-td">handmade</td>
                <td class="export-td">英:/hæn(d)'meɪd/ 美:/'hænd'med/ </td>
                <td class="export-td">adj. 手工的；手制的</td>
            </tr>
            
             <tr>
                <td class="export-td">108</td>
                <td class="export-td">handlebars</td>
                <td class="export-td">英:/'hændlba:z/ 美:/ˈhænd l..b ɑrz/ </td>
                <td class="export-td">把手</td>
            </tr>
            
             <tr>
                <td class="export-td">109</td>
                <td class="export-td">handgun</td>
                <td class="export-td">英:/'hæn(d)gʌn/ 美:/'hænd'gʌn/ </td>
                <td class="export-td">n. 手枪</td>
            </tr>
            
             <tr>
                <td class="export-td">110</td>
                <td class="export-td">handles</td>
                <td class="export-td">/'hændl/ </td>
                <td class="export-td">1. n. 把；柄；控键（handle的复数形式）
2. v. 操纵；掌握（handle的第三人称单数）</td>
            </tr>
            
             <tr>
                <td class="export-td">111</td>
                <td class="export-td">handbag</td>
                <td class="export-td">英:/'hæn(d)bæg/ 美:/'hænd'bæg/ </td>
                <td class="export-td">n. 手提包</td>
            </tr>
            
             <tr>
                <td class="export-td">112</td>
                <td class="export-td">hamster</td>
                <td class="export-td">英:/'hæmstə/ 美:/'hæmstɚ/ </td>
                <td class="export-td">n. 仓鼠；仓鼠毛皮</td>
            </tr>
            
             <tr>
                <td class="export-td">113</td>
                <td class="export-td">hammock</td>
                <td class="export-td">英:/'hæmək/ 美:/'hæmək/ </td>
                <td class="export-td">1. n. 吊床；吊铺；吊带
2. vt. 睡吊床</td>
            </tr>
            
             <tr>
                <td class="export-td">114</td>
                <td class="export-td">hammers</td>
                <td class="export-td">/'hæmə/ </td>
                <td class="export-td">1. n. 锤子（hammer的复数）
2. v. 锤击；[口]使惨败（hammer的三单形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">115</td>
                <td class="export-td">ham</td>
                <td class="export-td">英:/hæm/ 美:/hæm/ </td>
                <td class="export-td">1. n. 火腿；[口]业余无线电爱好者；[俚]蹩脚演员
2. vi. 表演过火</td>
            </tr>
            
             <tr>
                <td class="export-td">116</td>
                <td class="export-td">halves</td>
                <td class="export-td">英:/hɑːvz/ 美:/hævz/ </td>
                <td class="export-td">n. 一学期；两等份（half的复数形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">117</td>
                <td class="export-td">halve</td>
                <td class="export-td">英:/hɑːv/ 美:/hæv/ </td>
                <td class="export-td">vt. 二等分；把……减半</td>
            </tr>
            
             <tr>
                <td class="export-td">118</td>
                <td class="export-td">Halloween</td>
                <td class="export-td">/ˌhæləu'i:n/ </td>
                <td class="export-td">n. 万圣节前夕（指十月三十一日夜晚）</td>
            </tr>
            
             <tr>
                <td class="export-td">119</td>
                <td class="export-td">halfway</td>
                <td class="export-td">英:/hɑːf'weɪ/ 美:/ˈhæfˈwe/ </td>
                <td class="export-td">1. adv. 在中途；到一半
2. adj. 中途的；不彻底的</td>
            </tr>
            
             <tr>
                <td class="export-td">120</td>
                <td class="export-td">hairy</td>
                <td class="export-td">英:/'heərɪ/ 美:/'hɛri/ </td>
                <td class="export-td">adj. 多毛的；毛状的；长毛的</td>
            </tr>
            
             <tr>
                <td class="export-td">121</td>
                <td class="export-td">hairstylist</td>
                <td class="export-td">/'hεə,stailist/ </td>
                <td class="export-td">发型师</td>
            </tr>
            
             <tr>
                <td class="export-td">122</td>
                <td class="export-td">hairbrush</td>
                <td class="export-td">英:/'heəbrʌʃ/ 美:/ˈhɛrˌbrʌʃ/ </td>
                <td class="export-td">发刷</td>
            </tr>
            
             <tr>
                <td class="export-td">123</td>
                <td class="export-td">hairdryer</td>
                <td class="export-td">英:/ˈheədraɪə/ 美:/'hɛrdraɪɚ/ </td>
                <td class="export-td">电吹风</td>
            </tr>
            
             <tr>
                <td class="export-td">124</td>
                <td class="export-td">hairstyle</td>
                <td class="export-td">英:/'heəstaɪl/ 美:/'hɛr'staɪl/ </td>
                <td class="export-td">发型</td>
            </tr>
            
             <tr>
                <td class="export-td">125</td>
                <td class="export-td">hairdresser</td>
                <td class="export-td">英:/'heədresə/ 美:/ˈhɛrˌdrɛsɚ/ </td>
                <td class="export-td">理发师</td>
            </tr>
            
             <tr>
                <td class="export-td">126</td>
                <td class="export-td">hairs</td>
                <td class="export-td">/hɛr/ </td>
                <td class="export-td">毛</td>
            </tr>
            
             <tr>
                <td class="export-td">127</td>
                <td class="export-td">had</td>
                <td class="export-td">英:/hæd/ 美:/hæd/ </td>
                <td class="export-td">v. 有；使（have的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">128</td>
                <td class="export-td">gypsy</td>
                <td class="export-td">英:/'dʒipsi/ 美:/ˈdʒɪpsi/ </td>
                <td class="export-td">1. n. 吉卜赛人；吉卜赛语；像吉布赛的人；歌舞剧中的歌舞队员
2. adj. 象吉卜赛人的；吉卜赛人的；[口]无照的</td>
            </tr>
            
             <tr>
                <td class="export-td">129</td>
                <td class="export-td">gymnastics</td>
                <td class="export-td">英:/dʒɪm'næstɪks/ 美:/dʒɪm'næstɪks/ </td>
                <td class="export-td">体操</td>
            </tr>
            
             <tr>
                <td class="export-td">130</td>
                <td class="export-td">guts</td>
                <td class="export-td">/ɡʌts/ </td>
                <td class="export-td">1. n. 飞碟游戏（比赛双方每组5人，相距15码，互相掷接飞碟）；内脏；狭道；[口语]贪食者（gut的复数）
2. v. 取出…的内脏；毁坏…的内部；贪婪地吃（gut的第三人称单数）</td>
            </tr>
            
             <tr>
                <td class="export-td">131</td>
                <td class="export-td">gunman</td>
                <td class="export-td">英:/'gʌnmən/ 美:/'ɡʌnmən/ </td>
                <td class="export-td">n. 枪手；持枪歹徒</td>
            </tr>
            
             <tr>
                <td class="export-td">132</td>
                <td class="export-td">guitar</td>
                <td class="export-td">英:/gɪ'tɑː/ 美:/ɡɪ'tɑr/ </td>
                <td class="export-td">1. n. 吉他，六弦琴
2. vi. 弹吉他</td>
            </tr>
            
             <tr>
                <td class="export-td">133</td>
                <td class="export-td">grieved</td>
                <td class="export-td">/gri:vd/ </td>
                <td class="export-td">1. adj. 伤心的
2. v. 悲伤（grieve的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">134</td>
                <td class="export-td">gratebar</td>
                <td class="export-td"></td>
                <td class="export-td">炉条</td>
            </tr>
            
             <tr>
                <td class="export-td">135</td>
                <td class="export-td">granny</td>
                <td class="export-td">英:/'grænɪ/ 美:/ˈɡræni/ </td>
                <td class="export-td">n. 奶奶；外婆</td>
            </tr>
            
             <tr>
                <td class="export-td">136</td>
                <td class="export-td">grandparents</td>
                <td class="export-td">/'ɡrænd,pεərənt/ </td>
                <td class="export-td">外祖父母, 祖父母</td>
            </tr>
            
             <tr>
                <td class="export-td">137</td>
                <td class="export-td">grandchild</td>
                <td class="export-td">英:/'græn(d)tʃaɪld/ 美:/'ɡræntʃaɪld/ </td>
                <td class="export-td">孙</td>
            </tr>
            
             <tr>
                <td class="export-td">138</td>
                <td class="export-td">gram</td>
                <td class="export-td">/ɡræm/ </td>
                <td class="export-td">n. 克；[植]鹰嘴豆（用作饲料）</td>
            </tr>
            
             <tr>
                <td class="export-td">139</td>
                <td class="export-td">goes</td>
                <td class="export-td">英:/gəuz/ 美:/ɡoz/ </td>
                <td class="export-td">v. 前进；行走（go的第三人称单数形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">140</td>
                <td class="export-td">godparent</td>
                <td class="export-td">英:/'gɒdpeər(ə)nt/ 美:/'ɡɑdpɛrənt/ </td>
                <td class="export-td">契爷</td>
            </tr>
            
             <tr>
                <td class="export-td">141</td>
                <td class="export-td">goalkeeper</td>
                <td class="export-td">英:/'gəʊlkiːpə/ 美:/'ɡolkipɚ/ </td>
                <td class="export-td">守门员</td>
            </tr>
            
             <tr>
                <td class="export-td">142</td>
                <td class="export-td">glued</td>
                <td class="export-td">/ɡlu:d/ </td>
                <td class="export-td">1. adj. 胶合的
2. v. 粘；用胶水粘住（glue的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">143</td>
                <td class="export-td">glitters</td>
                <td class="export-td">/'ɡlitə/ </td>
                <td class="export-td">1. n. 灿烂，辉耀（glitter的复数形式）
2. v. 灿烂，闪烁（glitter的第三人称单数）</td>
            </tr>
            
             <tr>
                <td class="export-td">144</td>
                <td class="export-td">glasses</td>
                <td class="export-td">英:/'glɑ:siz/ 美:/ˈɡlæsɪz/ </td>
                <td class="export-td">1. n. 眼镜；双筒望远镜；玻璃（glass的复数形式）
2. v. 把…装入玻璃容器内；给…装上玻璃（glass的第三人称单数形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">145</td>
                <td class="export-td">girlfriend</td>
                <td class="export-td">英:/'gɜːlfrend/ 美:/'ɡɝlfrɛnd/ </td>
                <td class="export-td">女朋友, 女性朋友</td>
            </tr>
            
             <tr>
                <td class="export-td">146</td>
                <td class="export-td">giraffe</td>
                <td class="export-td">英:/dʒɪ'rɑːf/ 美:/dʒə'ræf/ </td>
                <td class="export-td">n. 长颈鹿</td>
            </tr>
            
             <tr>
                <td class="export-td">147</td>
                <td class="export-td">gill</td>
                <td class="export-td">英:/gɪl/ 美:/ɡɪl/ </td>
                <td class="export-td">1. n. 腮；菌褶；（山谷中的）沟壑，峡流；及耳（容量单位）
2. vi. 被刺网捕住</td>
            </tr>
            
             <tr>
                <td class="export-td">148</td>
                <td class="export-td">gigabyte</td>
                <td class="export-td">英:/'dʒiɡə,bait/ 美:/ˈdʒɪɡəˌbaɪt/ </td>
                <td class="export-td">n. 十亿字节；十亿位组</td>
            </tr>
            
             <tr>
                <td class="export-td">149</td>
                <td class="export-td">ghetto</td>
                <td class="export-td">英:/'getəʊ/ 美:/'ɡɛto/ </td>
                <td class="export-td">1. n. 犹太人区；贫民区
2. vt. 使集中居住</td>
            </tr>
            
             <tr>
                <td class="export-td">150</td>
                <td class="export-td">geek</td>
                <td class="export-td">英:/giːk/ 美:/ɡik/ </td>
                <td class="export-td">n. 做低级滑稽表演的人；反常的人；畸形人；野人</td>
            </tr>
            
             <tr>
                <td class="export-td">151</td>
                <td class="export-td">gatherer</td>
                <td class="export-td">/'ɡæðərɚ/ </td>
                <td class="export-td">n. 采集者，收集器</td>
            </tr>
            
             <tr>
                <td class="export-td">152</td>
                <td class="export-td">garlic</td>
                <td class="export-td">英:/'gɑːlɪk/ 美:/'ɡɑrlɪk/ </td>
                <td class="export-td">n. 大蒜；蒜头</td>
            </tr>
            
             <tr>
                <td class="export-td">153</td>
                <td class="export-td">gaping</td>
                <td class="export-td">英:/'gæpiŋ/ 美:/ˈɡepɪŋ/ </td>
                <td class="export-td">adj. 多洞穴的</td>
            </tr>
            
             <tr>
                <td class="export-td">154</td>
                <td class="export-td">gapper</td>
                <td class="export-td">/'ɡæpɚ/ </td>
                <td class="export-td">间苗机;疏苗机</td>
            </tr>
            
             <tr>
                <td class="export-td">155</td>
                <td class="export-td">gamblesome</td>
                <td class="export-td">/'ɡæmblsəm/ </td>
                <td class="export-td">adj. 喜欢赌博的,喜欢投机的</td>
            </tr>
            
             <tr>
                <td class="export-td">156</td>
                <td class="export-td">furnished</td>
                <td class="export-td">英:/ˈfɜ:nɪʃt/ 美:/'fɝnɪʃt/ </td>
                <td class="export-td">家具</td>
            </tr>
            
             <tr>
                <td class="export-td">157</td>
                <td class="export-td">funfair</td>
                <td class="export-td">英:/ˈfʌnfeə/ 美:/'fʌnfɛr/ </td>
                <td class="export-td">n. 游乐场；游艺集市</td>
            </tr>
            
             <tr>
                <td class="export-td">158</td>
                <td class="export-td">freezing</td>
                <td class="export-td">英:/ˈfri:ziŋ/ 美:/'frizɪŋ/ </td>
                <td class="export-td">adj. 冰冻的；严寒的；冷冻用的</td>
            </tr>
            
             <tr>
                <td class="export-td">159</td>
                <td class="export-td">freckles</td>
                <td class="export-td">/frekəlz/ </td>
                <td class="export-td">1. n. 雀斑（freckle的复数）
2. v. 使生雀斑（freckle的第三人称单数形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">160</td>
                <td class="export-td">fought</td>
                <td class="export-td">英:/fɔːt/ 美:/fɔt/ </td>
                <td class="export-td">v. 打架；战斗（fight的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">161</td>
                <td class="export-td">fortress</td>
                <td class="export-td">英:/'fɔːtrɪs/ 美:/'fɔrtrəs/ </td>
                <td class="export-td">1. n. 要塞；堡垒
2. vt. 筑要塞；以要塞防守</td>
            </tr>
            
             <tr>
                <td class="export-td">162</td>
                <td class="export-td">forttage</td>
                <td class="export-td"></td>
                <td class="export-td">临拓</td>
            </tr>
            
             <tr>
                <td class="export-td">163</td>
                <td class="export-td">fortieth</td>
                <td class="export-td">英:/'fɔːtɪɪθ/ 美:/ˈfɔrtiɪθ/ </td>
                <td class="export-td">1. num. 第四十；四十分之一
2. adj. 四十分之一的；第四十的</td>
            </tr>
            
             <tr>
                <td class="export-td">164</td>
                <td class="export-td">formerly</td>
                <td class="export-td">英:/'fɔːməlɪ/ 美:/'fɔrmɚli/ </td>
                <td class="export-td">adv. 以前；原来</td>
            </tr>
            
             <tr>
                <td class="export-td">165</td>
                <td class="export-td">forgot</td>
                <td class="export-td">英:/fə'ɡɒt/ 美:/fɚ'ɡɑt/ </td>
                <td class="export-td">v. 忘记；轻忽；遗漏（forget的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">166</td>
                <td class="export-td">forgiveness</td>
                <td class="export-td">英:/fə'gɪvnɪs/ 美:/fɚ'ɡɪvnəs/ </td>
                <td class="export-td">饶恕</td>
            </tr>
            
             <tr>
                <td class="export-td">167</td>
                <td class="export-td">forgetful</td>
                <td class="export-td">英:/fə'getfʊl/ 美:/fɚ'gɛtfəl/ </td>
                <td class="export-td">健忘的，疏忽的</td>
            </tr>
            
             <tr>
                <td class="export-td">168</td>
                <td class="export-td">forgave</td>
                <td class="export-td">英:/fə'ɡeɪv/ 美:/fɚ'ɡev/ </td>
                <td class="export-td">v. 原谅；饶恕；免除（forgive的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">169</td>
                <td class="export-td">foreman</td>
                <td class="export-td">英:/'fɔːmən/ 美:/'fɔrmən/ </td>
                <td class="export-td">n. 领班；陪审团主席</td>
            </tr>
            
             <tr>
                <td class="export-td">170</td>
                <td class="export-td">forgotten</td>
                <td class="export-td">英:/fə'ɡɒtn/ 美:/fɚ'ɡɑtn/ </td>
                <td class="export-td">遗忘</td>
            </tr>
            
             <tr>
                <td class="export-td">171</td>
                <td class="export-td">footstool</td>
                <td class="export-td">英:/'fʊtstuːl/ 美:/'fʊt'stʊl/ </td>
                <td class="export-td">脚凳</td>
            </tr>
            
             <tr>
                <td class="export-td">172</td>
                <td class="export-td">footprint</td>
                <td class="export-td">英:/'fʊtprɪnt/ 美:/'fʊtprɪnt/ </td>
                <td class="export-td">脚印</td>
            </tr>
            
             <tr>
                <td class="export-td">173</td>
                <td class="export-td">footpath</td>
                <td class="export-td">英:/'fʊtpɑːθ/ 美:/ˈfʊtˌpæθ/ </td>
                <td class="export-td">n. 小路；人行道；小径</td>
            </tr>
            
             <tr>
                <td class="export-td">174</td>
                <td class="export-td">font</td>
                <td class="export-td">英:/fɒnt/ 美:/fɑnt/ </td>
                <td class="export-td">n. 字体；字形；洗礼盘，圣水器；泉</td>
            </tr>
            
             <tr>
                <td class="export-td">175</td>
                <td class="export-td">follower</td>
                <td class="export-td">英:/'fɒləʊə/ 美:/'fɑloɚ/ </td>
                <td class="export-td">n. 追随者；属下；信徒</td>
            </tr>
            
             <tr>
                <td class="export-td">176</td>
                <td class="export-td">foggy</td>
                <td class="export-td">英:/'fɒgɪ/ 美:/'fɔɡi/ </td>
                <td class="export-td">adj. 有雾的；模糊的，朦胧的</td>
            </tr>
            
             <tr>
                <td class="export-td">177</td>
                <td class="export-td">foetus</td>
                <td class="export-td">英:/'fiːtəs/ 美:/'fitəs/ </td>
                <td class="export-td">n. 胎儿</td>
            </tr>
            
             <tr>
                <td class="export-td">178</td>
                <td class="export-td">foal</td>
                <td class="export-td">英:/fəʊl/ 美:/fol/ </td>
                <td class="export-td">1. n. 驹（尤指一岁以下的马、驴、骡）
2. vi. （马等）生仔</td>
            </tr>
            
             <tr>
                <td class="export-td">179</td>
                <td class="export-td">flyover</td>
                <td class="export-td">英:/'flaɪəʊvə/ 美:/'flaɪovɚ/ </td>
                <td class="export-td">n. 天桥；立交桥；立交马路</td>
            </tr>
            
             <tr>
                <td class="export-td">180</td>
                <td class="export-td">flying</td>
                <td class="export-td">英:/'flaɪɪŋ/ 美:/'flaɪɪŋ/ </td>
                <td class="export-td">1. adj. 飞行的
2. n. 飞行</td>
            </tr>
            
             <tr>
                <td class="export-td">181</td>
                <td class="export-td">flushed</td>
                <td class="export-td">英:/flʌʃt/ 美:/fl ʌʃt/ </td>
                <td class="export-td">1. adj. 激动的；心情愉快的
2. v. 脸发红；使激动；排水（flush的过去式和过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">182</td>
                <td class="export-td">flung</td>
                <td class="export-td">英:/flʌŋ/ 美:/flʌŋ/ </td>
                <td class="export-td">vt. 挥动（fling的过去式及过去分词形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">183</td>
                <td class="export-td">fluff</td>
                <td class="export-td">英:/flʌf/ 美:/flʌf/ </td>
                <td class="export-td">1. n. 绒毛；错误；无价值的东西
2. vt. 念错；抖松；使…起毛</td>
            </tr>
            
             <tr>
                <td class="export-td">184</td>
                <td class="export-td">fluently</td>
                <td class="export-td">英:/'flu:əntlɪ/ 美:/ˈfluəntlɪ/ </td>
                <td class="export-td">adv. 流利地；通畅地</td>
            </tr>
            
             <tr>
                <td class="export-td">185</td>
                <td class="export-td">flown</td>
                <td class="export-td">英:/fləʊn/ 美:/flon/ </td>
                <td class="export-td">v. fly的过去分词</td>
            </tr>
            
             <tr>
                <td class="export-td">186</td>
                <td class="export-td">flowery</td>
                <td class="export-td">英:/'flaʊərɪ/ 美:/ˈflaʊəri/ </td>
                <td class="export-td">adj. 多花的；花的；华丽的；绚丽的</td>
            </tr>
            
             <tr>
                <td class="export-td">187</td>
                <td class="export-td">flowerpot</td>
                <td class="export-td">英:/'flaʊəpɒt/ 美:/ˈflaʊɚˌpɑt/ </td>
                <td class="export-td">花盆, 花钵</td>
            </tr>
            
             <tr>
                <td class="export-td">188</td>
                <td class="export-td">flowered</td>
                <td class="export-td">英:/'flaʊəd/ 美:/'flaʊɚd/ </td>
                <td class="export-td">adj. 用花装饰的；花开着的</td>
            </tr>
            
             <tr>
                <td class="export-td">189</td>
                <td class="export-td">florist</td>
                <td class="export-td">英:/'flɒrɪst/ 美:/ˈflɔrɪst/ </td>
                <td class="export-td">n. 花商，种花人；花卉研究者</td>
            </tr>
            
             <tr>
                <td class="export-td">190</td>
                <td class="export-td">floorboard</td>
                <td class="export-td">英:/'flɔːbɔːd/ 美:/ˈflɔrˌbɔrd/ </td>
                <td class="export-td">地板</td>
            </tr>
            
             <tr>
                <td class="export-td">191</td>
                <td class="export-td">floodlight</td>
                <td class="export-td">英:/'flʌdlaɪt/ 美:/'flʌdlaɪt/ </td>
                <td class="export-td">泛光灯</td>
            </tr>
            
             <tr>
                <td class="export-td">192</td>
                <td class="export-td">flipper</td>
                <td class="export-td">英:/'flɪpə/ 美:/ˈflɪpɚ/ </td>
                <td class="export-td">1. n. 鳍状肢；鳍；烤饼；胖听罐头
2. vi. 靠鳍足（或鸭甲板）行动</td>
            </tr>
            
             <tr>
                <td class="export-td">193</td>
                <td class="export-td">flippant</td>
                <td class="export-td">英:/'flɪp(ə)nt/ 美:/ˈflɪpənt/ </td>
                <td class="export-td">adj. 轻率的；嘴碎的；没礼貌的</td>
            </tr>
            
             <tr>
                <td class="export-td">194</td>
                <td class="export-td">flew</td>
                <td class="export-td">英:/fluː/ 美:/flu/ </td>
                <td class="export-td">v. 飞，飞翔（fly的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">195</td>
                <td class="export-td">fleets</td>
                <td class="export-td">/fli:t/ </td>
                <td class="export-td">1. n. 舰队（fleet的复数）
2. v. 掠过（fleet的第三人称单数形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">196</td>
                <td class="export-td">flea</td>
                <td class="export-td">英:/fliː/ 美:/fli/ </td>
                <td class="export-td">n. 低廉的旅馆；跳蚤；生蚤的动物</td>
            </tr>
            
             <tr>
                <td class="export-td">197</td>
                <td class="export-td">flatware</td>
                <td class="export-td">英:/'flætweə/ 美:/'flætwɛr/ </td>
                <td class="export-td">n. 扁平的餐具（指刀，叉，匙等）</td>
            </tr>
            
             <tr>
                <td class="export-td">198</td>
                <td class="export-td">flattery</td>
                <td class="export-td">英:/'flæt(ə)rɪ/ 美:/'flætəri/ </td>
                <td class="export-td">n. 谄媚；奉承；恭维话</td>
            </tr>
            
             <tr>
                <td class="export-td">199</td>
                <td class="export-td">flattering</td>
                <td class="export-td">/'flætəriŋ/ </td>
                <td class="export-td">谄媚的</td>
            </tr>
            
             <tr>
                <td class="export-td">200</td>
                <td class="export-td">flashlight</td>
                <td class="export-td">英:/'flæʃlaɪt/ 美:/'flæʃlaɪt/ </td>
                <td class="export-td">手电筒，闪光灯</td>
            </tr>
            
             <tr>
                <td class="export-td">201</td>
                <td class="export-td">flake</td>
                <td class="export-td">英:/fleɪk/ 美:/flek/ </td>
                <td class="export-td">1. vi. 剥落；成片状剥落
2. vt. 使…成薄片；将…剥落</td>
            </tr>
            
             <tr>
                <td class="export-td">202</td>
                <td class="export-td">fizzy</td>
                <td class="export-td">英:/'fɪzɪ/ 美:/'fɪzi/ </td>
                <td class="export-td">adj. 起泡沫的；嘶嘶作响的</td>
            </tr>
            
             <tr>
                <td class="export-td">203</td>
                <td class="export-td">fixed</td>
                <td class="export-td">英:/fɪkst/ 美:/fɪkst/ </td>
                <td class="export-td">adj. 固执的，处境...的，准备好的，确定的</td>
            </tr>
            
             <tr>
                <td class="export-td">204</td>
                <td class="export-td">fitness</td>
                <td class="export-td">英:/'fɪtnəs/ 美:/'fɪtnəs/ </td>
                <td class="export-td">n. 健康；适当；适合性</td>
            </tr>
            
             <tr>
                <td class="export-td">205</td>
                <td class="export-td">fishman</td>
                <td class="export-td"></td>
                <td class="export-td">n. 捕鱼人</td>
            </tr>
            
             <tr>
                <td class="export-td">206</td>
                <td class="export-td">fishmonger</td>
                <td class="export-td">英:/'fɪʃmʌŋgə/ 美:/'fɪʃ'mʌŋgɚ/ </td>
                <td class="export-td">鱼贩</td>
            </tr>
            
             <tr>
                <td class="export-td">207</td>
                <td class="export-td">fireworks</td>
                <td class="export-td">/'faɪr,wɝks/ </td>
                <td class="export-td">烟火</td>
            </tr>
            
             <tr>
                <td class="export-td">208</td>
                <td class="export-td">fireplace</td>
                <td class="export-td">英:/'faɪəpleɪs/ 美:/'faɪɚples/ </td>
                <td class="export-td">壁炉</td>
            </tr>
            
             <tr>
                <td class="export-td">209</td>
                <td class="export-td">firemen</td>
                <td class="export-td">/'faiəmən/ </td>
                <td class="export-td">消防员</td>
            </tr>
            
             <tr>
                <td class="export-td">210</td>
                <td class="export-td">firefighter</td>
                <td class="export-td">英:/'faɪəfaɪtə/ 美:/'faɪɚfaɪtɚ/ </td>
                <td class="export-td">消防队员</td>
            </tr>
            
             <tr>
                <td class="export-td">211</td>
                <td class="export-td">fir</td>
                <td class="export-td">英:/fɜː/ 美:/fɝ/ </td>
                <td class="export-td">1. n. 冷杉；枞木
2. abbr. 弗京（firkin）</td>
            </tr>
            
             <tr>
                <td class="export-td">212</td>
                <td class="export-td">fingertip</td>
                <td class="export-td">英:/'fiŋɡətip/ 美:/ˈfɪŋɡɚˌtɪp/ </td>
                <td class="export-td">指尖</td>
            </tr>
            
             <tr>
                <td class="export-td">213</td>
                <td class="export-td">fingerprint</td>
                <td class="export-td">英:/'fɪŋgəprɪnt/ 美:/'fɪŋɡɚprɪnt/ </td>
                <td class="export-td">指纹，特点</td>
            </tr>
            
             <tr>
                <td class="export-td">214</td>
                <td class="export-td">fingernail</td>
                <td class="export-td">英:/'fɪŋgəneɪl/ 美:/'fɪŋɡɚnel/ </td>
                <td class="export-td">指甲</td>
            </tr>
            
             <tr>
                <td class="export-td">215</td>
                <td class="export-td">findings</td>
                <td class="export-td"></td>
                <td class="export-td">n. 发现，调查结果；检验发现的情况（finding复数）</td>
            </tr>
            
             <tr>
                <td class="export-td">216</td>
                <td class="export-td">filthy</td>
                <td class="export-td">英:/'fɪlθɪ/ 美:/'fɪlθi/ </td>
                <td class="export-td">adj. 污秽的；猥亵的；肮脏的</td>
            </tr>
            
             <tr>
                <td class="export-td">217</td>
                <td class="export-td">filling</td>
                <td class="export-td">英:/'fɪlɪŋ/ 美:/'fɪlɪŋ/ </td>
                <td class="export-td">1. n. 填充；填料
2. v. 填满；遍及（fill的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">218</td>
                <td class="export-td">fighter</td>
                <td class="export-td">英:/'faɪtə/ 美:/'faɪtɚ/ </td>
                <td class="export-td">n. 战士，斗争者；斗士；奋斗者；好战者</td>
            </tr>
            
             <tr>
                <td class="export-td">219</td>
                <td class="export-td">fighting</td>
                <td class="export-td">英:/ˈfaɪtɪŋ/ 美:/'faɪtɪŋ/ </td>
                <td class="export-td">1. adj. 好战的；战斗的；适于格斗的
2. n. 战斗，搏斗</td>
            </tr>
            
             <tr>
                <td class="export-td">220</td>
                <td class="export-td">fib</td>
                <td class="export-td">英:/fɪb/ 美:/fɪb/ </td>
                <td class="export-td">1. n. 无伤大雅的谎言，小谎；一击
2. vi. 撒小谎</td>
            </tr>
            
             <tr>
                <td class="export-td">221</td>
                <td class="export-td">fiancee</td>
                <td class="export-td">/'fi:ɑ:nsei/ </td>
                <td class="export-td">n. （法）未婚妻</td>
            </tr>
            
             <tr>
                <td class="export-td">222</td>
                <td class="export-td">fiance</td>
                <td class="export-td">/'fi:ɑ:nsei/ </td>
                <td class="export-td">n. 未婚夫</td>
            </tr>
            
             <tr>
                <td class="export-td">223</td>
                <td class="export-td">fete</td>
                <td class="export-td">英:/feɪt/ 美:/fet/ </td>
                <td class="export-td">1. n. 庆祝；节日；祭祀；游乐会
2. vt. 宴请；招待</td>
            </tr>
            
             <tr>
                <td class="export-td">224</td>
                <td class="export-td">felt</td>
                <td class="export-td">英:/felt/ 美:/fɛlt/ </td>
                <td class="export-td">1. n. 毡；毡制品
2. vi. 粘结</td>
            </tr>
            
             <tr>
                <td class="export-td">225</td>
                <td class="export-td">feet</td>
                <td class="export-td">英:/fiːt/ 美:/fit/ </td>
                <td class="export-td">n. 脚（foot的复数形式）；尺；韵脚</td>
            </tr>
            
             <tr>
                <td class="export-td">226</td>
                <td class="export-td">fed</td>
                <td class="export-td">英:/fed/ 美:/fɛd/ </td>
                <td class="export-td">v. 饲养（feed 的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">227</td>
                <td class="export-td">fearless</td>
                <td class="export-td">英:/'fɪəlɪs/ 美:/'fɪrləs/ </td>
                <td class="export-td">adj. 无畏的；大胆的</td>
            </tr>
            
             <tr>
                <td class="export-td">228</td>
                <td class="export-td">fearfully</td>
                <td class="export-td">英:/ˈfɪəfəlɪ/ 美:/ˈfɪrfəlɪ/ </td>
                <td class="export-td">可怕</td>
            </tr>
            
             <tr>
                <td class="export-td">229</td>
                <td class="export-td">faultless</td>
                <td class="export-td">英:/'fɔːltlɪs/ 美:/'fɔltləs/ </td>
                <td class="export-td">完美的, 无缺点的</td>
            </tr>
            
             <tr>
                <td class="export-td">230</td>
                <td class="export-td">fatherhood</td>
                <td class="export-td">英:/'fɑːðəhʊd/ 美:/'fɑðɚ'hʊd/ </td>
                <td class="export-td">父亲的身份, 父道</td>
            </tr>
            
             <tr>
                <td class="export-td">231</td>
                <td class="export-td">fat</td>
                <td class="export-td">英:/fæt/ 美:/fæt/ </td>
                <td class="export-td">1. adj. 肥的，胖的；丰满的；油腻的
2. n. 脂肪，肥肉</td>
            </tr>
            
             <tr>
                <td class="export-td">232</td>
                <td class="export-td">fastener</td>
                <td class="export-td">英:/'fɑːsənə/ 美:/'fæsnɚ/ </td>
                <td class="export-td">n. 扣件；钮扣；按钮；使系牢之物</td>
            </tr>
            
             <tr>
                <td class="export-td">233</td>
                <td class="export-td">fascinating</td>
                <td class="export-td">英:/ˈfæsineitiŋ/ 美:/'fæsɪnetɪŋ/ </td>
                <td class="export-td">迷人的</td>
            </tr>
            
             <tr>
                <td class="export-td">234</td>
                <td class="export-td">fascination</td>
                <td class="export-td">英:/ˌfæsɪ'neɪʃ(ə)n/ 美:/ˌfæsɪ'neʃən/ </td>
                <td class="export-td">魔力,魅力</td>
            </tr>
            
             <tr>
                <td class="export-td">235</td>
                <td class="export-td">farmyard</td>
                <td class="export-td">英:/'fɑːmjɑːd/ 美:/'fɑrmjɑrd/ </td>
                <td class="export-td">n. 农家庭院</td>
            </tr>
            
             <tr>
                <td class="export-td">236</td>
                <td class="export-td">farming</td>
                <td class="export-td">英:/'fɑːmɪŋ/ 美:/'fɑrmɪŋ/ </td>
                <td class="export-td">1. n. 农业，耕作
2. v. 耕种；出租（farm的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">237</td>
                <td class="export-td">farmhouse</td>
                <td class="export-td">英:/'fɑːmhaʊs/ 美:/'fɑrm'haʊs/ </td>
                <td class="export-td">农舍, 农家</td>
            </tr>
            
             <tr>
                <td class="export-td">238</td>
                <td class="export-td">FAQ</td>
                <td class="export-td">/fæk/ </td>
                <td class="export-td">abbr. 常见问题（Frequently Asked Question）；中等品（Fair Average Quality）；码头交货价格（Free at Quay）</td>
            </tr>
            
             <tr>
                <td class="export-td">239</td>
                <td class="export-td">fallen</td>
                <td class="export-td">英:/'fɔːl(ə)n/ 美:/'fɔlən/ </td>
                <td class="export-td">1. adj. 落下来的；堕落的；陷落的
2. v. 落下；跌倒（fall的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">240</td>
                <td class="export-td">faithfully</td>
                <td class="export-td">英:/ˈfeɪθfʊlɪ/ 美:/'feθfəli/ </td>
                <td class="export-td">忠实</td>
            </tr>
            
             <tr>
                <td class="export-td">241</td>
                <td class="export-td">failing</td>
                <td class="export-td">英:/'feɪlɪŋ/ 美:/'felɪŋ/ </td>
                <td class="export-td">1. n. 缺点，过失；弱点；失败
2. prep. 如果没有…</td>
            </tr>
            
             <tr>
                <td class="export-td">242</td>
                <td class="export-td">fact</td>
                <td class="export-td">英:/fækt/ 美:/fækt/ </td>
                <td class="export-td">n. 事实；实际；真相</td>
            </tr>
            
             <tr>
                <td class="export-td">243</td>
                <td class="export-td">FaceBook</td>
                <td class="export-td"></td>
                <td class="export-td">n. 脸谱网</td>
            </tr>
            
             <tr>
                <td class="export-td">244</td>
                <td class="export-td">face</td>
                <td class="export-td">英:/feɪs/ 美:/fes/ </td>
                <td class="export-td">1. n. 脸；面容；表面；面子；威信；外观
2. vi. 朝；向</td>
            </tr>
            
             <tr>
                <td class="export-td">245</td>
                <td class="export-td">fable</td>
                <td class="export-td">英:/'feɪb(ə)l/ 美:/'febl/ </td>
                <td class="export-td">1. n. 寓言；无稽之谈
2. vi. 编寓言；虚构</td>
            </tr>
            
             <tr>
                <td class="export-td">246</td>
                <td class="export-td">axe</td>
                <td class="export-td">英:/æks/ 美:/æks/ </td>
                <td class="export-td">1. n. 斧
2. vt. 用斧砍；削减</td>
            </tr>
            
             <tr>
                <td class="export-td">247</td>
                <td class="export-td">awesome</td>
                <td class="export-td">英:/'ɔːs(ə)m/ 美:/'ɔsəm/ </td>
                <td class="export-td">adj. 可怕的，引起敬畏的</td>
            </tr>
            
             <tr>
                <td class="export-td">248</td>
                <td class="export-td">autography</td>
                <td class="export-td">英:/ɔː'tɒgrəfɪ/ 美:/ɔ'tɑgrəfi/ </td>
                <td class="export-td">亲笔</td>
            </tr>
            
             <tr>
                <td class="export-td">249</td>
                <td class="export-td">autism</td>
                <td class="export-td">英:/'ɔːtɪz(ə)m/ 美:/'ɔtɪzəm/ </td>
                <td class="export-td">n. [心]孤独症；自我中心主义</td>
            </tr>
            
             <tr>
                <td class="export-td">250</td>
                <td class="export-td">aubergine</td>
                <td class="export-td">英:/'əʊbəʒiːn/ 美:/'obɚʒin/ </td>
                <td class="export-td">1. n. （英）茄子；紫红色
2. adj. 紫红色的</td>
            </tr>
            
             <tr>
                <td class="export-td">251</td>
                <td class="export-td">attendant</td>
                <td class="export-td">英:/ə'tend(ə)nt/ 美:/ə'tɛndənt/ </td>
                <td class="export-td">伴随的</td>
            </tr>
            
             <tr>
                <td class="export-td">252</td>
                <td class="export-td">attended</td>
                <td class="export-td">/ə'tendid/ </td>
                <td class="export-td">出席</td>
            </tr>
            
             <tr>
                <td class="export-td">253</td>
                <td class="export-td">arose</td>
                <td class="export-td">英:/ə'rəʊz/ 美:/əˈroz/ </td>
                <td class="export-td">vi. 引发；出现（arise的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">254</td>
                <td class="export-td">archaeologist</td>
                <td class="export-td">英:/ˌɑ:ki'ɔlədʒist/ 美:/ˌ ɑrkɪˈ ɑləd ʒɪst/ </td>
                <td class="export-td">考古学家</td>
            </tr>
            
             <tr>
                <td class="export-td">255</td>
                <td class="export-td">animated</td>
                <td class="export-td">英:/'ænɪmeɪtɪd/ 美:/'ænə'metɪd/ </td>
                <td class="export-td">1. adj. 活生生的；活泼的；愉快的
2. n. 使…有生气（animate的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">256</td>
                <td class="export-td">an</td>
                <td class="export-td">英:/æn/ 美:/ən/ </td>
                <td class="export-td">一</td>
            </tr>
            
             <tr>
                <td class="export-td">257</td>
                <td class="export-td">aluminum</td>
                <td class="export-td">英:/ə'ljuːmɪnəm/ 美:/ə'lʊmɪnəm/ </td>
                <td class="export-td">n. 铝</td>
            </tr>
            
             <tr>
                <td class="export-td">258</td>
                <td class="export-td">alternating</td>
                <td class="export-td">/'ɔ:ltə,neitiŋ/ </td>
                <td class="export-td">交替</td>
            </tr>
            
             <tr>
                <td class="export-td">259</td>
                <td class="export-td">almonds</td>
                <td class="export-td">/'ɑ:mənd/ </td>
                <td class="export-td">n. 杏仁；杏仁粉（almond的复数）</td>
            </tr>
            
             <tr>
                <td class="export-td">260</td>
                <td class="export-td">agreeing</td>
                <td class="export-td"></td>
                <td class="export-td">v. 同意（agree的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">261</td>
                <td class="export-td">advertizement</td>
                <td class="export-td"></td>
                <td class="export-td">n. 广告,做广告</td>
            </tr>
            
             <tr>
                <td class="export-td">262</td>
                <td class="export-td">advance payment</td>
                <td class="export-td"></td>
                <td class="export-td">预付款</td>
            </tr>
            
             <tr>
                <td class="export-td">263</td>
                <td class="export-td">acknowledgment</td>
                <td class="export-td">英:/əkˈnɔlidʒmənt/ 美:/ək'nɑlɪdʒmənt/ </td>
                <td class="export-td">承认</td>
            </tr>
            
             <tr>
                <td class="export-td">264</td>
                <td class="export-td">absurd</td>
                <td class="export-td">英:/əb'sɜːd/ 美:/əb'sɝd/ </td>
                <td class="export-td">1. adj. 荒谬的；可笑的
2. n. 荒诞；荒诞作品</td>
            </tr>
            
             <tr>
                <td class="export-td">265</td>
                <td class="export-td">a-</td>
                <td class="export-td"></td>
                <td class="export-td"></td>
            </tr>
            
             <tr>
                <td class="export-td">266</td>
                <td class="export-td">eyelids</td>
                <td class="export-td">/'ai,lid/ </td>
                <td class="export-td">n. 眼睑；眼皮（eyelid的复数）</td>
            </tr>
            
             <tr>
                <td class="export-td">267</td>
                <td class="export-td">eyelash</td>
                <td class="export-td">英:/'aɪlæʃ/ 美:/'aɪ'læʃ/ </td>
                <td class="export-td">n. 睫毛</td>
            </tr>
            
             <tr>
                <td class="export-td">268</td>
                <td class="export-td">eyebrows</td>
                <td class="export-td">/'aibrau/ </td>
                <td class="export-td">1. n. 眉毛（eyebrow的复数）
2. v. 为…描眉（eyebrow的第三人称单数）</td>
            </tr>
            
             <tr>
                <td class="export-td">269</td>
                <td class="export-td">extrema</td>
                <td class="export-td">/ik'stri:mə/ </td>
                <td class="export-td">极值</td>
            </tr>
            
             <tr>
                <td class="export-td">270</td>
                <td class="export-td">experienced</td>
                <td class="export-td">英:/ɪk'spɪərɪənst/ 美:/ɪkˈspɪriənst/ </td>
                <td class="export-td">有经验的</td>
            </tr>
            
             <tr>
                <td class="export-td">271</td>
                <td class="export-td">exhausting</td>
                <td class="export-td">英:/iɡ'zɔ:stiŋ/ 美:/ ɪɡˈzɔstɪŋ/ </td>
                <td class="export-td">辛苦</td>
            </tr>
            
             <tr>
                <td class="export-td">272</td>
                <td class="export-td">excluding</td>
                <td class="export-td">英:/ɪksˈklu:dɪŋ/ 美:/ɪk'skludɪŋ/ </td>
                <td class="export-td">不包括</td>
            </tr>
            
             <tr>
                <td class="export-td">273</td>
                <td class="export-td">evidently</td>
                <td class="export-td">英:/ˈevidəntli/ 美:/'ɛvɪdəntli/ </td>
                <td class="export-td">明显地</td>
            </tr>
            
             <tr>
                <td class="export-td">274</td>
                <td class="export-td">euro</td>
                <td class="export-td">英:/ˈjʊərəʊ/ 美:/'jʊro/ </td>
                <td class="export-td">n. 欧元（欧盟的统一货币单位）</td>
            </tr>
            
             <tr>
                <td class="export-td">275</td>
                <td class="export-td">ESOL</td>
                <td class="export-td">/'esəl/ </td>
                <td class="export-td">abbr. English for Speakers of Other Languages 操其他语...</td>
            </tr>
            
             <tr>
                <td class="export-td">276</td>
                <td class="export-td">environmentalist</td>
                <td class="export-td">英:/ɪn,vaɪrən'ment(ə)lɪst/ 美:/ɪn,vaɪrən'mɛntəlɪst/ </td>
                <td class="export-td">环保人士</td>
            </tr>
            
             <tr>
                <td class="export-td">277</td>
                <td class="export-td">envied</td>
                <td class="export-td">/'envid/ </td>
                <td class="export-td">1. adj. 被羡慕的；被妒忌的
2. v. 羡慕；嫉妒（envy的过去式和过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">278</td>
                <td class="export-td">enrol</td>
                <td class="export-td">英:/in'rəul/ 美:/ɛnˈrol/ </td>
                <td class="export-td">1. vt. 登记；卷起；入学；使入会
2. vi. 参军；注册</td>
            </tr>
            
             <tr>
                <td class="export-td">279</td>
                <td class="export-td">enquiry</td>
                <td class="export-td">英:/in'kwaiəri/ 美:/ɛnˈkwaɪri/ </td>
                <td class="export-td">n. 询问，询盘</td>
            </tr>
            
             <tr>
                <td class="export-td">280</td>
                <td class="export-td">enlarged</td>
                <td class="export-td">/in'lɑ:dʒd/ </td>
                <td class="export-td">1. adj. 放大的；增大的；扩展的
2. v. 扩大，增大（enlarge的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">281</td>
                <td class="export-td">embarrassed</td>
                <td class="export-td">英:/ɪmˈbærəst/ 美:/ɪm'bærəst/ </td>
                <td class="export-td">尴尬</td>
            </tr>
            
             <tr>
                <td class="export-td">282</td>
                <td class="export-td">email</td>
                <td class="export-td">/'i:'meil/ </td>
                <td class="export-td">电子邮件</td>
            </tr>
            
             <tr>
                <td class="export-td">283</td>
                <td class="export-td">elf</td>
                <td class="export-td">英:/elf/ 美:/ɛlf/ </td>
                <td class="export-td">n. 小精灵；淘气鬼</td>
            </tr>
            
             <tr>
                <td class="export-td">284</td>
                <td class="export-td">eldest</td>
                <td class="export-td">英:/'eldɪst/ 美:/'ɛldɪst/ </td>
                <td class="export-td">1. adj. 最年长的；年事最高的（old的最高级）
2. n. 最年长者</td>
            </tr>
            
             <tr>
                <td class="export-td">285</td>
                <td class="export-td">eggplant</td>
                <td class="export-td">英:/'egplɑːnt/ 美:/'ɛɡplænt/ </td>
                <td class="export-td">1. n. 茄子
2. adj. 深紫色的</td>
            </tr>
            
             <tr>
                <td class="export-td">286</td>
                <td class="export-td">earphones</td>
                <td class="export-td">/'ɪrfonz/ </td>
                <td class="export-td">耳机</td>
            </tr>
            
             <tr>
                <td class="export-td">287</td>
                <td class="export-td">earning</td>
                <td class="export-td">/'ɝnɪŋ/ </td>
                <td class="export-td">n. 收入（earn的现在分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">288</td>
                <td class="export-td">DVD</td>
                <td class="export-td">英:/ˌdi:vi:ˈdi:/ 美:/ˌdiviˈdi/ </td>
                <td class="export-td">abbr. 数字化视频光盘</td>
            </tr>
            
             <tr>
                <td class="export-td">289</td>
                <td class="export-td">dungaree</td>
                <td class="export-td">英:/ˌdʌŋgə'riː/ 美:/ˌdʌŋgə'ri/ </td>
                <td class="export-td">n. 用粗棉布所做的裤子，工作服；粗蓝布（粗棉布的一种）</td>
            </tr>
            
             <tr>
                <td class="export-td">290</td>
                <td class="export-td">dryer</td>
                <td class="export-td">英:/'draɪə/ 美:/'draɪɚ/ </td>
                <td class="export-td">n. 干燥剂；烘干机</td>
            </tr>
            
             <tr>
                <td class="export-td">291</td>
                <td class="export-td">driving</td>
                <td class="export-td">英:/'draɪvɪŋ/ 美:/'draɪvɪŋ/ </td>
                <td class="export-td">1. adj. 强劲的；推进的；精力旺盛的
2. n. 操纵；驾驶</td>
            </tr>
            
             <tr>
                <td class="export-td">292</td>
                <td class="export-td">drainpipe</td>
                <td class="export-td">英:/'dreɪnpaɪp/ 美:/'drenpaɪp/ </td>
                <td class="export-td">排水管</td>
            </tr>
            
             <tr>
                <td class="export-td">293</td>
                <td class="export-td">dragonfly</td>
                <td class="export-td">英:/'dræg(ə)nflaɪ/ 美:/'dræɡənflaɪ/ </td>
                <td class="export-td">蜻蜓</td>
            </tr>
            
             <tr>
                <td class="export-td">294</td>
                <td class="export-td">distressing</td>
                <td class="export-td">英:/dɪ'stresɪŋ/ 美:/dɪ'strɛsɪŋ/ </td>
                <td class="export-td">令人痛心</td>
            </tr>
            
             <tr>
                <td class="export-td">295</td>
                <td class="export-td">diseases</td>
                <td class="export-td">/dɪ'ziz/ </td>
                <td class="export-td">n. 病害；疾病；疾病种类；病（disease的复数）</td>
            </tr>
            
             <tr>
                <td class="export-td">296</td>
                <td class="export-td">disc</td>
                <td class="export-td">英:/dɪsk/ 美:/dɪsk/ </td>
                <td class="export-td">1. n. 圆盘，唱片（等于disk）
2. vt. 灌唱片</td>
            </tr>
            
             <tr>
                <td class="export-td">297</td>
                <td class="export-td">diarrhoea</td>
                <td class="export-td">/ˌdaiə'riə/ </td>
                <td class="export-td">腹泻</td>
            </tr>
            
             <tr>
                <td class="export-td">298</td>
                <td class="export-td">dialogue</td>
                <td class="export-td">英:/'daɪəlɒg/ 美:/'daɪəlɑɡ/ </td>
                <td class="export-td">1. n. 对话；意见交换
2. vi. 对话</td>
            </tr>
            
             <tr>
                <td class="export-td">299</td>
                <td class="export-td">determined</td>
                <td class="export-td">英:/dɪ'tɜːmɪnd/ 美:/dɪ'tɝmɪnd/ </td>
                <td class="export-td">坚毅的,下定决心的</td>
            </tr>
            
             <tr>
                <td class="export-td">300</td>
                <td class="export-td">detention</td>
                <td class="export-td">英:/dɪ'tenʃ(ə)n/ 美:/dɪ'tɛnʃən/ </td>
                <td class="export-td">羁押,拘留</td>
            </tr>
            
             <tr>
                <td class="export-td">301</td>
                <td class="export-td">detailed</td>
                <td class="export-td">英:/'diːteɪld/ 美:/dɪ'teld/ </td>
                <td class="export-td">1. adj. 详细的，精细的；复杂的，详尽的
2. v. 详细说明（detail的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">302</td>
                <td class="export-td">dessertspoon</td>
                <td class="export-td">英:/dɪ'zɜːtspuːn/ 美:/dɪ'zɝtspun/ </td>
                <td class="export-td">n. 餐后甜点匙名 词:   dessertspoonful</td>
            </tr>
            
             <tr>
                <td class="export-td">303</td>
                <td class="export-td">desperation</td>
                <td class="export-td">英:/despə'reɪʃn/ 美:/ˌdɛspə'reʃən/ </td>
                <td class="export-td">绝望，铤而走险</td>
            </tr>
            
             <tr>
                <td class="export-td">304</td>
                <td class="export-td">desktop</td>
                <td class="export-td">英:/ˈdeskˌtɔp/ 美:/'dɛsk'tɑp/ </td>
                <td class="export-td">n. 桌面；台式机</td>
            </tr>
            
             <tr>
                <td class="export-td">305</td>
                <td class="export-td">designer</td>
                <td class="export-td">英:/dɪ'zaɪnə/ 美:/dɪ'zaɪnɚ/ </td>
                <td class="export-td">1. n. 设计师；谋划者
2. adj. 由设计师专门设计的；享有盛名的；赶时髦的</td>
            </tr>
            
             <tr>
                <td class="export-td">306</td>
                <td class="export-td">deserved</td>
                <td class="export-td">英:/dɪ'zɜːvd/ 美:/dɪ'zɝvd/ </td>
                <td class="export-td">1. adj. 应得的；理所当然的
2. v. 值得；应得；应受报答（deserve的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">307</td>
                <td class="export-td">depressing</td>
                <td class="export-td">英:/dɪˈpresɪŋ/ 美:/dɪ'prɛsɪŋ/ </td>
                <td class="export-td">沉闷</td>
            </tr>
            
             <tr>
                <td class="export-td">308</td>
                <td class="export-td">dependant</td>
                <td class="export-td">英:/di'pendənt/ 美:/dɪˈpɛndənt/ </td>
                <td class="export-td">n. 家眷；侍从；食客（等于dependent）</td>
            </tr>
            
             <tr>
                <td class="export-td">309</td>
                <td class="export-td">deodorant</td>
                <td class="export-td">英:/dɪ'əʊd(ə)r(ə)nt/ 美:/dɪ'odərənt/ </td>
                <td class="export-td">除臭剂; 可除臭的</td>
            </tr>
            
             <tr>
                <td class="export-td">310</td>
                <td class="export-td">dental</td>
                <td class="export-td">英:/'dent(ə)l/ 美:/'dɛntl/ </td>
                <td class="export-td">1. adj. 牙齿的，牙的；牙科的
2. n. 齿音</td>
            </tr>
            
             <tr>
                <td class="export-td">311</td>
                <td class="export-td">denim</td>
                <td class="export-td">英:/'denɪm/ 美:/'dɛnɪm/ </td>
                <td class="export-td">n. 斜纹粗棉布，丁尼布；劳动布</td>
            </tr>
            
             <tr>
                <td class="export-td">312</td>
                <td class="export-td">demonstration</td>
                <td class="export-td">英:/demən'streɪʃ(ə)n/ 美:/ˌdɛmən'streʃən/ </td>
                <td class="export-td">示范</td>
            </tr>
            
             <tr>
                <td class="export-td">313</td>
                <td class="export-td">demo</td>
                <td class="export-td">英:/ˈdeməu/ 美:/ˈdɛmo/ </td>
                <td class="export-td">n. 样本唱片；演示；示威；民主党员</td>
            </tr>
            
             <tr>
                <td class="export-td">314</td>
                <td class="export-td">delightful</td>
                <td class="export-td">英:/dɪ'laɪtfʊl/ 美:/dɪ'laɪtfl/ </td>
                <td class="export-td">令人愉快的, 可喜的</td>
            </tr>
            
             <tr>
                <td class="export-td">315</td>
                <td class="export-td">delighted</td>
                <td class="export-td">英:/dɪ'laɪtɪd/ 美:/dɪ'laɪtɪd/ </td>
                <td class="export-td">高兴的, 快乐的</td>
            </tr>
            
             <tr>
                <td class="export-td">316</td>
                <td class="export-td">delicatessen</td>
                <td class="export-td">英:/ˌdelɪkə'tes(ə)n/ 美:/ˌdɛlɪkə'tɛsn/ </td>
                <td class="export-td">熟食</td>
            </tr>
            
             <tr>
                <td class="export-td">317</td>
                <td class="export-td">deliberately</td>
                <td class="export-td">英:/dɪˈlɪbərɪtlɪ/ 美:/dɪ'lɪbərətli/ </td>
                <td class="export-td">慎重地,故意地</td>
            </tr>
            
             <tr>
                <td class="export-td">318</td>
                <td class="export-td">degrees</td>
                <td class="export-td">/di'ɡri:/ </td>
                <td class="export-td">n. 角度，学历；度数（degree的复数）</td>
            </tr>
            
             <tr>
                <td class="export-td">319</td>
                <td class="export-td">defiant</td>
                <td class="export-td">英:/dɪ'faɪənt/ 美:/dɪ'faɪənt/ </td>
                <td class="export-td">adj. 挑衅的；目中无人的，蔑视的；挑战的</td>
            </tr>
            
             <tr>
                <td class="export-td">320</td>
                <td class="export-td">deeply</td>
                <td class="export-td">英:/'di:pli/ 美:/ˈdiplɪ/ </td>
                <td class="export-td">adv. 深刻地；在深处；浓浓地</td>
            </tr>
            
             <tr>
                <td class="export-td">321</td>
                <td class="export-td">decoration</td>
                <td class="export-td">英:/dekə'reɪʃ(ə)n/ 美:/ˌdɛkə'reʃən/ </td>
                <td class="export-td">装饰, 装饰品</td>
            </tr>
            
             <tr>
                <td class="export-td">322</td>
                <td class="export-td">deck chair</td>
                <td class="export-td"></td>
                <td class="export-td">折叠式躺椅；折叠帆布躺椅</td>
            </tr>
            
             <tr>
                <td class="export-td">323</td>
                <td class="export-td">decaffeinated</td>
                <td class="export-td">英:/di:ˈkæfəˌneɪtɪd/ 美:/ˌdi'kæfɪnetɪd/ </td>
                <td class="export-td">不含咖啡因</td>
            </tr>
            
             <tr>
                <td class="export-td">324</td>
                <td class="export-td">deathly</td>
                <td class="export-td">英:/'deθlɪ/ 美:/'dɛθli/ </td>
                <td class="export-td">1. adj. 死一般的；致命的
2. adv. 死了一样地；非常</td>
            </tr>
            
             <tr>
                <td class="export-td">325</td>
                <td class="export-td">deafen</td>
                <td class="export-td">英:/'def(ə)n/ 美:/'dɛfən/ </td>
                <td class="export-td">1. vt. 使聋；淹没
2. vi. 变聋</td>
            </tr>
            
             <tr>
                <td class="export-td">326</td>
                <td class="export-td">deadline</td>
                <td class="export-td">英:/'dedlaɪn/ 美:/'dɛdlaɪn/ </td>
                <td class="export-td">n. 截止期限，最后期限</td>
            </tr>
            
             <tr>
                <td class="export-td">327</td>
                <td class="export-td">daydream</td>
                <td class="export-td">英:/'deɪdriːm/ 美:/'dedrim/ </td>
                <td class="export-td">1. vi. 做白日梦
2. n. 白日梦</td>
            </tr>
            
             <tr>
                <td class="export-td">328</td>
                <td class="export-td">dashboard</td>
                <td class="export-td">英:/'dæʃbɔːd/ 美:/'dæʃ'bɔrd/ </td>
                <td class="export-td">仪表盘</td>
            </tr>
            
             <tr>
                <td class="export-td">329</td>
                <td class="export-td">darts</td>
                <td class="export-td">/da:ts/ </td>
                <td class="export-td">1. n. 射镖游戏；镖（dart的复数形式）
2. v. 投掷；投射（dart的单三形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">330</td>
                <td class="export-td">cyclinder</td>
                <td class="export-td"></td>
                <td class="export-td">圆柱</td>
            </tr>
            
             <tr>
                <td class="export-td">331</td>
                <td class="export-td">cyclization</td>
                <td class="export-td">英:/ˌsaɪklɪ'zeʃən/ 美:/ˌsaɪklɪˈzeʃən/ </td>
                <td class="export-td">环化</td>
            </tr>
            
             <tr>
                <td class="export-td">332</td>
                <td class="export-td">cycling</td>
                <td class="export-td">英:/'saikliŋ/ 美:/ˈsaɪklɪŋ/ </td>
                <td class="export-td">n. 骑脚踏车消遣；骑脚踏车兜风</td>
            </tr>
            
             <tr>
                <td class="export-td">333</td>
                <td class="export-td">cyberspace</td>
                <td class="export-td">英:/ˈsaibəˌspeis/ 美:/'saɪbɚspes/ </td>
                <td class="export-td">网络空间</td>
            </tr>
            
             <tr>
                <td class="export-td">334</td>
                <td class="export-td">cruelhearted</td>
                <td class="export-td">/'kru:əl'hɑ:tid/ </td>
                <td class="export-td">adj. 狠心的,绝情的</td>
            </tr>
            
             <tr>
                <td class="export-td">335</td>
                <td class="export-td">crowned</td>
                <td class="export-td">/kraʊnd/ </td>
                <td class="export-td">1. adj. 王室的；戴王冠的
2. v. 加冕，使成王（crown的过去式和过去分词形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">336</td>
                <td class="export-td">crosse</td>
                <td class="export-td">英:/krɒs/ 美:/krɔs/ </td>
                <td class="export-td">n. 长曲棍球的球棒</td>
            </tr>
            
             <tr>
                <td class="export-td">337</td>
                <td class="export-td">crackles</td>
                <td class="export-td">/'krækl/ </td>
                <td class="export-td">1. v. 发出爆裂声；表面形成碎裂花纹；充满（crackle的第三人称单数）
2. n. 细碎爆裂声；陶瓷器的碎裂花纹；陶瓷器皿（crackle的复数）</td>
            </tr>
            
             <tr>
                <td class="export-td">338</td>
                <td class="export-td">coursebook</td>
                <td class="export-td"></td>
                <td class="export-td"></td>
            </tr>
            
             <tr>
                <td class="export-td">339</td>
                <td class="export-td">counterclockwise</td>
                <td class="export-td">英:/kaʊntə'klɒkwaɪz/ 美:/'kaʊntɚ'klɑk'waɪz/ </td>
                <td class="export-td">反时针方向</td>
            </tr>
            
             <tr>
                <td class="export-td">340</td>
                <td class="export-td">councilor</td>
                <td class="export-td">英:/'kaʊnsələ/ 美:/'kaʊnslɚ/ </td>
                <td class="export-td">议员</td>
            </tr>
            
             <tr>
                <td class="export-td">341</td>
                <td class="export-td">couldn't</td>
                <td class="export-td">英:/'kudənt/ 美:/ˈkʊdnt/ </td>
                <td class="export-td">不能</td>
            </tr>
            
             <tr>
                <td class="export-td">342</td>
                <td class="export-td">cooperation</td>
                <td class="export-td">英:/kəʊ,ɒpə'reɪʃ(ə)n/ 美:/ko,ɑpə'reʃən/ </td>
                <td class="export-td">合作, 协作</td>
            </tr>
            
             <tr>
                <td class="export-td">343</td>
                <td class="export-td">cooperator</td>
                <td class="export-td">/kəu'ɔpə,reitə/ </td>
                <td class="export-td">合作者</td>
            </tr>
            
             <tr>
                <td class="export-td">344</td>
                <td class="export-td">controversialism</td>
                <td class="export-td"></td>
                <td class="export-td">争论精神,争论癖</td>
            </tr>
            
             <tr>
                <td class="export-td">345</td>
                <td class="export-td">continuo</td>
                <td class="export-td">英:/kən'tɪnjʊəʊ/ 美:/kən'tɪnjuo/ </td>
                <td class="export-td">n. 数字低音；键盘乐器的低音部</td>
            </tr>
            
             <tr>
                <td class="export-td">346</td>
                <td class="export-td">contents</td>
                <td class="export-td">/'kɔntents/ </td>
                <td class="export-td">1. n. 目录；内容；要旨（content的复数）
2. v. 使满意（content的三单形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">347</td>
                <td class="export-td">conjuror</td>
                <td class="export-td">英:/'kʌndʒərə/ 美:/ˈkɑndʒəɚ/ </td>
                <td class="export-td">n. 魔术师；变戏法的人</td>
            </tr>
            
             <tr>
                <td class="export-td">348</td>
                <td class="export-td">concernment</td>
                <td class="export-td">英:/kən'sɜːnm(ə)nt/ 美:/kənˈsɚnmənt/ </td>
                <td class="export-td">要事</td>
            </tr>
            
             <tr>
                <td class="export-td">349</td>
                <td class="export-td">comparability</td>
                <td class="export-td">/ˌkɔmpərə'biləti/ </td>
                <td class="export-td">可比性</td>
            </tr>
            
             <tr>
                <td class="export-td">350</td>
                <td class="export-td">comeback</td>
                <td class="export-td">英:/'kʌmbæk/ 美:/'kʌmbæk/ </td>
                <td class="export-td">n. 恢复；复原</td>
            </tr>
            
             <tr>
                <td class="export-td">351</td>
                <td class="export-td">colorful</td>
                <td class="export-td">英:/ˈkʌləfəl/ 美:/'kʌlɚfəl/ </td>
                <td class="export-td">adj. 华美的；有趣的；富有色彩的</td>
            </tr>
            
             <tr>
                <td class="export-td">352</td>
                <td class="export-td">colored</td>
                <td class="export-td">英:/ˈkʌləd/ 美:/'kʌlɚd/ </td>
                <td class="export-td">1. adj. 有色的；有色人种的；着色的
2. v. 把...染色，粉饰，脸红（color的过去时和过去分词形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">353</td>
                <td class="export-td">colour</td>
                <td class="export-td">英:/'kʌlə/ 美:/ˈkʌlɚ/ </td>
                <td class="export-td">1. vt. 把…涂颜色，粉饰；歪曲；使脸红
2. vi. 变色</td>
            </tr>
            
             <tr>
                <td class="export-td">354</td>
                <td class="export-td">collapsed</td>
                <td class="export-td"></td>
                <td class="export-td">倒塌</td>
            </tr>
            
             <tr>
                <td class="export-td">355</td>
                <td class="export-td">coffin</td>
                <td class="export-td">英:/ˈkɔfin/ 美:/ˈkɔfɪn/ </td>
                <td class="export-td">n. 棺材</td>
            </tr>
            
             <tr>
                <td class="export-td">356</td>
                <td class="export-td">cockroach</td>
                <td class="export-td">英:/'kɒkrəʊtʃ/ 美:/'kɑk'rotʃ/ </td>
                <td class="export-td">蟑螂</td>
            </tr>
            
             <tr>
                <td class="export-td">357</td>
                <td class="export-td">clock out</td>
                <td class="export-td"></td>
                <td class="export-td">打卡下班</td>
            </tr>
            
             <tr>
                <td class="export-td">358</td>
                <td class="export-td">cloak room</td>
                <td class="export-td"></td>
                <td class="export-td">行李寄放处；寄存室；衣帽间</td>
            </tr>
            
             <tr>
                <td class="export-td">359</td>
                <td class="export-td">climbing</td>
                <td class="export-td">英:/ˈklaimiŋ/ 美:/'klaɪmɪŋ/ </td>
                <td class="export-td">1. adj. 上升的；攀缘而登的
2. n. 攀登</td>
            </tr>
            
             <tr>
                <td class="export-td">360</td>
                <td class="export-td">clatterer</td>
                <td class="export-td"></td>
                <td class="export-td">n. 饶舌家,长舌者</td>
            </tr>
            
             <tr>
                <td class="export-td">361</td>
                <td class="export-td">civilized</td>
                <td class="export-td">英:/ˈsɪvəˌlaɪzd/ 美:/'sɪvə'laɪzd/ </td>
                <td class="export-td">文明的, 有礼的</td>
            </tr>
            
             <tr>
                <td class="export-td">362</td>
                <td class="export-td">circulatory</td>
                <td class="export-td">英:/ˈsɜ:kjələˌtɔ:ri:/ 美:/'sɝkjələtɔri/ </td>
                <td class="export-td">循环的，循环系统的</td>
            </tr>
            
             <tr>
                <td class="export-td">363</td>
                <td class="export-td">cigar</td>
                <td class="export-td">英:/sɪ'gɑː/ 美:/sɪ'ɡɑr/ </td>
                <td class="export-td">n. 雪茄</td>
            </tr>
            
             <tr>
                <td class="export-td">364</td>
                <td class="export-td">chosen</td>
                <td class="export-td">英:/'tʃəʊzn/ 美:/'tʃozn/ </td>
                <td class="export-td">1. vt. 选择（choose的过去分词）
2. adj. 挑选出来的，精选的</td>
            </tr>
            
             <tr>
                <td class="export-td">365</td>
                <td class="export-td">chopstick</td>
                <td class="export-td">英:/ˈtʃɔpˌstɪk/ 美:/'tʃɑpstɪk/ </td>
                <td class="export-td">筷子</td>
            </tr>
            
             <tr>
                <td class="export-td">366</td>
                <td class="export-td">chillily</td>
                <td class="export-td">/'tʃɪləli/ </td>
                <td class="export-td">adv. 冷漠地</td>
            </tr>
            
             <tr>
                <td class="export-td">367</td>
                <td class="export-td">childminder</td>
                <td class="export-td">/'tʃaɪldmaɪndɚ/ </td>
                <td class="export-td">保姆</td>
            </tr>
            
             <tr>
                <td class="export-td">368</td>
                <td class="export-td">chickenpox</td>
                <td class="export-td">/'tʃɪkɪnpɑks/ </td>
                <td class="export-td">水痘</td>
            </tr>
            
             <tr>
                <td class="export-td">369</td>
                <td class="export-td">chewy</td>
                <td class="export-td">英:/'tʃuːɪ/ 美:/'tʃui/ </td>
                <td class="export-td">adj. 柔软而会黏着的；难嚼的</td>
            </tr>
            
             <tr>
                <td class="export-td">370</td>
                <td class="export-td">chequebook</td>
                <td class="export-td">/'tʃekbuk/ </td>
                <td class="export-td">支票簿</td>
            </tr>
            
             <tr>
                <td class="export-td">371</td>
                <td class="export-td">cheers</td>
                <td class="export-td">英:/tʃɪəz/ 美:/tʃɪrz/ </td>
                <td class="export-td">1. int. 干杯
2. n. 喝采；欢呼</td>
            </tr>
            
             <tr>
                <td class="export-td">372</td>
                <td class="export-td">cheerfully</td>
                <td class="export-td">英:/'tʃiəfəli/ 美:/ˈtʃɪrfəlɪ/ </td>
                <td class="export-td">高高兴兴地</td>
            </tr>
            
             <tr>
                <td class="export-td">373</td>
                <td class="export-td">checkout</td>
                <td class="export-td">英:/'tʃekaʊt/ 美:/'tʃɛkaʊt/ </td>
                <td class="export-td">n. 检验；结帐台；签出；检出</td>
            </tr>
            
             <tr>
                <td class="export-td">374</td>
                <td class="export-td">charmed</td>
                <td class="export-td">英:/tʃɑ:md/ 美:/tʃɑrmd/ </td>
                <td class="export-td">1. adj. 喜悦的；着迷的
2. v. 迷住；对…行魔法；哄诱（charm的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">375</td>
                <td class="export-td">charge card</td>
                <td class="export-td"></td>
                <td class="export-td">付款卡，信用卡；签帐卡</td>
            </tr>
            
             <tr>
                <td class="export-td">376</td>
                <td class="export-td">chair lift</td>
                <td class="export-td"></td>
                <td class="export-td">升降椅；架空滑车</td>
            </tr>
            
             <tr>
                <td class="export-td">377</td>
                <td class="export-td">centimeter</td>
                <td class="export-td">英:/ˈsentimi:tər/ 美:/'sɛntə,mitɚ/ </td>
                <td class="export-td">厘米，公分</td>
            </tr>
            
             <tr>
                <td class="export-td">378</td>
                <td class="export-td">centilitre</td>
                <td class="export-td">/'senti,li:tə/ </td>
                <td class="export-td">厘升</td>
            </tr>
            
             <tr>
                <td class="export-td">379</td>
                <td class="export-td">Celsius</td>
                <td class="export-td">/'selsiəs/ </td>
                <td class="export-td">1. adj. 摄氏的
2. n. 摄氏度</td>
            </tr>
            
             <tr>
                <td class="export-td">380</td>
                <td class="export-td">cellphone</td>
                <td class="export-td">/'sɛl'fon/ </td>
                <td class="export-td">手机</td>
            </tr>
            
             <tr>
                <td class="export-td">381</td>
                <td class="export-td">celery</td>
                <td class="export-td">英:/'selərɪ/ 美:/'sɛləri/ </td>
                <td class="export-td">n. 芹菜</td>
            </tr>
            
             <tr>
                <td class="export-td">382</td>
                <td class="export-td">celebration</td>
                <td class="export-td">英:/selɪ'breɪʃ(ə)n/ 美:/ˌsɛlɪ'breʃən/ </td>
                <td class="export-td">典礼,宗教仪式,庆祝</td>
            </tr>
            
             <tr>
                <td class="export-td">383</td>
                <td class="export-td">CD player</td>
                <td class="export-td"></td>
                <td class="export-td">激光唱机；CD播放器</td>
            </tr>
            
             <tr>
                <td class="export-td">384</td>
                <td class="export-td">CD</td>
                <td class="export-td">/ˌsi: 'di:/ </td>
                <td class="export-td">abbr. 光盘，激光唱片（Compact Disc）；呼叫设备（Calling Device）；中央地区（Central District）；商务部（Commerce Department）</td>
            </tr>
            
             <tr>
                <td class="export-td">385</td>
                <td class="export-td">CCTV</td>
                <td class="export-td">/ˌsi: si: ti: 'vi:/ </td>
                <td class="export-td">abbr. 闭路电视（Closed Circuit Television）；中国中央电视台（China Central Television）</td>
            </tr>
            
             <tr>
                <td class="export-td">386</td>
                <td class="export-td">cauliflower</td>
                <td class="export-td">英:/'kɒlɪflaʊə/ 美:/'kɔlɪ'flaʊɚ/ </td>
                <td class="export-td">花椰菜</td>
            </tr>
            
             <tr>
                <td class="export-td">387</td>
                <td class="export-td">caught</td>
                <td class="export-td">英:/kɔːt/ 美:/kɔt/ </td>
                <td class="export-td">v. 捕捉（catch的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">388</td>
                <td class="export-td">catalogue</td>
                <td class="export-td">英:/ˈkætəlɔɡ/ 美:/'kætəlɔɡ/ </td>
                <td class="export-td">目录,总目,系列</td>
            </tr>
            
             <tr>
                <td class="export-td">389</td>
                <td class="export-td">casually</td>
                <td class="export-td">英:/'kæʒjuəli/ 美:/ˈkæ ʒjʊəlɪ/ </td>
                <td class="export-td">adv. 偶然地；随便地；临时地</td>
            </tr>
            
             <tr>
                <td class="export-td">390</td>
                <td class="export-td">cashier</td>
                <td class="export-td">英:/kæ'ʃɪə/ 美:/kæ'ʃɪr/ </td>
                <td class="export-td">1. n. 出纳员；司库
2. vt. 解雇；抛弃</td>
            </tr>
            
             <tr>
                <td class="export-td">391</td>
                <td class="export-td">carried</td>
                <td class="export-td">/'kærid/ </td>
                <td class="export-td">进行</td>
            </tr>
            
             <tr>
                <td class="export-td">392</td>
                <td class="export-td">carousel</td>
                <td class="export-td">英:/ˌkærə'sel/ 美:/'kærə'sɛl/ </td>
                <td class="export-td">n. 旋转木马</td>
            </tr>
            
             <tr>
                <td class="export-td">393</td>
                <td class="export-td">carnival</td>
                <td class="export-td">英:/'kɑːnɪv(ə)l/ 美:/'kɑrnɪvl/ </td>
                <td class="export-td">n. 狂欢节，嘉年华会；饮宴狂欢</td>
            </tr>
            
             <tr>
                <td class="export-td">394</td>
                <td class="export-td">cardigan</td>
                <td class="export-td">英:/'kɑːdɪg(ə)n/ 美:/'kɑrdɪɡən/ </td>
                <td class="export-td">n. 羊毛衫，开襟羊毛衫（等于cardigan sweater）</td>
            </tr>
            
             <tr>
                <td class="export-td">395</td>
                <td class="export-td">captured</td>
                <td class="export-td"></td>
                <td class="export-td">1. adj. 被俘的；捕获的
2. v. 捕获；占领；引起（capture的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">396</td>
                <td class="export-td">captivity</td>
                <td class="export-td">英:/kæp'tɪvɪtɪ/ 美:/kæp'tɪvəti/ </td>
                <td class="export-td">囚禁, 被俘虏</td>
            </tr>
            
             <tr>
                <td class="export-td">397</td>
                <td class="export-td">captains</td>
                <td class="export-td">/'kæptin/ </td>
                <td class="export-td">n. 船长；军官；首领；（体育运动中的）队长（captain的复数）</td>
            </tr>
            
             <tr>
                <td class="export-td">398</td>
                <td class="export-td">cannot</td>
                <td class="export-td">英:/'kænɒt/ 美:/'kænɑt/ </td>
                <td class="export-td">v. 不能；无法</td>
            </tr>
            
             <tr>
                <td class="export-td">399</td>
                <td class="export-td">cannibal</td>
                <td class="export-td">英:/'kænɪb(ə)l/ 美:/'kænəbl/ </td>
                <td class="export-td">1. n. 食人者；吃同类的动物
2. adj. 食同类的；吃人肉的；凶残的</td>
            </tr>
            
             <tr>
                <td class="export-td">400</td>
                <td class="export-td">canned</td>
                <td class="export-td">英:/kænd/ 美:/kænd/ </td>
                <td class="export-td">1. adj. 录音的；罐装的
2. v. 装于罐头（can的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">401</td>
                <td class="export-td">candlestick</td>
                <td class="export-td">英:/'kænd(ə)lstɪk/ 美:/'kændlstɪk/ </td>
                <td class="export-td">烛台</td>
            </tr>
            
             <tr>
                <td class="export-td">402</td>
                <td class="export-td">cancellation</td>
                <td class="export-td">英:/ˌkænsə'leɪʃ(ə)n/ 美:/ˌkænsə'leʃən/ </td>
                <td class="export-td">取消</td>
            </tr>
            
             <tr>
                <td class="export-td">403</td>
                <td class="export-td">campsite</td>
                <td class="export-td">英:/'kæmpsaɪt/ 美:/'kæmpsaɪt/ </td>
                <td class="export-td">n. 营地</td>
            </tr>
            
             <tr>
                <td class="export-td">404</td>
                <td class="export-td">camping</td>
                <td class="export-td">/'kæmpiŋ/ </td>
                <td class="export-td">1. n. 露营；野营
2. v. 扎营；露营；临时安顿（camp的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">405</td>
                <td class="export-td">camels</td>
                <td class="export-td">/'kæml/ </td>
                <td class="export-td">n. 骆驼体系；骆驼（camel的复数）</td>
            </tr>
            
             <tr>
                <td class="export-td">406</td>
                <td class="export-td">calves</td>
                <td class="export-td">英:/kɑːvz/ 美:/kævz/ </td>
                <td class="export-td">n. 小牛；小腿；腓；[口]呆子（calf的复数）</td>
            </tr>
            
             <tr>
                <td class="export-td">407</td>
                <td class="export-td">caffeine</td>
                <td class="export-td">英:/'kæfiːn/ 美:/'kæfin/ </td>
                <td class="export-td">n. 咖啡因；茶精（兴奋剂）</td>
            </tr>
            
             <tr>
                <td class="export-td">408</td>
                <td class="export-td">cab</td>
                <td class="export-td">英:/kæb/ 美:/kæb/ </td>
                <td class="export-td">1. n. 出租汽车；出租马车；驾驶室
2. vi. 乘出租马车（或汽车）</td>
            </tr>
            
             <tr>
                <td class="export-td">409</td>
                <td class="export-td">businesswoman</td>
                <td class="export-td">英:/'biznis,wumən/ 美:/ˈbɪznɪsˌwʊmən/ </td>
                <td class="export-td">女商人</td>
            </tr>
            
             <tr>
                <td class="export-td">410</td>
                <td class="export-td">buried</td>
                <td class="export-td">/'berid/ </td>
                <td class="export-td">1. adj. 埋葬的；[地]埋藏的
2. v. 埋葬（bury的过去式和过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">411</td>
                <td class="export-td">burglarize</td>
                <td class="export-td">英:/'bɜːgləraɪz/ 美:/'bɝglə,raɪz/ </td>
                <td class="export-td">vt. 闯入…盗窃; vi. 破门盗窃时 态:   burglarized, burglarizin...</td>
            </tr>
            
             <tr>
                <td class="export-td">412</td>
                <td class="export-td">bulldog</td>
                <td class="export-td">英:/'bʊldɒg/ 美:/'bʊl'dɔg/ </td>
                <td class="export-td">n. 牛头犬，恶犬；短枪管大型手枪</td>
            </tr>
            
             <tr>
                <td class="export-td">413</td>
                <td class="export-td">buildable</td>
                <td class="export-td">英:/'bɪldəbl/ 美:/'bɪldəbəl/ </td>
                <td class="export-td">可建</td>
            </tr>
            
             <tr>
                <td class="export-td">414</td>
                <td class="export-td">budgeter</td>
                <td class="export-td">/ˌbʌdʒi'tiə/ </td>
                <td class="export-td">n. 预算编制者</td>
            </tr>
            
             <tr>
                <td class="export-td">415</td>
                <td class="export-td">browser</td>
                <td class="export-td">英:/'brauzə/ 美:/ˈbraʊzɚ/ </td>
                <td class="export-td">n. 吃嫩叶的动物；浏览书本的人；[电脑]浏览器</td>
            </tr>
            
             <tr>
                <td class="export-td">416</td>
                <td class="export-td">breathability</td>
                <td class="export-td">/ˌbri:ðə'biləti/ </td>
                <td class="export-td">透气</td>
            </tr>
            
             <tr>
                <td class="export-td">417</td>
                <td class="export-td">breaststroke</td>
                <td class="export-td">英:/ˈbrestˌstrəuk/ 美:/'brɛststrok/ </td>
                <td class="export-td">蛙泳</td>
            </tr>
            
             <tr>
                <td class="export-td">418</td>
                <td class="export-td">breadcrumb</td>
                <td class="export-td">英:/'bredkrʌm/ 美:/ˈbr ɛdkr ʌmb/ </td>
                <td class="export-td">面包屑</td>
            </tr>
            
             <tr>
                <td class="export-td">419</td>
                <td class="export-td">brackets</td>
                <td class="export-td">/'brækɪt/ </td>
                <td class="export-td">1. n. 支架；方括号；舱口围板支架（bracket的复数）
2. v. 给…装上托架；把…容纳在内（bracket的三单形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">420</td>
                <td class="export-td">boyfriend</td>
                <td class="export-td">英:/'bɒɪfrend/ 美:/'bɔɪfrɛnd/ </td>
                <td class="export-td">男朋友</td>
            </tr>
            
             <tr>
                <td class="export-td">421</td>
                <td class="export-td">bored</td>
                <td class="export-td">英:/bɔ:d/ 美:/bɔrd/ </td>
                <td class="export-td">1. adj. 无聊的；烦人的；无趣的
2. v. 烦扰；使厌烦（bore的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">422</td>
                <td class="export-td">bookshelf</td>
                <td class="export-td">英:/'bʊkʃelf/ 美:/ˈbʊkˌʃɛlf/ </td>
                <td class="export-td">书架</td>
            </tr>
            
             <tr>
                <td class="export-td">423</td>
                <td class="export-td">bookshop</td>
                <td class="export-td">英:/'bʊkʃɒp/ 美:/'bʊkʃɑp/ </td>
                <td class="export-td">n. 书店</td>
            </tr>
            
             <tr>
                <td class="export-td">424</td>
                <td class="export-td">bookmark</td>
                <td class="export-td">英:/'bʊkmɑːk/ 美:/'bʊkmɑrk/ </td>
                <td class="export-td">n. 书签（等于bookmarker）；标记</td>
            </tr>
            
             <tr>
                <td class="export-td">425</td>
                <td class="export-td">bookshelves</td>
                <td class="export-td">/'bukʃelvz/ </td>
                <td class="export-td">书架</td>
            </tr>
            
             <tr>
                <td class="export-td">426</td>
                <td class="export-td">bodybuild</td>
                <td class="export-td"></td>
                <td class="export-td">健身，</td>
            </tr>
            
             <tr>
                <td class="export-td">427</td>
                <td class="export-td">BMX</td>
                <td class="export-td">/'bi:em'eks/ </td>
                <td class="export-td">abbr. 自行车越野赛（bicycle motocross）</td>
            </tr>
            
             <tr>
                <td class="export-td">428</td>
                <td class="export-td">blosson</td>
                <td class="export-td"></td>
                <td class="export-td"></td>
            </tr>
            
             <tr>
                <td class="export-td">429</td>
                <td class="export-td">blog</td>
                <td class="export-td">/blɔg/ </td>
                <td class="export-td">网络随笔，日志 博客</td>
            </tr>
            
             <tr>
                <td class="export-td">430</td>
                <td class="export-td">bishop</td>
                <td class="export-td">英:/ˈbɪʃəp/ 美:/ˈbɪʃəp/ </td>
                <td class="export-td">n. 主教</td>
            </tr>
            
             <tr>
                <td class="export-td">431</td>
                <td class="export-td">biro</td>
                <td class="export-td">/'baiərəu/ </td>
                <td class="export-td">1. n. 圆珠笔的一种
2. vt. 用圆珠笔写</td>
            </tr>
            
             <tr>
                <td class="export-td">432</td>
                <td class="export-td">biologist</td>
                <td class="export-td">/bai'ɔlədʒist/ </td>
                <td class="export-td">生物学家</td>
            </tr>
            
             <tr>
                <td class="export-td">433</td>
                <td class="export-td">biodiversity</td>
                <td class="export-td">英:/ˌbaiəudaiˈvə:səti/ 美:/ˌbaɪodaɪ'vɝsəti/ </td>
                <td class="export-td">生物多样性</td>
            </tr>
            
             <tr>
                <td class="export-td">434</td>
                <td class="export-td">biodegradable</td>
                <td class="export-td">英:/ˌbaɪə(ʊ)dɪ'greɪdəb(ə)l/ 美:/ˌbaɪodɪ'ɡredəbl/ </td>
                <td class="export-td">可生物降解</td>
            </tr>
            
             <tr>
                <td class="export-td">435</td>
                <td class="export-td">binoculars</td>
                <td class="export-td">/bɪ'nɑkjəlɚz/ </td>
                <td class="export-td">双眼望远镜</td>
            </tr>
            
             <tr>
                <td class="export-td">436</td>
                <td class="export-td">bingo</td>
                <td class="export-td">英:/'bɪŋgəʊ/ 美:/'bɪŋɡo/ </td>
                <td class="export-td">n. 宾戈游戏</td>
            </tr>
            
             <tr>
                <td class="export-td">437</td>
                <td class="export-td">billfold</td>
                <td class="export-td">英:/'bɪlfəʊld/ 美:/'bɪlfold/ </td>
                <td class="export-td">n. 皮夹子</td>
            </tr>
            
             <tr>
                <td class="export-td">438</td>
                <td class="export-td">billboard</td>
                <td class="export-td">英:/'bɪlbɔːd/ 美:/'bɪlbɔrd/ </td>
                <td class="export-td">广告牌; 宣传</td>
            </tr>
            
             <tr>
                <td class="export-td">439</td>
                <td class="export-td">bikini</td>
                <td class="export-td">英:/biˈki:ni/ 美:/bɪˈkini/ </td>
                <td class="export-td">n. 比基尼泳装；大爆炸</td>
            </tr>
            
             <tr>
                <td class="export-td">440</td>
                <td class="export-td">bib</td>
                <td class="export-td">英:/bɪb/ 美:/bɪb/ </td>
                <td class="export-td">1. n. 围嘴，围涎；围裙的上部
2. vi. 饮酒，不断地饮酒</td>
            </tr>
            
             <tr>
                <td class="export-td">441</td>
                <td class="export-td">bewildered</td>
                <td class="export-td"></td>
                <td class="export-td"></td>
            </tr>
            
             <tr>
                <td class="export-td">442</td>
                <td class="export-td">behaviour</td>
                <td class="export-td">英:/bɪ'heɪvjə/ 美:/bɪˈhevjɚ/ </td>
                <td class="export-td">行为</td>
            </tr>
            
             <tr>
                <td class="export-td">443</td>
                <td class="export-td">begining</td>
                <td class="export-td">/bi'ɡin/ </td>
                <td class="export-td">1. n. 开始
2. v. 开始；创办（begin的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">444</td>
                <td class="export-td">bedsit</td>
                <td class="export-td">英:/bed'sɪt/ 美:/'bɛdsɪt/ </td>
                <td class="export-td">1. n. 卧室兼起居室
2. vt. 租用卧室兼起居室</td>
            </tr>
            
             <tr>
                <td class="export-td">445</td>
                <td class="export-td">bathtub</td>
                <td class="export-td">英:/'bɑːθtʌb/ 美:/bæθtʌb/ </td>
                <td class="export-td">n. 浴缸</td>
            </tr>
            
             <tr>
                <td class="export-td">446</td>
                <td class="export-td">bathrobe</td>
                <td class="export-td">英:/'bɑːθrəʊb/ 美:/'bæθrob/ </td>
                <td class="export-td">n. 睡衣；浴衣</td>
            </tr>
            
             <tr>
                <td class="export-td">447</td>
                <td class="export-td">Bach</td>
                <td class="export-td">英:/bætʃ/ 美:/bɑk/ </td>
                <td class="export-td">n. 巴赫（德国作曲家）</td>
            </tr>
            
             <tr>
                <td class="export-td">448</td>
                <td class="export-td">barefoot</td>
                <td class="export-td">英:/'beəfʊt/ 美:/'bɛr'fʊt/ </td>
                <td class="export-td">1. adj. 赤脚的
2. adv. 赤着脚地</td>
            </tr>
            
             <tr>
                <td class="export-td">449</td>
                <td class="export-td">ballpoint</td>
                <td class="export-td">英:/ˈbɔ:lˌpɔɪnt/ 美:/'bɔlpɔɪnt/ </td>
                <td class="export-td">圆珠笔</td>
            </tr>
            
             <tr>
                <td class="export-td">450</td>
                <td class="export-td">ballpiont</td>
                <td class="export-td"></td>
                <td class="export-td"></td>
            </tr>
            
             <tr>
                <td class="export-td">451</td>
                <td class="export-td">bakehead</td>
                <td class="export-td">/'beik,hed/ </td>
                <td class="export-td">n. 〈俚〉火车司炉</td>
            </tr>
            
             <tr>
                <td class="export-td">452</td>
                <td class="export-td">baked</td>
                <td class="export-td">英:/'beikid/ 美:/bekt/ </td>
                <td class="export-td">1. adj. 烘焙的；烤的
2. v. 烘培；烧制（bake的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">453</td>
                <td class="export-td">baguette</td>
                <td class="export-td">英:/bæ'get/ 美:/bæˈɡɛt/ </td>
                <td class="export-td">n. 法国棍子面包；成长方形的宝石</td>
            </tr>
            
             <tr>
                <td class="export-td">454</td>
                <td class="export-td">backwards</td>
                <td class="export-td">英:/'bækwədz/ 美:/'bækwɚdz/ </td>
                <td class="export-td">落后的, 向后的</td>
            </tr>
            
             <tr>
                <td class="export-td">455</td>
                <td class="export-td">backup</td>
                <td class="export-td">英:/'bækʌp/ 美:/'bæk,ʌp/ </td>
                <td class="export-td">1. n. 支持；后援；阻塞
2. adj. 候补的；支持的</td>
            </tr>
            
             <tr>
                <td class="export-td">456</td>
                <td class="export-td">babysitter</td>
                <td class="export-td">/'beibisitə/ </td>
                <td class="export-td">保姆</td>
            </tr>
            
             <tr>
                <td class="export-td">457</td>
                <td class="export-td">babysit</td>
                <td class="export-td">/'bebɪsɪt/ </td>
                <td class="export-td">vi. （临时代人）照看婴孩</td>
            </tr>
            
             <tr>
                <td class="export-td">458</td>
                <td class="export-td">B.A</td>
                <td class="export-td"></td>
                <td class="export-td"></td>
            </tr>
            
             <tr>
                <td class="export-td">459</td>
                <td class="export-td">Resistac</td>
                <td class="export-td"></td>
                <td class="export-td">瑞西斯达克铜铝合金</td>
            </tr>
            
             <tr>
                <td class="export-td">460</td>
                <td class="export-td">resistable</td>
                <td class="export-td">/ri'zistəbl/ </td>
                <td class="export-td">adj. 可抵抗的</td>
            </tr>
            
             <tr>
                <td class="export-td">461</td>
                <td class="export-td">resistless</td>
                <td class="export-td">英:/rɪ'zɪs(t)lɪs/ 美:/rɪ'zɪstlɪs/ </td>
                <td class="export-td">不可抗拒的</td>
            </tr>
            
             <tr>
                <td class="export-td">462</td>
                <td class="export-td">resistent</td>
                <td class="export-td">/ri'zistənt/ </td>
                <td class="export-td">性能稳定的</td>
            </tr>
            
             <tr>
                <td class="export-td">463</td>
                <td class="export-td">resistible</td>
                <td class="export-td">英:/rɪ'zɪstəbl/ 美:/rɪ'zɪstəbl/ </td>
                <td class="export-td">可抵抗的</td>
            </tr>
            
             <tr>
                <td class="export-td">464</td>
                <td class="export-td">resister</td>
                <td class="export-td">/ri'zistə/ </td>
                <td class="export-td">n. 抵抗者；反抗者；[物]电阻器</td>
            </tr>
            
             <tr>
                <td class="export-td">465</td>
                <td class="export-td">resistin</td>
                <td class="export-td">/ri'zistin/ </td>
                <td class="export-td">n. 抵抗素；一种锰铜电阻合金</td>
            </tr>
            
             <tr>
                <td class="export-td">466</td>
                <td class="export-td">attendance</td>
                <td class="export-td">英:/ə'tend(ə)ns/ 美:/ə'tɛndəns/ </td>
                <td class="export-td">n.出席，到场<br /><br />护理</td>
            </tr>
            
             <tr>
                <td class="export-td">467</td>
                <td class="export-td">attachment</td>
                <td class="export-td">英:/ə'tætʃm(ə)nt/ 美:/ə'tætʃmənt/ </td>
                <td class="export-td">附件</td>
            </tr>
            
             <tr>
                <td class="export-td">468</td>
                <td class="export-td">attached</td>
                <td class="export-td">英:/əˈtætʃt/ 美:/ə'tætʃt/ </td>
                <td class="export-td">1. adj. 附加的；依恋的，充满爱心的
2. v. 附上（attach的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">469</td>
                <td class="export-td">ATM</td>
                <td class="export-td">/ˌei ti: 'em/ </td>
                <td class="export-td">abbr. 异步传输模式（Asynchronous Transfer Mode）；自动出纳机（Automatic Teller Machine）；空中交通管理（Air Traffic Management）</td>
            </tr>
            
             <tr>
                <td class="export-td">470</td>
                <td class="export-td">athletic</td>
                <td class="export-td">英:/æθ'letɪk/ 美:/æθ'lɛtɪk/ </td>
                <td class="export-td">adj. 运动的，运动员的；体格健壮的</td>
            </tr>
            
             <tr>
                <td class="export-td">471</td>
                <td class="export-td">ate</td>
                <td class="export-td">英:/et/ 美:/ɛt/ </td>
                <td class="export-td">v. 吃（eat的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">472</td>
                <td class="export-td">astronomer</td>
                <td class="export-td">英:/ə'strɒnəmə/ 美:/ə'strɑnəmɚ/ </td>
                <td class="export-td">天文学家</td>
            </tr>
            
             <tr>
                <td class="export-td">473</td>
                <td class="export-td">astonishment</td>
                <td class="export-td">英:/ə'stɒnɪʃmənt/ 美:/ə'stɑnɪʃmənt/ </td>
                <td class="export-td">惊讶，令人惊讶的事</td>
            </tr>
            
             <tr>
                <td class="export-td">474</td>
                <td class="export-td">astonishing</td>
                <td class="export-td">英:/əsˈtɔnɪʃɪŋ/ 美:/ə'stɑnɪʃɪŋ/ </td>
                <td class="export-td">惊人</td>
            </tr>
            
             <tr>
                <td class="export-td">475</td>
                <td class="export-td">astonished</td>
                <td class="export-td">/ə'stɑnɪʃt/ </td>
                <td class="export-td">惊讶</td>
            </tr>
            
             <tr>
                <td class="export-td">476</td>
                <td class="export-td">assistance</td>
                <td class="export-td">英:/ə'sɪst(ə)ns/ 美:/ə'sɪstəns/ </td>
                <td class="export-td">n. 援助，帮助；辅助设备</td>
            </tr>
            
             <tr>
                <td class="export-td">477</td>
                <td class="export-td">assassinate</td>
                <td class="export-td">英:/ə'sæsɪneɪt/ 美:/ə'sæsn'et/ </td>
                <td class="export-td">暗杀</td>
            </tr>
            
             <tr>
                <td class="export-td">478</td>
                <td class="export-td">aspirin</td>
                <td class="export-td">英:/'æsp(ə)rɪn/ 美:/'æsprɪn/ </td>
                <td class="export-td">n. 阿司匹林（解热镇痛药）</td>
            </tr>
            
             <tr>
                <td class="export-td">479</td>
                <td class="export-td">asparagus</td>
                <td class="export-td">英:/ə'spærəgəs/ 美:/ə'spærəgəs/ </td>
                <td class="export-td">芦笋</td>
            </tr>
            
             <tr>
                <td class="export-td">480</td>
                <td class="export-td">ashtray</td>
                <td class="export-td">英:/'æʃtreɪ/ 美:/'æʃtre/ </td>
                <td class="export-td">n. 烟灰缸</td>
            </tr>
            
             <tr>
                <td class="export-td">481</td>
                <td class="export-td">ASAP</td>
                <td class="export-td">/ˌei es ei 'pi:/ </td>
                <td class="export-td">abbr. 尽快（As Soon As Possible）</td>
            </tr>
            
             <tr>
                <td class="export-td">482</td>
                <td class="export-td">artichoke</td>
                <td class="export-td">英:/'ɑːtɪtʃəʊk/ 美:/'ɑrtɪtʃok/ </td>
                <td class="export-td">洋蓟，朝鲜蓟</td>
            </tr>
            
             <tr>
                <td class="export-td">483</td>
                <td class="export-td">arms</td>
                <td class="export-td">/a:mz/ </td>
                <td class="export-td">1. n. 武器；纹章；臂（arm的复数）
2. v. 武装；配备（arm的三单形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">484</td>
                <td class="export-td">armpit</td>
                <td class="export-td">英:/'ɑːmpɪt/ 美:/'ɑrm'pɪt/ </td>
                <td class="export-td">n. 腋窝</td>
            </tr>
            
             <tr>
                <td class="export-td">485</td>
                <td class="export-td">armour</td>
                <td class="export-td">英:/'ɑːmə/ 美:/ˈɑrmɚ/ </td>
                <td class="export-td">n. 装甲；护面；盔甲</td>
            </tr>
            
             <tr>
                <td class="export-td">486</td>
                <td class="export-td">armed</td>
                <td class="export-td">英:/ɑːmd/ 美:/ɑrmd/ </td>
                <td class="export-td">adj. 武装的；有扶手的；有防卫器官的（指动物）</td>
            </tr>
            
             <tr>
                <td class="export-td">487</td>
                <td class="export-td">armchair</td>
                <td class="export-td">英:/ɑːm'tʃeə/ 美:/'ɑrmtʃɛr/ </td>
                <td class="export-td">n. 扶手椅</td>
            </tr>
            
             <tr>
                <td class="export-td">488</td>
                <td class="export-td">are</td>
                <td class="export-td">英:/ɑː/ 美:/ɚ/ </td>
                <td class="export-td">1. v. 是（be的第二人称单复数现在式）
2. n. 公亩</td>
            </tr>
            
             <tr>
                <td class="export-td">489</td>
                <td class="export-td">aquarium</td>
                <td class="export-td">英:/ə'kweərɪəm/ 美:/ə'kwɛrɪəm/ </td>
                <td class="export-td">n. 水族馆；养鱼池；玻璃缸</td>
            </tr>
            
             <tr>
                <td class="export-td">490</td>
                <td class="export-td">APP</td>
                <td class="export-td">英:/æp/ 美:/æp/ </td>
                <td class="export-td">abbr. 穿甲试验（Armor Piercing Proof）；应用（Application）</td>
            </tr>
            
             <tr>
                <td class="export-td">491</td>
                <td class="export-td">anyplace</td>
                <td class="export-td">英:/'enɪpleɪs/ 美:/'ɛnɪples/ </td>
                <td class="export-td">adv. 任何地方</td>
            </tr>
            
             <tr>
                <td class="export-td">492</td>
                <td class="export-td">antivirus</td>
                <td class="export-td">英:/ˌænti'vaɪrəs/ 美:/ˌæntiˈvaɪrəs/ </td>
                <td class="export-td">杀毒软件</td>
            </tr>
            
             <tr>
                <td class="export-td">493</td>
                <td class="export-td">anticlockwise</td>
                <td class="export-td">英:/æntɪ'klɒkwaɪz/ 美:/'æntɪ'klɑkwaɪz/ </td>
                <td class="export-td">逆时针</td>
            </tr>
            
             <tr>
                <td class="export-td">494</td>
                <td class="export-td">anticipation</td>
                <td class="export-td">英:/æntɪsɪ'peɪʃ(ə)n/ 美:/æn,tɪsɪ'peʃən/ </td>
                <td class="export-td">预期, 预料</td>
            </tr>
            
             <tr>
                <td class="export-td">495</td>
                <td class="export-td">anti</td>
                <td class="export-td">英:/'æntɪ/ 美:/'æntaɪ/ </td>
                <td class="export-td">1. adj. 反对的
2. n. 反对者，反对论者</td>
            </tr>
            
             <tr>
                <td class="export-td">496</td>
                <td class="export-td">antelope</td>
                <td class="export-td">英:/'æntɪləʊp/ 美:/'æntɪlop/ </td>
                <td class="export-td">n. 羚羊；羚羊皮革</td>
            </tr>
            
             <tr>
                <td class="export-td">497</td>
                <td class="export-td">anorak</td>
                <td class="export-td">英:/'ænəræk/ 美:/'ænəræk/ </td>
                <td class="export-td">n. 厚夹克；防水布；滑雪衫</td>
            </tr>
            
             <tr>
                <td class="export-td">498</td>
                <td class="export-td">annoying</td>
                <td class="export-td">英:/ə'nɒɪɪŋ/ 美:/ə'nɔɪɪŋ/ </td>
                <td class="export-td">1. adj. 恼人的；讨厌的
2. v. 骚扰（annoy的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">499</td>
                <td class="export-td">annoyed</td>
                <td class="export-td">英:/əˈnɔɪd/ 美:/ə'nɔɪd/ </td>
                <td class="export-td">1. adj. 恼怒的；烦闷的
2. v. 使烦恼；打扰（annoy的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">500</td>
                <td class="export-td">annoyance</td>
                <td class="export-td">英:/ə'nɒɪəns/ 美:/ə'nɔɪəns/ </td>
                <td class="export-td">烦恼</td>
            </tr>
            
             <tr>
                <td class="export-td">501</td>
                <td class="export-td">announcement</td>
                <td class="export-td">英:/ə'naʊnsm(ə)nt/ 美:/ə'naʊnsmənt/ </td>
                <td class="export-td">通知,发表,宣布</td>
            </tr>
            
             <tr>
                <td class="export-td">502</td>
                <td class="export-td">animation</td>
                <td class="export-td">英:/ænɪ'meɪʃ(ə)n/ 美:/ˌænɪ'meʃən/ </td>
                <td class="export-td">动画</td>
            </tr>
            
             <tr>
                <td class="export-td">503</td>
                <td class="export-td">anesthetic</td>
                <td class="export-td">英:/ˌænɪsˈθetɪk/ 美:/ˌænɪs'θɛtɪk/ </td>
                <td class="export-td">麻醉剂, 麻药</td>
            </tr>
            
             <tr>
                <td class="export-td">504</td>
                <td class="export-td">anaesthetic</td>
                <td class="export-td">英:/ˌænis'θetik/ 美:/ˌænɪsˈθɛtɪk/ </td>
                <td class="export-td">麻醉剂</td>
            </tr>
            
             <tr>
                <td class="export-td">505</td>
                <td class="export-td">amusing</td>
                <td class="export-td">英:/ə'mjuːzɪŋ/ 美:/ə'mjuzɪŋ/ </td>
                <td class="export-td">1. adj. 有趣的，好玩的；引人发笑的
2. v. 逗乐；打发；使…高兴（amuse的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">506</td>
                <td class="export-td">amusement</td>
                <td class="export-td">英:/ə'mjuːzm(ə)nt/ 美:/ə'mjuzmənt/ </td>
                <td class="export-td">娱乐, 消遣</td>
            </tr>
            
             <tr>
                <td class="export-td">507</td>
                <td class="export-td">amused</td>
                <td class="export-td">/ə'mju:zd/ </td>
                <td class="export-td">1. adj. 愉快的，顽皮的；被逗乐的
2. v. 使欢乐；逗笑（amuse的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">508</td>
                <td class="export-td">amplifier</td>
                <td class="export-td">英:/'æmplɪfaɪə/ 美:/'æmplɪfaɪɚ/ </td>
                <td class="export-td">放大器, 扩音机</td>
            </tr>
            
             <tr>
                <td class="export-td">509</td>
                <td class="export-td">amp</td>
                <td class="export-td">英:/ˌeɪemˈpi:/ 美:/ˌeemˈpi/ </td>
                <td class="export-td">1. abbr. 安培（ampere，电流强度的单位）；放大器（amplifier）
2. n. [俚]电吉他</td>
            </tr>
            
             <tr>
                <td class="export-td">510</td>
                <td class="export-td">amazing</td>
                <td class="export-td">/ə'mezɪŋ/ </td>
                <td class="export-td">1. adj. 令人惊异的
2. v. 使吃惊（amaze的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">511</td>
                <td class="export-td">amazement</td>
                <td class="export-td">英:/ə'meɪzm(ə)nt/ 美:/ə'mezmənt/ </td>
                <td class="export-td">惊愕, 惊异</td>
            </tr>
            
             <tr>
                <td class="export-td">512</td>
                <td class="export-td">amazed</td>
                <td class="export-td">/ə'meizd/ </td>
                <td class="export-td">1. adj. 惊奇的，吃惊的
2. v. 使…吃惊；把…弄糊涂（amaze的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">513</td>
                <td class="export-td">am</td>
                <td class="export-td">英:/强 æm/ 美:/æm/ </td>
                <td class="export-td">1. abbr. 调幅
2. v. 是</td>
            </tr>
            
             <tr>
                <td class="export-td">514</td>
                <td class="export-td">airmail</td>
                <td class="export-td">英:/'eəmeɪl/ 美:/'ɛrmel/ </td>
                <td class="export-td">航空邮件，航空邮政</td>
            </tr>
            
             <tr>
                <td class="export-td">515</td>
                <td class="export-td">AIDS</td>
                <td class="export-td">/edz/ </td>
                <td class="export-td">abbr. 获得性免疫缺乏综合症；爱滋病（Acquired Immure Deficiency Syndrome）</td>
            </tr>
            
             <tr>
                <td class="export-td">516</td>
                <td class="export-td">accommodatometer</td>
                <td class="export-td"></td>
                <td class="export-td">调节计</td>
            </tr>
            
             <tr>
                <td class="export-td">517</td>
                <td class="export-td">accommodationist</td>
                <td class="export-td">英:/ə,kɑmə'deʃənɪst/ 美:/əˌkɑməˈdeʃənɪst/ </td>
                <td class="export-td">妥协派</td>
            </tr>
            
             <tr>
                <td class="export-td">518</td>
                <td class="export-td">accommodation</td>
                <td class="export-td">英:/əkɒmə'deɪʃ(ə)n/ 美:/ə,kɑmə'deʃən/ </td>
                <td class="export-td">住处,膳宿</td>
            </tr>
            
             <tr>
                <td class="export-td">519</td>
                <td class="export-td">GMT</td>
                <td class="export-td">/ˌdʒi: em 'ti:/ </td>
                <td class="export-td">abbr. 格林威治标准时间（Greenwich Mean Time）</td>
            </tr>
            
             <tr>
                <td class="export-td">520</td>
                <td class="export-td">glacier</td>
                <td class="export-td">英:/'glæsɪə/ 美:/'ɡleʃɚ/ </td>
                <td class="export-td">n. 冰河，冰川</td>
            </tr>
            
             <tr>
                <td class="export-td">521</td>
                <td class="export-td">GCSE</td>
                <td class="export-td">/ˌdʒi: si: es 'i:/ </td>
                <td class="export-td">abbr. （英国）普通中等教育证书（General Certificate of Secondary Education）</td>
            </tr>
            
             <tr>
                <td class="export-td">522</td>
                <td class="export-td">glad</td>
                <td class="export-td">英:/glæd/ 美:/ɡlæd/ </td>
                <td class="export-td">1. adj. 高兴的；乐意的；令人高兴的；灿烂美丽的
2. vt. [古]使高兴</td>
            </tr>
            
             <tr>
                <td class="export-td">523</td>
                <td class="export-td">gnaw</td>
                <td class="export-td">英:/nɔː/ 美:/nɔ/ </td>
                <td class="export-td">1. vt. 咬；折磨；侵蚀
2. vi. 咬；折磨；侵蚀</td>
            </tr>
            
             <tr>
                <td class="export-td">524</td>
                <td class="export-td">head</td>
                <td class="export-td">英:/hed/ 美:/hɛd/ </td>
                <td class="export-td">1. n. 头；上端；最前的部分；头痛；理解力
2. vt. 用头顶；作为…的首领；前进；站在…的前头；给…加标题</td>
            </tr>
            
             <tr>
                <td class="export-td">525</td>
                <td class="export-td">headmaster</td>
                <td class="export-td">英:/hed'mɑːstə/ 美:/ˌhɛd'mæstɚ/ </td>
                <td class="export-td">headmistress<br /><br />校长</td>
            </tr>
            
             <tr>
                <td class="export-td">526</td>
                <td class="export-td">fraction</td>
                <td class="export-td">英:/'frækʃ(ə)n/ 美:/'frækʃən/ </td>
                <td class="export-td">n. 小部分；部分；稍微；[数]分数</td>
            </tr>
            
             <tr>
                <td class="export-td">527</td>
                <td class="export-td">gear</td>
                <td class="export-td">英:/gɪə/ 美:/ɡɪr/ </td>
                <td class="export-td">1. n. 齿轮；传动装置；装置，工具
2. vi. 适合；搭上齿轮；开始工作</td>
            </tr>
            
             <tr>
                <td class="export-td">528</td>
                <td class="export-td">fuel</td>
                <td class="export-td">英:/fjʊəl/ 美:/'fjuəl/ </td>
                <td class="export-td">1. vi. 得到燃料
2. vt. 供以燃料，加燃料</td>
            </tr>
            
             <tr>
                <td class="export-td">529</td>
                <td class="export-td">headache</td>
                <td class="export-td">英:/'hedeɪk/ 美:/'hɛd'ek/ </td>
                <td class="export-td">n. 头痛；麻烦；令人头痛之事</td>
            </tr>
            
             <tr>
                <td class="export-td">530</td>
                <td class="export-td">gadget</td>
                <td class="export-td">英:/'gædʒɪt/ 美:/'gædʒɪt/ </td>
                <td class="export-td">n. 小玩意；小器具；小配件；诡计</td>
            </tr>
            
             <tr>
                <td class="export-td">531</td>
                <td class="export-td">go</td>
                <td class="export-td">英:/gəʊ/ 美:/ɡo/ </td>
                <td class="export-td">1. vi. 走；趋于；达到；运转
2. n. 去；尝试；进行</td>
            </tr>
            
             <tr>
                <td class="export-td">532</td>
                <td class="export-td">fracture</td>
                <td class="export-td">英:/'fræktʃə/ 美:/'fræktʃɚ/ </td>
                <td class="export-td">1. n. 破裂，断裂；骨折
2. vi. 破裂；折断</td>
            </tr>
            
             <tr>
                <td class="export-td">533</td>
                <td class="export-td">fragile</td>
                <td class="export-td">英:/'frædʒaɪl/ 美:/'frædʒəl/ </td>
                <td class="export-td">adj. 脆的；易碎的</td>
            </tr>
            
             <tr>
                <td class="export-td">534</td>
                <td class="export-td">gracious</td>
                <td class="export-td">英:/'greɪʃəs/ 美:/'ɡreʃəs/ </td>
                <td class="export-td">1. adj. 亲切的；和蔼的；高尚的；雅致的
2. int. 天哪；哎呀</td>
            </tr>
            
             <tr>
                <td class="export-td">535</td>
                <td class="export-td">glamorous</td>
                <td class="export-td">英:/'glæmərəs/ 美:/'glæmərəs/ </td>
                <td class="export-td">富有魅力的,迷人的</td>
            </tr>
            
             <tr>
                <td class="export-td">536</td>
                <td class="export-td">geese</td>
                <td class="export-td">英:/ɡiːs/ 美:/ɡis/ </td>
                <td class="export-td">n. 鹅（goose复数）</td>
            </tr>
            
             <tr>
                <td class="export-td">537</td>
                <td class="export-td">fragment</td>
                <td class="export-td">英:/'frægm(ə)nt/ 美:/'fræɡmənt/ </td>
                <td class="export-td">1. n. 碎片；片断或不完整部分
2. vt. 使成碎片</td>
            </tr>
            
             <tr>
                <td class="export-td">538</td>
                <td class="export-td">grade</td>
                <td class="export-td">英:/greɪd/ 美:/ɡred/ </td>
                <td class="export-td">1. n. 等级；年级；阶段；级别；成绩
2. vt. 评分；把…分等级</td>
            </tr>
            
             <tr>
                <td class="export-td">539</td>
                <td class="export-td">glance</td>
                <td class="export-td">英:/glɑːns/ 美:/ɡlæns/ </td>
                <td class="export-td">1. n. 一瞥；一滑；闪光
2. vi. 扫视，匆匆一看；瞥闪，瞥见；反光</td>
            </tr>
            
             <tr>
                <td class="export-td">540</td>
                <td class="export-td">gel</td>
                <td class="export-td">英:/dʒel/ 美:/dʒɛl/ </td>
                <td class="export-td">1. vi. 胶化
2. n. 凝胶，胶体</td>
            </tr>
            
             <tr>
                <td class="export-td">541</td>
                <td class="export-td">fragrance</td>
                <td class="export-td">英:/'freɪgr(ə)ns/ 美:/ˈfreɡrəns/ </td>
                <td class="export-td">香味</td>
            </tr>
            
             <tr>
                <td class="export-td">542</td>
                <td class="export-td">full</td>
                <td class="export-td">英:/fʊl/ 美:/fʊl/ </td>
                <td class="export-td">1. adj. 完全的，完整的；满的，充满的；丰满的；丰富的；详尽的；完美的
2. adv. 完全地；十分，非常；整整</td>
            </tr>
            
             <tr>
                <td class="export-td">543</td>
                <td class="export-td">headlight</td>
                <td class="export-td">英:/'hedlaɪt/ 美:/'hɛdlaɪt/ </td>
                <td class="export-td">前灯, 桅灯</td>
            </tr>
            
             <tr>
                <td class="export-td">544</td>
                <td class="export-td">fragrant</td>
                <td class="export-td">英:/'freɪgr(ə)nt/ 美:/'fregrənt/ </td>
                <td class="export-td">adj. 芳香的；愉快的</td>
            </tr>
            
             <tr>
                <td class="export-td">545</td>
                <td class="export-td">glare</td>
                <td class="export-td">英:/gleə/ 美:/ɡlɛr/ </td>
                <td class="export-td">1. n. 刺眼；耀眼的光；受公众注目
2. vi. 瞪眼表示</td>
            </tr>
            
             <tr>
                <td class="export-td">546</td>
                <td class="export-td">headline</td>
                <td class="export-td">英:/'hedlaɪn/ 美:/'hɛdlaɪn/ </td>
                <td class="export-td">1. n. 大标题；内容提要；栏外标题；头版头条新闻
2. vt. 给…加标题；使成为注意中心；大力宣传</td>
            </tr>
            
             <tr>
                <td class="export-td">547</td>
                <td class="export-td">epic</td>
                <td class="export-td">英:/'epɪk/ 美:/'ɛpɪk/ </td>
                <td class="export-td">1. adj. 史诗的，叙事诗的
2. n. 史诗；叙事诗；史诗般的作品</td>
            </tr>
            
             <tr>
                <td class="export-td">548</td>
                <td class="export-td">glaring</td>
                <td class="export-td">英:/'gleərɪŋ/ 美:/ˈɡlɛrɪŋ/ </td>
                <td class="export-td">adj. 耀眼的；瞪视的；炯炯的</td>
            </tr>
            
             <tr>
                <td class="export-td">549</td>
                <td class="export-td">each</td>
                <td class="export-td">英:/iːtʃ/ 美:/itʃ/ </td>
                <td class="export-td">1. adj. 每；各自的
2. adv. 每个；各自</td>
            </tr>
            
             <tr>
                <td class="export-td">550</td>
                <td class="export-td">by</td>
                <td class="export-td">英:/baɪ/ 美:/baɪ/ </td>
                <td class="export-td">1. prep. 被；经由；在……之前；在附近；依据；通过
2. adv. 经过；通过；附近；[域]白俄罗斯</td>
            </tr>
            
             <tr>
                <td class="export-td">551</td>
                <td class="export-td">eraser</td>
                <td class="export-td">英:/ɪ'reɪzə/ 美:/ɪ'resɚ/ </td>
                <td class="export-td">n. 擦除器；清除器</td>
            </tr>
            
             <tr>
                <td class="export-td">552</td>
                <td class="export-td">frail</td>
                <td class="export-td">英:/freɪl/ 美:/frel/ </td>
                <td class="export-td">1. adj. 虚弱的；脆弱的
2. n. 灯心草篓；少妇；少女</td>
            </tr>
            
             <tr>
                <td class="export-td">553</td>
                <td class="export-td">cook</td>
                <td class="export-td">英:/kʊk/ 美:/kʊk/ </td>
                <td class="export-td">1. vt. 烹调，煮
2. vi. 烹调，做菜</td>
            </tr>
            
             <tr>
                <td class="export-td">554</td>
                <td class="export-td">gradual</td>
                <td class="export-td">英:/'grædʒʊəl/ 美:/'ɡrædʒuəl/ </td>
                <td class="export-td">1. adj. 逐渐的；平缓的
2. n. 弥撒升阶圣歌集</td>
            </tr>
            
             <tr>
                <td class="export-td">555</td>
                <td class="export-td">fully</td>
                <td class="export-td">英:/'fʊlɪ/ 美:/'fʊli/ </td>
                <td class="export-td">adv. 完全地；充分地；彻底地</td>
            </tr>
            
             <tr>
                <td class="export-td">556</td>
                <td class="export-td">cooking</td>
                <td class="export-td">英:/'kʊkɪŋ/ 美:/'kʊkɪŋ/ </td>
                <td class="export-td">1. n. 烹饪
2. adj. 烹调用的</td>
            </tr>
            
             <tr>
                <td class="export-td">557</td>
                <td class="export-td">gradually</td>
                <td class="export-td">英:/ˈ grædjʊəlɪ/ 美:/'grædʒʊəli/ </td>
                <td class="export-td">逐渐地</td>
            </tr>
            
             <tr>
                <td class="export-td">558</td>
                <td class="export-td">grandfather</td>
                <td class="export-td">英:/'græn(d)fɑːðə/ 美:/'græn'fɑðɚ/ </td>
                <td class="export-td">grandmother, grandparent<br /><br />祖父</td>
            </tr>
            
             <tr>
                <td class="export-td">559</td>
                <td class="export-td">frame</td>
                <td class="export-td">英:/freɪm/ 美:/frem/ </td>
                <td class="export-td">1. n. 框架；结构；画面
2. vt. 设计；陷害；建造；使…适合</td>
            </tr>
            
             <tr>
                <td class="export-td">560</td>
                <td class="export-td">glass</td>
                <td class="export-td">英:/glɑːs/ 美:/ɡlæs/ </td>
                <td class="export-td">1. n. 玻璃；镜子；玻璃制品
2. vt. 反映；给某物加玻璃</td>
            </tr>
            
             <tr>
                <td class="export-td">561</td>
                <td class="export-td">eager</td>
                <td class="export-td">英:/'iːgə/ 美:/'igɚ/ </td>
                <td class="export-td">adj. 渴望的；热心的；热切的</td>
            </tr>
            
             <tr>
                <td class="export-td">562</td>
                <td class="export-td">diabetes</td>
                <td class="export-td">英:/ˌdaɪə'biːtiːz/ 美:/ˌdaɪə'bitiz/ </td>
                <td class="export-td">n. 糖尿病；多尿症</td>
            </tr>
            
             <tr>
                <td class="export-td">563</td>
                <td class="export-td">gain</td>
                <td class="export-td">英:/geɪn/ 美:/ɡen/ </td>
                <td class="export-td">1. n. 收获；增加；利润
2. vt. 获得；增加；赚到</td>
            </tr>
            
             <tr>
                <td class="export-td">564</td>
                <td class="export-td">erect</td>
                <td class="export-td">英:/ɪ'rekt/ 美:/ɪ'rɛkt/ </td>
                <td class="export-td">1. vt. 使竖立；建造；安装
2. adj. 竖立的；笔直的；因性刺激而勃起的</td>
            </tr>
            
             <tr>
                <td class="export-td">565</td>
                <td class="export-td">edge</td>
                <td class="export-td">英:/edʒ/ 美:/ɛdʒ/ </td>
                <td class="export-td">1. n. 边缘；刀刃；优势；锋利
2. vt. 使锐利；将…开刃；给…加上边</td>
            </tr>
            
             <tr>
                <td class="export-td">566</td>
                <td class="export-td">exact</td>
                <td class="export-td">英:/ɪg'zækt/ 美:/ɪɡ'zækt/ </td>
                <td class="export-td">1. adj. 精确的；准确的，精密的
2. vt. 强求；要求；急需</td>
            </tr>
            
             <tr>
                <td class="export-td">567</td>
                <td class="export-td">crab</td>
                <td class="export-td">英:/kræb/ 美:/kræb/ </td>
                <td class="export-td">1. n. 螃蟹；蟹肉；脾气乖戾的人；起重机
2. vt. 抱怨；破坏；使偏航</td>
            </tr>
            
             <tr>
                <td class="export-td">568</td>
                <td class="export-td">BC</td>
                <td class="export-td">/ˌbi: 'si:/ </td>
                <td class="export-td">abbr. 公元前（Before Christ）</td>
            </tr>
            
             <tr>
                <td class="export-td">569</td>
                <td class="export-td">graduate</td>
                <td class="export-td">英:/'grædʒʊət/ 美:/'ɡrædʒuət/ </td>
                <td class="export-td">1. vt. 授予…学位；分等级；标上刻度
2. vi. 毕业；渐变</td>
            </tr>
            
             <tr>
                <td class="export-td">570</td>
                <td class="export-td">claim</td>
                <td class="export-td">英:/kleɪm/ 美:/klem/ </td>
                <td class="export-td">1. vi. 提出要求
2. vt. 要求；声称；认领；需要</td>
            </tr>
            
             <tr>
                <td class="export-td">571</td>
                <td class="export-td">gem</td>
                <td class="export-td">英:/dʒem/ 美:/dʒɛm/ </td>
                <td class="export-td">1. n. 宝石；精华；宝物；珍品；美玉
2. vt. 点缀；用宝石镶嵌；饰以宝石</td>
            </tr>
            
             <tr>
                <td class="export-td">572</td>
                <td class="export-td">cub</td>
                <td class="export-td">英:/kʌb/ 美:/kʌb/ </td>
                <td class="export-td">1. n. 幼兽；不懂规矩的年轻人
2. vi. 生育幼兽</td>
            </tr>
            
             <tr>
                <td class="export-td">573</td>
                <td class="export-td">epidemic</td>
                <td class="export-td">英:/epɪ'demɪk/ 美:/ˌɛpɪ'dɛmɪk/ </td>
                <td class="export-td">1. adj. 流行的；传染性的
2. n. 流行病；传染病；风尚等的流行</td>
            </tr>
            
             <tr>
                <td class="export-td">574</td>
                <td class="export-td">framework</td>
                <td class="export-td">英:/'freɪmwɜːk/ 美:/'fremwɝk/ </td>
                <td class="export-td">骨架</td>
            </tr>
            
             <tr>
                <td class="export-td">575</td>
                <td class="export-td">cooker</td>
                <td class="export-td">英:/'kʊkə/ 美:/'kʊkɚ/ </td>
                <td class="export-td">n. 炊具；烹饪用水果；窜改者</td>
            </tr>
            
             <tr>
                <td class="export-td">576</td>
                <td class="export-td">enable</td>
                <td class="export-td">英:/ɪn'eɪb(ə)l/ 美:/ɛˈnebəl/ </td>
                <td class="export-td">vt. 使能够，使成为可能；授予权利或方法</td>
            </tr>
            
             <tr>
                <td class="export-td">577</td>
                <td class="export-td">boar</td>
                <td class="export-td">英:/bɔː/ 美:/bɔr/ </td>
                <td class="export-td">n. 野猪；（未阉的）公猪</td>
            </tr>
            
             <tr>
                <td class="export-td">578</td>
                <td class="export-td">headquarters</td>
                <td class="export-td">英:/hed'kwɔːtəz/ 美:/'hɛdkwɔrtɚz/ </td>
                <td class="export-td">司令部</td>
            </tr>
            
             <tr>
                <td class="export-td">579</td>
                <td class="export-td">cookery</td>
                <td class="export-td">英:/'kʊk(ə)rɪ/ 美:/ˈkʊkəri/ </td>
                <td class="export-td">n. 烹调术；烹调业</td>
            </tr>
            
             <tr>
                <td class="export-td">580</td>
                <td class="export-td">be</td>
                <td class="export-td">英:/biː/ 美:/bi/ </td>
                <td class="export-td">prep. 在，存在；是</td>
            </tr>
            
             <tr>
                <td class="export-td">581</td>
                <td class="export-td">board</td>
                <td class="export-td">英:/bɔːd/ 美:/bɔrd/ </td>
                <td class="export-td">1. n. 木板；甲板；膳食；董事会
2. vt. 用板盖上；上（飞机、车、船等）；给提供膳宿</td>
            </tr>
            
             <tr>
                <td class="export-td">582</td>
                <td class="export-td">exactly</td>
                <td class="export-td">英:/ɪg'zæk(t)lɪ/ 美:/ɪɡ'zæktli/ </td>
                <td class="export-td">adv. 精确地；正确地；正是；恰好地</td>
            </tr>
            
             <tr>
                <td class="export-td">583</td>
                <td class="export-td">apart</td>
                <td class="export-td">英:/ə'pɑːt/ 美:/ə'pɑrt/ </td>
                <td class="export-td">1. adv. 分离着；相距；与众不同地
2. adj. 分离的；与众不同的</td>
            </tr>
            
             <tr>
                <td class="export-td">584</td>
                <td class="export-td">bra</td>
                <td class="export-td">英:/brɑː/ 美:/brɑ/ </td>
                <td class="export-td">n. 胸罩</td>
            </tr>
            
             <tr>
                <td class="export-td">585</td>
                <td class="export-td">boarding</td>
                <td class="export-td">英:/'bɔːdɪŋ/ 美:/'bɔrdɪŋ/ </td>
                <td class="export-td">1. n. 木板；寄膳宿；上船
2. adj. 供膳的</td>
            </tr>
            
             <tr>
                <td class="export-td">586</td>
                <td class="export-td">eagle</td>
                <td class="export-td">英:/'iːg(ə)l/ 美:/'igl/ </td>
                <td class="export-td">n. 鹰；鹰状标饰</td>
            </tr>
            
             <tr>
                <td class="export-td">587</td>
                <td class="export-td">bye</td>
                <td class="export-td">英:/baɪ/ 美:/baɪ/ </td>
                <td class="export-td">1. int. 再见
2. n. 轮空；次要的东西</td>
            </tr>
            
             <tr>
                <td class="export-td">588</td>
                <td class="export-td">black</td>
                <td class="export-td">英:/blæk/ 美:/blæk/ </td>
                <td class="export-td">黑色</td>
            </tr>
            
             <tr>
                <td class="export-td">589</td>
                <td class="export-td">do</td>
                <td class="export-td">英:/duː/ 美:/du/ </td>
                <td class="export-td">1. n. 要求；规定；C大调音阶中的第一音
2. vt. 做；完成；进行；解答</td>
            </tr>
            
             <tr>
                <td class="export-td">590</td>
                <td class="export-td">beach</td>
                <td class="export-td">英:/biːtʃ/ 美:/bitʃ/ </td>
                <td class="export-td">1. n. 海滩；湖滨
2. vt. 将…拖上岸</td>
            </tr>
            
             <tr>
                <td class="export-td">591</td>
                <td class="export-td">conceal</td>
                <td class="export-td">英:/kən'siːl/ 美:/kən'sil/ </td>
                <td class="export-td">vt. 隐藏；隐瞒</td>
            </tr>
            
             <tr>
                <td class="export-td">592</td>
                <td class="export-td">cube</td>
                <td class="export-td">英:/kjuːb/ 美:/kjʊb/ </td>
                <td class="export-td">1. n. 立方体；立方；骰子
2. vt. 使成立方形；使自乘二次；量…的体积</td>
            </tr>
            
             <tr>
                <td class="export-td">593</td>
                <td class="export-td">apartment</td>
                <td class="export-td">英:/ə'pɑːtm(ə)nt/ 美:/ə'pɑrtmənt/ </td>
                <td class="export-td">一套公寓房间</td>
            </tr>
            
             <tr>
                <td class="export-td">594</td>
                <td class="export-td">graffiti</td>
                <td class="export-td">英:/ɡrəˈfi:ti:/ 美:/ɡrə'fiti/ </td>
                <td class="export-td">n. 墙上乱写乱画的东西（graffito的复数形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">595</td>
                <td class="export-td">cool</td>
                <td class="export-td">英:/kuːl/ 美:/kʊl/ </td>
                <td class="export-td">1. adj. 冷静的；凉爽的；[口]出色的
2. vt. 使…冷却；使…平静下来</td>
            </tr>
            
             <tr>
                <td class="export-td">596</td>
                <td class="export-td">gala</td>
                <td class="export-td">英:/'gɑːlə/ 美:/'ɡelə/ </td>
                <td class="export-td">1. n. 节日，特别娱乐；祝贺，庆祝
2. adj. 欢乐的；节日的，欢庆的</td>
            </tr>
            
             <tr>
                <td class="export-td">597</td>
                <td class="export-td">chain</td>
                <td class="export-td">英:/tʃein/ 美:/tʃen/ </td>
                <td class="export-td">1. n. 链；束缚；枷锁
2. vt. 束缚；囚禁；用铁练锁住</td>
            </tr>
            
             <tr>
                <td class="export-td">598</td>
                <td class="export-td">crack</td>
                <td class="export-td">英:/kræk/ 美:/kræk/ </td>
                <td class="export-td">1. vt. 使破裂；打开；变声
2. vi. 爆裂；破裂</td>
            </tr>
            
             <tr>
                <td class="export-td">599</td>
                <td class="export-td">bracelet</td>
                <td class="export-td">英:/'breɪslɪt/ 美:/'breslət/ </td>
                <td class="export-td">n. 手镯</td>
            </tr>
            
             <tr>
                <td class="export-td">600</td>
                <td class="export-td">exaggerate</td>
                <td class="export-td">英:/ɪg'zædʒəreɪt/ 美:/ɪɡ'zædʒəret/ </td>
                <td class="export-td">夸大,夸张</td>
            </tr>
            
             <tr>
                <td class="export-td">601</td>
                <td class="export-td">bubble</td>
                <td class="export-td">英:/'bʌb(ə)l/ 美:/'bʌbl/ </td>
                <td class="export-td">1. n. 气泡，泡沫，泡状物；透明圆形罩，圆形顶
2. vi. 沸腾，冒泡；发出气泡声</td>
            </tr>
            
             <tr>
                <td class="export-td">602</td>
                <td class="export-td">again</td>
                <td class="export-td">英:/ə'gen/ 美:/ə'ɡɛn/ </td>
                <td class="export-td">adv. 再一次；又，此外</td>
            </tr>
            
             <tr>
                <td class="export-td">603</td>
                <td class="export-td">grain</td>
                <td class="export-td">英:/greɪn/ 美:/ɡren/ </td>
                <td class="export-td">1. n. 粮食；颗粒；谷物；纹理
2. vi. 成谷粒</td>
            </tr>
            
             <tr>
                <td class="export-td">604</td>
                <td class="export-td">ear</td>
                <td class="export-td">英:/ɪə/ 美:/ɪr/ </td>
                <td class="export-td">1. n. 耳朵；听觉；倾听；穗
2. vi. （美俚）听见；抽穗</td>
            </tr>
            
             <tr>
                <td class="export-td">605</td>
                <td class="export-td">gender</td>
                <td class="export-td">英:/'dʒendə/ 美:/'dʒɛndɚ/ </td>
                <td class="export-td">1. n. 性；性别；性交
2. vt. 生（过去式gendered，过去分词gendered，现在分词gendering，第三人称单数genders，形容词genderless）</td>
            </tr>
            
             <tr>
                <td class="export-td">606</td>
                <td class="export-td">conceited</td>
                <td class="export-td">英:/kən'siːtɪd/ 美:/kən'sitɪd/ </td>
                <td class="export-td">自负的, 幻想的</td>
            </tr>
            
             <tr>
                <td class="export-td">607</td>
                <td class="export-td">AD</td>
                <td class="export-td">英:/æd/ 美:/'e 'di/ </td>
                <td class="export-td">n. 公元</td>
            </tr>
            
             <tr>
                <td class="export-td">608</td>
                <td class="export-td">ad</td>
                <td class="export-td">/əd/ </td>
                <td class="export-td">广告</td>
            </tr>
            
             <tr>
                <td class="export-td">609</td>
                <td class="export-td">dab</td>
                <td class="export-td">英:/dæb/ 美:/dæb/ </td>
                <td class="export-td">1. n. 轻拍；少量；熟手；比目鱼
2. v. 涂；轻拍；轻擦；轻敷（过去式dabbed，过去分词dabbed，现在分词dabbing，第三人称单数dabs）</td>
            </tr>
            
             <tr>
                <td class="export-td">610</td>
                <td class="export-td">gene</td>
                <td class="export-td">英:/dʒiːn/ 美:/dʒin/ </td>
                <td class="export-td">n. 基因，遗传因子</td>
            </tr>
            
             <tr>
                <td class="export-td">611</td>
                <td class="export-td">ahead</td>
                <td class="export-td">英:/ə'hed/ 美:/ə'hɛd/ </td>
                <td class="export-td">1. adv. 向前；预先；领先
2. adj. 向前的；领先的</td>
            </tr>
            
             <tr>
                <td class="export-td">612</td>
                <td class="export-td">frank</td>
                <td class="export-td">/fræŋk/ </td>
                <td class="export-td">1. adj. 坦白的，直率的；老实的
2. n. 免费邮寄特权</td>
            </tr>
            
             <tr>
                <td class="export-td">613</td>
                <td class="export-td">cubicle</td>
                <td class="export-td">英:/'kjuːbɪk(ə)l/ 美:/'kjubɪkl/ </td>
                <td class="export-td">n. 小卧室；小隔间</td>
            </tr>
            
             <tr>
                <td class="export-td">614</td>
                <td class="export-td">edible</td>
                <td class="export-td">英:/'edɪb(ə)l/ 美:/'ɛdəbl/ </td>
                <td class="export-td">1. adj. 可食用的
2. n. 食物；食品</td>
            </tr>
            
             <tr>
                <td class="export-td">615</td>
                <td class="export-td">blackberry</td>
                <td class="export-td">英:/'blækb(ə)rɪ/ 美:/'blæk'bɛri/ </td>
                <td class="export-td">黑莓</td>
            </tr>
            
             <tr>
                <td class="export-td">616</td>
                <td class="export-td">galaxy</td>
                <td class="export-td">英:/'gæləksɪ/ 美:/'ɡæləksi/ </td>
                <td class="export-td">n. 银河；星系；银河系；一群显赫的人</td>
            </tr>
            
             <tr>
                <td class="export-td">617</td>
                <td class="export-td">blackbird</td>
                <td class="export-td">英:/'blækbɜːd/ 美:/'blækbɝd/ </td>
                <td class="export-td">画眉, 燕八哥</td>
            </tr>
            
             <tr>
                <td class="export-td">618</td>
                <td class="export-td">duchess</td>
                <td class="export-td">英:/'dʌtʃɪs/ 美:/'dʌtʃəs/ </td>
                <td class="export-td">1. n. 公爵夫人；女公爵；雍容华贵的妇女；[英俚]小老板娘
2. vt. （澳）盛情款待；[口]讨好</td>
            </tr>
            
             <tr>
                <td class="export-td">619</td>
                <td class="export-td">academic</td>
                <td class="export-td">英:/ækə'demɪk/ 美:/ˌækə'dɛmɪk/ </td>
                <td class="export-td">1. adj. 学院的；学术的；理论的
2. n. 大学生，大学教师；学者</td>
            </tr>
            
             <tr>
                <td class="export-td">620</td>
                <td class="export-td">age</td>
                <td class="export-td">英:/eɪdʒ/ 美:/edʒ/ </td>
                <td class="export-td">1. n. 年龄；时代；阶段；寿命，使用年限
2. vi. 变老；成熟</td>
            </tr>
            
             <tr>
                <td class="export-td">621</td>
                <td class="export-td">earache</td>
                <td class="export-td">英:/'ɪəreɪk/ 美:/'ɪr'ek/ </td>
                <td class="export-td">n. 耳朵痛，耳痛</td>
            </tr>
            
             <tr>
                <td class="export-td">622</td>
                <td class="export-td">byte</td>
                <td class="export-td">英:/baɪt/ 美:/baɪt/ </td>
                <td class="export-td">n. [计]字节；8位元组</td>
            </tr>
            
             <tr>
                <td class="export-td">623</td>
                <td class="export-td">boast</td>
                <td class="export-td">英:/bəʊst/ 美:/bost/ </td>
                <td class="export-td">1. vt. 以有…而自豪；夸口说，自吹自擂说
2. n. 自夸；值得夸耀的事物，引以为荣的事物</td>
            </tr>
            
             <tr>
                <td class="export-td">624</td>
                <td class="export-td">embarrass</td>
                <td class="export-td">英:/ɪm'bærəs/ 美:/ɪm'bærəs/ </td>
                <td class="export-td">使...困窘,阻碍</td>
            </tr>
            
             <tr>
                <td class="export-td">625</td>
                <td class="export-td">drag</td>
                <td class="export-td">英:/dræg/ 美:/dræɡ/ </td>
                <td class="export-td">1. vt. 拖拉；拖累；缓慢而吃力地行进
2. vi. 拖曳；缓慢而吃力地行进</td>
            </tr>
            
             <tr>
                <td class="export-td">626</td>
                <td class="export-td">embarrassing</td>
                <td class="export-td">英:/ɪmˈbærəsɪŋ/ 美:/ɪm'bærəsɪŋ/ </td>
                <td class="export-td">令人为难的</td>
            </tr>
            
             <tr>
                <td class="export-td">627</td>
                <td class="export-td">godchild</td>
                <td class="export-td">英:/'gɒdtʃaɪld/ 美:/ˈɡɑdˌtʃaɪld/ </td>
                <td class="export-td">god-daughter, godson   god-daughter, godson<br /><br />n. 教子（名义上的儿子）</td>
            </tr>
            
             <tr>
                <td class="export-td">628</td>
                <td class="export-td">diagonal</td>
                <td class="export-td">英:/daɪ'æg(ə)n(ə)l/ 美:/daɪ'æɡənl/ </td>
                <td class="export-td">1. adj. 对角线的；斜纹的；斜的
2. n. 对角线；斜线</td>
            </tr>
            
             <tr>
                <td class="export-td">629</td>
                <td class="export-td">apologize</td>
                <td class="export-td">英:/əˈpɔlədʒaiz/ 美:/ə'pɑlədʒaɪz/ </td>
                <td class="export-td">apologise<br /><br />道歉,谢罪</td>
            </tr>
            
             <tr>
                <td class="export-td">630</td>
                <td class="export-td">coach</td>
                <td class="export-td">英:/kəʊtʃ/ 美:/kotʃ/ </td>
                <td class="export-td">1. n. 教练；旅客车厢；长途公车；四轮大马车
2. vt. 训练；指导</td>
            </tr>
            
             <tr>
                <td class="export-td">631</td>
                <td class="export-td">grammar</td>
                <td class="export-td">英:/'græmə/ 美:/'græmɚ/ </td>
                <td class="export-td">n. 语法；语法书</td>
            </tr>
            
             <tr>
                <td class="export-td">632</td>
                <td class="export-td">aerial</td>
                <td class="export-td">英:/'eərɪəl/ 美:/'ɛrɪəl/ </td>
                <td class="export-td">1. adj. 空气的；空中的，航空的；空想的
2. n. 天线</td>
            </tr>
            
             <tr>
                <td class="export-td">633</td>
                <td class="export-td">exam</td>
                <td class="export-td">英:/ɪg'zæm/ 美:/ɪg'zæm/ </td>
                <td class="export-td">n. 测验；考试</td>
            </tr>
            
             <tr>
                <td class="export-td">634</td>
                <td class="export-td">duck</td>
                <td class="export-td">英:/dʌk/ 美:/dʌk/ </td>
                <td class="export-td">1. n. 鸭子；鸭肉；（英）宝贝儿；[版]零分
2. vi. 闪避；没入水中</td>
            </tr>
            
             <tr>
                <td class="export-td">635</td>
                <td class="export-td">affair</td>
                <td class="export-td">英:/ə'feə/ 美:/ə'fɛr/ </td>
                <td class="export-td">n. 事情；事务；私事；（尤指关系不长久的）风流韵事</td>
            </tr>
            
             <tr>
                <td class="export-td">636</td>
                <td class="export-td">alarm</td>
                <td class="export-td">英:/ə'lɑːm/ 美:/ə'lɑrm/ </td>
                <td class="export-td">1. n. 警报，警告器；惊慌
2. vt. 警告；使惊恐</td>
            </tr>
            
             <tr>
                <td class="export-td">637</td>
                <td class="export-td">duckling</td>
                <td class="export-td">英:/'dʌklɪŋ/ 美:/'dʌklɪŋ/ </td>
                <td class="export-td">n. 小鸭子</td>
            </tr>
            
             <tr>
                <td class="export-td">638</td>
                <td class="export-td">erotic</td>
                <td class="export-td">英:/ɪ'rɒtɪk/ 美:/ɪ'rɑtɪk/ </td>
                <td class="export-td">1. adj. 色情的；性欲的；性爱的
2. n. 好色之徒</td>
            </tr>
            
             <tr>
                <td class="export-td">639</td>
                <td class="export-td">cracker</td>
                <td class="export-td">英:/'krækə/ 美:/'krækɚ/ </td>
                <td class="export-td">n. 爆竹；饼干；胡桃钳；解密高手</td>
            </tr>
            
             <tr>
                <td class="export-td">640</td>
                <td class="export-td">headway</td>
                <td class="export-td">英:/'hedweɪ/ 美:/'hɛd,we/ </td>
                <td class="export-td">n. 前进；进步；航行速度；间隔时间</td>
            </tr>
            
             <tr>
                <td class="export-td">641</td>
                <td class="export-td">affect</td>
                <td class="export-td">英:/ə'fekt/ 美:/ə'fɛkt/ </td>
                <td class="export-td">1. vt. 影响；假装；感动；感染
2. vi. 倾向；喜欢</td>
            </tr>
            
             <tr>
                <td class="export-td">642</td>
                <td class="export-td">concentrate</td>
                <td class="export-td">英:/'kɒns(ə)ntreɪt/ 美:/'kɑnsn'tret/ </td>
                <td class="export-td">浓缩,精选</td>
            </tr>
            
             <tr>
                <td class="export-td">643</td>
                <td class="export-td">embarrassment</td>
                <td class="export-td">英:/emˈbærəsmənt/ 美:/ɪm'bærəsmənt/ </td>
                <td class="export-td">困窘，尴尬，困难</td>
            </tr>
            
             <tr>
                <td class="export-td">644</td>
                <td class="export-td">examination</td>
                <td class="export-td">英:/ɪg,zæmɪ'neɪʃ(ə)n/ 美:/ɪg'zæmə'neʃən/ </td>
                <td class="export-td">考查,考试,审讯</td>
            </tr>
            
             <tr>
                <td class="export-td">645</td>
                <td class="export-td">general</td>
                <td class="export-td">英:/'dʒen(ə)r(ə)l/ 美:/'dʒɛnrəl/ </td>
                <td class="export-td">1. adj. 一般的，普通的；综合的；大体的
2. n. 将军，上将；一般；常规</td>
            </tr>
            
             <tr>
                <td class="export-td">646</td>
                <td class="export-td">embassy</td>
                <td class="export-td">英:/'embəsɪ/ 美:/'ɛmbəsi/ </td>
                <td class="export-td">n. 大使馆；大使馆全体人员</td>
            </tr>
            
             <tr>
                <td class="export-td">647</td>
                <td class="export-td">examine</td>
                <td class="export-td">英:/ɪg'zæmɪn/ 美:/ɪg'zæmɪn/ </td>
                <td class="export-td">1. vt. 调查；考试；检查；[计算机] 检测
2. vi. 检查；调查</td>
            </tr>
            
             <tr>
                <td class="export-td">648</td>
                <td class="export-td">blackcurrant</td>
                <td class="export-td">/ˌblæk'kɝənt/ </td>
                <td class="export-td">黑加仑</td>
            </tr>
            
             <tr>
                <td class="export-td">649</td>
                <td class="export-td">diagram</td>
                <td class="export-td">英:/'daɪəgræm/ 美:/'daɪəɡræm/ </td>
                <td class="export-td">1. n. 图表；图解
2. vt. 用图解法表示</td>
            </tr>
            
             <tr>
                <td class="export-td">650</td>
                <td class="export-td">aged</td>
                <td class="export-td">英:/'eidʒid/ 美:/ˈedʒɪd/ </td>
                <td class="export-td">1. adj. 年老的；…岁的；老年人特有的
2. v. 变老；成熟；老化（age的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">651</td>
                <td class="export-td">brag</td>
                <td class="export-td">英:/bræg/ 美:/bræɡ/ </td>
                <td class="export-td">1. n. 吹牛，自夸
2. vi. 吹牛，自夸</td>
            </tr>
            
             <tr>
                <td class="export-td">652</td>
                <td class="export-td">boat</td>
                <td class="export-td">英:/bəʊt/ 美:/bot/ </td>
                <td class="export-td">1. n. 小船；轮船
2. vi. 划船</td>
            </tr>
            
             <tr>
                <td class="export-td">653</td>
                <td class="export-td">concentration</td>
                <td class="export-td">英:/kɒns(ə)n'treɪʃ(ə)n/ 美:/'kɑnsn'treʃən/ </td>
                <td class="export-td">集中, 专心, 浓度</td>
            </tr>
            
             <tr>
                <td class="export-td">654</td>
                <td class="export-td">grammatical</td>
                <td class="export-td">英:/grə'mætɪk(ə)l/ 美:/grə'mætɪkl/ </td>
                <td class="export-td">语法的, 合乎文法的</td>
            </tr>
            
             <tr>
                <td class="export-td">655</td>
                <td class="export-td">edition</td>
                <td class="export-td">英:/ɪ'dɪʃ(ə)n/ 美:/ɪ'dɪʃən/ </td>
                <td class="export-td">n. 版本</td>
            </tr>
            
             <tr>
                <td class="export-td">656</td>
                <td class="export-td">gleam</td>
                <td class="export-td">英:/gliːm/ 美:/ɡlim/ </td>
                <td class="export-td">1. n. 微光；闪光；瞬息的一现
2. vi. 闪烁；隐约地闪现</td>
            </tr>
            
             <tr>
                <td class="export-td">657</td>
                <td class="export-td">beak</td>
                <td class="export-td">英:/biːk/ 美:/bik/ </td>
                <td class="export-td">n. 鸟嘴；鹰钩鼻子；地方执法官；男教师</td>
            </tr>
            
             <tr>
                <td class="export-td">658</td>
                <td class="export-td">cucumber</td>
                <td class="export-td">英:/'kjuːkʌmbə/ 美:/'kjʊ,kʌmbɚ/ </td>
                <td class="export-td">n. 黄瓜；胡瓜</td>
            </tr>
            
             <tr>
                <td class="export-td">659</td>
                <td class="export-td">editor</td>
                <td class="export-td">英:/'edɪtə/ 美:/'ɛdɪtɚ/ </td>
                <td class="export-td">n. 编者，编辑；社论撰写人；编辑装置</td>
            </tr>
            
             <tr>
                <td class="export-td">660</td>
                <td class="export-td">episode</td>
                <td class="export-td">英:/'epɪsəʊd/ 美:/'ɛpɪsod/ </td>
                <td class="export-td">n. 插曲；插话；一段情节；有趣的事件</td>
            </tr>
            
             <tr>
                <td class="export-td">661</td>
                <td class="export-td">dial</td>
                <td class="export-td">英:/ˈdaiəl/ 美:/'daɪəl/ </td>
                <td class="export-td">1. n. 钟面；转盘；刻度盘
2. vi. 拨号</td>
            </tr>
            
             <tr>
                <td class="export-td">662</td>
                <td class="export-td">heading</td>
                <td class="export-td">英:/'hedɪŋ/ 美:/'hɛdɪŋ/ </td>
                <td class="export-td">1. n. 标题；信头；（足球）头球
2. v. 用头顶（head的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">663</td>
                <td class="export-td">eclipse</td>
                <td class="export-td">英:/ɪ'klɪps/ 美:/ɪ'klɪps/ </td>
                <td class="export-td">1. vt. 形成蚀；使黯然失色
2. n. 日蚀，月蚀；黯然失色</td>
            </tr>
            
             <tr>
                <td class="export-td">664</td>
                <td class="export-td">baby</td>
                <td class="export-td">英:/'beɪbɪ/ 美:/'bebi/ </td>
                <td class="export-td">1. n. 婴儿，婴孩；孩子气的人
2. vt. 纵容，娇纵；把……当婴儿般对待</td>
            </tr>
            
             <tr>
                <td class="export-td">665</td>
                <td class="export-td">aerobics</td>
                <td class="export-td">英:/eəˈrəʊbɪks/ 美:/ɛ'robɪks/ </td>
                <td class="export-td">n. 有氧运动法；增氧健身法</td>
            </tr>
            
             <tr>
                <td class="export-td">666</td>
                <td class="export-td">cuddle</td>
                <td class="export-td">英:/'kʌd(ə)l/ 美:/'kʌdl/ </td>
                <td class="export-td">1. vi. 拥抱；偎依；舒服地贴著身睡
2. vt. 拥抱；亲热地搂住；抚爱地拥抱</td>
            </tr>
            
             <tr>
                <td class="export-td">667</td>
                <td class="export-td">example</td>
                <td class="export-td">英:/ɪg'zɑːmp(ə)l/ 美:/ɪg'zæmpl/ </td>
                <td class="export-td">1. n. 例子；榜样
2. vt. 作为…的例子；为…做出榜样</td>
            </tr>
            
             <tr>
                <td class="export-td">668</td>
                <td class="export-td">dialect</td>
                <td class="export-td">英:/'daɪəlekt/ 美:/'daɪə'lɛkt/ </td>
                <td class="export-td">1. n. 方言，土话；同源语；行话；个人用语特征
2. adj. 方言的</td>
            </tr>
            
             <tr>
                <td class="export-td">669</td>
                <td class="export-td">bucket</td>
                <td class="export-td">英:/'bʌkɪt/ 美:/'bʌkɪt/ </td>
                <td class="export-td">1. n. 铲斗；桶，水桶；一桶的量
2. v. 倾盆而下；颠簸着行进</td>
            </tr>
            
             <tr>
                <td class="export-td">670</td>
                <td class="export-td">braid</td>
                <td class="export-td">英:/breɪd/ 美:/bred/ </td>
                <td class="export-td">1. vt. 编织
2. n. 辫子；穗带；发辫</td>
            </tr>
            
             <tr>
                <td class="export-td">671</td>
                <td class="export-td">coal</td>
                <td class="export-td">英:/kəʊl/ 美:/kol/ </td>
                <td class="export-td">1. vi. 加煤；上煤
2. vt. 给…加煤；把…烧成炭</td>
            </tr>
            
             <tr>
                <td class="export-td">672</td>
                <td class="export-td">affection</td>
                <td class="export-td">英:/ə'fekʃ(ə)n/ 美:/ə'fɛkʃən/ </td>
                <td class="export-td">感情</td>
            </tr>
            
             <tr>
                <td class="export-td">673</td>
                <td class="export-td">exasperate</td>
                <td class="export-td">英:/ɪg'zæsp(ə)reɪt/ 美:/ɪɡ'zæspəret/ </td>
                <td class="export-td">恶化</td>
            </tr>
            
             <tr>
                <td class="export-td">674</td>
                <td class="export-td">Braille</td>
                <td class="export-td">英:/breil/ 美:/brel/ </td>
                <td class="export-td">1. vt. 用盲字印
2. n. 布莱叶（法国盲人教育家）；盲人用点字法</td>
            </tr>
            
             <tr>
                <td class="export-td">675</td>
                <td class="export-td">affectionate</td>
                <td class="export-td">英:/ə'fekʃ(ə)nət/ 美:/ə'fɛkʃənət/ </td>
                <td class="export-td">情深的,充满情爱的</td>
            </tr>
            
             <tr>
                <td class="export-td">676</td>
                <td class="export-td">album</td>
                <td class="export-td">英:/'ælbəm/ 美:/'ælbəm/ </td>
                <td class="export-td">n. 相簿；唱片集；集邮簿；签名纪念册</td>
            </tr>
            
             <tr>
                <td class="export-td">677</td>
                <td class="export-td">chair</td>
                <td class="export-td">英:/tʃeə/ 美:/tʃɛr/ </td>
                <td class="export-td">1. n. 椅子；（会议的）主席位；大学教授的职位；讲座
2. vt. 使…入座；使就任要职；担任（会议的）主席</td>
            </tr>
            
             <tr>
                <td class="export-td">678</td>
                <td class="export-td">dragon</td>
                <td class="export-td">英:/'dræg(ə)n/ 美:/'dræɡən/ </td>
                <td class="export-td">n. 龙；凶暴的人，凶恶的人；严厉而有警觉性的女人</td>
            </tr>
            
             <tr>
                <td class="export-td">679</td>
                <td class="export-td">daddy</td>
                <td class="export-td">英:/'dædɪ/ 美:/'dædi/ </td>
                <td class="export-td">n. [口]爸爸</td>
            </tr>
            
             <tr>
                <td class="export-td">680</td>
                <td class="export-td">beam</td>
                <td class="export-td">英:/biːm/ 美:/bim/ </td>
                <td class="export-td">1. n. 横梁；船宽；电波；光线；秤杆
2. vt. 以梁支撑；用…照射；流露；发送</td>
            </tr>
            
             <tr>
                <td class="export-td">681</td>
                <td class="export-td">ecology</td>
                <td class="export-td">英:/ɪ'kɒlədʒɪ/ 美:/ɪ'kɑlədʒi/ </td>
                <td class="export-td">n. 生态学；社会生态学</td>
            </tr>
            
             <tr>
                <td class="export-td">682</td>
                <td class="export-td">adapt</td>
                <td class="export-td">英:/ə'dæpt/ 美:/ə'dæpt/ </td>
                <td class="export-td">1. vt. 改编；使适应
2. vi. 适应</td>
            </tr>
            
             <tr>
                <td class="export-td">683</td>
                <td class="export-td">gallery</td>
                <td class="export-td">英:/'gæl(ə)rɪ/ 美:/'gæləri/ </td>
                <td class="export-td">1. n. 走廊；画廊；地道；旁听席
2. vt. 在…修建走廊；在…挖地道</td>
            </tr>
            
             <tr>
                <td class="export-td">684</td>
                <td class="export-td">accelerator</td>
                <td class="export-td">英:/ək'seləreɪtə/ 美:/ək'sɛlə'retɚ/ </td>
                <td class="export-td">加速器</td>
            </tr>
            
             <tr>
                <td class="export-td">685</td>
                <td class="export-td">heal</td>
                <td class="export-td">英:/hiːl/ 美:/hil/ </td>
                <td class="export-td">1. vt. 治愈，痊愈；和解
2. vi. 痊愈</td>
            </tr>
            
             <tr>
                <td class="export-td">686</td>
                <td class="export-td">dock</td>
                <td class="export-td">英:/dɒk/ 美:/dɑk/ </td>
                <td class="export-td">1. n. 船坞；码头；被告席；尾巴的骨肉部分
2. vt. 剪短；使靠码头</td>
            </tr>
            
             <tr>
                <td class="export-td">687</td>
                <td class="export-td">animal</td>
                <td class="export-td">英:/'ænɪm(ə)l/ 美:/'ænɪml/ </td>
                <td class="export-td">such as a donkey, used for carrying heavy loads on its back 力畜, 役畜, 牲口（如驴）.<br /><br />n. 动物</td>
            </tr>
            
             <tr>
                <td class="export-td">688</td>
                <td class="export-td">clang</td>
                <td class="export-td">英:/klæŋ/ 美:/klæŋ/ </td>
                <td class="export-td">1. n. 叮当声；铿锵声
2. vi. 发铿锵声</td>
            </tr>
            
             <tr>
                <td class="export-td">689</td>
                <td class="export-td">concern</td>
                <td class="export-td">英:/kən'sɜːn/ 美:/kən'sɝn/ </td>
                <td class="export-td">1. vt. 涉及，关系到；使担心
2. n. 关心；关系；关心的事</td>
            </tr>
            
             <tr>
                <td class="export-td">690</td>
                <td class="export-td">adaptable</td>
                <td class="export-td">英:/ə'dæptəb(ə)l/ 美:/ə'dæptəbl/ </td>
                <td class="export-td">适应能力强</td>
            </tr>
            
             <tr>
                <td class="export-td">691</td>
                <td class="export-td">buckle</td>
                <td class="export-td">英:/ˈbʌkl/ 美:/ˈbʌkəl/ </td>
                <td class="export-td">1. vi. 扣住；变弯曲
2. vt. 扣住；使弯曲</td>
            </tr>
            
             <tr>
                <td class="export-td">692</td>
                <td class="export-td">accent</td>
                <td class="export-td">英:/'æks(ə)nt/ 美:/'æksɛnt/ </td>
                <td class="export-td">1. n. 口音；重音；重音符号；强调；特点
2. vt. 重读；强调；带…口音讲话</td>
            </tr>
            
             <tr>
                <td class="export-td">693</td>
                <td class="export-td">fun</td>
                <td class="export-td">英:/fʌn/ 美:/fʌn/ </td>
                <td class="export-td">1. n. 乐趣；玩笑；有趣的人或事
2. adj. 供娱乐用的</td>
            </tr>
            
             <tr>
                <td class="export-td">694</td>
                <td class="export-td">concerned</td>
                <td class="export-td">英:/kən'sɜːnd/ 美:/kən'sɝnd/ </td>
                <td class="export-td">担忧的,关心的</td>
            </tr>
            
             <tr>
                <td class="export-td">695</td>
                <td class="export-td">black hole</td>
                <td class="export-td"></td>
                <td class="export-td">黑洞</td>
            </tr>
            
             <tr>
                <td class="export-td">696</td>
                <td class="export-td">chairperson</td>
                <td class="export-td">英:/'tʃeəpɜːs(ə)n/ 美:/'tʃɛrpɝsn/ </td>
                <td class="export-td">主席</td>
            </tr>
            
             <tr>
                <td class="export-td">697</td>
                <td class="export-td">brainy</td>
                <td class="export-td">英:/'breɪnɪ/ 美:/'breni/ </td>
                <td class="export-td">adj. 聪明的；脑筋好的；有头脑的</td>
            </tr>
            
             <tr>
                <td class="export-td">698</td>
                <td class="export-td">glee</td>
                <td class="export-td">英:/gliː/ 美:/ɡli/ </td>
                <td class="export-td">n. 快乐；欢欣；重唱歌曲</td>
            </tr>
            
             <tr>
                <td class="export-td">699</td>
                <td class="export-td">bean</td>
                <td class="export-td">英:/biːn/ 美:/bin/ </td>
                <td class="export-td">1. n. 豆；[动]嘴峰；[美口]毫无价值的东西
2. vt. [美口]击…的头部</td>
            </tr>
            
             <tr>
                <td class="export-td">700</td>
                <td class="export-td">aeroplane</td>
                <td class="export-td">英:/'eərəpleɪn/ 美:/'ɛrə'plen/ </td>
                <td class="export-td">飞机</td>
            </tr>
            
             <tr>
                <td class="export-td">701</td>
                <td class="export-td">cuff</td>
                <td class="export-td">英:/kʌf/ 美:/kʌf/ </td>
                <td class="export-td">1. n. 手铐；一巴掌；袖口，裤子翻边
2. vt. 给…上袖口；用巴掌打；给…带上手铐</td>
            </tr>
            
             <tr>
                <td class="export-td">702</td>
                <td class="export-td">goal</td>
                <td class="export-td">英:/gəʊl/ 美:/ɡol/ </td>
                <td class="export-td">1. n. 目标；终点；球门，得分数
2. vi. 攻门，射门得分</td>
            </tr>
            
             <tr>
                <td class="export-td">703</td>
                <td class="export-td">educate</td>
                <td class="export-td">英:/'edjʊkeɪt/ 美:/'ɛdʒuket/ </td>
                <td class="export-td">1. vt. 教育；培养；训练
2. vi. 教育；训练</td>
            </tr>
            
             <tr>
                <td class="export-td">704</td>
                <td class="export-td">function</td>
                <td class="export-td">英:/'fʌŋ(k)ʃ(ə)n/ 美:/'fʌŋkʃən/ </td>
                <td class="export-td">1. n. 功能；函数；职责；盛大的集会
2. vi. 行使职责；运行；活动</td>
            </tr>
            
             <tr>
                <td class="export-td">705</td>
                <td class="export-td">health</td>
                <td class="export-td">英:/helθ/ 美:/hɛlθ/ </td>
                <td class="export-td">n. 健康；兴旺；卫生；保健</td>
            </tr>
            
             <tr>
                <td class="export-td">706</td>
                <td class="export-td">aerosol</td>
                <td class="export-td">英:/'eərəsɒl/ 美:/'ɛrəsɔl/ </td>
                <td class="export-td">1. n. 喷雾器；气雾剂；浮质；气溶胶
2. adj. 喷雾器的；喷雾的</td>
            </tr>
            
             <tr>
                <td class="export-td">707</td>
                <td class="export-td">educated</td>
                <td class="export-td">英:/'edjʊkeɪtɪd/ 美:/'ɛdʒə'ketɪd/ </td>
                <td class="export-td">1. adj. 有教养的；受过教育的
2. v. 教导；训练；培育（educate的过去分词形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">708</td>
                <td class="export-td">craft</td>
                <td class="export-td">英:/krɑːft/ 美:/kræft/ </td>
                <td class="export-td">1. n. 手艺；工艺；太空船
2. vt. 精巧地制作</td>
            </tr>
            
             <tr>
                <td class="export-td">709</td>
                <td class="export-td">agency</td>
                <td class="export-td">英:/'eɪdʒ(ə)nsɪ/ 美:/'edʒənsi/ </td>
                <td class="export-td">n. 代理，中介；代理处，经销处</td>
            </tr>
            
             <tr>
                <td class="export-td">710</td>
                <td class="export-td">fraud</td>
                <td class="export-td">英:/frɔːd/ 美:/frɔd/ </td>
                <td class="export-td">n. 欺骗；骗子；诡计</td>
            </tr>
            
             <tr>
                <td class="export-td">711</td>
                <td class="export-td">alcohol</td>
                <td class="export-td">英:/'ælkəhɒl/ 美:/'ælkəhɔl/ </td>
                <td class="export-td">n. 酒精，乙醇</td>
            </tr>
            
             <tr>
                <td class="export-td">712</td>
                <td class="export-td">drain</td>
                <td class="export-td">英:/dreɪn/ 美:/dren/ </td>
                <td class="export-td">1. vi. 排水；流干
2. vt. 喝光，耗尽；使流出；排掉水</td>
            </tr>
            
             <tr>
                <td class="export-td">713</td>
                <td class="export-td">agenda</td>
                <td class="export-td">英:/ə'dʒendə/ 美:/ə'dʒɛndə/ </td>
                <td class="export-td">n. 议程；日常工作事项</td>
            </tr>
            
             <tr>
                <td class="export-td">714</td>
                <td class="export-td">daffodil</td>
                <td class="export-td">英:/'dæfədɪl/ 美:/'dæfədɪl/ </td>
                <td class="export-td">1. n. 水仙花
2. adj. 水仙花色的</td>
            </tr>
            
             <tr>
                <td class="export-td">715</td>
                <td class="export-td">grand</td>
                <td class="export-td">英:/grænd/ 美:/ɡrænd/ </td>
                <td class="export-td">1. adj. 宏伟的；豪华的；极重要的
2. n. 大钢琴；一千美元</td>
            </tr>
            
             <tr>
                <td class="export-td">716</td>
                <td class="export-td">early</td>
                <td class="export-td">英:/ˈə:li/ 美:/ˈɚli/ </td>
                <td class="export-td">1. adj. 早期的；早熟的
2. adv. 提早；在初期</td>
            </tr>
            
             <tr>
                <td class="export-td">717</td>
                <td class="export-td">concerning</td>
                <td class="export-td">英:/kən'sɜːnɪŋ/ 美:/kən'sɝnɪŋ/ </td>
                <td class="export-td">关于</td>
            </tr>
            
             <tr>
                <td class="export-td">718</td>
                <td class="export-td">alcoholic</td>
                <td class="export-td">英:/ælkə'hɒlɪk/ 美:/ˌælkə'hɔlɪk/ </td>
                <td class="export-td">酒精</td>
            </tr>
            
             <tr>
                <td class="export-td">719</td>
                <td class="export-td">error</td>
                <td class="export-td">英:/'erə/ 美:/'ɛrɚ/ </td>
                <td class="export-td">n. 错误；误差；过失</td>
            </tr>
            
             <tr>
                <td class="export-td">720</td>
                <td class="export-td">fence</td>
                <td class="export-td">英:/fens/ 美:/fɛns/ </td>
                <td class="export-td">rail, etc to restrain crowds, divide vehicles travelling in opposite directions on a motorway, etc （限制人群通行的）隔离栅; （高速公路等的双程行车道之间的）防撞护栏. =>illus at App 1 见附录1之插图, page xiii.<br /><br />1. n. 栅栏；围墙；剑术
2. vt. 防护；用篱笆围住；练习剑术</td>
            </tr>
            
             <tr>
                <td class="export-td">721</td>
                <td class="export-td">accept</td>
                <td class="export-td">英:/ək'sept/ 美:/ək'sɛpt/ </td>
                <td class="export-td">1. vt. 接受；承认；承担；承兑；容纳
2. vi. 同意；承认；承兑</td>
            </tr>
            
             <tr>
                <td class="export-td">722</td>
                <td class="export-td">agent</td>
                <td class="export-td">英:/'eɪdʒ(ə)nt/ 美:/'edʒənt/ </td>
                <td class="export-td">1. n. 代理人，代理商；药剂；特工
2. vt. 由…作中介；由…代理</td>
            </tr>
            
             <tr>
                <td class="export-td">723</td>
                <td class="export-td">daft</td>
                <td class="export-td">英:/dɑːft/ 美:/dæft/ </td>
                <td class="export-td">adj. 癫狂的；愚笨的；狂闹的</td>
            </tr>
            
             <tr>
                <td class="export-td">724</td>
                <td class="export-td">economic</td>
                <td class="export-td">英:/ˌiːkə'nɒmɪk/ 美:/ˌikə'nɑmɪk/ </td>
                <td class="export-td">adj. 经济的，经济上的；经济学的</td>
            </tr>
            
             <tr>
                <td class="export-td">725</td>
                <td class="export-td">clap</td>
                <td class="export-td">英:/klæp/ 美:/klæp/ </td>
                <td class="export-td">1. vi. 鼓掌，拍手；啪地关上
2. vt. 拍手，鼓掌；轻轻拍打某人</td>
            </tr>
            
             <tr>
                <td class="export-td">726</td>
                <td class="export-td">education</td>
                <td class="export-td">英:/edjʊ'keɪʃ(ə)n/ 美:/ˌɛdʒu'keʃən/ </td>
                <td class="export-td">教育,培养</td>
            </tr>
            
             <tr>
                <td class="export-td">727</td>
                <td class="export-td">crafty</td>
                <td class="export-td">英:/'krɑːftɪ/ 美:/'kræfti/ </td>
                <td class="export-td">adj. 灵巧的；狡猾的</td>
            </tr>
            
             <tr>
                <td class="export-td">728</td>
                <td class="export-td">acceptable</td>
                <td class="export-td">英:/ək'septəb(ə)l/ 美:/ək'sɛptəbl/ </td>
                <td class="export-td">接受</td>
            </tr>
            
             <tr>
                <td class="export-td">729</td>
                <td class="export-td">economical</td>
                <td class="export-td">英:/iːkə'nɒmɪk(ə)l/ 美:/ˌikə'nɑmɪkl/ </td>
                <td class="export-td">经济</td>
            </tr>
            
             <tr>
                <td class="export-td">730</td>
                <td class="export-td">bob</td>
                <td class="export-td">英:/bɒb/ 美:/bɑb/ </td>
                <td class="export-td">1. n. 短发；浮子；摆动；轻敲；悬挂的饰品
2. vt. 剪短；敲击；使上下快速摆动</td>
            </tr>
            
             <tr>
                <td class="export-td">731</td>
                <td class="export-td">concert</td>
                <td class="export-td">英:/'kɒnsət/ 美:/'kɑnsɚt/ </td>
                <td class="export-td">1. n. 音乐会；和谐；一致
2. vt. 使协调；协同安排</td>
            </tr>
            
             <tr>
                <td class="export-td">732</td>
                <td class="export-td">exceed</td>
                <td class="export-td">英:/ɪk'siːd/ 美:/ɪk'sid/ </td>
                <td class="export-td">1. vt. 胜过；超过
2. vi. 超过其他</td>
            </tr>
            
             <tr>
                <td class="export-td">733</td>
                <td class="export-td">add</td>
                <td class="export-td">英:/æd/ 美:/æd/ </td>
                <td class="export-td">1. vi. 加；增加；加起来；做加法
2. vt. 增加，添加；补充说；计算…总和</td>
            </tr>
            
             <tr>
                <td class="export-td">734</td>
                <td class="export-td">chalk</td>
                <td class="export-td">英:/tʃɔːk/ 美:/tʃɔk/ </td>
                <td class="export-td">1. vt. 用粉笔写；用白垩粉擦；记录；规划
2. n. 粉笔；白垩；用粉笔划的记号</td>
            </tr>
            
             <tr>
                <td class="export-td">735</td>
                <td class="export-td">due</td>
                <td class="export-td">英:/djuː/ 美:/du/ </td>
                <td class="export-td">1. adj. 到期的；应得的；应付的；预期的
2. n. 应付款；应得之物</td>
            </tr>
            
             <tr>
                <td class="export-td">736</td>
                <td class="export-td">dagger</td>
                <td class="export-td">英:/'dægə/ 美:/'dæɡɚ/ </td>
                <td class="export-td">1. n. 匕首，短剑
2. vt. 用剑刺</td>
            </tr>
            
             <tr>
                <td class="export-td">737</td>
                <td class="export-td">gallon</td>
                <td class="export-td">英:/'gælən/ 美:/ˈɡælən/ </td>
                <td class="export-td">n. 加仑（容量单位）</td>
            </tr>
            
             <tr>
                <td class="export-td">738</td>
                <td class="export-td">glide</td>
                <td class="export-td">英:/glaɪd/ 美:/ɡlaɪd/ </td>
                <td class="export-td">1. n. 滑翔；滑行；滑移；滑音
2. vt. 滑翔；滑行；悄悄地走；消逝</td>
            </tr>
            
             <tr>
                <td class="export-td">739</td>
                <td class="export-td">bear</td>
                <td class="export-td">英:/beə/ 美:/bɛr/ </td>
                <td class="export-td">1. vi. 结果实；承受
2. vt. 忍受；具有；支撑</td>
            </tr>
            
             <tr>
                <td class="export-td">740</td>
                <td class="export-td">economics</td>
                <td class="export-td">英:/iːkə'nɒmɪks/ 美:/'ikə'nɑmɪks/ </td>
                <td class="export-td">经济学</td>
            </tr>
            
             <tr>
                <td class="export-td">741</td>
                <td class="export-td">earn</td>
                <td class="export-td">英:/ɜːn/ 美:/ɝn/ </td>
                <td class="export-td">vt. 获得，挣得；赚，赚得；博得；使得到</td>
            </tr>
            
             <tr>
                <td class="export-td">742</td>
                <td class="export-td">gallop</td>
                <td class="export-td">英:/'gæləp/ 美:/'ɡæləp/ </td>
                <td class="export-td">1. n. 疾驰；飞奔
2. vi. 急速进行；飞驰；急急忙忙地说</td>
            </tr>
            
             <tr>
                <td class="export-td">743</td>
                <td class="export-td">equal</td>
                <td class="export-td">英:/ˈi:kwəl/ 美:/'ikwəl/ </td>
                <td class="export-td">1. adj. 相等的；胜任的；平等的
2. vt. 等于；比得上</td>
            </tr>
            
             <tr>
                <td class="export-td">744</td>
                <td class="export-td">doctor</td>
                <td class="export-td">英:/'dɒktə/ 美:/'dɑktɚ/ </td>
                <td class="export-td">1. n. 医生；博士
2. vt. 为…治病；授以博士学位；修理；窜改，伪造</td>
            </tr>
            
             <tr>
                <td class="export-td">745</td>
                <td class="export-td">economist</td>
                <td class="export-td">英:/ɪ'kɒnəmɪst/ 美:/ɪ'kɑnəmɪst/ </td>
                <td class="export-td">经济学家 节俭的人</td>
            </tr>
            
             <tr>
                <td class="export-td">746</td>
                <td class="export-td">enclose</td>
                <td class="export-td">英:/ɪn'kləʊz/ 美:/ɛnˈkloz/ </td>
                <td class="export-td">vt. 围绕；装入；放入封套</td>
            </tr>
            
             <tr>
                <td class="export-td">747</td>
                <td class="export-td">craftsman</td>
                <td class="export-td">英:/'krɑːf(t)smən/ 美:/'kræftsmən/ </td>
                <td class="export-td">匠</td>
            </tr>
            
             <tr>
                <td class="export-td">748</td>
                <td class="export-td">acceptance</td>
                <td class="export-td">英:/ək'sept(ə)ns/ 美:/ək'sɛptəns/ </td>
                <td class="export-td">接受 ，同意，认可</td>
            </tr>
            
             <tr>
                <td class="export-td">749</td>
                <td class="export-td">equality</td>
                <td class="export-td">英:/ɪ'kwɒlɪtɪ/ 美:/ɪ'kwɑləti/ </td>
                <td class="export-td">n. 平等；相等；[数]等式</td>
            </tr>
            
             <tr>
                <td class="export-td">750</td>
                <td class="export-td">fray</td>
                <td class="export-td">英:/freɪ/ 美:/fre/ </td>
                <td class="export-td">1. n. 争论；打架；磨损处
2. vt. 使磨损；变得令人紧张、急躁</td>
            </tr>
            
             <tr>
                <td class="export-td">751</td>
                <td class="export-td">glider</td>
                <td class="export-td">英:/'ɡlaidə/ 美:/ˈɡlaɪdɚ/ </td>
                <td class="export-td">n. 滑翔机；滑翔员；滑翔导弹</td>
            </tr>
            
             <tr>
                <td class="export-td">752</td>
                <td class="export-td">generally</td>
                <td class="export-td">英:/'dʒen(ə)rəlɪ/ 美:/'dʒɛnrəli/ </td>
                <td class="export-td">一般地</td>
            </tr>
            
             <tr>
                <td class="export-td">753</td>
                <td class="export-td">emphasize</td>
                <td class="export-td">英:/ˈemfəsaiz/ 美:/'ɛmfəsaɪz/ </td>
                <td class="export-td">emphasise<br /><br />强调,着重</td>
            </tr>
            
             <tr>
                <td class="export-td">754</td>
                <td class="export-td">addicted</td>
                <td class="export-td">/ə'dɪktɪd/ </td>
                <td class="export-td">1. adj. 沉溺于某种（尤其是不良的）嗜好的；入了迷的，上了瘾的
2. v. 使…上瘾（addict的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">755</td>
                <td class="export-td">appetizer</td>
                <td class="export-td">英:/'æpɪtaɪzə/ 美:/'æpə'taɪzɚ/ </td>
                <td class="export-td">appetiser<br /><br />开胃菜</td>
            </tr>
            
             <tr>
                <td class="export-td">756</td>
                <td class="export-td">economy</td>
                <td class="export-td">英:/ɪ'kɒnəmɪ/ 美:/ɪ'kɑnəmi/ </td>
                <td class="export-td">n. 节约；经济；理财</td>
            </tr>
            
             <tr>
                <td class="export-td">757</td>
                <td class="export-td">aback</td>
                <td class="export-td">英:/ə'bæk/ 美:/ə'bæk/ </td>
                <td class="export-td">adv. 向后；处于顶风位置；向后地</td>
            </tr>
            
             <tr>
                <td class="export-td">758</td>
                <td class="export-td">bud</td>
                <td class="export-td">英:/bʌd/ 美:/bʌd/ </td>
                <td class="export-td">1. n. 芽，萌芽；蓓蕾
2. vi. 发芽，萌芽</td>
            </tr>
            
             <tr>
                <td class="export-td">759</td>
                <td class="export-td">erupt</td>
                <td class="export-td">英:/ɪ'rʌpt/ 美:/ɪ'rʌpt/ </td>
                <td class="export-td">1. vi. 爆发；喷出；发疹；长牙
2. vt. 爆发；喷出</td>
            </tr>
            
             <tr>
                <td class="export-td">760</td>
                <td class="export-td">fund</td>
                <td class="export-td">英:/fʌnd/ 美:/fʌnd/ </td>
                <td class="export-td">1. n. 资金；基金；存款
2. vt. 投资；资助</td>
            </tr>
            
             <tr>
                <td class="export-td">761</td>
                <td class="export-td">equally</td>
                <td class="export-td">英:/'iːkw(ə)lɪ/ 美:/'ikwəli/ </td>
                <td class="export-td">adv. 相等地，平等地；公平地；同样地</td>
            </tr>
            
             <tr>
                <td class="export-td">762</td>
                <td class="export-td">freak</td>
                <td class="export-td">英:/friːk/ 美:/frik/ </td>
                <td class="export-td">1. n. 反复无常；怪人，怪事；畸形人
2. adj. 奇异的，反常的</td>
            </tr>
            
             <tr>
                <td class="export-td">763</td>
                <td class="export-td">diamond</td>
                <td class="export-td">英:/'daɪəmənd/ 美:/'daɪəmənd/ </td>
                <td class="export-td">1. n. 钻石，金刚石；菱形；方块牌
2. adj. 金刚钻的；菱形的</td>
            </tr>
            
             <tr>
                <td class="export-td">764</td>
                <td class="export-td">Buddhism</td>
                <td class="export-td">英:/'bʊdɪz(ə)m/ 美:/'bʊdɪzəm/ </td>
                <td class="export-td">n. 佛教</td>
            </tr>
            
             <tr>
                <td class="export-td">765</td>
                <td class="export-td">duet</td>
                <td class="export-td">英:/djuː'et/ 美:/dʊ'ɛt/ </td>
                <td class="export-td">n. 二重奏</td>
            </tr>
            
             <tr>
                <td class="export-td">766</td>
                <td class="export-td">challenge</td>
                <td class="export-td">英:/'tʃælɪn(d)ʒ/ 美:/'tʃælɪndʒ/ </td>
                <td class="export-td">挑战</td>
            </tr>
            
             <tr>
                <td class="export-td">767</td>
                <td class="export-td">drama</td>
                <td class="export-td">英:/'drɑːmə/ 美:/'drɑmə/ </td>
                <td class="export-td">n. 戏剧，戏剧艺术；剧本；戏剧性事件</td>
            </tr>
            
             <tr>
                <td class="export-td">768</td>
                <td class="export-td">access</td>
                <td class="export-td">英:/'ækses/ 美:/'æksɛs/ </td>
                <td class="export-td">1. vt. 存取；接近；使用
2. n. 通路；进入；使用权</td>
            </tr>
            
             <tr>
                <td class="export-td">769</td>
                <td class="export-td">fundamental</td>
                <td class="export-td">英:/fʌndə'ment(ə)l/ 美:/ˌfʌndə'mɛntl/ </td>
                <td class="export-td">根本</td>
            </tr>
            
             <tr>
                <td class="export-td">770</td>
                <td class="export-td">healthy</td>
                <td class="export-td">英:/'helθɪ/ 美:/'hɛlθi/ </td>
                <td class="export-td">adj. 健康的，健全的；有益于健康的</td>
            </tr>
            
             <tr>
                <td class="export-td">771</td>
                <td class="export-td">cram</td>
                <td class="export-td">英:/kræm/ 美:/kræm/ </td>
                <td class="export-td">1. adj. 填鸭式学的
2. vi. 狼吞虎咽地吃东西；死记硬背功课</td>
            </tr>
            
             <tr>
                <td class="export-td">772</td>
                <td class="export-td">dramatic</td>
                <td class="export-td">英:/drə'mætɪk/ 美:/drə'mætɪk/ </td>
                <td class="export-td">adj. 戏剧的；引人注目的；激动人心的</td>
            </tr>
            
             <tr>
                <td class="export-td">773</td>
                <td class="export-td">glimmer</td>
                <td class="export-td">英:/'glɪmə/ 美:/'ɡlɪmɚ/ </td>
                <td class="export-td">1. n. 微光；闪光；少许
2. vi. 闪烁；发微光</td>
            </tr>
            
             <tr>
                <td class="export-td">774</td>
                <td class="export-td">cope</td>
                <td class="export-td">英:/kəʊp/ 美:/kop/ </td>
                <td class="export-td">1. vi. 处理；竞争；对付
2. n. 长袍</td>
            </tr>
            
             <tr>
                <td class="export-td">775</td>
                <td class="export-td">excellent</td>
                <td class="export-td">英:/'eks(ə)l(ə)nt/ 美:/'ɛksələnt/ </td>
                <td class="export-td">极好的,杰出的</td>
            </tr>
            
             <tr>
                <td class="export-td">776</td>
                <td class="export-td">addition</td>
                <td class="export-td">英:/ə'dɪʃ(ə)n/ 美:/ə'dɪʃən/ </td>
                <td class="export-td">n. 添加；增加物；加法</td>
            </tr>
            
             <tr>
                <td class="export-td">777</td>
                <td class="export-td">buddhist</td>
                <td class="export-td">/'budist/ </td>
                <td class="export-td">1. n. 佛教徒
2. adj. 佛教的</td>
            </tr>
            
             <tr>
                <td class="export-td">778</td>
                <td class="export-td">Buddhist</td>
                <td class="export-td">/'budist/ </td>
                <td class="export-td">1. n. 佛教徒
2. adj. 佛教的</td>
            </tr>
            
             <tr>
                <td class="export-td">779</td>
                <td class="export-td">daily</td>
                <td class="export-td">英:/'deɪlɪ/ 美:/'deli/ </td>
                <td class="export-td">1. adj. 每日的；日常的
2. n. 日报；[美口]朝来夜去的女佣</td>
            </tr>
            
             <tr>
                <td class="export-td">780</td>
                <td class="export-td">afford</td>
                <td class="export-td">英:/ə'fɔːd/ 美:/ə'fɔrd/ </td>
                <td class="export-td">vt. 给予，提供；买得起</td>
            </tr>
            
             <tr>
                <td class="export-td">781</td>
                <td class="export-td">clarinet</td>
                <td class="export-td">英:/klærɪ'net/ 美:/ˌklærə'nɛt/ </td>
                <td class="export-td">n. [乐]单簧管；竖笛，黑管</td>
            </tr>
            
             <tr>
                <td class="export-td">782</td>
                <td class="export-td">goat</td>
                <td class="export-td">英:/gəʊt/ 美:/ɡot/ </td>
                <td class="export-td">n. 山羊；替罪羊（美俚）；色鬼（美俚）</td>
            </tr>
            
             <tr>
                <td class="export-td">783</td>
                <td class="export-td">diaper</td>
                <td class="export-td">英:/'daɪəpə/ 美:/'daɪpɚ/ </td>
                <td class="export-td">1. n. 尿布
2. vt. 给孩子换尿布</td>
            </tr>
            
             <tr>
                <td class="export-td">784</td>
                <td class="export-td">equation</td>
                <td class="export-td">英:/ɪ'kweɪʒ(ə)n/ 美:/ɪ'kweʒn/ </td>
                <td class="export-td">n. 方程式，等式；相等；反应式</td>
            </tr>
            
             <tr>
                <td class="export-td">785</td>
                <td class="export-td">except</td>
                <td class="export-td">英:/ɪk'sept/ 美:/ɪk'sɛpt/ </td>
                <td class="export-td">1. vt. 不计；把…除外
2. vi. 反对</td>
            </tr>
            
             <tr>
                <td class="export-td">786</td>
                <td class="export-td">alert</td>
                <td class="export-td">英:/ə'lɜːt/ 美:/ə'lɝt/ </td>
                <td class="export-td">1. vt. 使警觉，使意识到；警告
2. adj. 警惕的，警觉的；留心的</td>
            </tr>
            
             <tr>
                <td class="export-td">787</td>
                <td class="export-td">budge</td>
                <td class="export-td">英:/bʌdʒ/ 美:/bʌdʒ/ </td>
                <td class="export-td">1. vi. 挪动；微微移动；改变态度或意见；服从
2. vt. 移动；使改变态度或意见；使让步</td>
            </tr>
            
             <tr>
                <td class="export-td">788</td>
                <td class="export-td">dainty</td>
                <td class="export-td">英:/'deɪntɪ/ 美:/'denti/ </td>
                <td class="export-td">1. adj. 秀丽的；美味的；讲究的；挑剔的
2. n. 美味</td>
            </tr>
            
             <tr>
                <td class="export-td">789</td>
                <td class="export-td">document</td>
                <td class="export-td">英:/'dɒkjʊm(ə)nt/ 美:/ˈdɑkjəmənt/ </td>
                <td class="export-td">1. n. 文件，公文；文档；证件
2. vt. 用文件证明</td>
            </tr>
            
             <tr>
                <td class="export-td">790</td>
                <td class="export-td">abandon</td>
                <td class="export-td">英:/ə'bænd(ə)n/ 美:/ə'bændən/ </td>
                <td class="export-td">1. n. 狂热，放任
2. vt. 遗弃，放弃</td>
            </tr>
            
             <tr>
                <td class="export-td">791</td>
                <td class="export-td">exception</td>
                <td class="export-td">英:/ɪk'sepʃ(ə)n/ 美:/ɪk'sɛpʃən/ </td>
                <td class="export-td">除外,例外</td>
            </tr>
            
             <tr>
                <td class="export-td">792</td>
                <td class="export-td">cramp</td>
                <td class="export-td">英:/kræmp/ 美:/kræmp/ </td>
                <td class="export-td">1. n. 铁夹钳；痉挛，绞痛
2. vt. 使…抽筋；以铁箍扣紧；束缚，限制</td>
            </tr>
            
             <tr>
                <td class="export-td">793</td>
                <td class="export-td">heap</td>
                <td class="export-td">英:/hiːp/ 美:/hip/ </td>
                <td class="export-td">1. n. 累积；堆；许多
2. vt. 堆积；堆</td>
            </tr>
            
             <tr>
                <td class="export-td">794</td>
                <td class="export-td">earth</td>
                <td class="export-td">英:/ɜːθ/ 美:/ɝθ/ </td>
                <td class="export-td">n. 地球；泥土；地线；尘世；陆地</td>
            </tr>
            
             <tr>
                <td class="export-td">795</td>
                <td class="export-td">budget</td>
                <td class="export-td">英:/'bʌdʒɪt/ 美:/'bʌdʒɪt/ </td>
                <td class="export-td">1. n. 预算，预算费
2. vt. 安排，预定；把…编入预算</td>
            </tr>
            
             <tr>
                <td class="export-td">796</td>
                <td class="export-td">brake</td>
                <td class="export-td">英:/breɪk/ 美:/brek/ </td>
                <td class="export-td">1. vi. 刹车
2. n. 闸，刹车；阻碍</td>
            </tr>
            
             <tr>
                <td class="export-td">797</td>
                <td class="export-td">funeral</td>
                <td class="export-td">英:/'fjuːn(ə)r(ə)l/ 美:/ˈfjunərəl/ </td>
                <td class="export-td">1. n. 葬礼；[口]麻烦事
2. adj. 丧葬的，出殡的</td>
            </tr>
            
             <tr>
                <td class="export-td">798</td>
                <td class="export-td">hear</td>
                <td class="export-td">英:/hɪə/ 美:/hɪr/ </td>
                <td class="export-td">1. vt. 审理；听说；听到，听
2. vi. 听见；听</td>
            </tr>
            
             <tr>
                <td class="export-td">799</td>
                <td class="export-td">glimpse</td>
                <td class="export-td">英:/glɪm(p)s/ 美:/ɡlɪmps/ </td>
                <td class="export-td">1. n. 一瞥，一看
2. vi. 瞥见</td>
            </tr>
            
             <tr>
                <td class="export-td">800</td>
                <td class="export-td">beard</td>
                <td class="export-td">英:/bɪəd/ 美:/bɪrd/ </td>
                <td class="export-td">1. vt. 公然反对；抓…的胡须
2. n. 胡须；颌毛</td>
            </tr>
            
             <tr>
                <td class="export-td">801</td>
                <td class="export-td">embroider</td>
                <td class="export-td">英:/ɪm'brɒɪdə/ 美:/ɪm'brɔɪdɚ/ </td>
                <td class="export-td">刺绣, 镶边, 装饰</td>
            </tr>
            
             <tr>
                <td class="export-td">802</td>
                <td class="export-td">documentary</td>
                <td class="export-td">英:/dɒkjʊ'ment(ə)rɪ/ 美:/'dɑkjə'mɛntri/ </td>
                <td class="export-td">文献的; 纪录片</td>
            </tr>
            
             <tr>
                <td class="export-td">803</td>
                <td class="export-td">encourage</td>
                <td class="export-td">英:/ɪn'kʌrɪdʒ/ 美:/ɪn'kɝɪdʒ/ </td>
                <td class="export-td">鼓励,激励,支持</td>
            </tr>
            
             <tr>
                <td class="export-td">804</td>
                <td class="export-td">clash</td>
                <td class="export-td">英:/klæʃ/ 美:/klæʃ/ </td>
                <td class="export-td">1. n. 冲突，不协调；碰撞声，铿锵声
2. vi. 冲突，抵触；砰地相碰撞，发出铿锵声</td>
            </tr>
            
             <tr>
                <td class="export-td">805</td>
                <td class="export-td">embroidery</td>
                <td class="export-td">英:/ɪm'brɒɪd(ə)rɪ/ 美:/ɪm'brɔɪdəri/ </td>
                <td class="export-td">刺绣</td>
            </tr>
            
             <tr>
                <td class="export-td">806</td>
                <td class="export-td">diary</td>
                <td class="export-td">英:/'daɪərɪ/ 美:/'daɪəri/ </td>
                <td class="export-td">n. 日记簿；日志，日记</td>
            </tr>
            
             <tr>
                <td class="export-td">807</td>
                <td class="export-td">gamble</td>
                <td class="export-td">英:/'gæmb(ə)l/ 美:/'ɡæmbl/ </td>
                <td class="export-td">1. vi. 赌博；投机；打赌；孤注一掷
2. vt. 赌博；孤注一掷；冒险假设</td>
            </tr>
            
             <tr>
                <td class="export-td">808</td>
                <td class="export-td">coarse</td>
                <td class="export-td">英:/kɔːs/ 美:/kɔrs/ </td>
                <td class="export-td">adj. 粗糙的；下等的；粗俗的</td>
            </tr>
            
             <tr>
                <td class="export-td">809</td>
                <td class="export-td">hearing</td>
                <td class="export-td">英:/'hɪərɪŋ/ 美:/'hɪrɪŋ/ </td>
                <td class="export-td">1. n. 听力；审讯，听讯
2. v. 听见（hear的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">810</td>
                <td class="export-td">clasp</td>
                <td class="export-td">英:/klɑːsp/ 美:/klæsp/ </td>
                <td class="export-td">1. n. 扣子，钩子；握手
2. vt. 紧抱；扣紧；紧紧缠绕</td>
            </tr>
            
             <tr>
                <td class="export-td">811</td>
                <td class="export-td">gambler</td>
                <td class="export-td">英:/ˈgæmbəl/ 美:/'gæmblɚ/ </td>
                <td class="export-td">n. 赌徒；投机商人</td>
            </tr>
            
             <tr>
                <td class="export-td">812</td>
                <td class="export-td">dug</td>
                <td class="export-td">英:/dʌɡ/ 美:/dʌɡ/ </td>
                <td class="export-td">1. v. 挖，翻土（dig的过去式和过去分词）
2. n. 雌性哺乳动物的乳房</td>
            </tr>
            
             <tr>
                <td class="export-td">813</td>
                <td class="export-td">crane</td>
                <td class="export-td">英:/kreɪn/ 美:/kren/ </td>
                <td class="export-td">1. n. 鹤；吊车，起重机
2. vi. 伸着脖子看；迟疑，踌躇</td>
            </tr>
            
             <tr>
                <td class="export-td">814</td>
                <td class="export-td">dramatist</td>
                <td class="export-td">英:/'dræmətɪst/ 美:/'dræmətɪst/ </td>
                <td class="export-td">剧作家，戏剧家</td>
            </tr>
            
             <tr>
                <td class="export-td">815</td>
                <td class="export-td">dairy</td>
                <td class="export-td">英:/'deərɪ/ 美:/'dɛri/ </td>
                <td class="export-td">1. n. 乳品店；制酪场；牛奶及乳品业；乳牛；奶制品
2. adj. 牛奶的；牛奶制的；乳品的；产乳的</td>
            </tr>
            
             <tr>
                <td class="export-td">816</td>
                <td class="export-td">free</td>
                <td class="export-td">英:/friː/ 美:/fri/ </td>
                <td class="export-td">1. adj. 自由的，不受约束的；免费的；游离的
2. vt. 使自由，解放；释放</td>
            </tr>
            
             <tr>
                <td class="export-td">817</td>
                <td class="export-td">address</td>
                <td class="export-td">英:/ə'dres/ 美:/ə'drɛs/ </td>
                <td class="export-td">1. vt. 写姓名地址；向…致辞；演说；从事；忙于
2. n. 地址；致辞；演讲；说话的技巧</td>
            </tr>
            
             <tr>
                <td class="export-td">818</td>
                <td class="export-td">escalator</td>
                <td class="export-td">英:/'eskəleɪtə/ 美:/'ɛskə'letɚ/ </td>
                <td class="export-td">自动扶梯</td>
            </tr>
            
             <tr>
                <td class="export-td">819</td>
                <td class="export-td">accident</td>
                <td class="export-td">英:/'æksɪdənt/ 美:/'æksədənt/ </td>
                <td class="export-td">n. 事故；机遇；意外事件；意外</td>
            </tr>
            
             <tr>
                <td class="export-td">820</td>
                <td class="export-td">embryo</td>
                <td class="export-td">英:/'embrɪəʊ/ 美:/'ɛmbrɪo/ </td>
                <td class="export-td">1. n. [动]胚胎；[植]胚芽；初期
2. adj. 初期的；胚胎的</td>
            </tr>
            
             <tr>
                <td class="export-td">821</td>
                <td class="export-td">bachelor</td>
                <td class="export-td">英:/'bætʃələ/ 美:/'bætʃəlɚ/ </td>
                <td class="export-td">n. 单身汉；学士；（尚未交配的）小雄兽</td>
            </tr>
            
             <tr>
                <td class="export-td">822</td>
                <td class="export-td">duke</td>
                <td class="export-td">英:/djuːk/ 美:/dʊk/ </td>
                <td class="export-td">n. 公爵，（公国的）君主；[植]公爵（种）樱桃</td>
            </tr>
            
             <tr>
                <td class="export-td">823</td>
                <td class="export-td">aggressive</td>
                <td class="export-td">英:/ə'gresɪv/ 美:/ə'ɡrɛsɪv/ </td>
                <td class="export-td">积极</td>
            </tr>
            
             <tr>
                <td class="export-td">824</td>
                <td class="export-td">class</td>
                <td class="export-td">英:/klɑːs/ 美:/klæs/ </td>
                <td class="export-td">1. n. 班级；阶级；种类
2. vt. 分类；把…分等级</td>
            </tr>
            
             <tr>
                <td class="export-td">825</td>
                <td class="export-td">back</td>
                <td class="export-td">英:/bæk/ 美:/bæk/ </td>
                <td class="export-td">1. n. 背部；后面；靠背；足球等的后卫；书报等的末尾
2. vt. 支持；后退；下赌注；背书</td>
            </tr>
            
             <tr>
                <td class="export-td">826</td>
                <td class="export-td">excess</td>
                <td class="export-td">英:/ɪk'ses/ 美:/ˈɛkˌsɛs/ </td>
                <td class="export-td">1. n. 无节制；过度，过量；超过，超额
2. adj. 额外的，过量的；附加的</td>
            </tr>
            
             <tr>
                <td class="export-td">827</td>
                <td class="export-td">escape</td>
                <td class="export-td">英:/ɪ'skeɪp/ 美:/ə'skep/ </td>
                <td class="export-td">1. vt. 逃避，避免；被忘掉
2. vi. 逃脱；避开；溜走</td>
            </tr>
            
             <tr>
                <td class="export-td">828</td>
                <td class="export-td">accidental</td>
                <td class="export-td">英:/æksɪ'dent(ə)l/ 美:/ˌæksɪ'dɛntl/ </td>
                <td class="export-td">偶然</td>
            </tr>
            
             <tr>
                <td class="export-td">829</td>
                <td class="export-td">fungus</td>
                <td class="export-td">英:/'fʌŋgəs/ 美:/'fʌŋɡəs/ </td>
                <td class="export-td">n. 真菌，霉菌；菌类</td>
            </tr>
            
             <tr>
                <td class="export-td">830</td>
                <td class="export-td">glisten</td>
                <td class="export-td">英:/'glɪs(ə)n/ 美:/ˈɡlɪsən/ </td>
                <td class="export-td">1. vi. 闪光，闪亮
2. n. 闪光，闪耀</td>
            </tr>
            
             <tr>
                <td class="export-td">831</td>
                <td class="export-td">beast</td>
                <td class="export-td">英:/biːst/ 美:/bist/ </td>
                <td class="export-td">n. 野兽；畜生，人面兽心的人</td>
            </tr>
            
             <tr>
                <td class="export-td">832</td>
                <td class="export-td">algebra</td>
                <td class="export-td">英:/'ældʒɪbrə/ 美:/'ældʒɪbrə/ </td>
                <td class="export-td">n. 代数学</td>
            </tr>
            
             <tr>
                <td class="export-td">833</td>
                <td class="export-td">buffalo</td>
                <td class="export-td">英:/ˈbʌfələu/ 美:/ˈbʌfəˌlo/ </td>
                <td class="export-td">n. 水牛；野牛（产于北美）；水陆两用坦克</td>
            </tr>
            
             <tr>
                <td class="export-td">834</td>
                <td class="export-td">glitter</td>
                <td class="export-td">英:/'glɪtə/ 美:/'ɡlɪtɚ/ </td>
                <td class="export-td">1. vi. 闪烁；闪光
2. n. 闪光；灿烂</td>
            </tr>
            
             <tr>
                <td class="export-td">835</td>
                <td class="export-td">dodge</td>
                <td class="export-td">英:/dɒdʒ/ 美:/dɑdʒ/ </td>
                <td class="export-td">1. n. 躲闪；托词
2. vi. 躲避，避开</td>
            </tr>
            
             <tr>
                <td class="export-td">836</td>
                <td class="export-td">accidentally</td>
                <td class="export-td">英:/ˌæksɪˈdentəlɪ/ 美:/ˌæksə'dɛntli/ </td>
                <td class="export-td">偶然地, 意外地</td>
            </tr>
            
             <tr>
                <td class="export-td">837</td>
                <td class="export-td">heart</td>
                <td class="export-td">英:/hɑːt/ 美:/hɑrt/ </td>
                <td class="export-td">1. n. 心脏；要点；感情；勇气；心形
2. vt. 鼓励；铭记</td>
            </tr>
            
             <tr>
                <td class="export-td">838</td>
                <td class="export-td">cultivate</td>
                <td class="export-td">英:/'kʌltɪveɪt/ 美:/'kʌltɪvet/ </td>
                <td class="export-td">培育</td>
            </tr>
            
             <tr>
                <td class="export-td">839</td>
                <td class="export-td">effect</td>
                <td class="export-td">英:/ɪ'fekt/ 美:/ɪ'fɛkt/ </td>
                <td class="export-td">1. n. 效果；作用；影响
2. vt. 产生；达到目的</td>
            </tr>
            
             <tr>
                <td class="export-td">840</td>
                <td class="export-td">game</td>
                <td class="export-td">英:/geɪm/ 美:/ɡem/ </td>
                <td class="export-td">1. n. 游戏；比赛
2. adj. 勇敢的</td>
            </tr>
            
             <tr>
                <td class="export-td">841</td>
                <td class="export-td">apology</td>
                <td class="export-td">英:/ə'pɒlədʒɪ/ 美:/ə'pɑlədʒi/ </td>
                <td class="export-td">n. 道歉；谢罪；辩护；勉强的替代物</td>
            </tr>
            
             <tr>
                <td class="export-td">842</td>
                <td class="export-td">body</td>
                <td class="export-td">英:/'bɒdɪ/ 美:/'bɑdi/ </td>
                <td class="export-td">1. n. 身体；主体；团体；主要部分；大量
2. vt. 赋以形体</td>
            </tr>
            
             <tr>
                <td class="export-td">843</td>
                <td class="export-td">backbone</td>
                <td class="export-td">英:/'bækbəʊn/ 美:/'bæk'bon/ </td>
                <td class="export-td">n. 决心，毅力；支柱；脊椎；[计]主干网</td>
            </tr>
            
             <tr>
                <td class="export-td">844</td>
                <td class="export-td">effective</td>
                <td class="export-td">英:/ɪ'fektɪv/ 美:/ɪ'fɛktɪv/ </td>
                <td class="export-td">有效的,有影响的</td>
            </tr>
            
             <tr>
                <td class="export-td">845</td>
                <td class="export-td">dull</td>
                <td class="export-td">英:/dʌl/ 美:/dʌl/ </td>
                <td class="export-td">1. adj. 钝的；呆滞的；阴暗的；迟钝的；无趣的
2. vt. 使阴暗；缓和；使迟钝</td>
            </tr>
            
             <tr>
                <td class="export-td">846</td>
                <td class="export-td">coast</td>
                <td class="export-td">英:/kəʊst/ 美:/kost/ </td>
                <td class="export-td">1. vi. 沿岸航行；滑行
2. vt. 沿…岸航行</td>
            </tr>
            
             <tr>
                <td class="export-td">847</td>
                <td class="export-td">glittering</td>
                <td class="export-td">英:/ˈglɪtərɪŋ/ 美:/'ɡlɪtərɪŋ/ </td>
                <td class="export-td">荧</td>
            </tr>
            
             <tr>
                <td class="export-td">848</td>
                <td class="export-td">beat</td>
                <td class="export-td">英:/biːt/ 美:/bit/ </td>
                <td class="export-td">1. vt. 打；打败
2. vi. 打；打败；拍打；有节奏地舒张与收缩</td>
            </tr>
            
             <tr>
                <td class="export-td">849</td>
                <td class="export-td">adequate</td>
                <td class="export-td">英:/'ædɪkwət/ 美:/ˈædɪkwɪt/ </td>
                <td class="export-td">adj. 适当的；胜任的；充足的</td>
            </tr>
            
             <tr>
                <td class="export-td">850</td>
                <td class="export-td">buffet</td>
                <td class="export-td">英:/'bʊfeɪ/ 美:/bə'fe/ </td>
                <td class="export-td">1. n. 打击；小卖部；猛烈冲击；自助餐
2. vt. 与…搏斗；连续猛击</td>
            </tr>
            
             <tr>
                <td class="export-td">851</td>
                <td class="export-td">daisy</td>
                <td class="export-td">英:/'deɪzɪ/ 美:/'dezi/ </td>
                <td class="export-td">1. n. 雏菊；菊科植物；极好的东西
2. adj. [俚]极好的；上等的</td>
            </tr>
            
             <tr>
                <td class="export-td">852</td>
                <td class="export-td">heartless</td>
                <td class="export-td">英:/'hɑːtlɪs/ 美:/'hɑrtləs/ </td>
                <td class="export-td">无情的, 残酷的;</td>
            </tr>
            
             <tr>
                <td class="export-td">853</td>
                <td class="export-td">earthquake</td>
                <td class="export-td">英:/'ɜːθkweɪk/ 美:/'ɝθ'kwek/ </td>
                <td class="export-td">地震</td>
            </tr>
            
             <tr>
                <td class="export-td">854</td>
                <td class="export-td">backpack</td>
                <td class="export-td">英:/'bækpæk/ 美:/'bæk'pæk/ </td>
                <td class="export-td">1. n. 远足用的背包；双肩背包，背包
2. vt. 挑运；把…放入背包</td>
            </tr>
            
             <tr>
                <td class="export-td">855</td>
                <td class="export-td">effectively</td>
                <td class="export-td">英:/ɪˈfektɪvli:/ 美:/ɪ'fɛktɪvli/ </td>
                <td class="export-td">事实上,有效地</td>
            </tr>
            
             <tr>
                <td class="export-td">856</td>
                <td class="export-td">dice</td>
                <td class="export-td">英:/daɪs/ 美:/daɪs/ </td>
                <td class="export-td">1. vt. 切成方块
2. n. 骰子</td>
            </tr>
            
             <tr>
                <td class="export-td">857</td>
                <td class="export-td">branch</td>
                <td class="export-td">英:/brɑːn(t)ʃ/ 美:/bræntʃ/ </td>
                <td class="export-td">1. vt. 分支；出现分歧
2. vi. 分支；出现分歧</td>
            </tr>
            
             <tr>
                <td class="export-td">858</td>
                <td class="export-td">coastguard</td>
                <td class="export-td">/'kəustga:d/ </td>
                <td class="export-td">海岸警卫队</td>
            </tr>
            
             <tr>
                <td class="export-td">859</td>
                <td class="export-td">conclude</td>
                <td class="export-td">英:/kən'kluːd/ 美:/kən'klud/ </td>
                <td class="export-td">1. vt. 结束；推断；决定，作结论
2. vi. 决定；推断；断定</td>
            </tr>
            
             <tr>
                <td class="export-td">860</td>
                <td class="export-td">cultural</td>
                <td class="export-td">英:/'kʌltʃ(ə)r(ə)l/ 美:/'kʌltʃərəl/ </td>
                <td class="export-td">adj. 文化的；教养的</td>
            </tr>
            
             <tr>
                <td class="export-td">861</td>
                <td class="export-td">exchange</td>
                <td class="export-td">英:/ɪks'tʃeɪndʒ/ 美:/ɪks'tʃendʒ/ </td>
                <td class="export-td">1. n. 交换；兑换；交易所；交流
2. vt. 交换；交易；兑换</td>
            </tr>
            
             <tr>
                <td class="export-td">862</td>
                <td class="export-td">brand</td>
                <td class="export-td">英:/brænd/ 美:/brænd/ </td>
                <td class="export-td">1. vt. 打烙印于；印…商标于；铭刻于，铭记
2. n. 商标，牌子；烙印</td>
            </tr>
            
             <tr>
                <td class="export-td">863</td>
                <td class="export-td">coastline</td>
                <td class="export-td">英:/'kəʊs(t)laɪn/ 美:/'kostlaɪn/ </td>
                <td class="export-td">海岸线</td>
            </tr>
            
             <tr>
                <td class="export-td">864</td>
                <td class="export-td">conclusion</td>
                <td class="export-td">英:/kən'kluːʒ(ə)n/ 美:/kən'kluʒn/ </td>
                <td class="export-td">结论</td>
            </tr>
            
             <tr>
                <td class="export-td">865</td>
                <td class="export-td">funnel</td>
                <td class="export-td">英:/'fʌn(ə)l/ 美:/'fʌnl/ </td>
                <td class="export-td">1. n. 漏斗；烟囱
2. vt. 通过漏斗或烟囱等；使成漏斗形</td>
            </tr>
            
             <tr>
                <td class="export-td">866</td>
                <td class="export-td">equip</td>
                <td class="export-td">英:/ɪ'kwɪp/ 美:/ɪ'kwɪp/ </td>
                <td class="export-td">vt. 装备，配备</td>
            </tr>
            
             <tr>
                <td class="export-td">867</td>
                <td class="export-td">abbey</td>
                <td class="export-td">英:/ˈæbi/ 美:/ˈæbi/ </td>
                <td class="export-td">n. 大修道院，大寺院；修道院中全体修士或修女</td>
            </tr>
            
             <tr>
                <td class="export-td">868</td>
                <td class="export-td">ease</td>
                <td class="export-td">英:/iːz/ 美:/iz/ </td>
                <td class="export-td">1. vt. 减轻，缓和；使安心
2. n. 安逸，悠闲；轻松，舒适</td>
            </tr>
            
             <tr>
                <td class="export-td">869</td>
                <td class="export-td">emerald</td>
                <td class="export-td">英:/'em(ə)r(ə)ld/ 美:/'ɛmərəld/ </td>
                <td class="export-td">1. n. 绿宝石，翡翠；祖母绿；翠绿色
2. adj. 翠绿色的；翡翠的</td>
            </tr>
            
             <tr>
                <td class="export-td">870</td>
                <td class="export-td">funny</td>
                <td class="export-td">英:/'fʌnɪ/ 美:/'fʌni/ </td>
                <td class="export-td">1. adj. 有趣的；奇异的；滑稽的
2. n. 滑稽人物</td>
            </tr>
            
             <tr>
                <td class="export-td">871</td>
                <td class="export-td">coat</td>
                <td class="export-td">英:/kəʊt/ 美:/kot/ </td>
                <td class="export-td">1. n. 外套
2. vt. 覆盖…的表面</td>
            </tr>
            
             <tr>
                <td class="export-td">872</td>
                <td class="export-td">heartache</td>
                <td class="export-td">英:/'hɑːteɪk/ 美:/'hɑrtek/ </td>
                <td class="export-td">心痛</td>
            </tr>
            
             <tr>
                <td class="export-td">873</td>
                <td class="export-td">equipment</td>
                <td class="export-td">英:/ɪ'kwɪpm(ə)nt/ 美:/ɪ'kwɪpmənt/ </td>
                <td class="export-td">设备,装备</td>
            </tr>
            
             <tr>
                <td class="export-td">874</td>
                <td class="export-td">easel</td>
                <td class="export-td">英:/'iːz(ə)l/ 美:/'izl/ </td>
                <td class="export-td">n. 画架；黑板架</td>
            </tr>
            
             <tr>
                <td class="export-td">875</td>
                <td class="export-td">culture</td>
                <td class="export-td">英:/'kʌltʃə/ 美:/'kʌltʃɚ/ </td>
                <td class="export-td">1. n. 文化，文明；修养；栽培
2. vt. 培养（等于cultivate）</td>
            </tr>
            
             <tr>
                <td class="export-td">876</td>
                <td class="export-td">God</td>
                <td class="export-td">英:/ɡɔd/ 美:/ɡɑd/ </td>
                <td class="export-td">n. 神；（大写首字母时）上帝</td>
            </tr>
            
             <tr>
                <td class="export-td">877</td>
                <td class="export-td">emerge</td>
                <td class="export-td">英:/ɪ'mɜːdʒ/ 美:/ɪ'mɝdʒ/ </td>
                <td class="export-td">vi. 浮现；暴露；摆脱</td>
            </tr>
            
             <tr>
                <td class="export-td">878</td>
                <td class="export-td">champagne</td>
                <td class="export-td">英:/ʃæm'peɪn/ 美:/ʃæm'pen/ </td>
                <td class="export-td">香槟酒, 香槟色</td>
            </tr>
            
             <tr>
                <td class="export-td">879</td>
                <td class="export-td">draught</td>
                <td class="export-td">英:/drɑːft/ 美:/drɑft/ </td>
                <td class="export-td">1. n. 气流；汇票；草稿（等于draft）
2. vt. 起草；征兵；选派（等于draft）</td>
            </tr>
            
             <tr>
                <td class="export-td">880</td>
                <td class="export-td">dam</td>
                <td class="export-td">英:/dæm/ 美:/dæm/ </td>
                <td class="export-td">1. v. 筑坝；控制
2. n. 水坝；障碍</td>
            </tr>
            
             <tr>
                <td class="export-td">881</td>
                <td class="export-td">does</td>
                <td class="export-td">英:/dʌz/ 美:/dʌz/ </td>
                <td class="export-td">v. 做；工作；有用（do的第三人称单数形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">882</td>
                <td class="export-td">end</td>
                <td class="export-td">英:/end/ 美:/ɛnd/ </td>
                <td class="export-td">1. n. 结束；末端；目标；死亡；尽头
2. vi. 结束，终止；终结</td>
            </tr>
            
             <tr>
                <td class="export-td">883</td>
                <td class="export-td">east</td>
                <td class="export-td">英:/iːst/ 美:/ist/ </td>
                <td class="export-td">1. n. 东方；东方国家；东风
2. adj. 东方的；向东的；从东方来的</td>
            </tr>
            
             <tr>
                <td class="export-td">884</td>
                <td class="export-td">dumb</td>
                <td class="export-td">英:/dʌm/ 美:/dʌm/ </td>
                <td class="export-td">adj. 哑的，无说话能力的；不说话的，无声音的</td>
            </tr>
            
             <tr>
                <td class="export-td">885</td>
                <td class="export-td">champion</td>
                <td class="export-td">英:/'tʃæmpɪən/ 美:/'tʃæmpɪən/ </td>
                <td class="export-td">1. n. 冠军；拥护者；战士
2. vt. 拥护；支持</td>
            </tr>
            
             <tr>
                <td class="export-td">886</td>
                <td class="export-td">afraid</td>
                <td class="export-td">英:/ə'freɪd/ 美:/ə'fred/ </td>
                <td class="export-td">adj. 害怕的；担心的；恐怕</td>
            </tr>
            
             <tr>
                <td class="export-td">887</td>
                <td class="export-td">bug</td>
                <td class="export-td">英:/bʌg/ 美:/bʌɡ/ </td>
                <td class="export-td">1. n. 臭虫，小虫；窃听器；故障
2. vt. 烦扰，打扰；装窃听器</td>
            </tr>
            
             <tr>
                <td class="export-td">888</td>
                <td class="export-td">apostrophe</td>
                <td class="export-td">英:/ə'pɒstrəfɪ/ 美:/ə'pɑstrəfi/ </td>
                <td class="export-td">n. 省略符号，撇号；呼语，顿呼</td>
            </tr>
            
             <tr>
                <td class="export-td">889</td>
                <td class="export-td">brandy</td>
                <td class="export-td">英:/'brændɪ/ 美:/'brændi/ </td>
                <td class="export-td">n. 白兰地酒</td>
            </tr>
            
             <tr>
                <td class="export-td">890</td>
                <td class="export-td">fur</td>
                <td class="export-td">英:/fɜː/ 美:/fɝ/ </td>
                <td class="export-td">1. n. 毛皮；皮，皮子；软毛
2. vt. 用毛皮覆盖；使穿毛皮服装</td>
            </tr>
            
             <tr>
                <td class="export-td">891</td>
                <td class="export-td">damage</td>
                <td class="export-td">英:/'dæmɪdʒ/ 美:/'dæmɪdʒ/ </td>
                <td class="export-td">1. vi. 损害；损毁；赔偿金
2. n. 损害；损毁</td>
            </tr>
            
             <tr>
                <td class="export-td">892</td>
                <td class="export-td">grandpa</td>
                <td class="export-td">英:/'græn(d)pɑː/ 美:/ˈɡrændˌpɑ/ </td>
                <td class="export-td">n. [口]爷爷；[口]外公</td>
            </tr>
            
             <tr>
                <td class="export-td">893</td>
                <td class="export-td">backstroke</td>
                <td class="export-td">英:/'bækstrəʊk/ 美:/'bæk'strok/ </td>
                <td class="export-td">仰泳</td>
            </tr>
            
             <tr>
                <td class="export-td">894</td>
                <td class="export-td">championship</td>
                <td class="export-td">英:/'tʃæmpɪənʃɪp/ 美:/'tʃæmpɪənʃɪp/ </td>
                <td class="export-td">锦标赛,冠军，拥护</td>
            </tr>
            
             <tr>
                <td class="export-td">895</td>
                <td class="export-td">abbreviate</td>
                <td class="export-td">英:/ə'briːvɪeɪt/ 美:/ə'brivɪ'et/ </td>
                <td class="export-td">简略</td>
            </tr>
            
             <tr>
                <td class="export-td">896</td>
                <td class="export-td">emergency</td>
                <td class="export-td">英:/i'mə:dʒənsi/ 美:/ɪˈmɚdʒənsi/ </td>
                <td class="export-td">紧急状态, 突发事件</td>
            </tr>
            
             <tr>
                <td class="export-td">897</td>
                <td class="export-td">alien</td>
                <td class="export-td">英:/'eɪlɪən/ 美:/'elɪən/ </td>
                <td class="export-td">1. adj. 外国的；相异的，性质不同的；不相容的
2. n. 外星人；外国人，外侨</td>
            </tr>
            
             <tr>
                <td class="export-td">898</td>
                <td class="export-td">global</td>
                <td class="export-td">英:/'gləʊb(ə)l/ 美:/'ɡlobl/ </td>
                <td class="export-td">adj. 全球的；球形的；总体的</td>
            </tr>
            
             <tr>
                <td class="export-td">899</td>
                <td class="export-td">dog</td>
                <td class="export-td">英:/dɒg/ 美:/dɔɡ/ </td>
                <td class="export-td">1. n. 狗；；[美俚]丑女人；卑鄙的人；(俚)朋友
2. vt. 跟踪；尾随</td>
            </tr>
            
             <tr>
                <td class="export-td">900</td>
                <td class="export-td">abbreviation</td>
                <td class="export-td">英:/əbriːvɪ'eɪʃ(ə)n/ 美:/ə'brivɪ'eʃən/ </td>
                <td class="export-td">缩写</td>
            </tr>
            
             <tr>
                <td class="export-td">901</td>
                <td class="export-td">ending</td>
                <td class="export-td">英:/'endɪŋ/ 美:/'ɛndɪŋ/ </td>
                <td class="export-td">n. 结局；结尾</td>
            </tr>
            
             <tr>
                <td class="export-td">902</td>
                <td class="export-td">chance</td>
                <td class="export-td">英:/tʃɑːns/ 美:/tʃæns/ </td>
                <td class="export-td">1. n. 可能性；机会，际遇；运气，侥幸
2. vt. 偶然发生；冒……的险</td>
            </tr>
            
             <tr>
                <td class="export-td">903</td>
                <td class="export-td">classical</td>
                <td class="export-td">英:/'klæsɪk(ə)l/ 美:/'klæsɪkl/ </td>
                <td class="export-td">经典</td>
            </tr>
            
             <tr>
                <td class="export-td">904</td>
                <td class="export-td">excite</td>
                <td class="export-td">英:/ɪk'saɪt/ 美:/ɪk'saɪt/ </td>
                <td class="export-td">1. vt. 刺激…，使…兴奋；激起
2. vi. 激动</td>
            </tr>
            
             <tr>
                <td class="export-td">905</td>
                <td class="export-td">escort</td>
                <td class="export-td">英:/'eskɔːt/ 美:/ɪ'skɔt/ </td>
                <td class="export-td">1. n. 陪同；护送者；护航舰；护卫队
2. vt. 护送；陪同；为…护航</td>
            </tr>
            
             <tr>
                <td class="export-td">906</td>
                <td class="export-td">furious</td>
                <td class="export-td">英:/'fjʊərɪəs/ 美:/'fjʊrɪəs/ </td>
                <td class="export-td">adj. 狂怒的；激烈的；热烈兴奋的；喧闹的</td>
            </tr>
            
             <tr>
                <td class="export-td">907</td>
                <td class="export-td">globe</td>
                <td class="export-td">英:/gləʊb/ 美:/ɡlob/ </td>
                <td class="export-td">1. n. 地球仪；地球；球体
2. vt. 使…成球形</td>
            </tr>
            
             <tr>
                <td class="export-td">908</td>
                <td class="export-td">enquire</td>
                <td class="export-td">英:/ɪn'kwaɪə/ 美:/ɪn'kwaɪr/ </td>
                <td class="export-td">enquiry<br /><br />1. vi. 询问；调查；问候（等于inquire）
2. vt. 询问；打听</td>
            </tr>
            
             <tr>
                <td class="export-td">909</td>
                <td class="export-td">bodyguard</td>
                <td class="export-td">英:/'bɒdɪgɑːd/ 美:/'bɑdɪɡɑrd/ </td>
                <td class="export-td">保镖</td>
            </tr>
            
             <tr>
                <td class="export-td">910</td>
                <td class="export-td">excited</td>
                <td class="export-td">英:/ɪk'saɪtɪd/ 美:/ɪk'saɪtɪd/ </td>
                <td class="export-td">1. adj. 激动的；兴奋的；活跃的
2. v. 激动；唤起（excite的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">911</td>
                <td class="export-td">blackmail</td>
                <td class="export-td">英:/'blækmeɪl/ 美:/'blækmel/ </td>
                <td class="export-td">勒索; 勒索，讹诈</td>
            </tr>
            
             <tr>
                <td class="export-td">912</td>
                <td class="export-td">crash</td>
                <td class="export-td">英:/kræʃ/ 美:/kræʃ/ </td>
                <td class="export-td">1. n. 碰撞；崩溃；坠落
2. vt. 破碎；撞碎；坠落</td>
            </tr>
            
             <tr>
                <td class="export-td">913</td>
                <td class="export-td">draw</td>
                <td class="export-td">英:/drɔː/ 美:/drɔ/ </td>
                <td class="export-td">1. vt. 画；拉；吸引
2. vi. 拉；拖</td>
            </tr>
            
             <tr>
                <td class="export-td">914</td>
                <td class="export-td">brass</td>
                <td class="export-td">英:/brɑːs/ 美:/bræs/ </td>
                <td class="export-td">n. 黄铜；黄铜制品；厚脸皮；铜管乐器</td>
            </tr>
            
             <tr>
                <td class="export-td">915</td>
                <td class="export-td">damn</td>
                <td class="export-td">英:/dæm/ 美:/dæm/ </td>
                <td class="export-td">1. vt. 谴责；罚…下地狱
2. vi. 谴责</td>
            </tr>
            
             <tr>
                <td class="export-td">916</td>
                <td class="export-td">copy</td>
                <td class="export-td">英:/'kɒpɪ/ 美:/'kɑpi/ </td>
                <td class="export-td">1. vi. 复制；复印；抄袭
2. vt. 复制；复印；抄袭</td>
            </tr>
            
             <tr>
                <td class="export-td">917</td>
                <td class="export-td">accompany</td>
                <td class="export-td">英:/ə'kʌmpənɪ/ 美:/ə'kʌmpəni/ </td>
                <td class="export-td">陪</td>
            </tr>
            
             <tr>
                <td class="export-td">918</td>
                <td class="export-td">abdomen</td>
                <td class="export-td">英:/'æbdəmən/ 美:/'æbdəmən/ </td>
                <td class="export-td">n. 腹部；下腹；腹腔</td>
            </tr>
            
             <tr>
                <td class="export-td">919</td>
                <td class="export-td">emigrate</td>
                <td class="export-td">英:/'emɪgreɪt/ 美:/'ɛmɪɡret/ </td>
                <td class="export-td">1. vi. 移居；移居外国
2. vt. 移民</td>
            </tr>
            
             <tr>
                <td class="export-td">920</td>
                <td class="export-td">alight</td>
                <td class="export-td">英:/ə'laɪt/ 美:/ə'laɪt/ </td>
                <td class="export-td">1. vi. 下来；飞落
2. adj. 烧着的；点亮着的</td>
            </tr>
            
             <tr>
                <td class="export-td">921</td>
                <td class="export-td">dictate</td>
                <td class="export-td">英:/dɪk'teɪt/ 美:/'dɪktet/ </td>
                <td class="export-td">1. vt. 命令；口述；使听写
2. vi. 口述；听写</td>
            </tr>
            
             <tr>
                <td class="export-td">922</td>
                <td class="export-td">buggy</td>
                <td class="export-td">英:/'bʌgɪ/ 美:/'bʌɡi/ </td>
                <td class="export-td">1. n. 双轮单座轻马车；童车
2. adj. 多虫的</td>
            </tr>
            
             <tr>
                <td class="export-td">923</td>
                <td class="export-td">exciting</td>
                <td class="export-td">英:/ɪk'saɪtɪŋ/ 美:/ɪk'saɪtɪŋ/ </td>
                <td class="export-td">1. adj. 使人激动的；令人兴奋的
2. v. 激动；唤起；刺激（excite的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">924</td>
                <td class="export-td">blacksmith</td>
                <td class="export-td">英:/'blæksmɪθ/ 美:/'blæksmɪθ/ </td>
                <td class="export-td">铁匠</td>
            </tr>
            
             <tr>
                <td class="export-td">925</td>
                <td class="export-td">dictation</td>
                <td class="export-td">英:/dɪk'teɪʃ(ə)n/ 美:/dɪk'teʃən/ </td>
                <td class="export-td">听写</td>
            </tr>
            
             <tr>
                <td class="export-td">926</td>
                <td class="export-td">dummy</td>
                <td class="export-td">英:/'dʌmɪ/ 美:/'dʌmi/ </td>
                <td class="export-td">1. adj. 假的；虚拟的
2. n. 仿制品；傀儡；哑巴</td>
            </tr>
            
             <tr>
                <td class="export-td">927</td>
                <td class="export-td">grant</td>
                <td class="export-td">英:/ɡrɑ:nt/ 美:/ɡrænt/ </td>
                <td class="export-td">1. vt. 授予；承认；允许
2. vi. 同意</td>
            </tr>
            
             <tr>
                <td class="export-td">928</td>
                <td class="export-td">easter</td>
                <td class="export-td">/'i:stə/ </td>
                <td class="export-td">n. [宗]复活节</td>
            </tr>
            
             <tr>
                <td class="export-td">929</td>
                <td class="export-td">concrete</td>
                <td class="export-td">英:/'kɒŋkriːt/ 美:/'kɑŋkrit/ </td>
                <td class="export-td">1. adj. 实在的，具体的；有形的；混凝土的
2. vi. 凝结</td>
            </tr>
            
             <tr>
                <td class="export-td">930</td>
                <td class="export-td">goddess</td>
                <td class="export-td">英:/'gɒdɪs/ 美:/'ɡɑdəs/ </td>
                <td class="export-td">n. 女神，受崇拜的女性</td>
            </tr>
            
             <tr>
                <td class="export-td">931</td>
                <td class="export-td">dictator</td>
                <td class="export-td">英:/dɪk'teɪtə/ 美:/'dɪktetɚ/ </td>
                <td class="export-td">n. 独裁者；命令者</td>
            </tr>
            
             <tr>
                <td class="export-td">932</td>
                <td class="export-td">furnace</td>
                <td class="export-td">英:/'fɜːnɪs/ 美:/'fɝnɪs/ </td>
                <td class="export-td">n. 火炉，熔炉</td>
            </tr>
            
             <tr>
                <td class="export-td">933</td>
                <td class="export-td">dump</td>
                <td class="export-td">英:/dʌmp/ 美:/dʌmp/ </td>
                <td class="export-td">1. vt. 倾倒；倾卸
2. vi. 倒垃圾</td>
            </tr>
            
             <tr>
                <td class="export-td">934</td>
                <td class="export-td">appalling</td>
                <td class="export-td">英:/ə'pɔːlɪŋ/ 美:/ə'pɔlɪŋ/ </td>
                <td class="export-td">骇人听闻的</td>
            </tr>
            
             <tr>
                <td class="export-td">935</td>
                <td class="export-td">accomplish</td>
                <td class="export-td">英:/ə'kʌmplɪʃ/ 美:/ə'kɑmplɪʃ/ </td>
                <td class="export-td">完成</td>
            </tr>
            
             <tr>
                <td class="export-td">936</td>
                <td class="export-td">aspect</td>
                <td class="export-td">英:/'æspekt/ 美:/'æspɛkt/ </td>
                <td class="export-td">topic, etc that does not fit into a particular category, and is therefore difficult to deal with 灰色区域（不易归类故难以处理的方面、 题目等）: When the rules for police procedure were laid down, a lot of grey areas remained. 警方的程序规章定立後, 遗留下许多难以处理的灰色区域.<br /><br />n. 方面；外貌；形势；方向</td>
            </tr>
            
             <tr>
                <td class="export-td">937</td>
                <td class="export-td">excitement</td>
                <td class="export-td">英:/ɪk'saɪtmənt/ 美:/ɪk'saɪtmənt/ </td>
                <td class="export-td">激动, 兴奋</td>
            </tr>
            
             <tr>
                <td class="export-td">938</td>
                <td class="export-td">alike</td>
                <td class="export-td">英:/ə'laɪk/ 美:/ə'laɪk/ </td>
                <td class="export-td">1. adj. 相同的；相似的
2. adv. 以同样的方式；类似于</td>
            </tr>
            
             <tr>
                <td class="export-td">939</td>
                <td class="export-td">blade</td>
                <td class="export-td">英:/bleɪd/ 美:/bled/ </td>
                <td class="export-td">n. 刀片，刀锋；叶片；剑</td>
            </tr>
            
             <tr>
                <td class="export-td">940</td>
                <td class="export-td">build</td>
                <td class="export-td">英:/bɪld/ 美:/bɪld/ </td>
                <td class="export-td">1. vt. 建筑；建立
2. vi. 建筑；建造</td>
            </tr>
            
             <tr>
                <td class="export-td">941</td>
                <td class="export-td">ESL</td>
                <td class="export-td">/ˌi: es 'el/ </td>
                <td class="export-td">abbr. 非母语英语课程（English as a second language）</td>
            </tr>
            
             <tr>
                <td class="export-td">942</td>
                <td class="export-td">drawer</td>
                <td class="export-td">英:/drɔː/ 美:/drɔr/ </td>
                <td class="export-td">n. 抽屉；开票人</td>
            </tr>
            
             <tr>
                <td class="export-td">943</td>
                <td class="export-td">after</td>
                <td class="export-td">英:/'ɑːftə/ 美:/'æftɚ/ </td>
                <td class="export-td">1. adv. 后来，以后
2. prep. 在……之后</td>
            </tr>
            
             <tr>
                <td class="export-td">944</td>
                <td class="export-td">exclaim</td>
                <td class="export-td">英:/ɪk'skleɪm/ 美:/ɪk'sklem/ </td>
                <td class="export-td">1. vi. 呼喊，惊叫；大声叫嚷
2. vt. 大声说出</td>
            </tr>
            
             <tr>
                <td class="export-td">945</td>
                <td class="export-td">builder</td>
                <td class="export-td">英:/'bɪldə/ 美:/'bɪldɚ/ </td>
                <td class="export-td">n. 建筑者；建立者</td>
            </tr>
            
             <tr>
                <td class="export-td">946</td>
                <td class="export-td">furniture</td>
                <td class="export-td">英:/'fɜːnɪtʃə/ 美:/'fɝnɪtʃɚ/ </td>
                <td class="export-td">家具</td>
            </tr>
            
             <tr>
                <td class="export-td">947</td>
                <td class="export-td">endless</td>
                <td class="export-td">英:/'endlɪs/ 美:/'ɛndləs/ </td>
                <td class="export-td">adj. 无止境的；环状的；连续的；漫无目的的</td>
            </tr>
            
             <tr>
                <td class="export-td">948</td>
                <td class="export-td">eastern</td>
                <td class="export-td">英:/'iːst(ə)n/ 美:/'istɚn/ </td>
                <td class="export-td">1. adj. 东方的；朝东的；东洋的
2. n. 东方人；（美国）东部地区的人</td>
            </tr>
            
             <tr>
                <td class="export-td">949</td>
                <td class="export-td">exclamation</td>
                <td class="export-td">英:/ˌeksklə'meɪʃ(ə)n/ 美:/ˌɛksklə'meʃən/ </td>
                <td class="export-td">惊呼, 惊叹词</td>
            </tr>
            
             <tr>
                <td class="export-td">950</td>
                <td class="export-td">built</td>
                <td class="export-td">英:/bɪlt/ 美:/bɪlt/ </td>
                <td class="export-td">1. v. 建造（build的过去分词）
2. adj. 身段优美的；…建成的</td>
            </tr>
            
             <tr>
                <td class="export-td">951</td>
                <td class="export-td">accord</td>
                <td class="export-td">英:/ə'kɔːd/ 美:/ə'kɔrd/ </td>
                <td class="export-td">1. n. 一致；符合；协议；自愿
2. vt. 使一致；给予</td>
            </tr>
            
             <tr>
                <td class="export-td">952</td>
                <td class="export-td">copier</td>
                <td class="export-td">英:/'kɒpɪə/ 美:/'kɑpɪɚ/ </td>
                <td class="export-td">n. 抄写员；复印机（等于copying machine）；模仿者</td>
            </tr>
            
             <tr>
                <td class="export-td">953</td>
                <td class="export-td">efficient</td>
                <td class="export-td">英:/ɪ'fɪʃ(ə)nt/ 美:/ɪˈfɪʃənt/ </td>
                <td class="export-td">效率高的，胜任的</td>
            </tr>
            
             <tr>
                <td class="export-td">954</td>
                <td class="export-td">adjective</td>
                <td class="export-td">英:/'ædʒɪktɪv/ 美:/'ædʒɪktɪv/ </td>
                <td class="export-td">形容词</td>
            </tr>
            
             <tr>
                <td class="export-td">955</td>
                <td class="export-td">change</td>
                <td class="export-td">英:/tʃeɪn(d)ʒ/ 美:/tʃendʒ/ </td>
                <td class="export-td">变化, 零钱</td>
            </tr>
            
             <tr>
                <td class="export-td">956</td>
                <td class="export-td">drawing</td>
                <td class="export-td">英:/'drɔː(r)ɪŋ/ 美:/'drɔɪŋ/ </td>
                <td class="export-td">1. n. 图画；牵引；素描术
2. v. 拖曳；绘画；吸引（draw的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">957</td>
                <td class="export-td">blame</td>
                <td class="export-td">英:/bleɪm/ 美:/blem/ </td>
                <td class="export-td">1. vt. 责备；归咎于
2. n. 责备；过失；责任</td>
            </tr>
            
             <tr>
                <td class="export-td">958</td>
                <td class="export-td">apparent</td>
                <td class="export-td">英:/ə'pær(ə)nt/ 美:/ə'pærənt/ </td>
                <td class="export-td">adj. 显然的；表面上的</td>
            </tr>
            
             <tr>
                <td class="export-td">959</td>
                <td class="export-td">clause</td>
                <td class="export-td">英:/klɔːz/ 美:/klɔz/ </td>
                <td class="export-td">n. 条款；子句</td>
            </tr>
            
             <tr>
                <td class="export-td">960</td>
                <td class="export-td">cunning</td>
                <td class="export-td">英:/'kʌnɪŋ/ 美:/'kʌnɪŋ/ </td>
                <td class="export-td">1. adj. 狡猾的；可爱的；巧妙的
2. n. 狡猾</td>
            </tr>
            
             <tr>
                <td class="export-td">961</td>
                <td class="export-td">dictionary</td>
                <td class="export-td">英:/'dɪkʃ(ə)n(ə)rɪ/ 美:/'dɪkʃə'nɛri/ </td>
                <td class="export-td">词典, 字典, 辞典</td>
            </tr>
            
             <tr>
                <td class="export-td">962</td>
                <td class="export-td">apparently</td>
                <td class="export-td">英:/əˈpærəntlɪ/ 美:/ə'pærəntli/ </td>
                <td class="export-td">显然</td>
            </tr>
            
             <tr>
                <td class="export-td">963</td>
                <td class="export-td">ago</td>
                <td class="export-td">英:/ə'gəʊ/ 美:/ə'ɡo/ </td>
                <td class="export-td">1. adv. 以前，以往
2. adj. 过去的；以前的</td>
            </tr>
            
             <tr>
                <td class="export-td">964</td>
                <td class="export-td">damp</td>
                <td class="export-td">英:/dæmp/ 美:/dæmp/ </td>
                <td class="export-td">1. vt. 使潮湿；使沮丧，抑制；使阻尼
2. vi. 减幅，阻尼；变潮湿</td>
            </tr>
            
             <tr>
                <td class="export-td">965</td>
                <td class="export-td">beautician</td>
                <td class="export-td">英:/bjuː'tɪʃ(ə)n/ 美:/bjuˈtɪʃən/ </td>
                <td class="export-td">美容师</td>
            </tr>
            
             <tr>
                <td class="export-td">966</td>
                <td class="export-td">grape</td>
                <td class="export-td">英:/greɪp/ 美:/ɡrep/ </td>
                <td class="export-td">n. 葡萄；葡萄树；葡萄色；葡萄酒</td>
            </tr>
            
             <tr>
                <td class="export-td">967</td>
                <td class="export-td">easy</td>
                <td class="export-td">英:/'iːzɪ/ 美:/'izi/ </td>
                <td class="export-td">1. adj. 容易的；舒适的
2. adv. 不费力地，从容地</td>
            </tr>
            
             <tr>
                <td class="export-td">968</td>
                <td class="export-td">exclude</td>
                <td class="export-td">英:/ɪk'skluːd/ 美:/ɪk'sklʊd/ </td>
                <td class="export-td">vt. 排除；排斥；拒绝接纳；逐出</td>
            </tr>
            
             <tr>
                <td class="export-td">969</td>
                <td class="export-td">building</td>
                <td class="export-td">英:/'bɪldɪŋ/ 美:/'bɪldɪŋ/ </td>
                <td class="export-td">1. n. 建筑；建筑物
2. v. 建筑；建立；增加（build的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">970</td>
                <td class="export-td">easily</td>
                <td class="export-td">英:/'iːzɪlɪ/ 美:/'izəli/ </td>
                <td class="export-td">adv. 容易地；无疑地</td>
            </tr>
            
             <tr>
                <td class="export-td">971</td>
                <td class="export-td">exclusion</td>
                <td class="export-td">英:/ɪk'skluːʒ(ə)n/ 美:/ɪk'skluʒn/ </td>
                <td class="export-td">排除,除外,逐出</td>
            </tr>
            
             <tr>
                <td class="export-td">972</td>
                <td class="export-td">alive</td>
                <td class="export-td">英:/ə'laɪv/ 美:/ə'laɪv/ </td>
                <td class="export-td">adj. 活着的；活泼的；有生气的</td>
            </tr>
            
             <tr>
                <td class="export-td">973</td>
                <td class="export-td">cobweb</td>
                <td class="export-td">英:/'kɒbweb/ 美:/'kɑb'wɛb/ </td>
                <td class="export-td">1. n. 蜘蛛网；蛛丝；圈套
2. vt. 使布满蛛网；使混乱</td>
            </tr>
            
             <tr>
                <td class="export-td">974</td>
                <td class="export-td">beautiful</td>
                <td class="export-td">英:/'bjuːtɪfʊl/ 美:/'bjʊtəfəl/ </td>
                <td class="export-td">美丽的, 漂亮的</td>
            </tr>
            
             <tr>
                <td class="export-td">975</td>
                <td class="export-td">appeal</td>
                <td class="export-td">英:/ə'piːl/ 美:/ə'pil/ </td>
                <td class="export-td">1. vi. 呼吁，恳求；有吸引力，迎合爱好；诉诸，求助；上诉；（体育比赛中）诉诸裁判
2. n. 上诉；吸引力，感染力；呼吁，请求；诉诸裁判</td>
            </tr>
            
             <tr>
                <td class="export-td">976</td>
                <td class="export-td">account</td>
                <td class="export-td">英:/ə'kaʊnt/ 美:/ə'kaʊnt/ </td>
                <td class="export-td">1. n. 帐目，帐单；理由；帐户；解释
2. vi. 报帐；解释；导致</td>
            </tr>
            
             <tr>
                <td class="export-td">977</td>
                <td class="export-td">agony</td>
                <td class="export-td">英:/'ægənɪ/ 美:/'æɡəni/ </td>
                <td class="export-td">n. 极大的痛苦；苦恼；临死的挣扎</td>
            </tr>
            
             <tr>
                <td class="export-td">978</td>
                <td class="export-td">gloomy</td>
                <td class="export-td">英:/'gluːmɪ/ 美:/'ɡlumi/ </td>
                <td class="export-td">adj. 黑暗的；沮丧的；阴郁的</td>
            </tr>
            
             <tr>
                <td class="export-td">979</td>
                <td class="export-td">backside</td>
                <td class="export-td">英:/bæk'saɪd/ 美:/'bæksaɪd/ </td>
                <td class="export-td">n. 背部；后方；臀部</td>
            </tr>
            
             <tr>
                <td class="export-td">980</td>
                <td class="export-td">cup</td>
                <td class="export-td">英:/kʌp/ 美:/kʌp/ </td>
                <td class="export-td">1. n. 杯子；奖杯；酒杯
2. vt. 使成杯状；为…拔火罐</td>
            </tr>
            
             <tr>
                <td class="export-td">981</td>
                <td class="export-td">did</td>
                <td class="export-td">英:/dɪd/ 美:/dɪd/ </td>
                <td class="export-td">v. 做（do的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">982</td>
                <td class="export-td">drawn</td>
                <td class="export-td">英:/drɔːn/ 美:/drɔn/ </td>
                <td class="export-td">1. adj. 拔出的
2. v. 画，绘图（draw的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">983</td>
                <td class="export-td">further</td>
                <td class="export-td">英:/'fɜːðə/ 美:/'fɝðɚ/ </td>
                <td class="export-td">1. adv. 更远地；进一步地；而且
2. adj. 更远的；深一层的</td>
            </tr>
            
             <tr>
                <td class="export-td">984</td>
                <td class="export-td">aftershave</td>
                <td class="export-td">英:/'ɑːftəʃeɪv/ 美:/'æftə,ʃev/ </td>
                <td class="export-td">擦面液</td>
            </tr>
            
             <tr>
                <td class="export-td">985</td>
                <td class="export-td">bulb</td>
                <td class="export-td">英:/bʌlb/ 美:/bʌlb/ </td>
                <td class="export-td">1. n. 电灯泡；球状物；[植]鳞茎
2. vi. 生球茎；膨胀成球状</td>
            </tr>
            
             <tr>
                <td class="export-td">986</td>
                <td class="export-td">channel</td>
                <td class="export-td">英:/'tʃæn(ə)l/ 美:/'tʃænl/ </td>
                <td class="export-td">1. vt. 引导，开导；形成河道
2. n. 海峡；频道；通道</td>
            </tr>
            
             <tr>
                <td class="export-td">987</td>
                <td class="export-td">accountant</td>
                <td class="export-td">英:/ə'kaʊnt(ə)nt/ 美:/ə'kaʊntənt/ </td>
                <td class="export-td">会计人员</td>
            </tr>
            
             <tr>
                <td class="export-td">988</td>
                <td class="export-td">grapefruit</td>
                <td class="export-td">英:/'greɪpfruːt/ 美:/ˈɡrepˌfrut/ </td>
                <td class="export-td">葡萄柚，葡萄柚树</td>
            </tr>
            
             <tr>
                <td class="export-td">989</td>
                <td class="export-td">endure</td>
                <td class="export-td">英:/ɪn'djʊə/ 美:/ɛnˈdʊr/ </td>
                <td class="export-td">1. vt. 忍耐；容忍
2. vi. 忍耐；持续</td>
            </tr>
            
             <tr>
                <td class="export-td">990</td>
                <td class="export-td">bland</td>
                <td class="export-td">英:/blænd/ 美:/blænd/ </td>
                <td class="export-td">1. adj. 乏味的；冷漠的；温和的
2. vt. 使…变得淡而无味；除掉…的特性</td>
            </tr>
            
             <tr>
                <td class="export-td">991</td>
                <td class="export-td">boil</td>
                <td class="export-td">英:/bɒɪl/ 美:/bɔɪl/ </td>
                <td class="export-td">1. vi. 煮沸，沸腾；激动，激昂
2. vt. 煮沸，烧开；使…激动；使…蒸发</td>
            </tr>
            
             <tr>
                <td class="export-td">992</td>
                <td class="export-td">effort</td>
                <td class="export-td">英:/'efət/ 美:/'ɛfɚt/ </td>
                <td class="export-td">n. 成就；努力</td>
            </tr>
            
             <tr>
                <td class="export-td">993</td>
                <td class="export-td">gang</td>
                <td class="export-td">英:/gæŋ/ 美:/ɡæŋ/ </td>
                <td class="export-td">队,群,帮</td>
            </tr>
            
             <tr>
                <td class="export-td">994</td>
                <td class="export-td">graph</td>
                <td class="export-td">英:/grɑːf/ 美:/ɡræf/ </td>
                <td class="export-td">1. n. [数]图表；曲线图
2. vt. 用曲线图表示</td>
            </tr>
            
             <tr>
                <td class="export-td">995</td>
                <td class="export-td">boiling</td>
                <td class="export-td">英:/'bɒɪlɪŋ/ 美:/'bɔɪlɪŋ/ </td>
                <td class="export-td">1. adj. 沸腾的；激昂的
2. n. 煮沸；沸腾；起泡</td>
            </tr>
            
             <tr>
                <td class="export-td">996</td>
                <td class="export-td">eat</td>
                <td class="export-td">英:/iːt/ 美:/it/ </td>
                <td class="export-td">1. vt. 吃，喝；腐蚀；烦扰
2. vi. 腐蚀，侵蚀；进食</td>
            </tr>
            
             <tr>
                <td class="export-td">997</td>
                <td class="export-td">all</td>
                <td class="export-td">英:/ɔːl/ 美:/ɔl/ </td>
                <td class="export-td">1. adj. 全部的
2. adv. 越发；全然地</td>
            </tr>
            
             <tr>
                <td class="export-td">998</td>
                <td class="export-td">bulge</td>
                <td class="export-td">英:/bʌldʒ/ 美:/bʌldʒ/ </td>
                <td class="export-td">1. n. 胀；膨胀；凸出部分
2. vt. 使膨胀；使凸起</td>
            </tr>
            
             <tr>
                <td class="export-td">999</td>
                <td class="export-td">dune</td>
                <td class="export-td">英:/djuːn/ 美:/dʊn/ </td>
                <td class="export-td">n. （由风吹积而成的）沙丘</td>
            </tr>
            
             <tr>
                <td class="export-td">1000</td>
                <td class="export-td">appear</td>
                <td class="export-td">英:/ə'pɪə/ 美:/ə'pɪr/ </td>
                <td class="export-td">vi. 出现；似乎；显得；[法]出庭</td>
            </tr>
            
             <tr>
                <td class="export-td">1001</td>
                <td class="export-td">brave</td>
                <td class="export-td">英:/breɪv/ 美:/brev/ </td>
                <td class="export-td">1. adj. 勇敢的；华丽的
2. vt. 勇敢地面对</td>
            </tr>
            
             <tr>
                <td class="export-td">1002</td>
                <td class="export-td">beauty</td>
                <td class="export-td">英:/'bjuːtɪ/ 美:/'bjuti/ </td>
                <td class="export-td">n. 美；美人；美好的东西；美丽</td>
            </tr>
            
             <tr>
                <td class="export-td">1003</td>
                <td class="export-td">claw</td>
                <td class="export-td">英:/klɔː/ 美:/klɔ/ </td>
                <td class="export-td">1. n. 爪；螯，钳；爪形器具
2. vi. 用爪抓（或挖）</td>
            </tr>
            
             <tr>
                <td class="export-td">1004</td>
                <td class="export-td">cupboard</td>
                <td class="export-td">英:/'kʌbəd/ 美:/'kʌbɚd/ </td>
                <td class="export-td">n. 食橱；碗柜</td>
            </tr>
            
             <tr>
                <td class="export-td">1005</td>
                <td class="export-td">chaos</td>
                <td class="export-td">英:/'keɪɒs/ 美:/'keɑs/ </td>
                <td class="export-td">n. 混沌，混乱</td>
            </tr>
            
             <tr>
                <td class="export-td">1006</td>
                <td class="export-td">especially</td>
                <td class="export-td">英:/ɪ'speʃ(ə)lɪ/ 美:/ɪ'spɛʃəli/ </td>
                <td class="export-td">特别,尤其</td>
            </tr>
            
             <tr>
                <td class="export-td">1007</td>
                <td class="export-td">appearance</td>
                <td class="export-td">英:/ə'pɪər(ə)ns/ 美:/ə'pɪrəns/ </td>
                <td class="export-td">外表,出现,出场</td>
            </tr>
            
             <tr>
                <td class="export-td">1008</td>
                <td class="export-td">dread</td>
                <td class="export-td">英:/dred/ 美:/drɛd/ </td>
                <td class="export-td">1. n. 恐惧；可怕的人（或物）
2. vi. 惧怕；担心</td>
            </tr>
            
             <tr>
                <td class="export-td">1009</td>
                <td class="export-td">afternoon</td>
                <td class="export-td">英:/ɑːftə'nuːn/ 美:/ˌæftɚ'nun/ </td>
                <td class="export-td">下午;下午好</td>
            </tr>
            
             <tr>
                <td class="export-td">1010</td>
                <td class="export-td">emotion</td>
                <td class="export-td">英:/ɪ'məʊʃ(ə)n/ 美:/ɪ'moʃən/ </td>
                <td class="export-td">n. 情感；情绪</td>
            </tr>
            
             <tr>
                <td class="export-td">1011</td>
                <td class="export-td">dreadful</td>
                <td class="export-td">英:/'dredfʊl/ 美:/'drɛdfəl/ </td>
                <td class="export-td">adj. 可怕的；糟透的，令人不快的</td>
            </tr>
            
             <tr>
                <td class="export-td">1012</td>
                <td class="export-td">coral</td>
                <td class="export-td">英:/'kɒr(ə)l/ 美:/'kɔrəl/ </td>
                <td class="export-td">1. n. 珊瑚；珊瑚虫
2. adj. 珊瑚色的；珊瑚的</td>
            </tr>
            
             <tr>
                <td class="export-td">1013</td>
                <td class="export-td">condemn</td>
                <td class="export-td">英:/kən'dem/ 美:/kən'dɛm/ </td>
                <td class="export-td">vt. 判刑，定罪；谴责；声讨</td>
            </tr>
            
             <tr>
                <td class="export-td">1014</td>
                <td class="export-td">emotional</td>
                <td class="export-td">英:/ɪ'məʊʃ(ə)n(ə)l/ 美:/ɪ'moʃənl/ </td>
                <td class="export-td">感情的, 情绪的</td>
            </tr>
            
             <tr>
                <td class="export-td">1015</td>
                <td class="export-td">die</td>
                <td class="export-td">英:/daɪ/ 美:/daɪ/ </td>
                <td class="export-td">死</td>
            </tr>
            
             <tr>
                <td class="export-td">1016</td>
                <td class="export-td">dreadfully</td>
                <td class="export-td">英:/'dredfəlɪ/ 美:/'drɛdfəli/ </td>
                <td class="export-td">可怕</td>
            </tr>
            
             <tr>
                <td class="export-td">1017</td>
                <td class="export-td">ability</td>
                <td class="export-td">英:/ə'bɪlɪtɪ/ 美:/ə'bɪləti/ </td>
                <td class="export-td">n. 能力，能耐；才能</td>
            </tr>
            
             <tr>
                <td class="export-td">1018</td>
                <td class="export-td">backyard</td>
                <td class="export-td">英:/bæk'jɑːd/ 美:/ˌbæk'jɑrd/ </td>
                <td class="export-td">n. 后院；后庭</td>
            </tr>
            
             <tr>
                <td class="export-td">1019</td>
                <td class="export-td">goggles</td>
                <td class="export-td">英:/'gɔglz/ 美:/ˈɡ ɑ ɡlz/ </td>
                <td class="export-td">1. n. 护目镜；防护眼镜；瞪视（goggle的复数）
2. v. 瞪大眼睛看；转动眼珠（goggle的三单形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">1020</td>
                <td class="export-td">blank</td>
                <td class="export-td">英:/blæŋk/ 美:/blæŋk/ </td>
                <td class="export-td">1. adj. 空白的；空虚的；单调的
2. n. 空白；空白表格；空虚</td>
            </tr>
            
             <tr>
                <td class="export-td">1021</td>
                <td class="export-td">furthest</td>
                <td class="export-td">英:/'fɜːðɪst/ 美:/'fɝðɪst/ </td>
                <td class="export-td">1. adv. 最远地；最大程度地（far的一种最高级）
2. adj. 最远的；最遥远的（far的一种最高级）</td>
            </tr>
            
             <tr>
                <td class="export-td">1022</td>
                <td class="export-td">dance</td>
                <td class="export-td">英:/dɑːns/ 美:/dæns/ </td>
                <td class="export-td">1. n. 舞蹈；舞曲；舞会
2. vi. 跳舞；飘扬；跳跃</td>
            </tr>
            
             <tr>
                <td class="export-td">1023</td>
                <td class="export-td">glorious</td>
                <td class="export-td">英:/'glɔːrɪəs/ 美:/'ɡlɔriəs/ </td>
                <td class="export-td">adj. 光荣的；辉煌的；极好的</td>
            </tr>
            
             <tr>
                <td class="export-td">1024</td>
                <td class="export-td">going</td>
                <td class="export-td">英:/'gəʊɪŋ/ 美:/ˈɡoɪŋ/ </td>
                <td class="export-td">1. n. 离去；工作情况；行为；地面状况
2. adj. 进行中的；流行的；现存的</td>
            </tr>
            
             <tr>
                <td class="export-td">1025</td>
                <td class="export-td">bulky</td>
                <td class="export-td">英:/'bʌlkɪ/ 美:/'bʌlki/ </td>
                <td class="export-td">adj. 庞大的；体积大的；笨重的</td>
            </tr>
            
             <tr>
                <td class="export-td">1026</td>
                <td class="export-td">clay</td>
                <td class="export-td">英:/klei/ 美:/kle/ </td>
                <td class="export-td">1. n. 泥土；粘土；肉体；似黏土的东西
2. vt. 用黏土处理</td>
            </tr>
            
             <tr>
                <td class="export-td">1027</td>
                <td class="export-td">adjust</td>
                <td class="export-td">英:/ə'dʒʌst/ 美:/ə'dʒʌst/ </td>
                <td class="export-td">1. vt. 校准；调整，使…适合
2. vi. 调整，校准；适应</td>
            </tr>
            
             <tr>
                <td class="export-td">1028</td>
                <td class="export-td">dungeon</td>
                <td class="export-td">英:/'dʌn(d)ʒ(ə)n/ 美:/'dʌndʒən/ </td>
                <td class="export-td">1. n. 地牢，土牢
2. vt. 将……囚禁于土牢</td>
            </tr>
            
             <tr>
                <td class="export-td">1029</td>
                <td class="export-td">agree</td>
                <td class="export-td">英:/ə'griː/ 美:/ə'ɡri/ </td>
                <td class="export-td">1. vt. 同意；赞成；承认
2. vi. 同意；意见一致</td>
            </tr>
            
             <tr>
                <td class="export-td">1030</td>
                <td class="export-td">glory</td>
                <td class="export-td">英:/'glɔːrɪ/ 美:/'ɡlɔri/ </td>
                <td class="export-td">1. n. 光荣，荣誉；赞颂
2. vi. 自豪，骄傲；狂喜</td>
            </tr>
            
             <tr>
                <td class="export-td">1031</td>
                <td class="export-td">cock</td>
                <td class="export-td">英:/kɒk/ 美:/'stɑp'kɑk/ </td>
                <td class="export-td">1. n. 公鸡；雄鸟；龙头；头目
2. vt. 使竖起；使耸立；使朝上</td>
            </tr>
            
             <tr>
                <td class="export-td">1032</td>
                <td class="export-td">enemy</td>
                <td class="export-td">英:/'enəmɪ/ 美:/ˈɛnəmi/ </td>
                <td class="export-td">1. n. 敌人，仇敌；敌军
2. adj. 敌人的，敌方的</td>
            </tr>
            
             <tr>
                <td class="export-td">1033</td>
                <td class="export-td">boiler</td>
                <td class="export-td">英:/'bɒɪlə/ 美:/'bɔɪlɚ/ </td>
                <td class="export-td">n. 锅炉；盛热水器；烧水壶，热水器</td>
            </tr>
            
             <tr>
                <td class="export-td">1034</td>
                <td class="export-td">bull</td>
                <td class="export-td">英:/bʊl/ 美:/bʊl/ </td>
                <td class="export-td">1. n. 公牛；看好股市者；粗壮如牛的人；[俚]胡说八道；印玺
2. adj. 公牛似的；雄性的；大型的</td>
            </tr>
            
             <tr>
                <td class="export-td">1035</td>
                <td class="export-td">chapel</td>
                <td class="export-td">英:/'tʃæp(ə)l/ 美:/'tʃæpl/ </td>
                <td class="export-td">1. n. 礼拜；小礼拜堂，小教堂
2. adj. 非国教的</td>
            </tr>
            
             <tr>
                <td class="export-td">1036</td>
                <td class="export-td">crawl</td>
                <td class="export-td">英:/krɔːl/ 美:/krɔl/ </td>
                <td class="export-td">1. vi. 爬行；匍匐行进
2. vt. 爬行；缓慢地行进</td>
            </tr>
            
             <tr>
                <td class="export-td">1037</td>
                <td class="export-td">fury</td>
                <td class="export-td">英:/'fjʊərɪ/ 美:/ˈfjʊri/ </td>
                <td class="export-td">n. 狂怒；暴怒；激怒者</td>
            </tr>
            
             <tr>
                <td class="export-td">1038</td>
                <td class="export-td">energy</td>
                <td class="export-td">英:/'enədʒɪ/ 美:/'ɛnɚdʒi/ </td>
                <td class="export-td">n. 精力；能量；活力；精神</td>
            </tr>
            
             <tr>
                <td class="export-td">1039</td>
                <td class="export-td">diesel</td>
                <td class="export-td">英:/'diːz(ə)l/ 美:/'dizl/ </td>
                <td class="export-td">1. n. 柴油机；柴油；（俚）健康的身体
2. adj. 内燃机传动的；供内燃机用的</td>
            </tr>
            
             <tr>
                <td class="export-td">1040</td>
                <td class="export-td">dream</td>
                <td class="export-td">英:/driːm/ 美:/drim/ </td>
                <td class="export-td">1. vi. 做梦，梦见；梦想；想到
2. n. 梦；梦想，愿望</td>
            </tr>
            
             <tr>
                <td class="export-td">1041</td>
                <td class="export-td">dancer</td>
                <td class="export-td">英:/ˈdɑ:nsə/ 美:/'dænsɚ/ </td>
                <td class="export-td">n. 舞女；跳舞者；舞蹈家；舞蹈演员</td>
            </tr>
            
             <tr>
                <td class="export-td">1042</td>
                <td class="export-td">glossy</td>
                <td class="export-td">英:/'glɒsɪ/ 美:/'ɡlɑsi/ </td>
                <td class="export-td">adj. 有光泽的；光滑的</td>
            </tr>
            
             <tr>
                <td class="export-td">1043</td>
                <td class="export-td">energetic</td>
                <td class="export-td">英:/ˌenə'dʒetɪk/ 美:/ˌɛnɚ'dʒɛtɪk/ </td>
                <td class="export-td">有活力</td>
            </tr>
            
             <tr>
                <td class="export-td">1044</td>
                <td class="export-td">afterwards</td>
                <td class="export-td">/'æftɚwɚdz/ </td>
                <td class="export-td">以后, 后来</td>
            </tr>
            
             <tr>
                <td class="export-td">1045</td>
                <td class="export-td">agreement</td>
                <td class="export-td">英:/ə'griːm(ə)nt/ 美:/ə'grimənt/ </td>
                <td class="export-td">同意, 一致, 协议</td>
            </tr>
            
             <tr>
                <td class="export-td">1046</td>
                <td class="export-td">heat</td>
                <td class="export-td">英:/hiːt/ 美:/hit/ </td>
                <td class="export-td">1. n. 热度；高温；压力；热烈
2. vt. 把…加热；使激动</td>
            </tr>
            
             <tr>
                <td class="export-td">1047</td>
                <td class="export-td">cord</td>
                <td class="export-td">英:/kɔːd/ 美:/kɔrd/ </td>
                <td class="export-td">1. n. 束缚；绳索
2. vt. 用绳子捆绑</td>
            </tr>
            
             <tr>
                <td class="export-td">1048</td>
                <td class="export-td">empathy</td>
                <td class="export-td">英:/'empəθɪ/ 美:/'ɛmpəθi/ </td>
                <td class="export-td">n. [心]神入；移情作用</td>
            </tr>
            
             <tr>
                <td class="export-td">1049</td>
                <td class="export-td">gold</td>
                <td class="export-td">英:/gəʊld/ 美:/ɡold/ </td>
                <td class="export-td">1. n. 金，黄金；金币；金色
2. adj. 金的，金制的；金色的</td>
            </tr>
            
             <tr>
                <td class="export-td">1050</td>
                <td class="export-td">crayon</td>
                <td class="export-td">英:/'kreɪən/ 美:/'kreən/ </td>
                <td class="export-td">1. n. 蜡笔，有色粉笔
2. vt. 以蜡笔作画，用颜色粉笔画</td>
            </tr>
            
             <tr>
                <td class="export-td">1051</td>
                <td class="export-td">fuse</td>
                <td class="export-td">英:/fjuːz/ 美:/fjuz/ </td>
                <td class="export-td">1. vi. 熔化，熔融；融合
2. vt. 使熔化，使熔融；使融合</td>
            </tr>
            
             <tr>
                <td class="export-td">1052</td>
                <td class="export-td">emperor</td>
                <td class="export-td">英:/'emp(ə)rə/ 美:/'ɛmpərɚ/ </td>
                <td class="export-td">n. 皇帝，君主</td>
            </tr>
            
             <tr>
                <td class="export-td">1053</td>
                <td class="export-td">blanket</td>
                <td class="export-td">英:/'blæŋkɪt/ 美:/'blæŋkɪt/ </td>
                <td class="export-td">1. n. 毛毯，毯子；毯状物，覆盖层
2. adj. 总括的，全体的；没有限制的</td>
            </tr>
            
             <tr>
                <td class="export-td">1054</td>
                <td class="export-td">diet</td>
                <td class="export-td">英:/'daɪət/ 美:/'daɪət/ </td>
                <td class="export-td">1. n. 饮食；食物；规定饮食
2. vi. 节食</td>
            </tr>
            
             <tr>
                <td class="export-td">1055</td>
                <td class="export-td">freeway</td>
                <td class="export-td">英:/'friːweɪ/ 美:/'friwe/ </td>
                <td class="export-td">n. 高速公路</td>
            </tr>
            
             <tr>
                <td class="export-td">1056</td>
                <td class="export-td">clean</td>
                <td class="export-td">英:/kliːn/ 美:/klin/ </td>
                <td class="export-td">1. adj. 清洁的，干净的；清白的
2. vt. 使干净</td>
            </tr>
            
             <tr>
                <td class="export-td">1057</td>
                <td class="export-td">gangster</td>
                <td class="export-td">英:/'gæŋstə/ 美:/'ɡæŋstɚ/ </td>
                <td class="export-td">n. 歹徒，流氓；恶棍</td>
            </tr>
            
             <tr>
                <td class="export-td">1058</td>
                <td class="export-td">agricultural</td>
                <td class="export-td">英:/ˌægriˈkʌltʃərəl/ 美:/ˌægrɪ'kʌltʃərəl/ </td>
                <td class="export-td">农业的</td>
            </tr>
            
             <tr>
                <td class="export-td">1059</td>
                <td class="export-td">emphasis</td>
                <td class="export-td">英:/'emfəsɪs/ 美:/'ɛmfəsɪs/ </td>
                <td class="export-td">n. 强调；重点；加强语气</td>
            </tr>
            
             <tr>
                <td class="export-td">1060</td>
                <td class="export-td">excuse</td>
                <td class="export-td">英:/ɪk'skjuːz/ 美:/ɪkˈskjuz/ </td>
                <td class="export-td">1. n. 理由；借口
2. vt. 原谅；为…申辩；给…免去</td>
            </tr>
            
             <tr>
                <td class="export-td">1061</td>
                <td class="export-td">crazy</td>
                <td class="export-td">英:/'kreɪzɪ/ 美:/'krezi/ </td>
                <td class="export-td">adj. 疯狂的；狂热的，着迷的</td>
            </tr>
            
             <tr>
                <td class="export-td">1062</td>
                <td class="export-td">able</td>
                <td class="export-td">英:/'eɪb(ə)l/ 美:/'ebl/ </td>
                <td class="export-td">adj. 能干的；有能力的；能</td>
            </tr>
            
             <tr>
                <td class="export-td">1063</td>
                <td class="export-td">gangway</td>
                <td class="export-td">英:/'gæŋweɪ/ 美:/'ɡæŋwe/ </td>
                <td class="export-td">1. n. 进出通路；跳板；舷梯；座间过道
2. int. 让路</td>
            </tr>
            
             <tr>
                <td class="export-td">1064</td>
                <td class="export-td">chapter</td>
                <td class="export-td">英:/'tʃæptə/ 美:/'tʃæptɚ/ </td>
                <td class="export-td">1. n. 章，回；人生或历史上的重要时期；（俱乐部、协会等的）分会
2. vt. 把…分成章节</td>
            </tr>
            
             <tr>
                <td class="export-td">1065</td>
                <td class="export-td">appendix</td>
                <td class="export-td">英:/ə'pendɪks/ 美:/ə'pɛndɪks/ </td>
                <td class="export-td">n. 附录；阑尾；附加物</td>
            </tr>
            
             <tr>
                <td class="export-td">1066</td>
                <td class="export-td">accurate</td>
                <td class="export-td">英:/'ækjʊrət/ 美:/'ækjərət/ </td>
                <td class="export-td">adj. 精确的</td>
            </tr>
            
             <tr>
                <td class="export-td">1067</td>
                <td class="export-td">bold</td>
                <td class="export-td">英:/bəʊld/ 美:/bold/ </td>
                <td class="export-td">adj. 大胆的，英勇的；厚颜无耻的；险峻的；黑体的</td>
            </tr>
            
             <tr>
                <td class="export-td">1068</td>
                <td class="export-td">egg</td>
                <td class="export-td">英:/eg/ 美:/ɛɡ/ </td>
                <td class="export-td">1. n. 蛋；卵子；[俚]家伙
2. vt. 煽动；怂恿</td>
            </tr>
            
             <tr>
                <td class="export-td">1069</td>
                <td class="export-td">boldly</td>
                <td class="export-td">/'bəuldli/ </td>
                <td class="export-td">adv. 大胆地；冒失地；显眼地</td>
            </tr>
            
             <tr>
                <td class="export-td">1070</td>
                <td class="export-td">creak</td>
                <td class="export-td">英:/kriːk/ 美:/krik/ </td>
                <td class="export-td">1. n. 嘎吱嘎吱声
2. vi. 发出咯吱咯吱声；勉强运转</td>
            </tr>
            
             <tr>
                <td class="export-td">1071</td>
                <td class="export-td">because</td>
                <td class="export-td">英:/bɪ'kɒz/ 美:/bɪ'kɔz/ </td>
                <td class="export-td">conj. 因为</td>
            </tr>
            
             <tr>
                <td class="export-td">1072</td>
                <td class="export-td">glove</td>
                <td class="export-td">英:/glʌv/ 美:/ɡlʌv/ </td>
                <td class="export-td">1. n. 手套
2. vt. 给…戴手套</td>
            </tr>
            
             <tr>
                <td class="export-td">1073</td>
                <td class="export-td">appetite</td>
                <td class="export-td">英:/'æpɪtaɪt/ 美:/'æpɪtaɪt/ </td>
                <td class="export-td">n. 食欲；嗜好</td>
            </tr>
            
             <tr>
                <td class="export-td">1074</td>
                <td class="export-td">dandelion</td>
                <td class="export-td">英:/'dændɪlaɪən/ 美:/'dændɪlaɪən/ </td>
                <td class="export-td">蒲公英</td>
            </tr>
            
             <tr>
                <td class="export-td">1075</td>
                <td class="export-td">empire</td>
                <td class="export-td">英:/'empaɪə/ 美:/'ɛmpaɪr/ </td>
                <td class="export-td">n. 帝国；帝王统治，君权</td>
            </tr>
            
             <tr>
                <td class="export-td">1076</td>
                <td class="export-td">character</td>
                <td class="export-td">英:/'kærəktə/ 美:/'kærəktɚ/ </td>
                <td class="export-td">个性, 品质</td>
            </tr>
            
             <tr>
                <td class="export-td">1077</td>
                <td class="export-td">essay</td>
                <td class="export-td">英:/'eseɪ/ 美:/ˈɛsˌe/ </td>
                <td class="export-td">1. n. 散文；随笔；试图
2. vt. 尝试；对…做试验</td>
            </tr>
            
             <tr>
                <td class="export-td">1078</td>
                <td class="export-td">applaud</td>
                <td class="export-td">英:/ə'plɔːd/ 美:/ə'plɔd/ </td>
                <td class="export-td">1. vt. 向…喝采；赞同；称赞
2. vi. 喝彩；鼓掌欢迎</td>
            </tr>
            
             <tr>
                <td class="export-td">1079</td>
                <td class="export-td">grasp</td>
                <td class="export-td">英:/grɑːsp/ 美:/ɡræsp/ </td>
                <td class="export-td">1. n. 理解；控制；抓住
2. vt. 抓住；领会</td>
            </tr>
            
             <tr>
                <td class="export-td">1080</td>
                <td class="export-td">cleaner</td>
                <td class="export-td">英:/'kliːnə/ 美:/'klinɚ/ </td>
                <td class="export-td">n. 清洁工；清洁剂；干洗商；干洗店；洗洁器</td>
            </tr>
            
             <tr>
                <td class="export-td">1081</td>
                <td class="export-td">condition</td>
                <td class="export-td">英:/kən'dɪʃ(ə)n/ 美:/kən'dɪʃən/ </td>
                <td class="export-td">情况, 条件</td>
            </tr>
            
             <tr>
                <td class="export-td">1082</td>
                <td class="export-td">difference</td>
                <td class="export-td">英:/'dɪf(ə)r(ə)ns/ 美:/'dɪfrəns/ </td>
                <td class="export-td">n. 差异；不同；争执</td>
            </tr>
            
             <tr>
                <td class="export-td">1083</td>
                <td class="export-td">cream</td>
                <td class="export-td">英:/kriːm/ 美:/krim/ </td>
                <td class="export-td">n. 奶油，乳脂；乳酪；精华；面霜</td>
            </tr>
            
             <tr>
                <td class="export-td">1084</td>
                <td class="export-td">applause</td>
                <td class="export-td">英:/ə'plɔːz/ 美:/ə'plɔz/ </td>
                <td class="export-td">n. 鼓掌欢迎；欢呼，喝采</td>
            </tr>
            
             <tr>
                <td class="export-td">1085</td>
                <td class="export-td">dreary</td>
                <td class="export-td">英:/'drɪərɪ/ 美:/'drɪri/ </td>
                <td class="export-td">adj. 沉闷的，枯燥的</td>
            </tr>
            
             <tr>
                <td class="export-td">1086</td>
                <td class="export-td">beckon</td>
                <td class="export-td">英:/'bek(ə)n/ 美:/'bɛkən/ </td>
                <td class="export-td">1. vt. 召唤；吸引
2. vi. （招手或点头）示意；吸引</td>
            </tr>
            
             <tr>
                <td class="export-td">1087</td>
                <td class="export-td">different</td>
                <td class="export-td">英:/'dɪf(ə)r(ə)nt/ 美:/'dɪfrənt/ </td>
                <td class="export-td">不同的,与众不同的</td>
            </tr>
            
             <tr>
                <td class="export-td">1088</td>
                <td class="export-td">accuse</td>
                <td class="export-td">英:/ə'kjuːz/ 美:/ə'kjuz/ </td>
                <td class="export-td">1. vt. 控告，指控；谴责；归咎于
2. vi. 控告；指责</td>
            </tr>
            
             <tr>
                <td class="export-td">1089</td>
                <td class="export-td">dandruff</td>
                <td class="export-td">英:/'dændrʌf/ 美:/'dændrʌf/ </td>
                <td class="export-td">n. 头皮屑</td>
            </tr>
            
             <tr>
                <td class="export-td">1090</td>
                <td class="export-td">heating</td>
                <td class="export-td">英:/ ˈhi:tɪŋ/ 美:/'hitɪŋ/ </td>
                <td class="export-td">1. n. 加热；供暖；暖气设备
2. adj. 加热的；供热的</td>
            </tr>
            
             <tr>
                <td class="export-td">1091</td>
                <td class="export-td">freedom</td>
                <td class="export-td">英:/'friːdəm/ 美:/'fridəm/ </td>
                <td class="export-td">n. 自由，自主；直率</td>
            </tr>
            
             <tr>
                <td class="export-td">1092</td>
                <td class="export-td">curb</td>
                <td class="export-td">英:/kɜːb/ 美:/kɝb/ </td>
                <td class="export-td">1. n. 抑制；勒马绳；路边
2. vt. 勒住；控制</td>
            </tr>
            
             <tr>
                <td class="export-td">1093</td>
                <td class="export-td">essential</td>
                <td class="export-td">英:/ɪ'senʃ(ə)l/ 美:/ɪ'sɛnʃl/ </td>
                <td class="export-td">要素, 要点</td>
            </tr>
            
             <tr>
                <td class="export-td">1094</td>
                <td class="export-td">creamy</td>
                <td class="export-td">英:/'kriːmɪ/ 美:/'krimi/ </td>
                <td class="export-td">adj. 含乳脂的；奶油色的；乳脂状的</td>
            </tr>
            
             <tr>
                <td class="export-td">1095</td>
                <td class="export-td">apple</td>
                <td class="export-td">英:/'æp(ə)l/ 美:/'æpl/ </td>
                <td class="export-td">n. 苹果；[俚]家伙</td>
            </tr>
            
             <tr>
                <td class="export-td">1096</td>
                <td class="export-td">fuss</td>
                <td class="export-td">英:/fʌs/ 美:/fʌs/ </td>
                <td class="export-td">1. vi. 小题大作；忙乱；焦燥；焦急；无事自扰
2. n. 大惊小怪，大惊小怪的人；小题大作；忙乱</td>
            </tr>
            
             <tr>
                <td class="export-td">1097</td>
                <td class="export-td">grass</td>
                <td class="export-td">英:/grɑːs/ 美:/ɡræs/ </td>
                <td class="export-td">1. n. 草；草地，草坪
2. vt. 使……长满草；使……吃草；放牧</td>
            </tr>
            
             <tr>
                <td class="export-td">1098</td>
                <td class="export-td">execute</td>
                <td class="export-td">英:/'eksɪkjuːt/ 美:/'ɛksɪkjut/ </td>
                <td class="export-td">vt. 执行；实行；处死</td>
            </tr>
            
             <tr>
                <td class="export-td">1099</td>
                <td class="export-td">glow</td>
                <td class="export-td">英:/gləʊ/ 美:/ɡlo/ </td>
                <td class="export-td">1. vi. 发热；洋溢；绚丽夺目
2. n. 灼热；色彩鲜艳；兴高采烈</td>
            </tr>
            
             <tr>
                <td class="export-td">1100</td>
                <td class="export-td">core</td>
                <td class="export-td">英:/kɔː/ 美:/kɔr/ </td>
                <td class="export-td">1. n. 核心；果心；要点；磁心
2. vt. 挖...的核</td>
            </tr>
            
             <tr>
                <td class="export-td">1101</td>
                <td class="export-td">bed</td>
                <td class="export-td">英:/bed/ 美:/bɛd/ </td>
                <td class="export-td">1. n. 床；基础；河底， 海底
2. vt. 使睡觉；安置，嵌入；栽种</td>
            </tr>
            
             <tr>
                <td class="export-td">1102</td>
                <td class="export-td">fussy</td>
                <td class="export-td">英:/'fʌsɪ/ 美:/'fʌsi/ </td>
                <td class="export-td">adj. 爱挑剔的，难取悦的；易烦恼的</td>
            </tr>
            
             <tr>
                <td class="export-td">1103</td>
                <td class="export-td">abnormal</td>
                <td class="export-td">英:/əb'nɔːm(ə)l/ 美:/æb'nɔrml/ </td>
                <td class="export-td">adj. 反常的，不规则的；变态的</td>
            </tr>
            
             <tr>
                <td class="export-td">1104</td>
                <td class="export-td">cure</td>
                <td class="export-td">英:/kjʊə/ 美:/kjʊr/ </td>
                <td class="export-td">1. vt. 治愈；治疗；加工处理；使硫化
2. vi. 受治疗；痊愈；治病；被硫化；被加工处理</td>
            </tr>
            
             <tr>
                <td class="export-td">1105</td>
                <td class="export-td">blast</td>
                <td class="export-td">英:/blɑːst/ 美:/blæst/ </td>
                <td class="export-td">1. n. 爆炸；冲击波；一阵
2. vi. 猛攻</td>
            </tr>
            
             <tr>
                <td class="export-td">1106</td>
                <td class="export-td">gap</td>
                <td class="export-td">英:/gæp/ 美:/ɡæp/ </td>
                <td class="export-td">1. n. 缺口；间隙；空白
2. vi. 裂开</td>
            </tr>
            
             <tr>
                <td class="export-td">1107</td>
                <td class="export-td">characteristic</td>
                <td class="export-td">英:/kærəktə'rɪstɪk/ 美:/ˌkærəktə'rɪstɪk/ </td>
                <td class="export-td">特有的, 典型的</td>
            </tr>
            
             <tr>
                <td class="export-td">1108</td>
                <td class="export-td">glowing</td>
                <td class="export-td">/'ɡləuiŋ/ </td>
                <td class="export-td">1. adj. 灼热的；鲜艳的；热情洋溢的
2. v. 发光；发热；容光焕发（glow的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">1109</td>
                <td class="export-td">bedclothes</td>
                <td class="export-td">英:/'bedkləʊðz/ 美:/ˈbɛdˌkloz/ </td>
                <td class="export-td">铺盖, 床单被褥类</td>
            </tr>
            
             <tr>
                <td class="export-td">1110</td>
                <td class="export-td">clear</td>
                <td class="export-td">英:/klɪə/ 美:/klɪr/ </td>
                <td class="export-td">1. adj. 清楚的；清澈的；晴朗的；无罪的
2. vt. 清除；跳过；使干净；通过</td>
            </tr>
            
             <tr>
                <td class="export-td">1111</td>
                <td class="export-td">bread</td>
                <td class="export-td">英:/bred/ 美:/brɛd/ </td>
                <td class="export-td">1. n. 生计；面包
2. vt. 在…上洒面包屑</td>
            </tr>
            
             <tr>
                <td class="export-td">1112</td>
                <td class="export-td">clearly</td>
                <td class="export-td">英:/'kliəli/ 美:/ˈklɪrlɪ/ </td>
                <td class="export-td">adv. 明净地；清晰地；无疑地；明显地</td>
            </tr>
            
             <tr>
                <td class="export-td">1113</td>
                <td class="export-td">executive</td>
                <td class="export-td">英:/ɪg'zekjʊtɪv/ 美:/ɪɡ'zɛkjətɪv/ </td>
                <td class="export-td">行政的</td>
            </tr>
            
             <tr>
                <td class="export-td">1114</td>
                <td class="export-td">crease</td>
                <td class="export-td">英:/kriːs/ 美:/kris/ </td>
                <td class="export-td">1. n. 折痕；折缝
2. vi. 起皱</td>
            </tr>
            
             <tr>
                <td class="export-td">1115</td>
                <td class="export-td">appliance</td>
                <td class="export-td">英:/ə'plaɪəns/ 美:/ə'plaɪəns/ </td>
                <td class="export-td">应用</td>
            </tr>
            
             <tr>
                <td class="export-td">1116</td>
                <td class="export-td">create</td>
                <td class="export-td">英:/kriː'eɪt/ 美:/krɪ'et/ </td>
                <td class="export-td">vt. 造成；创造，创作</td>
            </tr>
            
             <tr>
                <td class="export-td">1117</td>
                <td class="export-td">danger</td>
                <td class="export-td">英:/'deɪn(d)ʒə/ 美:/'dendʒɚ/ </td>
                <td class="export-td">n. 危险；危险物，威胁</td>
            </tr>
            
             <tr>
                <td class="export-td">1118</td>
                <td class="export-td">freeze</td>
                <td class="export-td">英:/friːz/ 美:/friz/ </td>
                <td class="export-td">1. vi. 僵硬；冻结；冷冻
2. vt. 使…冻住；使…结冰</td>
            </tr>
            
             <tr>
                <td class="export-td">1119</td>
                <td class="export-td">curiosity</td>
                <td class="export-td">英:/kjʊərɪ'ɒsɪtɪ/ 美:/ˌkjʊrɪ'ɑsəti/ </td>
                <td class="export-td">好奇, 好奇心</td>
            </tr>
            
             <tr>
                <td class="export-td">1120</td>
                <td class="export-td">golden</td>
                <td class="export-td">英:/'ɡəuldən/ 美:/ˈɡoldən/ </td>
                <td class="export-td">adj. 金色的，黄金般的；金制的；珍贵的</td>
            </tr>
            
             <tr>
                <td class="export-td">1121</td>
                <td class="export-td">difficult</td>
                <td class="export-td">英:/'dɪfɪk(ə)lt/ 美:/'dɪfɪkəlt/ </td>
                <td class="export-td">难</td>
            </tr>
            
             <tr>
                <td class="export-td">1122</td>
                <td class="export-td">creation</td>
                <td class="export-td">英:/kriː'eɪʃ(ə)n/ 美:/krɪ'eʃən/ </td>
                <td class="export-td">n. 创造，创作；创作物，产物</td>
            </tr>
            
             <tr>
                <td class="export-td">1123</td>
                <td class="export-td">accustomed</td>
                <td class="export-td">英:/ə'kʌstəmd/ 美:/ə'kʌstəmd/ </td>
                <td class="export-td">习惯了的,通常的</td>
            </tr>
            
             <tr>
                <td class="export-td">1124</td>
                <td class="export-td">heather</td>
                <td class="export-td">英:/'heðə/ 美:/'hɛðɚ/ </td>
                <td class="export-td">1. adj. 杂色的；似石南的
2. n. [植]石南属植物</td>
            </tr>
            
             <tr>
                <td class="export-td">1125</td>
                <td class="export-td">aboard</td>
                <td class="export-td">英:/ə'bɔːd/ 美:/ə'bɔrd/ </td>
                <td class="export-td">1. adv. 在火车上；在飞机上；在船上
2. prep. 在…上</td>
            </tr>
            
             <tr>
                <td class="export-td">1126</td>
                <td class="export-td">employ</td>
                <td class="export-td">英:/ɪm'plɒɪ/ 美:/ɪm'plɔɪ/ </td>
                <td class="export-td">1. vt. 使用，采用；雇用；使忙于，使从事于
2. n. 雇用；使用</td>
            </tr>
            
             <tr>
                <td class="export-td">1127</td>
                <td class="export-td">curious</td>
                <td class="export-td">英:/'kjʊərɪəs/ 美:/'kjʊrɪəs/ </td>
                <td class="export-td">adj. 好奇的，有求知欲的；古怪的；爱挑剔的</td>
            </tr>
            
             <tr>
                <td class="export-td">1128</td>
                <td class="export-td">difficulty</td>
                <td class="export-td">英:/'dɪfɪk(ə)ltɪ/ 美:/'dɪfɪkəlti/ </td>
                <td class="export-td">困难</td>
            </tr>
            
             <tr>
                <td class="export-td">1129</td>
                <td class="export-td">bulldozer</td>
                <td class="export-td">英:/'bʊldəʊzə/ 美:/'bʊl'dozɚ/ </td>
                <td class="export-td">推土机; 欺凌者</td>
            </tr>
            
             <tr>
                <td class="export-td">1130</td>
                <td class="export-td">establish</td>
                <td class="export-td">英:/ɪ'stæblɪʃ/ 美:/ə'stæblɪʃ/ </td>
                <td class="export-td">建立, 确立, 创办</td>
            </tr>
            
             <tr>
                <td class="export-td">1131</td>
                <td class="export-td">creative</td>
                <td class="export-td">英:/kriː'eɪtɪv/ 美:/krɪ'etɪv/ </td>
                <td class="export-td">adj. 创造性的</td>
            </tr>
            
             <tr>
                <td class="export-td">1132</td>
                <td class="export-td">dress</td>
                <td class="export-td">英:/dres/ 美:/drɛs/ </td>
                <td class="export-td">1. vt. 给…穿衣
2. vi. 穿衣</td>
            </tr>
            
             <tr>
                <td class="export-td">1133</td>
                <td class="export-td">ace</td>
                <td class="export-td">英:/eɪs/ 美:/es/ </td>
                <td class="export-td">1. n. 幺点；直接得分的发球；佼佼者；（俚）最好的朋友
2. adj. 一流的，突出的</td>
            </tr>
            
             <tr>
                <td class="export-td">1134</td>
                <td class="export-td">heave</td>
                <td class="export-td">英:/hiːv/ 美:/hiv/ </td>
                <td class="export-td">1. vt. 举起；使起伏；[口]投掷；恶心；发出（叹息等）
2. vi. 起伏；喘息；呕吐；举起</td>
            </tr>
            
             <tr>
                <td class="export-td">1135</td>
                <td class="export-td">grasshopper</td>
                <td class="export-td">英:/'grɑːshɒpə/ 美:/ˈɡræsˌhɑpɚ/ </td>
                <td class="export-td">蚱蜢</td>
            </tr>
            
             <tr>
                <td class="export-td">1136</td>
                <td class="export-td">engaged</td>
                <td class="export-td">英:/ɪn'geɪdʒd/ 美:/ɪn'gedʒd/ </td>
                <td class="export-td">1. adj. 使用中的，忙碌的
2. v. 约定；保证；同…订婚（engage的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1137</td>
                <td class="export-td">curl</td>
                <td class="export-td">英:/kɜːl/ 美:/kɝl/ </td>
                <td class="export-td">1. vt. 使…卷曲；使卷起来
2. vi. 卷曲；盘绕</td>
            </tr>
            
             <tr>
                <td class="export-td">1138</td>
                <td class="export-td">bullet</td>
                <td class="export-td">英:/'bʊlɪt/ 美:/'bʊlɪt/ </td>
                <td class="export-td">1. n. 子弹；只选某党全部候选人的投票；[美俚]豆子
2. vi. 射出；迅速行进</td>
            </tr>
            
             <tr>
                <td class="export-td">1139</td>
                <td class="export-td">applicant</td>
                <td class="export-td">英:/'æplɪk(ə)nt/ 美:/'æplɪkənt/ </td>
                <td class="export-td">申请人</td>
            </tr>
            
             <tr>
                <td class="export-td">1140</td>
                <td class="export-td">cockerel</td>
                <td class="export-td">英:/'kɒk(ə)r(ə)l/ 美:/'kɑkərəl/ </td>
                <td class="export-td">n. （未满一年的）小公鸡；好斗的年轻人</td>
            </tr>
            
             <tr>
                <td class="export-td">1141</td>
                <td class="export-td">dangerous</td>
                <td class="export-td">英:/'deɪn(d)ʒ(ə)rəs/ 美:/'dendʒərəs/ </td>
                <td class="export-td">危险的,引起危险的</td>
            </tr>
            
             <tr>
                <td class="export-td">1142</td>
                <td class="export-td">heaven</td>
                <td class="export-td">英:/'hev(ə)n/ 美:/'hɛvn/ </td>
                <td class="export-td">n. 天堂；天空；极乐</td>
            </tr>
            
             <tr>
                <td class="export-td">1143</td>
                <td class="export-td">freezer</td>
                <td class="export-td">英:/'friːzə/ 美:/'frizɚ/ </td>
                <td class="export-td">n. 冰箱；冷冻库；制冷工</td>
            </tr>
            
             <tr>
                <td class="export-td">1144</td>
                <td class="export-td">abolish</td>
                <td class="export-td">英:/ə'bɒlɪʃ/ 美:/ə'bɑlɪʃ/ </td>
                <td class="export-td">vt. 废除，废止；取消，革除</td>
            </tr>
            
             <tr>
                <td class="export-td">1145</td>
                <td class="export-td">background</td>
                <td class="export-td">英:/ˈbækɡraund/ 美:/'bækɡraʊnd/ </td>
                <td class="export-td">背景,幕后,配音</td>
            </tr>
            
             <tr>
                <td class="export-td">1146</td>
                <td class="export-td">curly</td>
                <td class="export-td">英:/'kɜːlɪ/ 美:/'kɝli/ </td>
                <td class="export-td">adj. 卷曲的；卷毛的；（木材）有皱状纹理的；蜷缩的</td>
            </tr>
            
             <tr>
                <td class="export-td">1147</td>
                <td class="export-td">application</td>
                <td class="export-td">英:/æplɪ'keɪʃ(ə)n/ 美:/ˌæplɪ'keʃən/ </td>
                <td class="export-td">应用</td>
            </tr>
            
             <tr>
                <td class="export-td">1148</td>
                <td class="export-td">grate</td>
                <td class="export-td">英:/greɪt/ 美:/ɡret/ </td>
                <td class="export-td">1. vt. 装格栅于；磨擦
2. vi. 发摩擦声</td>
            </tr>
            
             <tr>
                <td class="export-td">1149</td>
                <td class="export-td">freight</td>
                <td class="export-td">英:/freɪt/ 美:/fret/ </td>
                <td class="export-td">1. vt. 运送；装货；使充满
2. n. 运费；货运；船货</td>
            </tr>
            
             <tr>
                <td class="export-td">1150</td>
                <td class="export-td">cork</td>
                <td class="export-td">英:/kɔ:k/ 美:/kɔrk/ </td>
                <td class="export-td">1. n. 软木；软木塞，软木制品
2. vt. 用软木塞塞住；抑制，堵住</td>
            </tr>
            
             <tr>
                <td class="export-td">1151</td>
                <td class="export-td">engagement</td>
                <td class="export-td">英:/ɪn'geɪdʒm(ə)nt/ 美:/ɪn'ɡedʒmənt/ </td>
                <td class="export-td">订婚</td>
            </tr>
            
             <tr>
                <td class="export-td">1152</td>
                <td class="export-td">employee</td>
                <td class="export-td">英:/emplɒɪ'iː/ 美:/ɪm'plɔɪi/ </td>
                <td class="export-td">n. 雇员；从业员工</td>
            </tr>
            
             <tr>
                <td class="export-td">1153</td>
                <td class="export-td">estate</td>
                <td class="export-td">英:/ɪ'steɪt/ 美:/ɪ'stet/ </td>
                <td class="export-td">n. 财产；房地产；身份</td>
            </tr>
            
             <tr>
                <td class="export-td">1154</td>
                <td class="export-td">employer</td>
                <td class="export-td">英:/ɪm'plɒɪə/ 美:/ɪm'plɔɪɚ/ </td>
                <td class="export-td">n. 雇主，老板</td>
            </tr>
            
             <tr>
                <td class="export-td">1155</td>
                <td class="export-td">charge</td>
                <td class="export-td">英:/tʃɑːdʒ/ 美:/tʃɑrdʒ/ </td>
                <td class="export-td">1. n. 费用；掌管；控告；负载；电荷；命令
2. vt. 装载；对…索费；使承担；向…冲去；指责；使充电</td>
            </tr>
            
             <tr>
                <td class="export-td">1156</td>
                <td class="export-td">creator</td>
                <td class="export-td">英:/kri'eitə/ 美:/kriˈetɚ/ </td>
                <td class="export-td">n. 创造者；创建者</td>
            </tr>
            
             <tr>
                <td class="export-td">1157</td>
                <td class="export-td">ache</td>
                <td class="export-td">英:/eɪk/ 美:/ek/ </td>
                <td class="export-td">1. vi. 疼痛；渴望
2. n. 疼痛</td>
            </tr>
            
             <tr>
                <td class="export-td">1158</td>
                <td class="export-td">employment</td>
                <td class="export-td">英:/ɪm'plɒɪm(ə)nt/ 美:/ɪm'plɔɪmənt/ </td>
                <td class="export-td">职业,雇用,使用</td>
            </tr>
            
             <tr>
                <td class="export-td">1159</td>
                <td class="export-td">bacon</td>
                <td class="export-td">英:/ˈbeɪkən/ 美:/ˈbekən/ </td>
                <td class="export-td">n. 熏猪肉；咸肉；腌肉</td>
            </tr>
            
             <tr>
                <td class="export-td">1160</td>
                <td class="export-td">allergy</td>
                <td class="export-td">英:/'ælədʒɪ/ 美:/'ælɚdʒi/ </td>
                <td class="export-td">n. 过敏症；[口]反感；厌恶</td>
            </tr>
            
             <tr>
                <td class="export-td">1161</td>
                <td class="export-td">garbage</td>
                <td class="export-td">英:/'gɑːbɪdʒ/ 美:/'ɡɑrbɪdʒ/ </td>
                <td class="export-td">n. 垃圾；废物</td>
            </tr>
            
             <tr>
                <td class="export-td">1162</td>
                <td class="export-td">creature</td>
                <td class="export-td">英:/'kriːtʃə/ 美:/'kritʃɚ/ </td>
                <td class="export-td">n. 动物，生物；人；创造物</td>
            </tr>
            
             <tr>
                <td class="export-td">1163</td>
                <td class="export-td">cockpit</td>
                <td class="export-td">英:/'kɒkpɪt/ 美:/'kɑkpɪt/ </td>
                <td class="export-td">n. 驾驶员座舱；战场</td>
            </tr>
            
             <tr>
                <td class="export-td">1164</td>
                <td class="export-td">corkscrew</td>
                <td class="export-td">英:/'kɔːkskruː/ 美:/'kɔrkskru/ </td>
                <td class="export-td">拔塞钻, 螺丝锥</td>
            </tr>
            
             <tr>
                <td class="export-td">1165</td>
                <td class="export-td">bacteria</td>
                <td class="export-td">英:/bæk'tɪərɪə/ 美:/bæk'tɪrɪə/ </td>
                <td class="export-td">n. 细菌</td>
            </tr>
            
             <tr>
                <td class="export-td">1166</td>
                <td class="export-td">allergic</td>
                <td class="export-td">英:/ə'lɜːdʒɪk/ 美:/ə'lɝdʒɪk/ </td>
                <td class="export-td">adj. 对…过敏的；对…极讨厌的</td>
            </tr>
            
             <tr>
                <td class="export-td">1167</td>
                <td class="export-td">during</td>
                <td class="export-td">英:/'djʊərɪŋ/ 美:/'dʊrɪŋ/ </td>
                <td class="export-td">prep. 在…的时候，在…的期间</td>
            </tr>
            
             <tr>
                <td class="export-td">1168</td>
                <td class="export-td">heavy</td>
                <td class="export-td">英:/'hevɪ/ 美:/'hɛvi/ </td>
                <td class="export-td">1. adj. 沉重的；繁重的，巨大的；阴沉的
2. n. 重物；严肃角色</td>
            </tr>
            
             <tr>
                <td class="export-td">1169</td>
                <td class="export-td">bedroom</td>
                <td class="export-td">英:/'bedruːm/ 美:/'bɛdrum/ </td>
                <td class="export-td">1. n. 卧室
2. adj. 两性关系的；城郊住宅区的</td>
            </tr>
            
             <tr>
                <td class="export-td">1170</td>
                <td class="export-td">bolt</td>
                <td class="export-td">英:/bəʊlt/ 美:/bolt/ </td>
                <td class="export-td">1. n. 闪电；螺栓；门闩；弩箭
2. vt. 囫囵吞下；上门闩</td>
            </tr>
            
             <tr>
                <td class="export-td">1171</td>
                <td class="export-td">exercise</td>
                <td class="export-td">英:/'eksəsaɪz/ 美:/'ɛksɚsaɪz/ </td>
                <td class="export-td">1. n. 练习；运动；运用；操练；典礼；礼拜
2. vt. 练习；锻炼；使用；使忙碌；使惊恐</td>
            </tr>
            
             <tr>
                <td class="export-td">1172</td>
                <td class="export-td">glum</td>
                <td class="export-td">英:/glʌm/ 美:/ɡlʌm/ </td>
                <td class="export-td">adj. 阴沉的；忧郁的</td>
            </tr>
            
             <tr>
                <td class="export-td">1173</td>
                <td class="export-td">grateful</td>
                <td class="export-td">英:/'greɪtfʊl/ 美:/'ɡretfl/ </td>
                <td class="export-td">adj. 感谢的；令人愉快的，宜人的</td>
            </tr>
            
             <tr>
                <td class="export-td">1174</td>
                <td class="export-td">engine</td>
                <td class="export-td">英:/'endʒɪn/ 美:/'ɛndʒɪn/ </td>
                <td class="export-td">n. 引擎，发动机；机车，火车头；工具</td>
            </tr>
            
             <tr>
                <td class="export-td">1175</td>
                <td class="export-td">admire</td>
                <td class="export-td">英:/əd'maɪə/ 美:/əd'maɪɚ/ </td>
                <td class="export-td">1. vt. 钦佩；赞美
2. vi. 钦佩；称赞</td>
            </tr>
            
             <tr>
                <td class="export-td">1176</td>
                <td class="export-td">dusk</td>
                <td class="export-td">英:/dʌsk/ 美:/dʌsk/ </td>
                <td class="export-td">1. n. 黄昏，薄暮；幽暗，昏暗
2. adj. 微暗的</td>
            </tr>
            
             <tr>
                <td class="export-td">1177</td>
                <td class="export-td">apply</td>
                <td class="export-td">英:/ə'plaɪ/ 美:/ə'plaɪ/ </td>
                <td class="export-td">1. vt. 应用；申请；涂，敷
2. vi. 申请；适用；请求；涂，敷</td>
            </tr>
            
             <tr>
                <td class="export-td">1178</td>
                <td class="export-td">achieve</td>
                <td class="export-td">英:/ə'tʃiːv/ 美:/ə'tʃiv/ </td>
                <td class="export-td">1. vt. 完成；达到
2. vi. 达到目的；如愿以偿</td>
            </tr>
            
             <tr>
                <td class="export-td">1179</td>
                <td class="export-td">bedside</td>
                <td class="export-td">英:/'bedsaɪd/ 美:/'bɛd'saɪd/ </td>
                <td class="export-td">1. n. 床边，床旁
2. adj. 床旁的，枕边的</td>
            </tr>
            
             <tr>
                <td class="export-td">1180</td>
                <td class="export-td">conduct</td>
                <td class="export-td">英:/'kɒndʌkt/ 美:/kən'dʌkt/ </td>
                <td class="export-td">1. vi. 带领；导电
2. vt. 管理；表现；引导</td>
            </tr>
            
             <tr>
                <td class="export-td">1181</td>
                <td class="export-td">garden</td>
                <td class="export-td">英:/ˈɡɑ:dn/ 美:/ˈɡɑrdn/ </td>
                <td class="export-td">1. n. 菜园；花园
2. vt. 栽培花木</td>
            </tr>
            
             <tr>
                <td class="export-td">1182</td>
                <td class="export-td">appoint</td>
                <td class="export-td">英:/ə'pɒɪnt/ 美:/ə'pɔɪnt/ </td>
                <td class="export-td">1. vt. 任命；指定；约定
2. vi. 任命；委派</td>
            </tr>
            
             <tr>
                <td class="export-td">1183</td>
                <td class="export-td">currant</td>
                <td class="export-td">英:/'kʌr(ə)nt/ 美:/'kɝənt/ </td>
                <td class="export-td">n. 无籽葡萄干；红醋药；红醋栗</td>
            </tr>
            
             <tr>
                <td class="export-td">1184</td>
                <td class="export-td">goldfish</td>
                <td class="export-td">英:/'gəʊl(d)fɪʃ/ 美:/'ɡoldfɪʃ/ </td>
                <td class="export-td">n. 金鱼</td>
            </tr>
            
             <tr>
                <td class="export-td">1185</td>
                <td class="export-td">achievement</td>
                <td class="export-td">英:/ə'tʃiːvm(ə)nt/ 美:/ə'tʃivmənt/ </td>
                <td class="export-td">成就</td>
            </tr>
            
             <tr>
                <td class="export-td">1186</td>
                <td class="export-td">cocktail</td>
                <td class="export-td">英:/'kɒkteɪl/ 美:/'kɑktel/ </td>
                <td class="export-td">1. n. 鸡尾酒；开味食品
2. adj. 鸡尾酒的</td>
            </tr>
            
             <tr>
                <td class="export-td">1187</td>
                <td class="export-td">glut</td>
                <td class="export-td">英:/glʌt/ 美:/ɡlʌt/ </td>
                <td class="export-td">1. vt. 使…充满；使…吃饱；过多供应
2. vi. 吃得过多</td>
            </tr>
            
             <tr>
                <td class="export-td">1188</td>
                <td class="export-td">engineer</td>
                <td class="export-td">英:/endʒɪ'nɪə/ 美:/ˌɛndʒɪ'nɪr/ </td>
                <td class="export-td">1. n. 工程师；工兵；火车司机
2. vt. 策划；设计；精明地处理</td>
            </tr>
            
             <tr>
                <td class="export-td">1189</td>
                <td class="export-td">currency</td>
                <td class="export-td">英:/'kʌr(ə)nsɪ/ 美:/'kɝənsi/ </td>
                <td class="export-td">n. 货币；通货</td>
            </tr>
            
             <tr>
                <td class="export-td">1190</td>
                <td class="export-td">alley</td>
                <td class="export-td">英:/'ælɪ/ 美:/'æli/ </td>
                <td class="export-td">n. 小径；小巷；小路</td>
            </tr>
            
             <tr>
                <td class="export-td">1191</td>
                <td class="export-td">gardener</td>
                <td class="export-td">英:/'ɡɑːdənə/ 美:/'gɑrdənɚ/ </td>
                <td class="export-td">n. 花匠；园丁；园艺家</td>
            </tr>
            
             <tr>
                <td class="export-td">1192</td>
                <td class="export-td">dust</td>
                <td class="export-td">英:/dʌst/ 美:/dʌst/ </td>
                <td class="export-td">1. n. 灰尘；尘埃；尘土
2. vt. 拂去灰尘；撒</td>
            </tr>
            
             <tr>
                <td class="export-td">1193</td>
                <td class="export-td">charger</td>
                <td class="export-td">英:/'tʃɑːdʒə/ 美:/'tʃɑrdʒɚ/ </td>
                <td class="export-td">n. 充电器；军马；袭击者；委托者；控诉者</td>
            </tr>
            
             <tr>
                <td class="export-td">1194</td>
                <td class="export-td">estimate</td>
                <td class="export-td">英:/'estɪmeɪt/ 美:/'ɛstə,met/ </td>
                <td class="export-td">1. vi. 估计，估价
2. n. 估计，估价；判断，看法</td>
            </tr>
            
             <tr>
                <td class="export-td">1195</td>
                <td class="export-td">corn</td>
                <td class="export-td">英:/kɔːn/ 美:/kɔrn/ </td>
                <td class="export-td">1. n. （美）玉米；（英）谷物；鸡眼
2. vt. 腌；使成颗粒</td>
            </tr>
            
             <tr>
                <td class="export-td">1196</td>
                <td class="export-td">engineering</td>
                <td class="export-td">英:/endʒɪ'nɪərɪŋ/ 美:/'ɛndʒə'nɪrɪŋ/ </td>
                <td class="export-td">工程学,工程</td>
            </tr>
            
             <tr>
                <td class="export-td">1197</td>
                <td class="export-td">current</td>
                <td class="export-td">英:/'kʌr(ə)nt/ 美:/'kɝənt/ </td>
                <td class="export-td">1. adj. 现在的；最近的；草写的；流通的，通用的
2. n. 趋势；涌流；（水，气，电）流</td>
            </tr>
            
             <tr>
                <td class="export-td">1198</td>
                <td class="export-td">golf</td>
                <td class="export-td">英:/gɒlf/ 美:/ɡɑlf/ </td>
                <td class="export-td">1. n. 高尔夫球；高尔夫球运动
2. vi. 打高尔夫球</td>
            </tr>
            
             <tr>
                <td class="export-td">1199</td>
                <td class="export-td">blaze</td>
                <td class="export-td">英:/bleɪz/ 美:/blez/ </td>
                <td class="export-td">1. vt. 在树皮上刻路标；公开宣布
2. n. 火焰，烈火；光辉；情感爆发</td>
            </tr>
            
             <tr>
                <td class="export-td">1200</td>
                <td class="export-td">dustbin</td>
                <td class="export-td">英:/'dʌs(t)bɪn/ 美:/'dʌstbɪn/ </td>
                <td class="export-td">n. 垃圾箱</td>
            </tr>
            
             <tr>
                <td class="export-td">1201</td>
                <td class="export-td">bedspread</td>
                <td class="export-td">英:/'bedspred/ 美:/'bɛdsprɛd/ </td>
                <td class="export-td">床单, 床罩</td>
            </tr>
            
             <tr>
                <td class="export-td">1202</td>
                <td class="export-td">English</td>
                <td class="export-td">/'iŋɡliʃ/ </td>
                <td class="export-td">1. adj. 英国人的；英国的；英文的
2. n. 英语；英国人；英文；英格兰人</td>
            </tr>
            
             <tr>
                <td class="export-td">1203</td>
                <td class="export-td">empress</td>
                <td class="export-td">英:/'emprɪs/ 美:/ˈɛmprɪs/ </td>
                <td class="export-td">n. 皇后；女皇</td>
            </tr>
            
             <tr>
                <td class="export-td">1204</td>
                <td class="export-td">bad</td>
                <td class="export-td">英:/bæd/ 美:/bæd/ </td>
                <td class="export-td">1. adj. 坏的；严重的；劣质的
2. n. 坏人；坏事</td>
            </tr>
            
             <tr>
                <td class="export-td">1205</td>
                <td class="export-td">dressing</td>
                <td class="export-td">英:/'dresɪŋ/ 美:/'drɛsɪŋ/ </td>
                <td class="export-td">1. n. 穿衣；装饰；梳理；加工；调味品
2. v. 给…穿衣；为…打扮（dress的现在分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1206</td>
                <td class="export-td">break</td>
                <td class="export-td">英:/breɪk/ 美:/brek/ </td>
                <td class="export-td">1. n. 休息，中断；破裂处
2. vt. 打破，弄破；中断；弄坏；削弱</td>
            </tr>
            
             <tr>
                <td class="export-td">1207</td>
                <td class="export-td">doll</td>
                <td class="export-td">英:/dɔl/ 美:/dɑl/ </td>
                <td class="export-td">1. n. 洋娃娃；玩偶；无头脑的美丽女人
2. vt. 把…打扮得花枝招展</td>
            </tr>
            
             <tr>
                <td class="export-td">1208</td>
                <td class="export-td">conductor</td>
                <td class="export-td">英:/kən'dʌktə/ 美:/kən'dʌktɚ/ </td>
                <td class="export-td">售票员，导体，指挥</td>
            </tr>
            
             <tr>
                <td class="export-td">1209</td>
                <td class="export-td">exhaust</td>
                <td class="export-td">英:/ɪg'zɔːst/ 美:/ɪɡ'zɔst/ </td>
                <td class="export-td">1. vt. 耗尽；排出；使精疲力尽；彻底探讨
2. vi. 排气</td>
            </tr>
            
             <tr>
                <td class="export-td">1210</td>
                <td class="export-td">dig</td>
                <td class="export-td">英:/dɪg/ 美:/dɪɡ/ </td>
                <td class="export-td">1. vt. 挖，掘；探究
2. vi. 挖掘</td>
            </tr>
            
             <tr>
                <td class="export-td">1211</td>
                <td class="export-td">apportionment</td>
                <td class="export-td">英:/ə'pɔːʃ(ə)nm(ə)nt/ 美:/ə'pɔrʃənmənt/ </td>
                <td class="export-td">分配, 分摊, 分派</td>
            </tr>
            
             <tr>
                <td class="export-td">1212</td>
                <td class="export-td">empty</td>
                <td class="export-td">英:/'em(p)tɪ/ 美:/'ɛmpti/ </td>
                <td class="export-td">1. adj. 空的；无意义的；徒劳的；无知的
2. vt. 使…成为空的；使失去</td>
            </tr>
            
             <tr>
                <td class="export-td">1213</td>
                <td class="export-td">badly</td>
                <td class="export-td">英:/'bædlɪ/ 美:/'bædli/ </td>
                <td class="export-td">adv. 严重地，厉害地；恶劣地；非常，很</td>
            </tr>
            
             <tr>
                <td class="export-td">1214</td>
                <td class="export-td">credit</td>
                <td class="export-td">英:/'kredɪt/ 美:/'krɛdɪt/ </td>
                <td class="export-td">1. n. 信用，信誉；信任；贷款；声望；学分
2. vt. 相信，信任；把…归给，归功于；赞颂</td>
            </tr>
            
             <tr>
                <td class="export-td">1215</td>
                <td class="export-td">acid</td>
                <td class="export-td">英:/'æsɪd/ 美:/'æsɪd/ </td>
                <td class="export-td">1. n. 酸，迷幻药
2. adj. 酸的，讽刺的，刻薄的</td>
            </tr>
            
             <tr>
                <td class="export-td">1216</td>
                <td class="export-td">blazer</td>
                <td class="export-td">英:/'bleɪzə/ 美:/'blezɚ/ </td>
                <td class="export-td">n. 燃烧体；宣布者；颜色鲜明的运动上衣</td>
            </tr>
            
             <tr>
                <td class="export-td">1217</td>
                <td class="export-td">digest</td>
                <td class="export-td">英:/daɪ'dʒest/ 美:/daɪ'dʒɛst/ </td>
                <td class="export-td">1. vt. 消化；吸收；融会贯通
2. vi. 消化</td>
            </tr>
            
             <tr>
                <td class="export-td">1218</td>
                <td class="export-td">estuary</td>
                <td class="export-td">英:/'estjʊ(ə)rɪ/ 美:/'ɛstʃʊ'ɛri/ </td>
                <td class="export-td">n. 河口；江口</td>
            </tr>
            
             <tr>
                <td class="export-td">1219</td>
                <td class="export-td">cornflakes</td>
                <td class="export-td">英:/'kɔːnfleɪks/ 美:/'kɔrnfleks/ </td>
                <td class="export-td">玉米片</td>
            </tr>
            
             <tr>
                <td class="export-td">1220</td>
                <td class="export-td">bedtime</td>
                <td class="export-td">英:/'bedtaɪm/ 美:/'bɛdtaɪm/ </td>
                <td class="export-td">1. n. 就寝时间
2. adj. 适于睡前的</td>
            </tr>
            
             <tr>
                <td class="export-td">1221</td>
                <td class="export-td">bully</td>
                <td class="export-td">英:/'bʊlɪ/ 美:/'bʊli/ </td>
                <td class="export-td">1. n. 欺凌弱小者；土霸
2. adj. [口]第一流的；特好的</td>
            </tr>
            
             <tr>
                <td class="export-td">1222</td>
                <td class="export-td">dollar</td>
                <td class="export-td">英:/'dɒlə/ 美:/'dɑlɚ/ </td>
                <td class="export-td">n. 美元</td>
            </tr>
            
             <tr>
                <td class="export-td">1223</td>
                <td class="export-td">admission</td>
                <td class="export-td">英:/əd'mɪʃ(ə)n/ 美:/əd'mɪʃən/ </td>
                <td class="export-td">承认</td>
            </tr>
            
             <tr>
                <td class="export-td">1224</td>
                <td class="export-td">drew</td>
                <td class="export-td">英:/druː/ 美:/dru/ </td>
                <td class="export-td">v. 描绘；起草；牵引（draw的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1225</td>
                <td class="export-td">cocoa</td>
                <td class="export-td">英:/'kəʊkəʊ/ 美:/'koko/ </td>
                <td class="export-td">n. 可可粉；可可豆；深褐色；可可饮料</td>
            </tr>
            
             <tr>
                <td class="export-td">1226</td>
                <td class="export-td">dare</td>
                <td class="export-td">英:/deə/ 美:/dɛr/ </td>
                <td class="export-td">1. n. 挑战；挑动
2. vt. 不惧；敢冒</td>
            </tr>
            
             <tr>
                <td class="export-td">1227</td>
                <td class="export-td">cone</td>
                <td class="export-td">英:/kəʊn/ 美:/kon/ </td>
                <td class="export-td">1. n. 圆锥体，圆锥形；球果
2. vt. 使成锥形</td>
            </tr>
            
             <tr>
                <td class="export-td">1228</td>
                <td class="export-td">curriculum</td>
                <td class="export-td">英:/kʌ'rɪkjʊləm/ 美:/kə'rɪkjələm/ </td>
                <td class="export-td">课程</td>
            </tr>
            
             <tr>
                <td class="export-td">1229</td>
                <td class="export-td">admit</td>
                <td class="export-td">英:/əd'mɪt/ 美:/əd'mɪt/ </td>
                <td class="export-td">1. vt. 承认；准许进入；可容纳
2. vi. 承认；容许</td>
            </tr>
            
             <tr>
                <td class="export-td">1230</td>
                <td class="export-td">dustman</td>
                <td class="export-td">英:/'dʌs(t)mən/ 美:/'dʌstmən/ </td>
                <td class="export-td">n. 清洁工人</td>
            </tr>
            
             <tr>
                <td class="export-td">1231</td>
                <td class="export-td">coconut</td>
                <td class="export-td">英:/'kəʊkənʌt/ 美:/'kokənʌt/ </td>
                <td class="export-td">n. 椰子；椰子肉</td>
            </tr>
            
             <tr>
                <td class="export-td">1232</td>
                <td class="export-td">abortion</td>
                <td class="export-td">英:/ə'bɔːʃ(ə)n/ 美:/ə'bɔrʃən/ </td>
                <td class="export-td">n. 流产，小产；流产的胎儿</td>
            </tr>
            
             <tr>
                <td class="export-td">1233</td>
                <td class="export-td">curry</td>
                <td class="export-td">英:/ˈkʌri/ 美:/ˈkɚri/ </td>
                <td class="export-td">1. vt. 用咖喱烧，给…加咖喱粉
2. n. 咖哩粉，咖喱；咖哩饭菜；梳刷；鞭打</td>
            </tr>
            
             <tr>
                <td class="export-td">1234</td>
                <td class="export-td">exhibit</td>
                <td class="export-td">英:/ɪg'zɪbɪt/ 美:/ɪɡ'zɪbɪt/ </td>
                <td class="export-td">1. vt. 显示；展览；提出（证据等）
2. n. 展览品；证据；展示会</td>
            </tr>
            
             <tr>
                <td class="export-td">1235</td>
                <td class="export-td">dustpan</td>
                <td class="export-td">英:/'dʌs(t)pæn/ 美:/'dʌstpæn/ </td>
                <td class="export-td">n. 簸箕</td>
            </tr>
            
             <tr>
                <td class="export-td">1236</td>
                <td class="export-td">gratitude</td>
                <td class="export-td">英:/'grætɪtjuːd/ 美:/'ɡrætɪtud/ </td>
                <td class="export-td">感恩之心</td>
            </tr>
            
             <tr>
                <td class="export-td">1237</td>
                <td class="export-td">exhibition</td>
                <td class="export-td">英:/eksɪ'bɪʃ(ə)n/ 美:/ˌɛksɪ'bɪʃən/ </td>
                <td class="export-td">展示, 展览</td>
            </tr>
            
             <tr>
                <td class="export-td">1238</td>
                <td class="export-td">bum</td>
                <td class="export-td">英:/bʌm/ 美:/bʌm/ </td>
                <td class="export-td">1. n. 流浪汉；狂欢作乐；能力差的人；嗡嗡声；屁股；[贬]执达员（等于bumbailiff）
2. vi. 流浪；靠乞讨过活；发嗡嗡声</td>
            </tr>
            
             <tr>
                <td class="export-td">1239</td>
                <td class="export-td">dried</td>
                <td class="export-td">英:/draɪd/ 美:/draɪd/ </td>
                <td class="export-td">1. adj. 弄干了的；干燥的
2. v. 使干（原形是dry）</td>
            </tr>
            
             <tr>
                <td class="export-td">1240</td>
                <td class="export-td">dark</td>
                <td class="export-td">英:/dɑːk/ 美:/dɑrk/ </td>
                <td class="export-td">1. adj. 黑暗的，深色的；无知的；模糊的；忧郁的
2. n. 黑暗；黄昏；模糊；夜</td>
            </tr>
            
             <tr>
                <td class="export-td">1241</td>
                <td class="export-td">charity</td>
                <td class="export-td">英:/'tʃærɪtɪ/ 美:/'tʃærəti/ </td>
                <td class="export-td">n. 施舍；慈善；慈善团体；施舍物；宽容</td>
            </tr>
            
             <tr>
                <td class="export-td">1242</td>
                <td class="export-td">bad-tempered</td>
                <td class="export-td">英:/'bæd,tempəd/ 美:/ bædˈtɛmpɚd/ </td>
                <td class="export-td">易怒的</td>
            </tr>
            
             <tr>
                <td class="export-td">1243</td>
                <td class="export-td">about</td>
                <td class="export-td">英:/ə'baʊt/ 美:/ə'baʊt/ </td>
                <td class="export-td">1. prep. 关于；大约
2. adj. 四处走动的；在起作用的；在附近的</td>
            </tr>
            
             <tr>
                <td class="export-td">1244</td>
                <td class="export-td">factory</td>
                <td class="export-td">英:/'fækt(ə)rɪ/ 美:/'fæktri/ </td>
                <td class="export-td">business, etc whose employees must be members of a specified trade union （只雇用工会会员的）工厂、企业等: [attrib 作定语] a closed-shop agreement 只雇用工会会员的劳资协议.<br /><br />n. 工厂；制造厂；代理店</td>
            </tr>
            
             <tr>
                <td class="export-td">1245</td>
                <td class="export-td">curse</td>
                <td class="export-td">英:/kɜːs/ 美:/kɝs/ </td>
                <td class="export-td">1. n. 咒骂；诅咒
2. vt. 诅咒；咒骂</td>
            </tr>
            
             <tr>
                <td class="export-td">1246</td>
                <td class="export-td">adolescence</td>
                <td class="export-td">英:/ædə'les(ə)ns/ 美:/ˌædə'lɛsns/ </td>
                <td class="export-td">n. 青春期</td>
            </tr>
            
             <tr>
                <td class="export-td">1247</td>
                <td class="export-td">bleak</td>
                <td class="export-td">英:/bliːk/ 美:/blik/ </td>
                <td class="export-td">adj. 荒凉的，无遮蔽的；阴冷的；黯淡的，无希望的；冷酷的；单调的</td>
            </tr>
            
             <tr>
                <td class="export-td">1248</td>
                <td class="export-td">garment</td>
                <td class="export-td">英:/'gɑːm(ə)nt/ 美:/'gɑrmənt/ </td>
                <td class="export-td">1. n. 衣服，服装；外表，外观
2. vt. 给…穿衣服</td>
            </tr>
            
             <tr>
                <td class="export-td">1249</td>
                <td class="export-td">duster</td>
                <td class="export-td">英:/'dʌstə/ 美:/'dʌstɚ/ </td>
                <td class="export-td">n. 抹布，掸子；打扫灰尘的人；除尘器</td>
            </tr>
            
             <tr>
                <td class="export-td">1250</td>
                <td class="export-td">cod</td>
                <td class="export-td">英:/kɒd/ 美:/kɑd/ </td>
                <td class="export-td">1. n. 鳕鱼；愚弄；哄骗
2. vi. 欺骗；愚弄</td>
            </tr>
            
             <tr>
                <td class="export-td">1251</td>
                <td class="export-td">darkness</td>
                <td class="export-td">英:/dɑrknɪs/ 美:/ˈd ɑ:knɪs/ </td>
                <td class="export-td">n. 黑暗；模糊；无知；阴郁</td>
            </tr>
            
             <tr>
                <td class="export-td">1252</td>
                <td class="export-td">adolescent</td>
                <td class="export-td">英:/ædə'les(ə)nt/ 美:/ˌædə'lɛsnt/ </td>
                <td class="export-td">青少年</td>
            </tr>
            
             <tr>
                <td class="export-td">1253</td>
                <td class="export-td">digit</td>
                <td class="export-td">英:/'dɪdʒɪt/ 美:/'dɪdʒɪt/ </td>
                <td class="export-td">n. 数字；手指或足趾；一指宽</td>
            </tr>
            
             <tr>
                <td class="export-td">1254</td>
                <td class="export-td">dusty</td>
                <td class="export-td">英:/'dʌstɪ/ 美:/'dʌsti/ </td>
                <td class="export-td">adj. 落满灰尘的</td>
            </tr>
            
             <tr>
                <td class="export-td">1255</td>
                <td class="export-td">appreciate</td>
                <td class="export-td">英:/ə'priːʃɪeɪt/ 美:/ə'priʃɪet/ </td>
                <td class="export-td">欣赏,感激,赏识</td>
            </tr>
            
             <tr>
                <td class="export-td">1256</td>
                <td class="export-td">drift</td>
                <td class="export-td">英:/drɪft/ 美:/drɪft/ </td>
                <td class="export-td">1. n. 漂流，漂移；漂流物；趋势
2. vi. 漂流，漂移；漂泊</td>
            </tr>
            
             <tr>
                <td class="export-td">1257</td>
                <td class="export-td">dolphin</td>
                <td class="export-td">英:/'dɒlfɪn/ 美:/'dɑlfɪn/ </td>
                <td class="export-td">n. 海豚</td>
            </tr>
            
             <tr>
                <td class="export-td">1258</td>
                <td class="export-td">above</td>
                <td class="export-td">英:/ə'bʌv/ 美:/ə'bʌv/ </td>
                <td class="export-td">1. prep. 在……上面；在……之上；超过
2. adv. 在上面；在上文</td>
            </tr>
            
             <tr>
                <td class="export-td">1259</td>
                <td class="export-td">grave</td>
                <td class="export-td">英:/greɪv/ 美:/ɡrev/ </td>
                <td class="export-td">1. adj. 严肃的；重大的；黯淡的
2. n. 墓穴，坟墓；死亡</td>
            </tr>
            
             <tr>
                <td class="export-td">1260</td>
                <td class="export-td">adopt</td>
                <td class="export-td">英:/ə'dɒpt/ 美:/ə'dɑpt/ </td>
                <td class="export-td">1. vt. 收养；采取；接受；正式通过
2. vi. 过继；采取</td>
            </tr>
            
             <tr>
                <td class="export-td">1261</td>
                <td class="export-td">badge</td>
                <td class="export-td">英:/bædʒ/ 美:/bædʒ/ </td>
                <td class="export-td">1. n. 徽章；标记；证章
2. vt. 授给…徽章</td>
            </tr>
            
             <tr>
                <td class="export-td">1262</td>
                <td class="export-td">baptize</td>
                <td class="export-td">英:/bæpˈtaɪz/ 美:/bæp'taɪz/ </td>
                <td class="export-td">baptise<br /><br />1. vt. 给…施浸礼；命名；使经受考验（等于baptise）
2. vi. 施行洗礼（等于baptise）</td>
            </tr>
            
             <tr>
                <td class="export-td">1263</td>
                <td class="export-td">digital</td>
                <td class="export-td">英:/'dɪdʒɪt(ə)l/ 美:/'dɪdʒɪtl/ </td>
                <td class="export-td">1. adj. 数字的；手指的
2. n. 数字；键</td>
            </tr>
            
             <tr>
                <td class="export-td">1264</td>
                <td class="export-td">gravestone</td>
                <td class="export-td">英:/'greɪvstəʊn/ 美:/'ɡrevston/ </td>
                <td class="export-td">墓碑</td>
            </tr>
            
             <tr>
                <td class="export-td">1265</td>
                <td class="export-td">badger</td>
                <td class="export-td">英:/'bædʒə/ 美:/'bædʒɚ/ </td>
                <td class="export-td">n. 獾；獾皮毛</td>
            </tr>
            
             <tr>
                <td class="export-td">1266</td>
                <td class="export-td">appreciation</td>
                <td class="export-td">英:/əpriːʃɪ'eɪʃ(ə)n/ 美:/ə,priʃɪ'eʃən/ </td>
                <td class="export-td">赏识, 鉴识, 感激</td>
            </tr>
            
             <tr>
                <td class="export-td">1267</td>
                <td class="export-td">bee</td>
                <td class="export-td">英:/biː/ 美:/bi/ </td>
                <td class="export-td">n. 蜜蜂，蜂；勤劳的人</td>
            </tr>
            
             <tr>
                <td class="export-td">1268</td>
                <td class="export-td">graveyard</td>
                <td class="export-td">英:/'greɪvjɑːd/ 美:/'ɡrevjɑrd/ </td>
                <td class="export-td">墓地，坟场</td>
            </tr>
            
             <tr>
                <td class="export-td">1269</td>
                <td class="export-td">enjoy</td>
                <td class="export-td">英:/ɪn'dʒɒɪ/ 美:/ɪn'dʒɔɪ/ </td>
                <td class="export-td">vt. 喜爱；欣赏，享受；使过得快活</td>
            </tr>
            
             <tr>
                <td class="export-td">1270</td>
                <td class="export-td">cursor</td>
                <td class="export-td">英:/ˈkɜ:sə/ 美:/'kɝsɚ/ </td>
                <td class="export-td">n. （计算尺的）游标，指针；[计]光标</td>
            </tr>
            
             <tr>
                <td class="export-td">1271</td>
                <td class="export-td">dignified</td>
                <td class="export-td">英:/'dɪgnɪfaɪd/ 美:/'dɪɡnɪfaɪd/ </td>
                <td class="export-td">端庄</td>
            </tr>
            
             <tr>
                <td class="export-td">1272</td>
                <td class="export-td">beehive</td>
                <td class="export-td">英:/'biːhaɪv/ 美:/'bihaɪv/ </td>
                <td class="export-td">n. 蜂窝；蜂箱</td>
            </tr>
            
             <tr>
                <td class="export-td">1273</td>
                <td class="export-td">enjoyable</td>
                <td class="export-td">英:/ɪn'dʒɒɪəb(ə)l/ 美:/ɪn'dʒɔɪəbl/ </td>
                <td class="export-td">有趣的, 愉快的</td>
            </tr>
            
             <tr>
                <td class="export-td">1274</td>
                <td class="export-td">bump</td>
                <td class="export-td">英:/bʌmp/ 美:/bʌmp/ </td>
                <td class="export-td">1. n. 肿块，隆起物；撞击
2. vi. 碰撞，撞击；颠簸而行</td>
            </tr>
            
             <tr>
                <td class="export-td">1275</td>
                <td class="export-td">charm</td>
                <td class="export-td">英:/tʃɑːm/ 美:/tʃɑrm/ </td>
                <td class="export-td">1. n. 魅力，吸引力；魔力
2. vt. 使陶醉；行魔法</td>
            </tr>
            
             <tr>
                <td class="export-td">1276</td>
                <td class="export-td">gravel</td>
                <td class="export-td">英:/'græv(ə)l/ 美:/'ɡrævl/ </td>
                <td class="export-td">1. n. 砂砾；碎石
2. vt. 用碎石铺；使船搁浅在沙滩上；使困惑</td>
            </tr>
            
             <tr>
                <td class="export-td">1277</td>
                <td class="export-td">badminton</td>
                <td class="export-td">英:/'bædmɪnt(ə)n/ 美:/'bædmɪntən/ </td>
                <td class="export-td">羽毛球</td>
            </tr>
            
             <tr>
                <td class="export-td">1278</td>
                <td class="export-td">dignity</td>
                <td class="export-td">英:/'dɪgnɪtɪ/ 美:/'dɪɡnəti/ </td>
                <td class="export-td">n. 尊严；高贵</td>
            </tr>
            
             <tr>
                <td class="export-td">1279</td>
                <td class="export-td">corner</td>
                <td class="export-td">英:/'kɔːnə/ 美:/'kɔrnɚ/ </td>
                <td class="export-td">1. n. 角落，拐角处；困境，窘境；地区，偏僻处
2. vi. 相交成角；囤积</td>
            </tr>
            
             <tr>
                <td class="export-td">1280</td>
                <td class="export-td">bumpy</td>
                <td class="export-td">英:/'bʌmpɪ/ 美:/'bʌmpi/ </td>
                <td class="export-td">adj. 崎岖不平的；颠簸的</td>
            </tr>
            
             <tr>
                <td class="export-td">1281</td>
                <td class="export-td">code</td>
                <td class="export-td">英:/kəʊd/ 美:/kod/ </td>
                <td class="export-td">1. n. 代码，密码；法典；编码
2. vt. 编码；制成法典</td>
            </tr>
            
             <tr>
                <td class="export-td">1282</td>
                <td class="export-td">hectare</td>
                <td class="export-td">英:/'hekteə/ 美:/'hɛktɛr/ </td>
                <td class="export-td">n. 公顷（等于1万平方米）</td>
            </tr>
            
             <tr>
                <td class="export-td">1283</td>
                <td class="export-td">adore</td>
                <td class="export-td">英:/ə'dɔː/ 美:/ə'dɔr/ </td>
                <td class="export-td">1. vt. 爱慕；崇拜；喜爱；[口]极喜欢
2. vi. 爱慕；崇拜</td>
            </tr>
            
             <tr>
                <td class="export-td">1284</td>
                <td class="export-td">bleed</td>
                <td class="export-td">英:/bliːd/ 美:/blid/ </td>
                <td class="export-td">1. vt. 使出血；榨取
2. vi. 流血；渗出；悲痛</td>
            </tr>
            
             <tr>
                <td class="export-td">1285</td>
                <td class="export-td">drill</td>
                <td class="export-td">英:/drɪl/ 美:/drɪl/ </td>
                <td class="export-td">1. n. 钻子；钻孔机；播种机；训练
2. vi. 钻孔；训练</td>
            </tr>
            
             <tr>
                <td class="export-td">1286</td>
                <td class="export-td">hectic</td>
                <td class="export-td">英:/'hektɪk/ 美:/'hɛktɪk/ </td>
                <td class="export-td">1. n. 脸红；患肺结核
2. adj. 脸上发红；兴奋的，狂热的；肺病的</td>
            </tr>
            
             <tr>
                <td class="export-td">1287</td>
                <td class="export-td">enjoyment</td>
                <td class="export-td">英:/ɪn'dʒɒɪmənt/ 美:/ɪn'dʒɔɪmənt/ </td>
                <td class="export-td">享受</td>
            </tr>
            
             <tr>
                <td class="export-td">1288</td>
                <td class="export-td">apprentice</td>
                <td class="export-td">英:/ə'prentɪs/ 美:/ə'prɛntɪs/ </td>
                <td class="export-td">学徒; 使当学徒</td>
            </tr>
            
             <tr>
                <td class="export-td">1289</td>
                <td class="export-td">dome</td>
                <td class="export-td">英:/dəʊm/ 美:/dom/ </td>
                <td class="export-td">1. n. 圆屋顶
2. vi. 成圆顶状</td>
            </tr>
            
             <tr>
                <td class="export-td">1290</td>
                <td class="export-td">abroad</td>
                <td class="export-td">英:/ə'brɔːd/ 美:/ə'brɔd/ </td>
                <td class="export-td">1. adv. 到海外；在国外
2. adj. 往国外的</td>
            </tr>
            
             <tr>
                <td class="export-td">1291</td>
                <td class="export-td">conference</td>
                <td class="export-td">英:/'kɒnf(ə)r(ə)ns/ 美:/'kɑnfərəns/ </td>
                <td class="export-td">会议</td>
            </tr>
            
             <tr>
                <td class="export-td">1292</td>
                <td class="export-td">darling</td>
                <td class="export-td">英:/'dɑːlɪŋ/ 美:/'dɑrlɪŋ/ </td>
                <td class="export-td">n. 心爱的人，亲爱的</td>
            </tr>
            
             <tr>
                <td class="export-td">1293</td>
                <td class="export-td">confess</td>
                <td class="export-td">英:/kən'fes/ 美:/kən'fɛs/ </td>
                <td class="export-td">1. vt. 承认；坦白；供认；忏悔
2. vi. 承认；坦白；供认；忏悔</td>
            </tr>
            
             <tr>
                <td class="export-td">1294</td>
                <td class="export-td">bumper</td>
                <td class="export-td">英:/'bʌmpə/ 美:/'bʌmpɚ/ </td>
                <td class="export-td">1. adj. 丰盛的，丰富的
2. n. 缓冲器</td>
            </tr>
            
             <tr>
                <td class="export-td">1295</td>
                <td class="export-td">breakdown</td>
                <td class="export-td">英:/'breɪkdaʊn/ 美:/'brek'daʊn/ </td>
                <td class="export-td">击穿</td>
            </tr>
            
             <tr>
                <td class="export-td">1296</td>
                <td class="export-td">clerk</td>
                <td class="export-td">英:/klɑːk/ 美:/klɝk/ </td>
                <td class="export-td">1. n. 职员，办事员；店员；书记；记帐员
2. vi. 当销售员，当店员</td>
            </tr>
            
             <tr>
                <td class="export-td">1297</td>
                <td class="export-td">abrupt</td>
                <td class="export-td">英:/ə'brʌpt/ 美:/ə'brʌpt/ </td>
                <td class="export-td">adj. 突然的；唐突的；陡峭的；生硬的</td>
            </tr>
            
             <tr>
                <td class="export-td">1298</td>
                <td class="export-td">clever</td>
                <td class="export-td">英:/'klevə/ 美:/'klɛvɚ/ </td>
                <td class="export-td">adj. 聪明的；机灵的；熟练的</td>
            </tr>
            
             <tr>
                <td class="export-td">1299</td>
                <td class="export-td">ally</td>
                <td class="export-td">英:/'ælaɪ/ 美:/ə'laɪ/ </td>
                <td class="export-td">1. n. 同盟国；同盟者；助手；伙伴
2. vt. 使联盟；使联合</td>
            </tr>
            
             <tr>
                <td class="export-td">1300</td>
                <td class="export-td">chart</td>
                <td class="export-td">英:/tʃɑːt/ 美:/tʃɑrt/ </td>
                <td class="export-td">1. n. 图表；海图；图纸
2. vt. 绘制…的图表；在海图上标出；详细计划</td>
            </tr>
            
             <tr>
                <td class="export-td">1301</td>
                <td class="export-td">domestic</td>
                <td class="export-td">英:/də'mestɪk/ 美:/də'mɛstɪk/ </td>
                <td class="export-td">1. adj. 国内的；家庭的；驯养的；一心只管家务的
2. n. 佣人；国货</td>
            </tr>
            
             <tr>
                <td class="export-td">1302</td>
                <td class="export-td">beef</td>
                <td class="export-td">英:/biːf/ 美:/bif/ </td>
                <td class="export-td">1. n. 牛肉；食用牛；肌肉；牢骚
2. vi. 抱怨，告发；发牢骚</td>
            </tr>
            
             <tr>
                <td class="export-td">1303</td>
                <td class="export-td">confession</td>
                <td class="export-td">英:/kən'feʃ(ə)n/ 美:/kən'fɛʃən/ </td>
                <td class="export-td">自认, 自白, 招供</td>
            </tr>
            
             <tr>
                <td class="export-td">1304</td>
                <td class="export-td">creep</td>
                <td class="export-td">英:/kriːp/ 美:/krip/ </td>
                <td class="export-td">1. vi. 爬行；慢慢地移动；起鸡皮疙瘩；蔓延
2. n. 爬行；毛骨悚然的感觉；谄媚者</td>
            </tr>
            
             <tr>
                <td class="export-td">1305</td>
                <td class="export-td">breakfast</td>
                <td class="export-td">英:/'brekfəst/ 美:/'brɛkfəst/ </td>
                <td class="export-td">早餐</td>
            </tr>
            
             <tr>
                <td class="export-td">1306</td>
                <td class="export-td">bag</td>
                <td class="export-td">英:/bæg/ 美:/bæɡ/ </td>
                <td class="export-td">1. n. 袋；猎获物；（俚）一瓶啤酒
2. vt. 猎获；把…装入袋中；[口]占据，私吞；使膨大</td>
            </tr>
            
             <tr>
                <td class="export-td">1307</td>
                <td class="export-td">curtain</td>
                <td class="export-td">英:/'kɜːt(ə)n/ 美:/'kɝtn/ </td>
                <td class="export-td">1. n. 窗帘；幕
2. vt. 遮蔽；装上门帘</td>
            </tr>
            
             <tr>
                <td class="export-td">1308</td>
                <td class="export-td">gas</td>
                <td class="export-td">英:/gæs/ 美:/ɡæs/ </td>
                <td class="export-td">1. n. 气体；汽油；毒气；瓦斯
2. vt. 毒（死）；加油</td>
            </tr>
            
             <tr>
                <td class="export-td">1309</td>
                <td class="export-td">drink</td>
                <td class="export-td">英:/drɪŋk/ 美:/drɪŋk/ </td>
                <td class="export-td">usu for people who are ill, made by boiling beef in water 牛肉汁（通常作病人进补用）.<br /><br />1. vt. 喝，饮；吸收；举杯庆贺
2. vi. 喝酒；饮水；干杯</td>
            </tr>
            
             <tr>
                <td class="export-td">1310</td>
                <td class="export-td">hedge</td>
                <td class="export-td">英:/hedʒ/ 美:/hɛdʒ/ </td>
                <td class="export-td">1. vt. 用树篱笆围住；避免作正面答复
2. vi. 用树篱围住；避免作正面答复</td>
            </tr>
            
             <tr>
                <td class="export-td">1311</td>
                <td class="export-td">frequent</td>
                <td class="export-td">英:/'friːkw(ə)nt/ 美:/'frikwənt/ </td>
                <td class="export-td">1. adj. 时常发生的；频繁的；惯常的
2. vt. 常到，常去；时常出入于</td>
            </tr>
            
             <tr>
                <td class="export-td">1312</td>
                <td class="export-td">beefburger</td>
                <td class="export-td">/'bɛdbɝɡɚ/ </td>
                <td class="export-td">n. 德式牛排,煎牛肉饼</td>
            </tr>
            
             <tr>
                <td class="export-td">1313</td>
                <td class="export-td">confessor</td>
                <td class="export-td">英:/kən'fesə/ 美:/kən'fɛsɚ/ </td>
                <td class="export-td">忏悔</td>
            </tr>
            
             <tr>
                <td class="export-td">1314</td>
                <td class="export-td">approach</td>
                <td class="export-td">英:/ə'prəʊtʃ/ 美:/ə'protʃ/ </td>
                <td class="export-td">1. n. 接近；方法；途径
2. vt. 接近；着手处理</td>
            </tr>
            
             <tr>
                <td class="export-td">1315</td>
                <td class="export-td">acknowledge</td>
                <td class="export-td">英:/ək'nɒlɪdʒ/ 美:/ək'nɑlɪdʒ/ </td>
                <td class="export-td">承认</td>
            </tr>
            
             <tr>
                <td class="export-td">1316</td>
                <td class="export-td">bagel</td>
                <td class="export-td">英:/'beɪg(ə)l/ 美:/'beɡl/ </td>
                <td class="export-td">n. 百吉饼（先蒸后烤的发面圈）；[俚]（体育比赛中）零蛋</td>
            </tr>
            
             <tr>
                <td class="export-td">1317</td>
                <td class="export-td">creepy</td>
                <td class="export-td">英:/'kriːpɪ/ 美:/'kripi/ </td>
                <td class="export-td">adj. 令人毛骨悚然的；爬行的</td>
            </tr>
            
             <tr>
                <td class="export-td">1318</td>
                <td class="export-td">dart</td>
                <td class="export-td">英:/dɑːt/ 美:/dɑrt/ </td>
                <td class="export-td">1. n. 镖；标枪；飞镖；猛冲
2. vi. 突进；猛冲；投掷</td>
            </tr>
            
             <tr>
                <td class="export-td">1319</td>
                <td class="export-td">bone</td>
                <td class="export-td">英:/bəʊn/ 美:/bon/ </td>
                <td class="export-td">1. n. 骨；骨骼；香烟；一首歌
2. vt. 剔去...的骨；施骨肥于</td>
            </tr>
            
             <tr>
                <td class="export-td">1320</td>
                <td class="export-td">good</td>
                <td class="export-td">英:/gʊd/ 美:/ɡʊd/ </td>
                <td class="export-td">1. adj. 愉快的；好的；虔诚的；优良的
2. n. 好处；慷慨的行为；善行</td>
            </tr>
            
             <tr>
                <td class="export-td">1321</td>
                <td class="export-td">duty</td>
                <td class="export-td">英:/'djuːtɪ/ 美:/'dʊti/ </td>
                <td class="export-td">n. 责任；职务；关税</td>
            </tr>
            
             <tr>
                <td class="export-td">1322</td>
                <td class="export-td">hedgehog</td>
                <td class="export-td">英:/'hedʒ(h)ɒg/ 美:/'hɛdʒhɔɡ/ </td>
                <td class="export-td">n. 刺猬</td>
            </tr>
            
             <tr>
                <td class="export-td">1323</td>
                <td class="export-td">gravity</td>
                <td class="export-td">英:/'grævɪtɪ/ 美:/'ɡrævəti/ </td>
                <td class="export-td">n. 重力，地心引力；庄严；严重性</td>
            </tr>
            
             <tr>
                <td class="export-td">1324</td>
                <td class="export-td">baggage</td>
                <td class="export-td">英:/'bægɪdʒ/ 美:/'bæɡɪdʒ/ </td>
                <td class="export-td">n. 辎重（军队的）；行李</td>
            </tr>
            
             <tr>
                <td class="export-td">1325</td>
                <td class="export-td">exile</td>
                <td class="export-td">英:/'eksaɪl/ 美:/'ɛksaɪl/ </td>
                <td class="export-td">1. n. 流放，充军；流犯；放逐，被放逐者
2. vt. 放逐，流放；使背井离乡</td>
            </tr>
            
             <tr>
                <td class="export-td">1326</td>
                <td class="export-td">absence</td>
                <td class="export-td">英:/'æbs(ə)ns/ 美:/'æbsns/ </td>
                <td class="export-td">n. 缺席；缺乏；没有；不注意</td>
            </tr>
            
             <tr>
                <td class="export-td">1327</td>
                <td class="export-td">gravy</td>
                <td class="export-td">英:/'greɪvɪ/ 美:/'ɡrevi/ </td>
                <td class="export-td">n. 肉汁；不法利润；轻易得来的钱</td>
            </tr>
            
             <tr>
                <td class="export-td">1328</td>
                <td class="export-td">exist</td>
                <td class="export-td">英:/ɪg'zɪst/ 美:/ɪɡ'zɪst/ </td>
                <td class="export-td">vi. 存在；生存；生活；继续存在</td>
            </tr>
            
             <tr>
                <td class="export-td">1329</td>
                <td class="export-td">blend</td>
                <td class="export-td">英:/blend/ 美:/blɛnd/ </td>
                <td class="export-td">1. vt. 混合
2. vi. 混合；协调</td>
            </tr>
            
             <tr>
                <td class="export-td">1330</td>
                <td class="export-td">bun</td>
                <td class="export-td">英:/bʌn/ 美:/bʌn/ </td>
                <td class="export-td">n. 小圆面包</td>
            </tr>
            
             <tr>
                <td class="export-td">1331</td>
                <td class="export-td">fresh</td>
                <td class="export-td">英:/freʃ/ 美:/frɛʃ/ </td>
                <td class="export-td">1. adj. 新鲜的；无经验的；淡水的；清新的
2. n. 泛滥；开始；新生</td>
            </tr>
            
             <tr>
                <td class="export-td">1332</td>
                <td class="export-td">been</td>
                <td class="export-td">英:/biːn/ 美:/'hæz 'bin/ </td>
                <td class="export-td">v. 是，有（be的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1333</td>
                <td class="export-td">absent</td>
                <td class="export-td">英:/'æbs(ə)nt/ 美:/æb'sɛnt/ </td>
                <td class="export-td">1. adj. 缺席的；缺少的；心不在焉的；茫然的
2. vt. 使缺席</td>
            </tr>
            
             <tr>
                <td class="export-td">1334</td>
                <td class="export-td">click</td>
                <td class="export-td">英:/klɪk/ 美:/klɪk/ </td>
                <td class="export-td">1. vt. 点击；使发咔哒声
2. vi. 作咔哒声</td>
            </tr>
            
             <tr>
                <td class="export-td">1335</td>
                <td class="export-td">existence</td>
                <td class="export-td">英:/ɪg'zɪst(ə)ns/ 美:/ɪɡ'zɪstəns/ </td>
                <td class="export-td">存在, 生存</td>
            </tr>
            
             <tr>
                <td class="export-td">1336</td>
                <td class="export-td">duvet</td>
                <td class="export-td">英:/ˈdu:vei/ 美:/'duve/ </td>
                <td class="export-td">n. 羽绒被（等于continental quilt）；羽绒衫（等于duvet jacket）；[植]绒毛状生长物</td>
            </tr>
            
             <tr>
                <td class="export-td">1337</td>
                <td class="export-td">dash</td>
                <td class="export-td">英:/dæʃ/ 美:/dæʃ/ </td>
                <td class="export-td">1. n. 破折号；冲撞
2. vt. 使…破灭；猛撞；泼溅</td>
            </tr>
            
             <tr>
                <td class="export-td">1338</td>
                <td class="export-td">client</td>
                <td class="export-td">英:/'klaɪənt/ 美:/'klaɪənt/ </td>
                <td class="export-td">n. 委托人；顾客；客户</td>
            </tr>
            
             <tr>
                <td class="export-td">1339</td>
                <td class="export-td">confidence</td>
                <td class="export-td">英:/'kɒnfɪd(ə)ns/ 美:/'kɑnfɪdəns/ </td>
                <td class="export-td">骗得信任的</td>
            </tr>
            
             <tr>
                <td class="export-td">1340</td>
                <td class="export-td">curve</td>
                <td class="export-td">英:/kɜːv/ 美:/kɝv/ </td>
                <td class="export-td">1. n. 曲线；弯曲；曲线球；曲线图表
2. vt. 使弯曲；弯</td>
            </tr>
            
             <tr>
                <td class="export-td">1341</td>
                <td class="export-td">bless</td>
                <td class="export-td">英:/bles/ 美:/blɛs/ </td>
                <td class="export-td">vt. 祝福；保佑；赞美</td>
            </tr>
            
             <tr>
                <td class="export-td">1342</td>
                <td class="export-td">dilemma</td>
                <td class="export-td">英:/dɪ'lemə/ 美:/dɪˈlɛmə/ </td>
                <td class="export-td">n. 困境；进退两难；[逻]两刀论法</td>
            </tr>
            
             <tr>
                <td class="export-td">1343</td>
                <td class="export-td">bunch</td>
                <td class="export-td">英:/bʌn(t)ʃ/ 美:/bʌntʃ/ </td>
                <td class="export-td">1. n. 串；群；突出物
2. vi. 隆起；打褶；形成一串</td>
            </tr>
            
             <tr>
                <td class="export-td">1344</td>
                <td class="export-td">dwarf</td>
                <td class="export-td">英:/dwɔːf/ 美:/dwɔrf/ </td>
                <td class="export-td">1. vi. 变矮小
2. n. 侏儒，矮子</td>
            </tr>
            
             <tr>
                <td class="export-td">1345</td>
                <td class="export-td">appropriate</td>
                <td class="export-td">英:/ə'prəʊprɪət/ 美:/ə'proprɪət/ </td>
                <td class="export-td">适当的, 相称的</td>
            </tr>
            
             <tr>
                <td class="export-td">1346</td>
                <td class="export-td">cliff</td>
                <td class="export-td">英:/klɪf/ 美:/klɪf/ </td>
                <td class="export-td">n. 绝壁；悬崖</td>
            </tr>
            
             <tr>
                <td class="export-td">1347</td>
                <td class="export-td">baggy</td>
                <td class="export-td">英:/'bægɪ/ 美:/'bæɡi/ </td>
                <td class="export-td">adj. 袋状的，膨胀的；宽松而下垂的</td>
            </tr>
            
             <tr>
                <td class="export-td">1348</td>
                <td class="export-td">acorn</td>
                <td class="export-td">英:/'eɪkɔːn/ 美:/'ekɔrn/ </td>
                <td class="export-td">n. 橡子；橡实</td>
            </tr>
            
             <tr>
                <td class="export-td">1349</td>
                <td class="export-td">cushion</td>
                <td class="export-td">英:/'kʊʃ(ə)n/ 美:/'kʊʃən/ </td>
                <td class="export-td">1. n. 垫子；起缓解作用之物；（猪等的）臀肉；银行储蓄
2. vt. 给…安上垫子；把…安置在垫子上；缓和…的冲击</td>
            </tr>
            
             <tr>
                <td class="export-td">1350</td>
                <td class="export-td">appropriately</td>
                <td class="export-td">/ə'prəupri,eitli/ </td>
                <td class="export-td">适当地</td>
            </tr>
            
             <tr>
                <td class="export-td">1351</td>
                <td class="export-td">beer</td>
                <td class="export-td">英:/bɪə/ 美:/bɪr/ </td>
                <td class="export-td">1. n. 啤酒
2. vi. 喝啤酒</td>
            </tr>
            
             <tr>
                <td class="export-td">1352</td>
                <td class="export-td">drip</td>
                <td class="export-td">英:/drɪp/ 美:/drɪp/ </td>
                <td class="export-td">1. vi. 滴下；充满；漏下
2. n. 水滴，滴水声；[医]静脉滴注；使人厌烦的人</td>
            </tr>
            
             <tr>
                <td class="export-td">1353</td>
                <td class="export-td">graze</td>
                <td class="export-td">英:/greɪz/ 美:/ɡrez/ </td>
                <td class="export-td">1. vt. 擦伤；放牧
2. vi. 吃草；擦伤</td>
            </tr>
            
             <tr>
                <td class="export-td">1354</td>
                <td class="export-td">almost</td>
                <td class="export-td">英:/'ɔːlməʊst/ 美:/'ɔlmost/ </td>
                <td class="export-td">adv. 差不多，几乎</td>
            </tr>
            
             <tr>
                <td class="export-td">1355</td>
                <td class="export-td">confident</td>
                <td class="export-td">英:/'kɒnfɪd(ə)nt/ 美:/'kɑnfɪdənt/ </td>
                <td class="export-td">确信的, 自信的</td>
            </tr>
            
             <tr>
                <td class="export-td">1356</td>
                <td class="export-td">bagpipes</td>
                <td class="export-td">/'bæɡpaɪps/ </td>
                <td class="export-td">(also. 风笛</td>
            </tr>
            
             <tr>
                <td class="export-td">1357</td>
                <td class="export-td">exit</td>
                <td class="export-td">英:/'eksɪt/ 美:/'ɛɡzɪt/ </td>
                <td class="export-td">1. n. 出口，通道；退场
2. vi. 退出；离去</td>
            </tr>
            
             <tr>
                <td class="export-td">1358</td>
                <td class="export-td">bungalow</td>
                <td class="export-td">英:/'bʌŋgələʊ/ 美:/'bʌŋɡəlo/ </td>
                <td class="export-td">n. 平房；小屋</td>
            </tr>
            
             <tr>
                <td class="export-td">1359</td>
                <td class="export-td">chase</td>
                <td class="export-td">英:/tʃeɪs/ 美:/tʃes/ </td>
                <td class="export-td">1. vt. 追逐；追捕；试图赢得；雕镂
2. vi. 追赶；追逐；奔跑</td>
            </tr>
            
             <tr>
                <td class="export-td">1360</td>
                <td class="export-td">approval</td>
                <td class="export-td">英:/ə'pruːv(ə)l/ 美:/ə'pruvl/ </td>
                <td class="export-td">n. 赞成；批准；认可</td>
            </tr>
            
             <tr>
                <td class="export-td">1361</td>
                <td class="export-td">dominate</td>
                <td class="export-td">英:/'dɒmɪneɪt/ 美:/'dɑmɪnet/ </td>
                <td class="export-td">1. vt. 支配；控制；占优势；在…中占主要地位
2. vi. 处于支配地位；占优势</td>
            </tr>
            
             <tr>
                <td class="export-td">1362</td>
                <td class="export-td">enormous</td>
                <td class="export-td">英:/ɪ'nɔːməs/ 美:/ɪ'nɔrməs/ </td>
                <td class="export-td">adj. 庞大的，巨大的；凶暴的，极恶的</td>
            </tr>
            
             <tr>
                <td class="export-td">1363</td>
                <td class="export-td">confidential</td>
                <td class="export-td">英:/kɒnfɪ'denʃ(ə)l/ 美:/ˌkɑnfɪ'dɛnʃl/ </td>
                <td class="export-td">机密</td>
            </tr>
            
             <tr>
                <td class="export-td">1364</td>
                <td class="export-td">dye</td>
                <td class="export-td">英:/daɪ/ 美:/daɪ/ </td>
                <td class="export-td">1. n. 染料；染色
2. vt. 染；把…染上颜色</td>
            </tr>
            
             <tr>
                <td class="export-td">1365</td>
                <td class="export-td">approve</td>
                <td class="export-td">英:/ə'pruːv/ 美:/ə'prʊv/ </td>
                <td class="export-td">1. vt. 批准；赞成；为…提供证据
2. vi. 批准；赞成；满意</td>
            </tr>
            
             <tr>
                <td class="export-td">1366</td>
                <td class="export-td">breath</td>
                <td class="export-td">英:/breθ/ 美:/brɛθ/ </td>
                <td class="export-td">n. 呼吸，气息；一口气，（呼吸的）一次；微风；瞬间，瞬息；迹象；[语]无声音，气音</td>
            </tr>
            
             <tr>
                <td class="export-td">1367</td>
                <td class="export-td">beetle</td>
                <td class="export-td">英:/'biːt(ə)l/ 美:/ˈbitl/ </td>
                <td class="export-td">1. vi. 急忙来回；突出
2. vt. 用槌打</td>
            </tr>
            
             <tr>
                <td class="export-td">1368</td>
                <td class="export-td">bonfire</td>
                <td class="export-td">英:/'bɒnfaɪə/ 美:/'bɑnfaɪɚ/ </td>
                <td class="export-td">n. 营火；篝火</td>
            </tr>
            
             <tr>
                <td class="export-td">1369</td>
                <td class="export-td">date</td>
                <td class="export-td">英:/deɪt/ 美:/det/ </td>
                <td class="export-td">1. n. 日期；约会；年代；枣椰子
2. vi. 注明日期；始于（某一历史时期）；过时</td>
            </tr>
            
             <tr>
                <td class="export-td">1370</td>
                <td class="export-td">enormously</td>
                <td class="export-td">英:/ɪˈn ɔ:məslɪ/ 美:/ɪ'nɔrməsli/ </td>
                <td class="export-td">极大</td>
            </tr>
            
             <tr>
                <td class="export-td">1371</td>
                <td class="export-td">custard</td>
                <td class="export-td">英:/'kʌstəd/ 美:/'kʌstɚd/ </td>
                <td class="export-td">n. 奶油冻；奶油蛋羹</td>
            </tr>
            
             <tr>
                <td class="export-td">1372</td>
                <td class="export-td">drive</td>
                <td class="export-td">英:/draɪv/ 美:/draɪv/ </td>
                <td class="export-td">1. vi. 开车；猛击；飞跑
2. vt. 驾驶（马车，汽车等）；驱赶；推动，发动（机器等）</td>
            </tr>
            
             <tr>
                <td class="export-td">1373</td>
                <td class="export-td">absolute</td>
                <td class="export-td">英:/'æbsəluːt/ 美:/'æbsəlut/ </td>
                <td class="export-td">1. adj. 绝对的；完全的；专制的
2. n. 绝对事物；绝对</td>
            </tr>
            
             <tr>
                <td class="export-td">1374</td>
                <td class="export-td">grease</td>
                <td class="export-td">英:/griːs/ 美:/gris/ </td>
                <td class="export-td">1. vt. 涂脂于；贿赂
2. n. 油脂；贿赂</td>
            </tr>
            
             <tr>
                <td class="export-td">1375</td>
                <td class="export-td">climatic</td>
                <td class="export-td">英:/klaɪˈmætɪk/ 美:/klaɪ'mætɪk/ </td>
                <td class="export-td">adj. 气候的；气候上的；由气候引起的；受气候影响的</td>
            </tr>
            
             <tr>
                <td class="export-td">1376</td>
                <td class="export-td">alone</td>
                <td class="export-td">英:/ə'ləʊn/ 美:/ə'lon/ </td>
                <td class="export-td">1. adj. 单独的；孤独的；独自的
2. adv. 独自地；单独地</td>
            </tr>
            
             <tr>
                <td class="export-td">1377</td>
                <td class="export-td">beetroot</td>
                <td class="export-td">英:/'biːtruːt/ 美:/'bitrut/ </td>
                <td class="export-td">n. 甜菜的根</td>
            </tr>
            
             <tr>
                <td class="export-td">1378</td>
                <td class="export-td">along</td>
                <td class="export-td">英:/ə'lɒŋ/ 美:/ə'lɔŋ/ </td>
                <td class="export-td">1. adv. 向前；一起；来到
2. prep. 沿着；顺着</td>
            </tr>
            
             <tr>
                <td class="export-td">1379</td>
                <td class="export-td">bunk</td>
                <td class="export-td">英:/bʌŋk/ 美:/bʌŋk/ </td>
                <td class="export-td">1. n. 铺位；座床；床铺
2. vi. 睡在铺上；逃跑</td>
            </tr>
            
             <tr>
                <td class="export-td">1380</td>
                <td class="export-td">dying</td>
                <td class="export-td">英:/'daɪɪŋ/ 美:/'daɪɪŋ/ </td>
                <td class="export-td">1. adj. 临终的，垂死的
2. n. 死，死亡</td>
            </tr>
            
             <tr>
                <td class="export-td">1381</td>
                <td class="export-td">acquaintance</td>
                <td class="export-td">英:/ə'kweɪnt(ə)ns/ 美:/ə'kwentəns/ </td>
                <td class="export-td">熟人,相识,了解</td>
            </tr>
            
             <tr>
                <td class="export-td">1382</td>
                <td class="export-td">heel</td>
                <td class="export-td">英:/hiːl/ 美:/hil/ </td>
                <td class="export-td">1. n. 脚后跟；踵
2. vt. 倾侧</td>
            </tr>
            
             <tr>
                <td class="export-td">1383</td>
                <td class="export-td">enough</td>
                <td class="export-td">英:/ɪ'nʌf/ 美:/ɪ'nʌf/ </td>
                <td class="export-td">1. adv. 足够地，充足地
2. n. 充足；很多</td>
            </tr>
            
             <tr>
                <td class="export-td">1384</td>
                <td class="export-td">corporation</td>
                <td class="export-td">英:/kɔːpə'reɪʃ(ə)n/ 美:/ˌkɔrpə'reʃən/ </td>
                <td class="export-td">公司, 法人, 集团</td>
            </tr>
            
             <tr>
                <td class="export-td">1385</td>
                <td class="export-td">domino</td>
                <td class="export-td">英:/'dɒmɪnəʊ/ 美:/'dɑməno/ </td>
                <td class="export-td">n. 多米诺骨牌；面具；化装外衣</td>
            </tr>
            
             <tr>
                <td class="export-td">1386</td>
                <td class="export-td">alongside</td>
                <td class="export-td">英:/əlɒŋ'saɪd/ 美:/ə'lɔŋ'saɪd/ </td>
                <td class="export-td">在旁边</td>
            </tr>
            
             <tr>
                <td class="export-td">1387</td>
                <td class="export-td">dilute</td>
                <td class="export-td">英:/daɪ'l(j)uːt/ 美:/dɪ'ljʊt/ </td>
                <td class="export-td">1. adj. 稀释的；淡的
2. vt. 稀释；冲淡；削弱</td>
            </tr>
            
             <tr>
                <td class="export-td">1388</td>
                <td class="export-td">breathe</td>
                <td class="export-td">英:/briːð/ 美:/brið/ </td>
                <td class="export-td">1. vi. 呼吸；低语；松口气；（风）轻拂
2. vt. 呼吸；流露；使喘息；低声说</td>
            </tr>
            
             <tr>
                <td class="export-td">1389</td>
                <td class="export-td">blew</td>
                <td class="export-td">英:/bluː/ 美:/blʊ/ </td>
                <td class="export-td">blow的过去式</td>
            </tr>
            
             <tr>
                <td class="export-td">1390</td>
                <td class="export-td">crept</td>
                <td class="export-td">英:/krept/ 美:/krɛpt/ </td>
                <td class="export-td">v. 匍匐爬行（creep的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">1391</td>
                <td class="export-td">greasy</td>
                <td class="export-td">英:/'griːsɪ/ 美:/'grisi/ </td>
                <td class="export-td">adj. 油腻的；含脂肪多的；谄媚的</td>
            </tr>
            
             <tr>
                <td class="export-td">1392</td>
                <td class="export-td">coffee</td>
                <td class="export-td">英:/'kɒfɪ/ 美:/'kɔfi/ </td>
                <td class="export-td">n. 咖啡；咖啡豆；咖啡色</td>
            </tr>
            
             <tr>
                <td class="export-td">1393</td>
                <td class="export-td">climax</td>
                <td class="export-td">英:/'klaɪmæks/ 美:/'klaɪmæks/ </td>
                <td class="export-td">n. 高潮；顶点；层进法；极点</td>
            </tr>
            
             <tr>
                <td class="export-td">1394</td>
                <td class="export-td">custom</td>
                <td class="export-td">英:/'kʌstəm/ 美:/'kʌstəm/ </td>
                <td class="export-td">1. n. 风俗；习惯；海关
2. adj. 定制的，定做的</td>
            </tr>
            
             <tr>
                <td class="export-td">1395</td>
                <td class="export-td">adult</td>
                <td class="export-td">英:/'ædʌlt/ 美:/'ædʌlt/ </td>
                <td class="export-td">成人</td>
            </tr>
            
             <tr>
                <td class="export-td">1396</td>
                <td class="export-td">aloud</td>
                <td class="export-td">英:/ə'laʊd/ 美:/ə'laʊd/ </td>
                <td class="export-td">adv. 大声地；出声地</td>
            </tr>
            
             <tr>
                <td class="export-td">1397</td>
                <td class="export-td">dim</td>
                <td class="export-td">英:/dɪm/ 美:/dɪm/ </td>
                <td class="export-td">1. adj. 模糊的，看不清的；暗淡的，昏暗的；悲观的，怀疑的
2. vt. 使暗淡，使失去光泽；使变模糊</td>
            </tr>
            
             <tr>
                <td class="export-td">1398</td>
                <td class="export-td">acquire</td>
                <td class="export-td">英:/ə'kwaɪə/ 美:/ə'kwaɪr/ </td>
                <td class="export-td">vt. 获得；学到；取得；捕获</td>
            </tr>
            
             <tr>
                <td class="export-td">1399</td>
                <td class="export-td">absolutely</td>
                <td class="export-td">英:/'æbsəlju:tli/ 美:/ˈæbsəˌlutli/ </td>
                <td class="export-td">绝对地,完全地</td>
            </tr>
            
             <tr>
                <td class="export-td">1400</td>
                <td class="export-td">climb</td>
                <td class="export-td">英:/klaɪm/ 美:/klaɪm/ </td>
                <td class="export-td">1. vi. 攀登；爬；上升
2. vt. 攀登；爬；上升</td>
            </tr>
            
             <tr>
                <td class="export-td">1401</td>
                <td class="export-td">goodbye</td>
                <td class="export-td">/gʊd'baɪ/ </td>
                <td class="export-td">int. 再见</td>
            </tr>
            
             <tr>
                <td class="export-td">1402</td>
                <td class="export-td">bunny</td>
                <td class="export-td">英:/'bʌnɪ/ 美:/'bʌni/ </td>
                <td class="export-td">n. 兔子（特别是小兔子）；可爱女郎</td>
            </tr>
            
             <tr>
                <td class="export-td">1403</td>
                <td class="export-td">crescent</td>
                <td class="export-td">英:/'kresənt/ 美:/'krɛsnt/ </td>
                <td class="export-td">1. n. 新月；新月状物；伊斯兰教的标记；土耳其的新月形国徽
2. adj. 新月形的；逐渐增加的</td>
            </tr>
            
             <tr>
                <td class="export-td">1404</td>
                <td class="export-td">great</td>
                <td class="export-td">英:/greɪt/ 美:/ɡret/ </td>
                <td class="export-td">1. adj. 伟大的，重大的；极好的，好的；主要的
2. n. 大人物；大师；伟人们</td>
            </tr>
            
             <tr>
                <td class="export-td">1405</td>
                <td class="export-td">confirm</td>
                <td class="export-td">英:/kən'fɜːm/ 美:/kən'fɝm/ </td>
                <td class="export-td">vt. 确认；批准；证实；确定；使巩固</td>
            </tr>
            
             <tr>
                <td class="export-td">1406</td>
                <td class="export-td">exotic</td>
                <td class="export-td">英:/ɪg'zɒtɪk/ 美:/ɪɡ'zɑtɪk/ </td>
                <td class="export-td">adj. 外来的；异国的；异国情调的</td>
            </tr>
            
             <tr>
                <td class="export-td">1407</td>
                <td class="export-td">breathless</td>
                <td class="export-td">英:/'breθlɪs/ 美:/'brɛθləs/ </td>
                <td class="export-td">喘不过气来的</td>
            </tr>
            
             <tr>
                <td class="export-td">1408</td>
                <td class="export-td">corpse</td>
                <td class="export-td">英:/kɔːps/ 美:/kɔrps/ </td>
                <td class="export-td">n. 尸体</td>
            </tr>
            
             <tr>
                <td class="export-td">1409</td>
                <td class="export-td">greatly</td>
                <td class="export-td">英:/ˈgreitli/ 美:/'ɡretli/ </td>
                <td class="export-td">adv. 非常；很，大大地</td>
            </tr>
            
             <tr>
                <td class="export-td">1410</td>
                <td class="export-td">expand</td>
                <td class="export-td">英:/ɪk'spænd/ 美:/ɪk'spænd/ </td>
                <td class="export-td">1. vt. 扩张；使膨胀；详述
2. vi. 张开，展开；发展</td>
            </tr>
            
             <tr>
                <td class="export-td">1411</td>
                <td class="export-td">dynamite</td>
                <td class="export-td">英:/'daɪnəmaɪt/ 美:/'daɪnə'maɪt/ </td>
                <td class="export-td">1. n. 炸药；具有潜在危险的人（或物）
2. vt. 炸毁</td>
            </tr>
            
             <tr>
                <td class="export-td">1412</td>
                <td class="export-td">chat</td>
                <td class="export-td">英:/tʃæt/ 美:/tʃæt/ </td>
                <td class="export-td">1. vi. 聊天；闲谈
2. vt. 与…搭讪；与…攀谈</td>
            </tr>
            
             <tr>
                <td class="export-td">1413</td>
                <td class="export-td">crest</td>
                <td class="export-td">英:/krest/ 美:/krɛst/ </td>
                <td class="export-td">1. n. 冠；山顶；顶饰；波峰
2. vi. 到达绝顶；形成浪峰</td>
            </tr>
            
             <tr>
                <td class="export-td">1414</td>
                <td class="export-td">donate</td>
                <td class="export-td">英:/də(ʊ)'neɪt/ 美:/'donet/ </td>
                <td class="export-td">1. vt. 捐赠；捐献
2. vi. 捐赠；捐献</td>
            </tr>
            
             <tr>
                <td class="export-td">1415</td>
                <td class="export-td">confirmation</td>
                <td class="export-td">英:/kɒnfə'meɪʃ(ə)n/ 美:/ˌkɑnfɚ'meʃən/ </td>
                <td class="export-td">确认</td>
            </tr>
            
             <tr>
                <td class="export-td">1416</td>
                <td class="export-td">driven</td>
                <td class="export-td">英:/'drɪvn/ 美:/'drɪvn/ </td>
                <td class="export-td">1. adj. 被动的，受到驱策的
2. v. 驾驶，开车（drive的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1417</td>
                <td class="export-td">buoy</td>
                <td class="export-td">英:/bɒɪ/ 美:/'bʊi/ </td>
                <td class="export-td">1. n. 浮标；浮筒；救生圈；航标
2. vt. 使浮起；支撑；鼓励</td>
            </tr>
            
             <tr>
                <td class="export-td">1418</td>
                <td class="export-td">height</td>
                <td class="export-td">英:/haɪt/ 美:/haɪt/ </td>
                <td class="export-td">n. 高度；高地；身高；顶点</td>
            </tr>
            
             <tr>
                <td class="export-td">1419</td>
                <td class="export-td">before</td>
                <td class="export-td">英:/bɪ'fɔː/ 美:/bɪ'fɔr/ </td>
                <td class="export-td">1. prep. 在…之前，先于
2. adv. 在前；以前</td>
            </tr>
            
             <tr>
                <td class="export-td">1420</td>
                <td class="export-td">absorb</td>
                <td class="export-td">英:/əb'sɔ:b/ 美:/əbˈsɔrb/ </td>
                <td class="export-td">vt. 吸收；吸引；承受；理解；使…全神贯注</td>
            </tr>
            
             <tr>
                <td class="export-td">1421</td>
                <td class="export-td">customer</td>
                <td class="export-td">英:/'kʌstəmə/ 美:/'kʌstəmɚ/ </td>
                <td class="export-td">n. 顾客；[口]家伙</td>
            </tr>
            
             <tr>
                <td class="export-td">1422</td>
                <td class="export-td">daughter</td>
                <td class="export-td">英:/'dɔːtə/ 美:/'dɔtɚ/ </td>
                <td class="export-td">1. n. 女儿；子代
2. adj. 女儿的；子代的</td>
            </tr>
            
             <tr>
                <td class="export-td">1423</td>
                <td class="export-td">done</td>
                <td class="export-td">英:/dʌn/ 美:/dʌn/ </td>
                <td class="export-td">1. adj. 做好了的；完成了；煮熟的；合乎礼仪的
2. v. 做（do 的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1424</td>
                <td class="export-td">beforehand</td>
                <td class="export-td">英:/bɪ'fɔːhænd/ 美:/bɪ'fɔrhænd/ </td>
                <td class="export-td">预先, 事先</td>
            </tr>
            
             <tr>
                <td class="export-td">1425</td>
                <td class="export-td">apricot</td>
                <td class="export-td">英:/'eɪprɪkɒt/ 美:/'æprɪkɑt/ </td>
                <td class="export-td">1. n. 杏树；杏，杏子；杏黄色
2. adj. 杏黄色的</td>
            </tr>
            
             <tr>
                <td class="export-td">1426</td>
                <td class="export-td">acre</td>
                <td class="export-td">英:/ˈɑ:krə/ 美:/ˈekɚ/ </td>
                <td class="export-td">n. 英亩；土地，地产</td>
            </tr>
            
             <tr>
                <td class="export-td">1427</td>
                <td class="export-td">April</td>
                <td class="export-td">英:/ˈeiprəl/ 美:/ˈeprəl/ </td>
                <td class="export-td">n. 四月</td>
            </tr>
            
             <tr>
                <td class="export-td">1428</td>
                <td class="export-td">absorbent</td>
                <td class="export-td">英:/əb'zɔːb(ə)nt/ 美:/əb'sɔrbənt/ </td>
                <td class="export-td">能吸收的</td>
            </tr>
            
             <tr>
                <td class="export-td">1429</td>
                <td class="export-td">blind</td>
                <td class="export-td">英:/blaɪnd/ 美:/blaɪnd/ </td>
                <td class="export-td">1. adj. 瞎的；盲目的
2. adv. 看不见地；盲目地</td>
            </tr>
            
             <tr>
                <td class="export-td">1430</td>
                <td class="export-td">donkey</td>
                <td class="export-td">英:/'dɒŋkɪ/ 美:/'dɔŋki/ </td>
                <td class="export-td">n. 驴子；傻瓜；顽固的人</td>
            </tr>
            
             <tr>
                <td class="export-td">1431</td>
                <td class="export-td">beg</td>
                <td class="export-td">英:/beg/ 美:/bɛɡ/ </td>
                <td class="export-td">1. vt. 恳求；乞讨；回避正题
2. vi. 请求；乞讨</td>
            </tr>
            
             <tr>
                <td class="export-td">1432</td>
                <td class="export-td">absorbing</td>
                <td class="export-td">英:/əb'zɔːbɪŋ/ 美:/əb'sɔrbɪŋ/ </td>
                <td class="export-td">吸收</td>
            </tr>
            
             <tr>
                <td class="export-td">1433</td>
                <td class="export-td">apron</td>
                <td class="export-td">英:/'eɪpr(ə)n/ 美:/'eprən/ </td>
                <td class="export-td">1. n. 围裙；停机坪；舞台口
2. vt. 着围裙于；围绕</td>
            </tr>
            
             <tr>
                <td class="export-td">1434</td>
                <td class="export-td">heir</td>
                <td class="export-td">英:/eə/ 美:/ɛr/ </td>
                <td class="export-td">n. 继承人；后嗣；嗣子</td>
            </tr>
            
             <tr>
                <td class="export-td">1435</td>
                <td class="export-td">cut</td>
                <td class="export-td">英:/kʌt/ 美:/kʌt/ </td>
                <td class="export-td">1. n. 伤口；切口；削减；（服装等的）式样；[体育]削球；切入
2. vt. 切割；削减；缩短；刺痛</td>
            </tr>
            
             <tr>
                <td class="export-td">1436</td>
                <td class="export-td">alphabet</td>
                <td class="export-td">英:/'ælfəbet/ 美:/'ælfə'bɛt/ </td>
                <td class="export-td">n. 字母表，字母系统；入门，初步</td>
            </tr>
            
             <tr>
                <td class="export-td">1437</td>
                <td class="export-td">alphabetical</td>
                <td class="export-td">英:/ælfə'betɪk(ə)l/ 美:/ˌælfə'bɛtɪkl/ </td>
                <td class="export-td">按字母表顺序的</td>
            </tr>
            
             <tr>
                <td class="export-td">1438</td>
                <td class="export-td">burden</td>
                <td class="export-td">英:/'bɜːd(ə)n/ 美:/'bɝdn/ </td>
                <td class="export-td">1. n. 负担；责任；船的载货量
2. vt. 烦扰；使负担；装货于</td>
            </tr>
            
             <tr>
                <td class="export-td">1439</td>
                <td class="export-td">friction</td>
                <td class="export-td">英:/'frɪkʃ(ə)n/ 美:/'frɪkʃən/ </td>
                <td class="export-td">n. 摩擦，摩擦力</td>
            </tr>
            
             <tr>
                <td class="export-td">1440</td>
                <td class="export-td">correct</td>
                <td class="export-td">英:/kə'rekt/ 美:/kə'rɛkt/ </td>
                <td class="export-td">1. vt. 改正；告诫
2. vi. 纠正错误；调整</td>
            </tr>
            
             <tr>
                <td class="export-td">1441</td>
                <td class="export-td">cling</td>
                <td class="export-td">英:/klɪŋ/ 美:/klɪŋ/ </td>
                <td class="export-td">vi. 坚持，墨守；紧贴；附着</td>
            </tr>
            
             <tr>
                <td class="export-td">1442</td>
                <td class="export-td">advance</td>
                <td class="export-td">英:/əd'vɑːns/ 美:/əd'væns/ </td>
                <td class="export-td">1. n. 前进；预付款；发展；增长
2. vt. 预付；提出；使……前进；将……提前</td>
            </tr>
            
             <tr>
                <td class="export-td">1443</td>
                <td class="export-td">chatter</td>
                <td class="export-td">英:/'tʃætə/ 美:/'tʃætɚ/ </td>
                <td class="export-td">1. vi. 唠叨；喋喋不休；（动物等）吱吱叫
2. vt. 喋喋不休地说；使卡嗒卡嗒作声</td>
            </tr>
            
             <tr>
                <td class="export-td">1444</td>
                <td class="export-td">Friday</td>
                <td class="export-td">英:/ˈfraidi/ 美:/ˈfraɪdi/ </td>
                <td class="export-td">n. 星期五</td>
            </tr>
            
             <tr>
                <td class="export-td">1445</td>
                <td class="export-td">beggar</td>
                <td class="export-td">英:/'begə/ 美:/'bɛɡɚ/ </td>
                <td class="export-td">1. n. 乞丐；穷人；[英口]家伙
2. vt. 使贫穷；使沦为乞丐</td>
            </tr>
            
             <tr>
                <td class="export-td">1446</td>
                <td class="export-td">fridge</td>
                <td class="export-td">英:/frɪdʒ/ 美:/frɪdʒ/ </td>
                <td class="export-td">n. 电冰箱</td>
            </tr>
            
             <tr>
                <td class="export-td">1447</td>
                <td class="export-td">gasp</td>
                <td class="export-td">英:/gɑːsp/ 美:/ɡæsp/ </td>
                <td class="export-td">1. vi. 喘息；喘气；渴望
2. vt. 气喘吁吁地说；喘着气说话</td>
            </tr>
            
             <tr>
                <td class="export-td">1448</td>
                <td class="export-td">crew</td>
                <td class="export-td">英:/kruː/ 美:/krʊ/ </td>
                <td class="export-td">1. n. 全体人员，全体船员；队，组
2. vi. 一起工作</td>
            </tr>
            
             <tr>
                <td class="export-td">1449</td>
                <td class="export-td">donor</td>
                <td class="export-td">英:/'dəʊnə/ 美:/'donɚ/ </td>
                <td class="export-td">1. n. 供者；捐赠者；赠送人
2. adj. 捐献的；经人工授精出生的</td>
            </tr>
            
             <tr>
                <td class="export-td">1450</td>
                <td class="export-td">book</td>
                <td class="export-td">英:/bʊk/ 美:/bʊk/ </td>
                <td class="export-td">1. n. 书籍；帐簿；卷；名册；工作簿
2. vt. 预订；登记</td>
            </tr>
            
             <tr>
                <td class="export-td">1451</td>
                <td class="export-td">advantage</td>
                <td class="export-td">英:/əd'vɑːntɪdʒ/ 美:/əd'væntɪdʒ/ </td>
                <td class="export-td">优势,有利条件</td>
            </tr>
            
             <tr>
                <td class="export-td">1452</td>
                <td class="export-td">acrobat</td>
                <td class="export-td">英:/'ækrəbæt/ 美:/'ækrəbæt/ </td>
                <td class="export-td">n. 杂技演员，特技演员；随机应变者；翻云覆雨者，善变者</td>
            </tr>
            
             <tr>
                <td class="export-td">1453</td>
                <td class="export-td">breed</td>
                <td class="export-td">英:/briːd/ 美:/brid/ </td>
                <td class="export-td">1. vi. 繁殖；饲养；产生
2. vt. 繁殖；饲养；养育，教育；引起</td>
            </tr>
            
             <tr>
                <td class="export-td">1454</td>
                <td class="export-td">doodle</td>
                <td class="export-td">英:/'duːd(ə)l/ 美:/'dudl/ </td>
                <td class="export-td">1. vi. 涂鸦；闲混；[美口]随意弹奏
2. n. 涂鸦；蠢人</td>
            </tr>
            
             <tr>
                <td class="export-td">1455</td>
                <td class="export-td">balance</td>
                <td class="export-td">英:/'bæl(ə)ns/ 美:/'bæləns/ </td>
                <td class="export-td">1. n. 平衡；匀称；余额
2. vt. 使平衡；结算；使相称</td>
            </tr>
            
             <tr>
                <td class="export-td">1456</td>
                <td class="export-td">correction</td>
                <td class="export-td">英:/kə'rekʃ(ə)n/ 美:/kə'rɛkʃən/ </td>
                <td class="export-td">更正</td>
            </tr>
            
             <tr>
                <td class="export-td">1457</td>
                <td class="export-td">bookcase</td>
                <td class="export-td">英:/'bʊkkeɪs/ 美:/'bʊkkes/ </td>
                <td class="export-td">n. 书柜，书架</td>
            </tr>
            
             <tr>
                <td class="export-td">1458</td>
                <td class="export-td">clinic</td>
                <td class="export-td">英:/'klɪnɪk/ 美:/'klɪnɪk/ </td>
                <td class="export-td">n. 诊所；临床</td>
            </tr>
            
             <tr>
                <td class="export-td">1459</td>
                <td class="export-td">already</td>
                <td class="export-td">英:/ɔːl'redɪ/ 美:/ɔl'rɛdi/ </td>
                <td class="export-td">adv. 已经，早已；先前</td>
            </tr>
            
             <tr>
                <td class="export-td">1460</td>
                <td class="export-td">corrective</td>
                <td class="export-td">英:/kə'rektɪv/ 美:/kə'rɛktɪv/ </td>
                <td class="export-td">纠正的</td>
            </tr>
            
             <tr>
                <td class="export-td">1461</td>
                <td class="export-td">doom</td>
                <td class="export-td">英:/duːm/ 美:/dʊm/ </td>
                <td class="export-td">1. n. 厄运；死亡；判决；[宗]世界末日
2. vt. 判决；注定；使失败</td>
            </tr>
            
             <tr>
                <td class="export-td">1462</td>
                <td class="export-td">begin</td>
                <td class="export-td">英:/bɪ'gɪn/ 美:/bɪ'ɡɪn/ </td>
                <td class="export-td">1. vt. 开始
2. vi. 开始；首先</td>
            </tr>
            
             <tr>
                <td class="export-td">1463</td>
                <td class="export-td">alright</td>
                <td class="export-td">英:/ɔːl'raɪt/ 美:/ɔlˈraɪt/ </td>
                <td class="export-td">1. adj. 没问题的
2. adv. 好吧（等于all right）</td>
            </tr>
            
             <tr>
                <td class="export-td">1464</td>
                <td class="export-td">friend</td>
                <td class="export-td">英:/frend/ 美:/frɛnd/ </td>
                <td class="export-td">n. 朋友；赞助者；助手</td>
            </tr>
            
             <tr>
                <td class="export-td">1465</td>
                <td class="export-td">beginner</td>
                <td class="export-td">英:/bɪ'gɪnə/ 美:/bɪ'gɪnɚ/ </td>
                <td class="export-td">n. 初学者；新手；创始人</td>
            </tr>
            
             <tr>
                <td class="export-td">1466</td>
                <td class="export-td">expect</td>
                <td class="export-td">英:/ɪk'spekt/ 美:/ɪk'spɛkt/ </td>
                <td class="export-td">1. vt. 预料；期望；指望；[口]认为
2. vi. 期待；预期</td>
            </tr>
            
             <tr>
                <td class="export-td">1467</td>
                <td class="export-td">held</td>
                <td class="export-td">英:/held/ 美:/hɛld/ </td>
                <td class="export-td">v. 握住（hold的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1468</td>
                <td class="export-td">also</td>
                <td class="export-td">英:/'ɔːlsəʊ/ 美:/'ɔlso/ </td>
                <td class="export-td">1. adv. 也；同样；而且
2. conj. 并且；另外</td>
            </tr>
            
             <tr>
                <td class="export-td">1469</td>
                <td class="export-td">breeze</td>
                <td class="export-td">英:/briːz/ 美:/briz/ </td>
                <td class="export-td">1. n. 微风；轻而易举的事；煤屑；焦炭渣；小风波
2. vi. 吹微风；逃走</td>
            </tr>
            
             <tr>
                <td class="export-td">1470</td>
                <td class="export-td">friendly</td>
                <td class="export-td">英:/'fren(d)lɪ/ 美:/'frɛndli/ </td>
                <td class="export-td">1. adj. 友好的；亲切的；支持的；融洽的，和睦的
2. adv. 温和地；友善地</td>
            </tr>
            
             <tr>
                <td class="export-td">1471</td>
                <td class="export-td">door</td>
                <td class="export-td">英:/dɔː/ 美:/dɔr/ </td>
                <td class="export-td">n. 门；家，户；门口；通道</td>
            </tr>
            
             <tr>
                <td class="export-td">1472</td>
                <td class="export-td">abstract</td>
                <td class="export-td">英:/'æbstrækt/ 美:/'æbstrækt/ </td>
                <td class="export-td">1. n. 抽象；摘要；抽象的概念
2. adj. 抽象的；深奥的</td>
            </tr>
            
             <tr>
                <td class="export-td">1473</td>
                <td class="export-td">balcony</td>
                <td class="export-td">英:/'bælkənɪ/ 美:/'bælkəni/ </td>
                <td class="export-td">n. 阳台；包厢；戏院楼厅</td>
            </tr>
            
             <tr>
                <td class="export-td">1474</td>
                <td class="export-td">din</td>
                <td class="export-td">英:/dɪn/ 美:/dɪn/ </td>
                <td class="export-td">1. vt. 喧闹，絮絮不休地说
2. vi. 喧闹，絮絮不休地说</td>
            </tr>
            
             <tr>
                <td class="export-td">1475</td>
                <td class="export-td">helicopter</td>
                <td class="export-td">英:/'helɪkɒptə/ 美:/'hɛlɪkɑptɚ/ </td>
                <td class="export-td">直升飞机</td>
            </tr>
            
             <tr>
                <td class="export-td">1476</td>
                <td class="export-td">correspond</td>
                <td class="export-td">英:/kɒrɪ'spɒnd/ 美:/ˌkɔrə'spɑnd/ </td>
                <td class="export-td">符合,通信,相当</td>
            </tr>
            
             <tr>
                <td class="export-td">1477</td>
                <td class="export-td">doorbell</td>
                <td class="export-td">英:/'dɔːbel/ 美:/'dɔrbɛl/ </td>
                <td class="export-td">n. 门铃</td>
            </tr>
            
             <tr>
                <td class="export-td">1478</td>
                <td class="export-td">greed</td>
                <td class="export-td">英:/griːd/ 美:/ɡrid/ </td>
                <td class="export-td">n. 贪婪，贪心</td>
            </tr>
            
             <tr>
                <td class="export-td">1479</td>
                <td class="export-td">burger</td>
                <td class="export-td">英:/'bə:ɡə/ 美:/ˈbɚɡɚ/ </td>
                <td class="export-td">n. 汉堡包（等于hamburger）</td>
            </tr>
            
             <tr>
                <td class="export-td">1480</td>
                <td class="export-td">across</td>
                <td class="export-td">英:/ə'krɒs/ 美:/ə'krɔs/ </td>
                <td class="export-td">1. prep. 穿过；横穿
2. adv. 在对面；横过</td>
            </tr>
            
             <tr>
                <td class="export-td">1481</td>
                <td class="export-td">dawn</td>
                <td class="export-td">英:/dɔːn/ 美:/dɔn/ </td>
                <td class="export-td">1. n. 黎明；开端
2. vt. 破晓；出现；被领悟</td>
            </tr>
            
             <tr>
                <td class="export-td">1482</td>
                <td class="export-td">greedy</td>
                <td class="export-td">英:/'griːdɪ/ 美:/'gridi/ </td>
                <td class="export-td">adj. 贪婪的；贪吃的；渴望的</td>
            </tr>
            
             <tr>
                <td class="export-td">1483</td>
                <td class="export-td">bald</td>
                <td class="export-td">英:/bɔːld/ 美:/bɔld/ </td>
                <td class="export-td">1. adj. 秃顶的；单调的；光秃的；无装饰的
2. vi. 变秃</td>
            </tr>
            
             <tr>
                <td class="export-td">1484</td>
                <td class="export-td">adventure</td>
                <td class="export-td">英:/əd'ventʃə/ 美:/əd'vɛntʃɚ/ </td>
                <td class="export-td">冒险,奇遇</td>
            </tr>
            
             <tr>
                <td class="export-td">1485</td>
                <td class="export-td">cheap</td>
                <td class="export-td">英:/tʃiːp/ 美:/tʃip/ </td>
                <td class="export-td">1. adj. 便宜的；[口]小气的；不值钱的
2. adv. 便宜地</td>
            </tr>
            
             <tr>
                <td class="export-td">1486</td>
                <td class="export-td">droop</td>
                <td class="export-td">英:/druːp/ 美:/drup/ </td>
                <td class="export-td">1. vi. 下垂；萎靡；凋萎
2. vt. 使…下垂</td>
            </tr>
            
             <tr>
                <td class="export-td">1487</td>
                <td class="export-td">correspondence</td>
                <td class="export-td">英:/kɒrɪ'spɒnd(ə)ns/ 美:/ˌkɔrə'spɑndəns/ </td>
                <td class="export-td">相符, 通信, 信件</td>
            </tr>
            
             <tr>
                <td class="export-td">1488</td>
                <td class="export-td">clip</td>
                <td class="export-td">英:/klɪp/ 美:/klɪp/ </td>
                <td class="export-td">1. vt. 修剪；夹牢；痛打
2. vi. 修剪</td>
            </tr>
            
             <tr>
                <td class="export-td">1489</td>
                <td class="export-td">confuse</td>
                <td class="export-td">英:/kən'fjuːz/ 美:/kən'fjʊz/ </td>
                <td class="export-td">vt. 使混乱；使困惑</td>
            </tr>
            
             <tr>
                <td class="export-td">1490</td>
                <td class="export-td">blindfold</td>
                <td class="export-td">英:/'blaɪn(d)fəʊld/ 美:/'blaɪndfold/ </td>
                <td class="export-td">蒙住...的眼睛</td>
            </tr>
            
             <tr>
                <td class="export-td">1491</td>
                <td class="export-td">cricket</td>
                <td class="export-td">英:/'krɪkɪt/ 美:/'krɪkɪt/ </td>
                <td class="export-td">n. 蟋蟀；板球，板球运动</td>
            </tr>
            
             <tr>
                <td class="export-td">1492</td>
                <td class="export-td">confused</td>
                <td class="export-td">英:/kənˈfju:zd/ 美:/kən'fjuzd/ </td>
                <td class="export-td">1. adj. 困惑的；混乱的；糊涂的
2. v. 困惑（confuse的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">1493</td>
                <td class="export-td">adventurous</td>
                <td class="export-td">英:/əd'ventʃ(ə)rəs/ 美:/əd'vɛntʃərəs/ </td>
                <td class="export-td">爱冒险的</td>
            </tr>
            
             <tr>
                <td class="export-td">1494</td>
                <td class="export-td">alter</td>
                <td class="export-td">英:/'ɔːltə/ 美:/ˈɔltɚ/ </td>
                <td class="export-td">1. vt. 改变，更改
2. vi. 改变；修改</td>
            </tr>
            
             <tr>
                <td class="export-td">1495</td>
                <td class="export-td">drop</td>
                <td class="export-td">英:/drɒp/ 美:/drɑp/ </td>
                <td class="export-td">1. vt. 滴；使降低；随口漏出；使终止
2. vi. 终止；下降</td>
            </tr>
            
             <tr>
                <td class="export-td">1496</td>
                <td class="export-td">confusedly</td>
                <td class="export-td">/kən'fju:zidli/ </td>
                <td class="export-td">稀里糊涂</td>
            </tr>
            
             <tr>
                <td class="export-td">1497</td>
                <td class="export-td">blink</td>
                <td class="export-td">英:/blɪŋk/ 美:/blɪŋk/ </td>
                <td class="export-td">1. vt. 眨眼；使…闪烁
2. vi. 眨眼；闪烁</td>
            </tr>
            
             <tr>
                <td class="export-td">1498</td>
                <td class="export-td">gate</td>
                <td class="export-td">英:/geɪt/ 美:/ɡet/ </td>
                <td class="export-td">1. n. 大门；出入口；门道
2. vt. 给…装大门</td>
            </tr>
            
             <tr>
                <td class="export-td">1499</td>
                <td class="export-td">friendship</td>
                <td class="export-td">英:/'fren(d)ʃɪp/ 美:/ˈfrɛndˌʃɪp/ </td>
                <td class="export-td">友谊, 友好</td>
            </tr>
            
             <tr>
                <td class="export-td">1500</td>
                <td class="export-td">act</td>
                <td class="export-td">英:/ækt/ 美:/ækt/ </td>
                <td class="export-td">1. vt. 扮演；装作，举动像
2. vi. 行动；扮演，充当；起作用，见效；假装，演戏；表现，举止</td>
            </tr>
            
             <tr>
                <td class="export-td">1501</td>
                <td class="export-td">day</td>
                <td class="export-td">英:/deɪ/ 美:/de/ </td>
                <td class="export-td">1. n. 一天；白昼；时期
2. adv. 每天；经常在白天地</td>
            </tr>
            
             <tr>
                <td class="export-td">1502</td>
                <td class="export-td">hell</td>
                <td class="export-td">英:/hel/ 美:/hɛl/ </td>
                <td class="export-td">1. n. 地狱；训斥；黑暗势力；究竟（作加强语气词）
2. vi. 过放荡生活；飞驰</td>
            </tr>
            
             <tr>
                <td class="export-td">1503</td>
                <td class="export-td">doorknob</td>
                <td class="export-td">英:/'dɔːnɒb/ 美:/'dɔrnɑb/ </td>
                <td class="export-td">n. 门把手</td>
            </tr>
            
             <tr>
                <td class="export-td">1504</td>
                <td class="export-td">green</td>
                <td class="export-td">英:/griːn/ 美:/ɡrin/ </td>
                <td class="export-td">1. adj. 绿色的；青春的
2. n. 绿色；青春</td>
            </tr>
            
             <tr>
                <td class="export-td">1505</td>
                <td class="export-td">enter</td>
                <td class="export-td">英:/'entə/ 美:/'ɛntɚ/ </td>
                <td class="export-td">1. vt. 进入；开始；参加
2. vi. 进去；[戏]参加，登场</td>
            </tr>
            
             <tr>
                <td class="export-td">1506</td>
                <td class="export-td">expectation</td>
                <td class="export-td">英:/ekspek'teɪʃ(ə)n/ 美:/ˌɛkspɛk'teʃən/ </td>
                <td class="export-td">期待,期望</td>
            </tr>
            
             <tr>
                <td class="export-td">1507</td>
                <td class="export-td">cried</td>
                <td class="export-td">/kraɪd/ </td>
                <td class="export-td">v. 哭泣；喊叫（cry的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1508</td>
                <td class="export-td">acting</td>
                <td class="export-td">英:/'æktɪŋ/ 美:/'æktɪŋ/ </td>
                <td class="export-td">1. adj. 代理的；装腔作势的
2. n. 演戏；演技；假装</td>
            </tr>
            
             <tr>
                <td class="export-td">1509</td>
                <td class="export-td">adverb</td>
                <td class="export-td">英:/'ædvɜːb/ 美:/'ædvɝb/ </td>
                <td class="export-td">1. n. 副词
2. adj. 副词的</td>
            </tr>
            
             <tr>
                <td class="export-td">1510</td>
                <td class="export-td">burglar</td>
                <td class="export-td">英:/'bɜːglə/ 美:/'bɝɡlɚ/ </td>
                <td class="export-td">n. 夜贼，窃贼</td>
            </tr>
            
             <tr>
                <td class="export-td">1511</td>
                <td class="export-td">action</td>
                <td class="export-td">英:/'ækʃ(ə)n/ 美:/'ækʃən/ </td>
                <td class="export-td">n. 行动；活动；功能；情节；战斗</td>
            </tr>
            
             <tr>
                <td class="export-td">1512</td>
                <td class="export-td">daybreak</td>
                <td class="export-td">英:/'deɪbreɪk/ 美:/'debrek/ </td>
                <td class="export-td">n. 破晓；黎明</td>
            </tr>
            
             <tr>
                <td class="export-td">1513</td>
                <td class="export-td">confusion</td>
                <td class="export-td">英:/kən'fjuːʒ(ə)n/ 美:/kən'fjʊʒən/ </td>
                <td class="export-td">混乱</td>
            </tr>
            
             <tr>
                <td class="export-td">1514</td>
                <td class="export-td">dinghy</td>
                <td class="export-td">英:/'dɪŋgɪ/ 美:/dɪŋi/ </td>
                <td class="export-td">n. 小艇；小船</td>
            </tr>
            
             <tr>
                <td class="export-td">1515</td>
                <td class="export-td">burglary</td>
                <td class="export-td">英:/'bɜːglərɪ/ 美:/'bɝɡləri/ </td>
                <td class="export-td">1. n. 盗窃，夜盗；盗窃行为
2. v. 入室行窃</td>
            </tr>
            
             <tr>
                <td class="export-td">1516</td>
                <td class="export-td">enterprise</td>
                <td class="export-td">英:/'entəpraɪz/ 美:/'ɛntɚ'praɪz/ </td>
                <td class="export-td">企业,企划,进取心</td>
            </tr>
            
             <tr>
                <td class="export-td">1517</td>
                <td class="export-td">alternate</td>
                <td class="export-td">英:/'ɔːltəneɪt/ 美:/'ɔltɚnət/ </td>
                <td class="export-td">备用</td>
            </tr>
            
             <tr>
                <td class="export-td">1518</td>
                <td class="export-td">doormat</td>
                <td class="export-td">英:/'dɔːmæt/ 美:/'dɔr'mæt/ </td>
                <td class="export-td">n. 门垫；擦鞋垫</td>
            </tr>
            
             <tr>
                <td class="export-td">1519</td>
                <td class="export-td">check</td>
                <td class="export-td">英:/tʃek/ 美:/tʃɛk/ </td>
                <td class="export-td">1. vi. 证明无误；核对无误；将军（象棋）
2. vt. 检查；寄存；制止</td>
            </tr>
            
             <tr>
                <td class="export-td">1520</td>
                <td class="export-td">crime</td>
                <td class="export-td">英:/kraɪm/ 美:/kraɪm/ </td>
                <td class="export-td">1. n. 罪行，犯罪；罪恶；犯罪活动
2. vt. 控告……违反纪律</td>
            </tr>
            
             <tr>
                <td class="export-td">1521</td>
                <td class="export-td">entertain</td>
                <td class="export-td">英:/entə'teɪn/ 美:/ˌɛntɚ'ten/ </td>
                <td class="export-td">娱乐</td>
            </tr>
            
             <tr>
                <td class="export-td">1522</td>
                <td class="export-td">criminal</td>
                <td class="export-td">英:/'krɪmɪn(ə)l/ 美:/'krɪmɪnl/ </td>
                <td class="export-td">1. n. 罪犯
2. adj. 犯罪的；刑事的；罪恶的</td>
            </tr>
            
             <tr>
                <td class="export-td">1523</td>
                <td class="export-td">frightened</td>
                <td class="export-td">/'fraitnd/ </td>
                <td class="export-td">受惊的, 受恐吓的</td>
            </tr>
            
             <tr>
                <td class="export-td">1524</td>
                <td class="export-td">entertainer</td>
                <td class="export-td">英:/entə'teɪnə/ 美:/'ɛntɚ'tenɚ/ </td>
                <td class="export-td">艺人</td>
            </tr>
            
             <tr>
                <td class="export-td">1525</td>
                <td class="export-td">expedition</td>
                <td class="export-td">英:/ekspɪ'dɪʃ(ə)n/ 美:/ˌɛkspə'dɪʃən/ </td>
                <td class="export-td">远征,探险队,迅速</td>
            </tr>
            
             <tr>
                <td class="export-td">1526</td>
                <td class="export-td">burgle</td>
                <td class="export-td">英:/'bɜːg(ə)l/ 美:/ˈbə..ɡəl/ </td>
                <td class="export-td">1. vt. 偷窃，破门盗窃
2. vi. 偷窃，破门盗窃</td>
            </tr>
            
             <tr>
                <td class="export-td">1527</td>
                <td class="export-td">begun</td>
                <td class="export-td">英:/bɪ'ɡʌn/ 美:/bɪ'ɡʌn/ </td>
                <td class="export-td">v. 开始（begin的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1528</td>
                <td class="export-td">entertaining</td>
                <td class="export-td">英:/entə'teɪnɪŋ/ 美:/ˌɛntɚ'tenɪŋ/ </td>
                <td class="export-td">娱乐</td>
            </tr>
            
             <tr>
                <td class="export-td">1529</td>
                <td class="export-td">cutlery</td>
                <td class="export-td">英:/'kʌtlərɪ/ 美:/'kʌtləri/ </td>
                <td class="export-td">n. 餐具；刀剑制造业</td>
            </tr>
            
             <tr>
                <td class="export-td">1530</td>
                <td class="export-td">alternator</td>
                <td class="export-td">英:/'ɔːltəneɪtə/ 美:/'ɔltɚnetɚ/ </td>
                <td class="export-td">交流发电机</td>
            </tr>
            
             <tr>
                <td class="export-td">1531</td>
                <td class="export-td">activate</td>
                <td class="export-td">英:/'æktɪveɪt/ 美:/'æktə'vet/ </td>
                <td class="export-td">1. vt. 刺激；使活泼；使活动；使产生放射性
2. vi. 有活力；激活</td>
            </tr>
            
             <tr>
                <td class="export-td">1532</td>
                <td class="export-td">frightening</td>
                <td class="export-td">英:/ˈfraɪtnɪŋ/ 美:/'fraɪtnɪŋ/ </td>
                <td class="export-td">可怕</td>
            </tr>
            
             <tr>
                <td class="export-td">1533</td>
                <td class="export-td">advert</td>
                <td class="export-td">英:/'ædvɜːt/ 美:/'ædvɝt/ </td>
                <td class="export-td">1. vi. 注意；谈到
2. n. 广告</td>
            </tr>
            
             <tr>
                <td class="export-td">1534</td>
                <td class="export-td">blister</td>
                <td class="export-td">英:/'blɪstə/ 美:/'blɪstɚ/ </td>
                <td class="export-td">1. n. 水疱；水泡；气泡；砂眼；起泡剂
2. vt. 使起水泡；痛打；猛烈抨击</td>
            </tr>
            
             <tr>
                <td class="export-td">1535</td>
                <td class="export-td">gateway</td>
                <td class="export-td">英:/'geɪtweɪ/ 美:/'ɡetwe/ </td>
                <td class="export-td">n. [计]网关；门；通道；方法；途径</td>
            </tr>
            
             <tr>
                <td class="export-td">1536</td>
                <td class="export-td">brewery</td>
                <td class="export-td">英:/'brʊərɪ/ 美:/'bruəri/ </td>
                <td class="export-td">n. 啤酒厂</td>
            </tr>
            
             <tr>
                <td class="export-td">1537</td>
                <td class="export-td">booking</td>
                <td class="export-td">英:/'bʊkɪŋ/ 美:/'bʊkɪŋ/ </td>
                <td class="export-td">n. 预订；预约；演出契约</td>
            </tr>
            
             <tr>
                <td class="export-td">1538</td>
                <td class="export-td">behave</td>
                <td class="export-td">英:/bɪ'heɪv/ 美:/bɪ'hev/ </td>
                <td class="export-td">1. vi. 表现；举止端正；（机器等）运转；（事物）起某种作用
2. vt. 使守规矩；使表现得…</td>
            </tr>
            
             <tr>
                <td class="export-td">1539</td>
                <td class="export-td">entertainment</td>
                <td class="export-td">英:/entə'teɪnm(ə)nt/ 美:/'ɛntɚ'tenmənt/ </td>
                <td class="export-td">n. 款待, 请客; 娱乐, 文娱节目, 表演会</td>
            </tr>
            
             <tr>
                <td class="export-td">1540</td>
                <td class="export-td">advertise</td>
                <td class="export-td">英:/'ædvətaɪz/ 美:/'ædvɚtaɪz/ </td>
                <td class="export-td">登广告</td>
            </tr>
            
             <tr>
                <td class="export-td">1541</td>
                <td class="export-td">burial</td>
                <td class="export-td">英:/'berɪəl/ 美:/'bɛrɪəl/ </td>
                <td class="export-td">1. n. 埋葬；葬礼；弃绝
2. adj. 埋葬的</td>
            </tr>
            
             <tr>
                <td class="export-td">1542</td>
                <td class="export-td">hello</td>
                <td class="export-td">英:/hə'ləʊ/ 美:/hə'lo/ </td>
                <td class="export-td">1. int. 喂；哈罗
2. n. 表示问候， 惊奇或唤起注意时的用语</td>
            </tr>
            
             <tr>
                <td class="export-td">1543</td>
                <td class="export-td">doorstep</td>
                <td class="export-td">英:/'dɔːstep/ 美:/ˈdɔrˌstɛp/ </td>
                <td class="export-td">n. 门阶</td>
            </tr>
            
             <tr>
                <td class="export-td">1544</td>
                <td class="export-td">cloak</td>
                <td class="export-td">英:/kləʊk/ 美:/klok/ </td>
                <td class="export-td">1. n. 斗蓬；宽大外衣；托词
2. vt. 遮掩；隐匿</td>
            </tr>
            
             <tr>
                <td class="export-td">1545</td>
                <td class="export-td">alternative</td>
                <td class="export-td">英:/ɔːl'tɜːnətɪv/ 美:/ɔl'tɝnətɪv/ </td>
                <td class="export-td">两者择一的</td>
            </tr>
            
             <tr>
                <td class="export-td">1546</td>
                <td class="export-td">gather</td>
                <td class="export-td">英:/'gæðə/ 美:/'ɡæðɚ/ </td>
                <td class="export-td">1. vt. 收集；使…聚集；收割；使…皱起
2. vi. 聚集；化脓；皱起</td>
            </tr>
            
             <tr>
                <td class="export-td">1547</td>
                <td class="export-td">chose</td>
                <td class="export-td">英:/tʃəʊz/ 美:/tʃoz/ </td>
                <td class="export-td">chosen<br /><br />n. 选择（choose 的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">1548</td>
                <td class="export-td">expel</td>
                <td class="export-td">英:/ɪk'spel/ 美:/ɪk'spɛl/ </td>
                <td class="export-td">vt. 驱逐；开除</td>
            </tr>
            
             <tr>
                <td class="export-td">1549</td>
                <td class="export-td">alternatively</td>
                <td class="export-td">/ɔl'tɝnətɪvli/ </td>
                <td class="export-td">或者</td>
            </tr>
            
             <tr>
                <td class="export-td">1550</td>
                <td class="export-td">dinner</td>
                <td class="export-td">英:/'dɪnə/ 美:/'dɪnɚ/ </td>
                <td class="export-td">n. 宴会；正餐；晚餐，晚宴</td>
            </tr>
            
             <tr>
                <td class="export-td">1551</td>
                <td class="export-td">drought</td>
                <td class="export-td">英:/draʊt/ 美:/draʊt/ </td>
                <td class="export-td">n. 干旱；缺乏</td>
            </tr>
            
             <tr>
                <td class="export-td">1552</td>
                <td class="export-td">doorway</td>
                <td class="export-td">英:/'dɔːweɪ/ 美:/'dɔr'we/ </td>
                <td class="export-td">n. 门口；途径</td>
            </tr>
            
             <tr>
                <td class="export-td">1553</td>
                <td class="export-td">gathering</td>
                <td class="export-td">英:/'gæð(ə)rɪŋ/ 美:/'ɡæðərɪŋ/ </td>
                <td class="export-td">集会, 聚集</td>
            </tr>
            
             <tr>
                <td class="export-td">1554</td>
                <td class="export-td">drove</td>
                <td class="export-td">英:/drəʊv/ 美:/drov/ </td>
                <td class="export-td">1. n. 畜群；牛群、羊群等；移动的人群或大批的东西
2. v. 驾驶（drive的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1555</td>
                <td class="export-td">advertising</td>
                <td class="export-td">英:/'ædvətaɪzɪŋ/ 美:/'ædvɚ'taɪzɪŋ/ </td>
                <td class="export-td">广告业,广告</td>
            </tr>
            
             <tr>
                <td class="export-td">1556</td>
                <td class="export-td">although</td>
                <td class="export-td">英:/ɔːl'ðəʊ/ 美:/ɔl'ðo/ </td>
                <td class="export-td">conj. 虽然，尽管</td>
            </tr>
            
             <tr>
                <td class="export-td">1557</td>
                <td class="export-td">dinosaur</td>
                <td class="export-td">英:/'daɪnəsɔː/ 美:/'daɪnə'sɔr/ </td>
                <td class="export-td">n. [俚]过时、落伍的人或事物；恐龙</td>
            </tr>
            
             <tr>
                <td class="export-td">1558</td>
                <td class="export-td">crimson</td>
                <td class="export-td">英:/'krɪmz(ə)n/ 美:/'krɪmzn/ </td>
                <td class="export-td">1. n. 深红色
2. adj. 深红色的</td>
            </tr>
            
             <tr>
                <td class="export-td">1559</td>
                <td class="export-td">bribe</td>
                <td class="export-td">英:/braɪb/ 美:/braɪb/ </td>
                <td class="export-td">1. vt. 贿赂，收买
2. vi. 行贿</td>
            </tr>
            
             <tr>
                <td class="export-td">1560</td>
                <td class="export-td">greengrocer</td>
                <td class="export-td">英:/'griːngrəʊsə/ 美:/'ɡrinɡrosɚ/ </td>
                <td class="export-td">蔬菜水果商, 菜贩</td>
            </tr>
            
             <tr>
                <td class="export-td">1561</td>
                <td class="export-td">advice</td>
                <td class="export-td">英:/əd'vaɪs/ 美:/əd'vaɪs/ </td>
                <td class="export-td">n. 通知；忠告；建议；劝告</td>
            </tr>
            
             <tr>
                <td class="export-td">1562</td>
                <td class="export-td">expense</td>
                <td class="export-td">英:/ɪk'spens/ 美:/ɪk'spɛns/ </td>
                <td class="export-td">1. n. 开支；消费；损失，代价
2. vt. 向…收取费用</td>
            </tr>
            
             <tr>
                <td class="export-td">1563</td>
                <td class="export-td">drown</td>
                <td class="export-td">英:/draʊn/ 美:/draʊn/ </td>
                <td class="export-td">1. vt. 淹没；把…淹死
2. vi. 淹死；溺死</td>
            </tr>
            
             <tr>
                <td class="export-td">1564</td>
                <td class="export-td">activity</td>
                <td class="export-td">英:/æk'tɪvɪtɪ/ 美:/æk'tɪvəti/ </td>
                <td class="export-td">n. 活动；活跃；行动</td>
            </tr>
            
             <tr>
                <td class="export-td">1565</td>
                <td class="export-td">brick</td>
                <td class="export-td">英:/brɪk/ 美:/brɪk/ </td>
                <td class="export-td">1. n. 砖，砖块；砖形物；[口]心肠好的人
2. vt. 用砖砌</td>
            </tr>
            
             <tr>
                <td class="export-td">1566</td>
                <td class="export-td">frill</td>
                <td class="export-td">英:/frɪl/ 美:/frɪl/ </td>
                <td class="export-td">1. n. 褶边；装饰
2. vt. 折成皱边</td>
            </tr>
            
             <tr>
                <td class="export-td">1567</td>
                <td class="export-td">greenhouse</td>
                <td class="export-td">英:/'griːnhaʊs/ 美:/'ɡrinhaʊs/ </td>
                <td class="export-td">温室, 暖房</td>
            </tr>
            
             <tr>
                <td class="export-td">1568</td>
                <td class="export-td">boom</td>
                <td class="export-td">英:/buːm/ 美:/bʊm/ </td>
                <td class="export-td">1. vt. 发隆隆声；使兴旺
2. vi. 发隆隆声；急速发展</td>
            </tr>
            
             <tr>
                <td class="export-td">1569</td>
                <td class="export-td">clock</td>
                <td class="export-td">英:/klɒk/ 美:/klɑk/ </td>
                <td class="export-td">1. n. 时钟；计时器
2. vt. 记录；记时</td>
            </tr>
            
             <tr>
                <td class="export-td">1570</td>
                <td class="export-td">blizzard</td>
                <td class="export-td">英:/'blɪzəd/ 美:/'blɪzɚd/ </td>
                <td class="export-td">1. n. 暴风雪，大风雪；[俚]大打击
2. vi. 下暴风雪</td>
            </tr>
            
             <tr>
                <td class="export-td">1571</td>
                <td class="export-td">burn</td>
                <td class="export-td">英:/bɜːn/ 美:/bɝn/ </td>
                <td class="export-td">1. vt. 燃烧；烧毁，灼伤；激起…的愤怒
2. vi. 燃烧；烧毁；发热</td>
            </tr>
            
             <tr>
                <td class="export-td">1572</td>
                <td class="export-td">checkbook</td>
                <td class="export-td">英:/'tʃekbuk/ 美:/ˈtʃɛkˌbʊk/ </td>
                <td class="export-td">支票簿</td>
            </tr>
            
             <tr>
                <td class="export-td">1573</td>
                <td class="export-td">daytime</td>
                <td class="export-td">英:/'deɪtaɪm/ 美:/'detaɪm/ </td>
                <td class="export-td">n. 日间，白天</td>
            </tr>
            
             <tr>
                <td class="export-td">1574</td>
                <td class="export-td">helmet</td>
                <td class="export-td">英:/'helmɪt/ 美:/'hɛlmɪt/ </td>
                <td class="export-td">n. 钢盔，头盔</td>
            </tr>
            
             <tr>
                <td class="export-td">1575</td>
                <td class="export-td">clockwise</td>
                <td class="export-td">英:/'klɒkwaɪz/ 美:/'klɑk'waɪz/ </td>
                <td class="export-td">顺时针方向的</td>
            </tr>
            
             <tr>
                <td class="export-td">1576</td>
                <td class="export-td">expensive</td>
                <td class="export-td">英:/ɪk'spensɪv/ 美:/ɪk'spɛnsɪv/ </td>
                <td class="export-td">昂贵的,豪华的</td>
            </tr>
            
             <tr>
                <td class="export-td">1577</td>
                <td class="export-td">actress</td>
                <td class="export-td">英:/'æktrɪs/ 美:/'æktrəs/ </td>
                <td class="export-td">n. 女演员</td>
            </tr>
            
             <tr>
                <td class="export-td">1578</td>
                <td class="export-td">enthusiasm</td>
                <td class="export-td">英:/ɪn'θjuːzɪæz(ə)m/ 美:/ɪn'θuzɪæzəm/ </td>
                <td class="export-td">热情,热心</td>
            </tr>
            
             <tr>
                <td class="export-td">1579</td>
                <td class="export-td">checked</td>
                <td class="export-td">英:/tʃekt/ 美:/tʃɛkt/ </td>
                <td class="export-td">1. adj. 选中的；格子花纹的
2. v. 检查（check的过去式和过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1580</td>
                <td class="export-td">congratulate</td>
                <td class="export-td">英:/kən'grætjʊleɪt/ 美:/kən'ɡrætʃulet/ </td>
                <td class="export-td">祝贺</td>
            </tr>
            
             <tr>
                <td class="export-td">1581</td>
                <td class="export-td">ballerina</td>
                <td class="export-td">英:/bælə'riːnə/ 美:/ˌbælə'rinə/ </td>
                <td class="export-td">芭蕾舞女演员</td>
            </tr>
            
             <tr>
                <td class="export-td">1582</td>
                <td class="export-td">advise</td>
                <td class="export-td">英:/əd'vaɪz/ 美:/əd'vaɪz/ </td>
                <td class="export-td">1. vt. 劝告，忠告；通知；警告；建议
2. vi. 建议；与…商量</td>
            </tr>
            
             <tr>
                <td class="export-td">1583</td>
                <td class="export-td">altogether</td>
                <td class="export-td">英:/ɔːltə'geðə/ 美:/ˌɔltə'ɡɛðɚ/ </td>
                <td class="export-td">总共，完全</td>
            </tr>
            
             <tr>
                <td class="export-td">1584</td>
                <td class="export-td">drowsy</td>
                <td class="export-td">英:/'draʊzɪ/ 美:/'draʊzi/ </td>
                <td class="export-td">adj. 昏昏欲睡的；沉寂的；催眠的</td>
            </tr>
            
             <tr>
                <td class="export-td">1585</td>
                <td class="export-td">actual</td>
                <td class="export-td">英:/'æktʃʊəl/ 美:/'æktʃuəl/ </td>
                <td class="export-td">adj. 真实的，实际的；现行的，目前的</td>
            </tr>
            
             <tr>
                <td class="export-td">1586</td>
                <td class="export-td">daylight</td>
                <td class="export-td">英:/'deɪlaɪt/ 美:/'delaɪt/ </td>
                <td class="export-td">n. 日光；白天；黎明；公开</td>
            </tr>
            
             <tr>
                <td class="export-td">1587</td>
                <td class="export-td">help</td>
                <td class="export-td">英:/help/ 美:/hɛlp/ </td>
                <td class="export-td">1. vt. 帮助；治疗；促进；补救
2. n. 帮助；帮忙者；补救办法；有益的东西</td>
            </tr>
            
             <tr>
                <td class="export-td">1588</td>
                <td class="export-td">dormitory</td>
                <td class="export-td">英:/'dɔːmɪt(ə)rɪ/ 美:/'dɔrmətɔri/ </td>
                <td class="export-td">集体宿舍</td>
            </tr>
            
             <tr>
                <td class="export-td">1589</td>
                <td class="export-td">cv</td>
                <td class="export-td">/ˌsi: 'vi:/ </td>
                <td class="export-td">履历</td>
            </tr>
            
             <tr>
                <td class="export-td">1590</td>
                <td class="export-td">experience</td>
                <td class="export-td">英:/ɪk'spɪərɪəns/ 美:/ɪk'spɪrɪəns/ </td>
                <td class="export-td">经历, 经验</td>
            </tr>
            
             <tr>
                <td class="export-td">1591</td>
                <td class="export-td">actually</td>
                <td class="export-td">英:/'æktjʊəlɪ/ 美:/'æktʃuəli/ </td>
                <td class="export-td">adv. 实际上；事实上</td>
            </tr>
            
             <tr>
                <td class="export-td">1592</td>
                <td class="export-td">fringe</td>
                <td class="export-td">英:/frɪn(d)ʒ/ 美:/frɪndʒ/ </td>
                <td class="export-td">1. n. 边缘；穗；刘海
2. adj. 边缘的；附加的</td>
            </tr>
            
             <tr>
                <td class="export-td">1593</td>
                <td class="export-td">behind</td>
                <td class="export-td">英:/bɪ'haɪnd/ 美:/bɪ'haɪnd/ </td>
                <td class="export-td">1. prep. 支持；落后于；晚于
2. adv. 在后地；在原处</td>
            </tr>
            
             <tr>
                <td class="export-td">1594</td>
                <td class="export-td">congratulation</td>
                <td class="export-td">英:/kəngrætjʊ'leɪʃ(ə)n/ 美:/kən,ɡrætʃu'leʃən/ </td>
                <td class="export-td">祝贺</td>
            </tr>
            
             <tr>
                <td class="export-td">1595</td>
                <td class="export-td">experiment</td>
                <td class="export-td">英:/ɪk'sperɪm(ə)nt/ 美:/ɛk'spɛrɪmɛnt/ </td>
                <td class="export-td">实验,试验,尝试</td>
            </tr>
            
             <tr>
                <td class="export-td">1596</td>
                <td class="export-td">blob</td>
                <td class="export-td">英:/blɒb/ 美:/blɑb/ </td>
                <td class="export-td">1. n. 一滴；一抹；难以名状的一团
2. vt. 弄脏；[美俚]把…做错</td>
            </tr>
            
             <tr>
                <td class="export-td">1597</td>
                <td class="export-td">checkers</td>
                <td class="export-td">/'tʃekəz/ </td>
                <td class="export-td">n. 西洋棋</td>
            </tr>
            
             <tr>
                <td class="export-td">1598</td>
                <td class="export-td">cripple</td>
                <td class="export-td">英:/'krɪp(ə)l/ 美:/'krɪpl/ </td>
                <td class="export-td">1. vt. 削弱；使残废；使跛
2. n. 跛子；残废</td>
            </tr>
            
             <tr>
                <td class="export-td">1599</td>
                <td class="export-td">enthusiastic</td>
                <td class="export-td">英:/ɪn,θjuːzɪ'æstɪk/ 美:/ɪn,θuzɪ'æstɪk/ </td>
                <td class="export-td">热情的, 热心的</td>
            </tr>
            
             <tr>
                <td class="export-td">1600</td>
                <td class="export-td">ballet</td>
                <td class="export-td">英:/'bæleɪ/ 美:/'bæle/ </td>
                <td class="export-td">n. 芭蕾舞剧；芭蕾舞乐曲</td>
            </tr>
            
             <tr>
                <td class="export-td">1601</td>
                <td class="export-td">dip</td>
                <td class="export-td">英:/dɪp/ 美:/dɪp/ </td>
                <td class="export-td">1. vt. 浸，泡，蘸；舀取；把伸入
2. vi. 浸；倾斜；下降，下沉；舀，掏</td>
            </tr>
            
             <tr>
                <td class="export-td">1602</td>
                <td class="export-td">helpful</td>
                <td class="export-td">英:/'helpfʊl/ 美:/'hɛlpfl/ </td>
                <td class="export-td">adj. 有益的；有帮助的</td>
            </tr>
            
             <tr>
                <td class="export-td">1603</td>
                <td class="export-td">crisis</td>
                <td class="export-td">英:/'kraɪsɪs/ 美:/'kraɪsɪs/ </td>
                <td class="export-td">1. n. 危机；决定性时刻；危险期
2. adj. 危机的；用于处理危机的</td>
            </tr>
            
             <tr>
                <td class="export-td">1604</td>
                <td class="export-td">gauge</td>
                <td class="export-td">英:/geɪdʒ/ 美:/gedʒ/ </td>
                <td class="export-td">1. n. 计量器；标准尺寸；容量规格
2. vt. 估计；测量；给…定规格</td>
            </tr>
            
             <tr>
                <td class="export-td">1605</td>
                <td class="export-td">crisp</td>
                <td class="export-td">英:/krɪsp/ 美:/krɪsp/ </td>
                <td class="export-td">1. adj. 脆的；易碎的；新鲜的
2. vt. 使发脆；使卷曲</td>
            </tr>
            
             <tr>
                <td class="export-td">1606</td>
                <td class="export-td">expert</td>
                <td class="export-td">英:/'ekspɜːt/ 美:/'ɛkspɝt/ </td>
                <td class="export-td">1. adj. 熟练的；内行的；老练的
2. n. 专家；能手；行家</td>
            </tr>
            
             <tr>
                <td class="export-td">1607</td>
                <td class="export-td">block</td>
                <td class="export-td">英:/blɔk/ 美:/blɑk/ </td>
                <td class="export-td">1. n. 块；街区；障碍物；大厦
2. vt. 阻塞；阻止；限制</td>
            </tr>
            
             <tr>
                <td class="export-td">1608</td>
                <td class="export-td">bride</td>
                <td class="export-td">英:/braɪd/ 美:/braɪd/ </td>
                <td class="export-td">n. 新娘；[英俚]姑娘，女朋友</td>
            </tr>
            
             <tr>
                <td class="export-td">1609</td>
                <td class="export-td">beige</td>
                <td class="export-td">英:/beɪʒ/ 美:/beʒ/ </td>
                <td class="export-td">1. n. 米黄色
2. adj. 浅褐色的；米黄色的</td>
            </tr>
            
             <tr>
                <td class="export-td">1610</td>
                <td class="export-td">boost</td>
                <td class="export-td">英:/buːst/ 美:/bʊst/ </td>
                <td class="export-td">1. vt. 促进；增加；支援
2. vi. 宣扬；偷窃</td>
            </tr>
            
             <tr>
                <td class="export-td">1611</td>
                <td class="export-td">being</td>
                <td class="export-td">英:/'biːɪŋ/ 美:/'biɪŋ/ </td>
                <td class="export-td">1. n. 存在；生命；本质；品格
2. adj. 存在的；现有的</td>
            </tr>
            
             <tr>
                <td class="export-td">1612</td>
                <td class="export-td">congress</td>
                <td class="export-td">英:/'kɒŋgres/ 美:/kən'ɡrɛs/ </td>
                <td class="export-td">n. 国会；会议；代表大会；社交</td>
            </tr>
            
             <tr>
                <td class="export-td">1613</td>
                <td class="export-td">burnt</td>
                <td class="export-td">英:/bɜːnt/ 美:/bɝnt/ </td>
                <td class="export-td">1. adj. 烧焦的；烧伤的
2. v. 燃烧（burn的过去式、过去分词形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">1614</td>
                <td class="export-td">bridegroom</td>
                <td class="export-td">英:/'braɪdgruːm/ 美:/'braɪdɡrum/ </td>
                <td class="export-td">新郎</td>
            </tr>
            
             <tr>
                <td class="export-td">1615</td>
                <td class="export-td">boot</td>
                <td class="export-td">英:/buːt/ 美:/bʊt/ </td>
                <td class="export-td">1. vt. 使穿靴；引导；踢；解雇
2. n. 靴子；汽车行李箱；踢</td>
            </tr>
            
             <tr>
                <td class="export-td">1616</td>
                <td class="export-td">cheek</td>
                <td class="export-td">英:/tʃiːk/ 美:/tʃik/ </td>
                <td class="export-td">1. n. 面颊，脸颊；[俚]臀部
2. vt. 无礼地向…讲话，对…大胆无礼</td>
            </tr>
            
             <tr>
                <td class="export-td">1617</td>
                <td class="export-td">drug</td>
                <td class="export-td">英:/drʌg/ 美:/drʌg/ </td>
                <td class="export-td">1. n. 毒品；药；滞销货；麻醉药
2. vt. 使服麻醉药；使服毒品；掺麻醉药于</td>
            </tr>
            
             <tr>
                <td class="export-td">1618</td>
                <td class="export-td">bridesmaid</td>
                <td class="export-td">英:/'braɪdzmeɪd/ 美:/'braɪdzmed/ </td>
                <td class="export-td">女傧相</td>
            </tr>
            
             <tr>
                <td class="export-td">1619</td>
                <td class="export-td">coil</td>
                <td class="export-td">英:/kɒɪl/ 美:/kɔɪl/ </td>
                <td class="export-td">1. vt. 盘绕，把…卷成圈
2. n. 卷；线圈</td>
            </tr>
            
             <tr>
                <td class="export-td">1620</td>
                <td class="export-td">dazzle</td>
                <td class="export-td">英:/'dæz(ə)l/ 美:/'dæzl/ </td>
                <td class="export-td">1. n. 耀眼的光；灿烂
2. vt. 使……目眩；使……眼花</td>
            </tr>
            
             <tr>
                <td class="export-td">1621</td>
                <td class="export-td">dose</td>
                <td class="export-td">英:/dəʊs/ 美:/dos/ </td>
                <td class="export-td">1. n. 剂量；一剂，一服
2. vi. 服药</td>
            </tr>
            
             <tr>
                <td class="export-td">1622</td>
                <td class="export-td">entire</td>
                <td class="export-td">英:/ɪn'taɪə/ 美:/ɪn'taɪɚ/ </td>
                <td class="export-td">adj. 全部的，整个的；全体的</td>
            </tr>
            
             <tr>
                <td class="export-td">1623</td>
                <td class="export-td">coin</td>
                <td class="export-td">英:/kɒɪn/ 美:/kɔɪn/ </td>
                <td class="export-td">1. vt. 杜撰，创造；铸造（货币）
2. n. 硬币，钱币</td>
            </tr>
            
             <tr>
                <td class="export-td">1624</td>
                <td class="export-td">balloon</td>
                <td class="export-td">英:/bə'luːn/ 美:/bə'lun/ </td>
                <td class="export-td">1. vi. 激增；膨胀如气球
2. n. 气球</td>
            </tr>
            
             <tr>
                <td class="export-td">1625</td>
                <td class="export-td">greet</td>
                <td class="export-td">英:/griːt/ 美:/ɡrit/ </td>
                <td class="export-td">vt. 欢迎，迎接；致敬，致意；映入眼帘</td>
            </tr>
            
             <tr>
                <td class="export-td">1626</td>
                <td class="export-td">entirely</td>
                <td class="export-td">英:/ɪn'taɪəlɪ/ 美:/ɪn'taɪɚli/ </td>
                <td class="export-td">adv. 完全地，彻底地</td>
            </tr>
            
             <tr>
                <td class="export-td">1627</td>
                <td class="export-td">diploma</td>
                <td class="export-td">英:/dɪ'pləʊmə/ 美:/dɪ'plomə/ </td>
                <td class="export-td">1. n. 毕业证书，学位证书；公文，文书；奖状
2. vt. 发给…毕业文凭</td>
            </tr>
            
             <tr>
                <td class="export-td">1628</td>
                <td class="export-td">gave</td>
                <td class="export-td">英:/ɡeɪv/ 美:/ɡev/ </td>
                <td class="export-td">v. 给予（give的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">1629</td>
                <td class="export-td">critic</td>
                <td class="export-td">英:/'krɪtɪk/ 美:/'krɪtɪk/ </td>
                <td class="export-td">n. 批评家，评论家；爱挑剔的人</td>
            </tr>
            
             <tr>
                <td class="export-td">1630</td>
                <td class="export-td">acute</td>
                <td class="export-td">英:/ə'kjuːt/ 美:/ə'kjut/ </td>
                <td class="export-td">adj. 严重的，急性的；激烈的；敏锐的；尖声的</td>
            </tr>
            
             <tr>
                <td class="export-td">1631</td>
                <td class="export-td">bridge</td>
                <td class="export-td">英:/brɪdʒ/ 美:/brɪdʒ/ </td>
                <td class="export-td">1. n. 桥；桥牌；船桥；桥接器
2. vt. 渡过；架桥</td>
            </tr>
            
             <tr>
                <td class="export-td">1632</td>
                <td class="export-td">greeting</td>
                <td class="export-td">英:/'griːtɪŋ/ 美:/'ɡritɪŋ/ </td>
                <td class="export-td">1. n. 问候，招呼；祝贺
2. v. 致敬，欢迎（greet的现在分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1633</td>
                <td class="export-td">cheeky</td>
                <td class="export-td">英:/'tʃiːkɪ/ 美:/'tʃiki/ </td>
                <td class="export-td">adj. 无耻的；厚脸皮的</td>
            </tr>
            
             <tr>
                <td class="export-td">1634</td>
                <td class="export-td">critical</td>
                <td class="export-td">英:/'krɪtɪk(ə)l/ 美:/'krɪtɪkl/ </td>
                <td class="export-td">adj. 批评的，爱挑剔的；决定性的；危险的；临界的；鉴定的；评论的</td>
            </tr>
            
             <tr>
                <td class="export-td">1635</td>
                <td class="export-td">ballot</td>
                <td class="export-td">英:/'bælət/ 美:/'bælət/ </td>
                <td class="export-td">1. n. 投票；投票用纸；投票总数
2. vi. 投票；抽签决定</td>
            </tr>
            
             <tr>
                <td class="export-td">1636</td>
                <td class="export-td">cycle</td>
                <td class="export-td">英:/'saɪk(ə)l/ 美:/'saɪkl/ </td>
                <td class="export-td">1. n. 循环；周期；整套；自行车；一段时间
2. vt. 使循环；使轮转</td>
            </tr>
            
             <tr>
                <td class="export-td">1637</td>
                <td class="export-td">expire</td>
                <td class="export-td">英:/ɪk'spaɪə/ 美:/ɪk'spaɪɚ/ </td>
                <td class="export-td">1. vi. 终止；期满；死亡；呼气
2. vt. 呼出（空气）</td>
            </tr>
            
             <tr>
                <td class="export-td">1638</td>
                <td class="export-td">diplomat</td>
                <td class="export-td">英:/'dɪpləmæt/ 美:/'dɪpləmæt/ </td>
                <td class="export-td">n. 外交家，外交官；有外交手腕的人；处事圆滑机敏的人</td>
            </tr>
            
             <tr>
                <td class="export-td">1639</td>
                <td class="export-td">hem</td>
                <td class="export-td">英:/hem/ 美:/hɛm/ </td>
                <td class="export-td">1. n. 摺边；边，边缘
2. vt. 包围；给...缝边</td>
            </tr>
            
             <tr>
                <td class="export-td">1640</td>
                <td class="export-td">clone</td>
                <td class="export-td">英:/kləʊn/ 美:/klon/ </td>
                <td class="export-td">1. n. 靠营养生殖而由母体分离繁殖的植物；无性繁殖；无性系；克隆
2. vt. 无性繁殖，复制</td>
            </tr>
            
             <tr>
                <td class="export-td">1641</td>
                <td class="export-td">always</td>
                <td class="export-td">英:/'ɔːlweɪz/ 美:/'ɔlwez/ </td>
                <td class="export-td">adv. 总是；永远，一直；常常</td>
            </tr>
            
             <tr>
                <td class="export-td">1642</td>
                <td class="export-td">burp</td>
                <td class="export-td">英:/bɜːp/ 美:/bɝp/ </td>
                <td class="export-td">1. n. 打嗝；饱嗝儿
2. vi. 打饱嗝；打嗝</td>
            </tr>
            
             <tr>
                <td class="export-td">1643</td>
                <td class="export-td">coincidence</td>
                <td class="export-td">英:/kəʊ'ɪnsɪd(ə)ns/ 美:/ko'ɪnsɪdəns/ </td>
                <td class="export-td">巧合,同时发生</td>
            </tr>
            
             <tr>
                <td class="export-td">1644</td>
                <td class="export-td">dot</td>
                <td class="export-td">英:/dɒt/ 美:/dɑt/ </td>
                <td class="export-td">1. n. 点，圆点；嫁妆
2. vi. 打上点</td>
            </tr>
            
             <tr>
                <td class="export-td">1645</td>
                <td class="export-td">coincident</td>
                <td class="export-td">英:/kəʊ'ɪnsɪd(ə)nt/ 美:/ko'ɪnsɪdənt/ </td>
                <td class="export-td">一致</td>
            </tr>
            
             <tr>
                <td class="export-td">1646</td>
                <td class="export-td">close</td>
                <td class="export-td">英:/kləʊs/ 美:/kloz/ </td>
                <td class="export-td">1. adj. 亲密的；亲近的；紧密的
2. vt. 关；结束；使靠近</td>
            </tr>
            
             <tr>
                <td class="export-td">1647</td>
                <td class="export-td">explain</td>
                <td class="export-td">英:/ɪk'spleɪn/ 美:/ɪk'splen/ </td>
                <td class="export-td">v. 说明，解释</td>
            </tr>
            
             <tr>
                <td class="export-td">1648</td>
                <td class="export-td">explanation</td>
                <td class="export-td">英:/eksplə'neɪʃ(ə)n/ 美:/ˌɛksplə'neʃən/ </td>
                <td class="export-td">解释, 说明</td>
            </tr>
            
             <tr>
                <td class="export-td">1649</td>
                <td class="export-td">drugstore</td>
                <td class="export-td">英:/'drʌgstɔː/ 美:/'drʌɡstɔr/ </td>
                <td class="export-td">药房, 杂货店</td>
            </tr>
            
             <tr>
                <td class="export-td">1650</td>
                <td class="export-td">coincidental</td>
                <td class="export-td">英:/kəʊɪnsɪ'dent(ə)l/ 美:/ko,ɪnsɪ'dɛntl/ </td>
                <td class="export-td">巧合的</td>
            </tr>
            
             <tr>
                <td class="export-td">1651</td>
                <td class="export-td">brief</td>
                <td class="export-td">英:/briːf/ 美:/brif/ </td>
                <td class="export-td">1. adj. 简短的，简洁的；短暂的，草率的
2. n. 概要，诉书；摘要，简报</td>
            </tr>
            
             <tr>
                <td class="export-td">1652</td>
                <td class="export-td">belief</td>
                <td class="export-td">英:/bɪ'liːf/ 美:/bɪ'lif/ </td>
                <td class="export-td">n. 相信，信赖；教义；信仰</td>
            </tr>
            
             <tr>
                <td class="export-td">1653</td>
                <td class="export-td">cyclone</td>
                <td class="export-td">英:/'saɪkləʊn/ 美:/'saɪklon/ </td>
                <td class="export-td">n. 气旋；旋风；飓风</td>
            </tr>
            
             <tr>
                <td class="export-td">1654</td>
                <td class="export-td">burrow</td>
                <td class="export-td">英:/'bʌrəʊ/ 美:/'bɝro/ </td>
                <td class="export-td">1. vi. 挖地洞，挖通道；住入地洞，躲藏起来；钻进某处；探索，寻找；偎依著
2. vt. 在…挖洞（或通道）；使躲入洞穴；挖掘，挖出</td>
            </tr>
            
             <tr>
                <td class="export-td">1655</td>
                <td class="export-td">criticism</td>
                <td class="export-td">英:/'krɪtɪsɪz(ə)m/ 美:/'krɪtə'sɪzəm/ </td>
                <td class="export-td">批评,评论</td>
            </tr>
            
             <tr>
                <td class="export-td">1656</td>
                <td class="export-td">frizzy</td>
                <td class="export-td">英:/'frɪzɪ/ 美:/ˈfrɪzi/ </td>
                <td class="export-td">adj. 卷曲的</td>
            </tr>
            
             <tr>
                <td class="export-td">1657</td>
                <td class="export-td">believe</td>
                <td class="export-td">英:/bɪ'liːv/ 美:/bɪ'liv/ </td>
                <td class="export-td">1. vi. 信任；料想；笃信宗教
2. vt. 相信；认为；信任</td>
            </tr>
            
             <tr>
                <td class="export-td">1658</td>
                <td class="export-td">drum</td>
                <td class="export-td">英:/drʌm/ 美:/drʌm/ </td>
                <td class="export-td">1. vt. 击鼓；大力争取
2. vi. 击鼓；大力争取</td>
            </tr>
            
             <tr>
                <td class="export-td">1659</td>
                <td class="export-td">briefcase</td>
                <td class="export-td">英:/'briːfkeɪs/ 美:/'brifkes/ </td>
                <td class="export-td">公文包</td>
            </tr>
            
             <tr>
                <td class="export-td">1660</td>
                <td class="export-td">hemisphere</td>
                <td class="export-td">英:/'hemɪsfɪə/ 美:/'hɛmɪsfɪr/ </td>
                <td class="export-td">n. 半球</td>
            </tr>
            
             <tr>
                <td class="export-td">1661</td>
                <td class="export-td">gay</td>
                <td class="export-td">英:/geɪ/ 美:/ɡe/ </td>
                <td class="export-td">同性恋者</td>
            </tr>
            
             <tr>
                <td class="export-td">1662</td>
                <td class="export-td">cheer</td>
                <td class="export-td">英:/tʃɪə/ 美:/tʃɪr/ </td>
                <td class="export-td">1. vt. 欢呼；使高兴；为…加油
2. n. 欢呼；愉快；心情；令人愉快的事</td>
            </tr>
            
             <tr>
                <td class="export-td">1663</td>
                <td class="export-td">croak</td>
                <td class="export-td">英:/krəʊk/ 美:/krok/ </td>
                <td class="export-td">1. vi. 呱呱地叫；发牢骚；死
2. vt. 用嘶哑的声音说；死亡</td>
            </tr>
            
             <tr>
                <td class="export-td">1664</td>
                <td class="export-td">bloke</td>
                <td class="export-td">英:/bləʊk/ 美:/blok/ </td>
                <td class="export-td">n. [俚]家伙；小子</td>
            </tr>
            
             <tr>
                <td class="export-td">1665</td>
                <td class="export-td">burst</td>
                <td class="export-td">英:/bɜːst/ 美:/bɝst/ </td>
                <td class="export-td">1. vi. 爆炸；爆发，突发
2. vt. 爆炸；爆发，突发</td>
            </tr>
            
             <tr>
                <td class="export-td">1666</td>
                <td class="export-td">blood</td>
                <td class="export-td">英:/blʌd/ 美:/blʌd/ </td>
                <td class="export-td">1. n. 血，血液；血统
2. vt. 从…抽血；使先取得经验</td>
            </tr>
            
             <tr>
                <td class="export-td">1667</td>
                <td class="export-td">frog</td>
                <td class="export-td">英:/frɒg/ 美:/frɔɡ/ </td>
                <td class="export-td">1. n. 青蛙；饰扣；辙叉
2. vi. 捕蛙</td>
            </tr>
            
             <tr>
                <td class="export-td">1668</td>
                <td class="export-td">grew</td>
                <td class="export-td">英:/ɡruː/ 美:/ɡru/ </td>
                <td class="export-td">v. 成长，种植（grow的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">1669</td>
                <td class="export-td">explode</td>
                <td class="export-td">英:/ɪk'spləʊd/ 美:/ɪk'splod/ </td>
                <td class="export-td">1. vi. 爆炸，爆发；激增
2. vt. 使爆炸；爆炸；推翻</td>
            </tr>
            
             <tr>
                <td class="export-td">1670</td>
                <td class="export-td">gaze</td>
                <td class="export-td">英:/geɪz/ 美:/ɡez/ </td>
                <td class="export-td">1. vi. 注视；凝视
2. n. 注视；凝视</td>
            </tr>
            
             <tr>
                <td class="export-td">1671</td>
                <td class="export-td">bury</td>
                <td class="export-td">英:/'berɪ/ 美:/'bɛri/ </td>
                <td class="export-td">vt. 埋葬；隐藏</td>
            </tr>
            
             <tr>
                <td class="export-td">1672</td>
                <td class="export-td">cheerful</td>
                <td class="export-td">英:/'tʃɪəfʊl/ 美:/'tʃɪrfl/ </td>
                <td class="export-td">adj. 高兴的；快乐的；愉快的</td>
            </tr>
            
             <tr>
                <td class="export-td">1673</td>
                <td class="export-td">bell</td>
                <td class="export-td">英:/bel/ 美:/bɛl/ </td>
                <td class="export-td">1. n. 铃，钟；钟声，铃声；钟状物
2. vt. 装钟于，系铃于</td>
            </tr>
            
             <tr>
                <td class="export-td">1674</td>
                <td class="export-td">entrance</td>
                <td class="export-td">英:/'entr(ə)ns/ 美:/'ɛntrəns/ </td>
                <td class="export-td">1. n. 入口；进入
2. vt. 使出神，使入迷</td>
            </tr>
            
             <tr>
                <td class="export-td">1675</td>
                <td class="export-td">bus</td>
                <td class="export-td">英:/bʌs/ 美:/bʌs/ </td>
                <td class="export-td">n. 公共汽车</td>
            </tr>
            
             <tr>
                <td class="export-td">1676</td>
                <td class="export-td">double</td>
                <td class="export-td">英:/'dʌb(ə)l/ 美:/'dʌbl/ </td>
                <td class="export-td">1. n. 两倍；[计]双精度型
2. adj. 两倍的；双重的</td>
            </tr>
            
             <tr>
                <td class="export-td">1677</td>
                <td class="export-td">crockery</td>
                <td class="export-td">英:/'krɒk(ə)rɪ/ 美:/'krɑkəri/ </td>
                <td class="export-td">n. 陶器；瓦器；[化]土器</td>
            </tr>
            
             <tr>
                <td class="export-td">1678</td>
                <td class="export-td">exploit</td>
                <td class="export-td">英:/ɪk'splɒɪt/ 美:/ɪkˈsplɔɪt/ </td>
                <td class="export-td">1. vt. 开发，开拓；剥削；开采
2. n. 勋绩；功绩</td>
            </tr>
            
             <tr>
                <td class="export-td">1679</td>
                <td class="export-td">crocodile</td>
                <td class="export-td">英:/'krɒkədaɪl/ 美:/'krɑkə'daɪl/ </td>
                <td class="export-td">鳄鱼</td>
            </tr>
            
             <tr>
                <td class="export-td">1680</td>
                <td class="export-td">hen</td>
                <td class="export-td">英:/hen/ 美:/hɛn/ </td>
                <td class="export-td">母鸡</td>
            </tr>
            
             <tr>
                <td class="export-td">1681</td>
                <td class="export-td">direct</td>
                <td class="export-td">英:/dɪ'rekt/ 美:/də'rɛkt/ </td>
                <td class="export-td">1. adj. 直接的；亲身的；恰好的；直系的
2. vt. 指向；管理；指挥；导演</td>
            </tr>
            
             <tr>
                <td class="export-td">1682</td>
                <td class="export-td">bamboo</td>
                <td class="export-td">英:/bæm'buː/ 美:/ˌbæm'bu/ </td>
                <td class="export-td">1. n. 竹，竹子
2. vt. 为…装上篾条</td>
            </tr>
            
             <tr>
                <td class="export-td">1683</td>
                <td class="export-td">cylindrical</td>
                <td class="export-td">英:/sɪ'lɪndrɪkəl/ 美:/sə'lɪndrɪkl/ </td>
                <td class="export-td">圆柱的</td>
            </tr>
            
             <tr>
                <td class="export-td">1684</td>
                <td class="export-td">conjunction</td>
                <td class="export-td">英:/kən'dʒʌŋ(k)ʃ(ə)n/ 美:/kən'dʒʌŋkʃən/ </td>
                <td class="export-td">连词</td>
            </tr>
            
             <tr>
                <td class="export-td">1685</td>
                <td class="export-td">cheese</td>
                <td class="export-td">英:/tʃiːz/ 美:/tʃiz/ </td>
                <td class="export-td">1. n. 奶酪；干酪；[美俚]要人
2. vt. [俚]停止</td>
            </tr>
            
             <tr>
                <td class="export-td">1686</td>
                <td class="export-td">drummer</td>
                <td class="export-td">英:/'drʌmə/ 美:/'drʌmɚ/ </td>
                <td class="export-td">n. 鼓手；[美]旅行推销员；[经]跑街</td>
            </tr>
            
             <tr>
                <td class="export-td">1687</td>
                <td class="export-td">brighten</td>
                <td class="export-td">英:/'braɪt(ə)n/ 美:/'braɪtn/ </td>
                <td class="export-td">1. vi. 变亮；活跃；明亮；快乐高兴
2. vt. 使生辉；使闪亮；使快乐高兴</td>
            </tr>
            
             <tr>
                <td class="export-td">1688</td>
                <td class="export-td">border</td>
                <td class="export-td">英:/'bɔːdə/ 美:/'bɔrdɚ/ </td>
                <td class="export-td">1. n. 边界；边境；国界
2. vt. 接近；与…接壤；在…上镶边</td>
            </tr>
            
             <tr>
                <td class="export-td">1689</td>
                <td class="export-td">ban</td>
                <td class="export-td">英:/bæn/ 美:/bæn/ </td>
                <td class="export-td">禁令</td>
            </tr>
            
             <tr>
                <td class="export-td">1690</td>
                <td class="export-td">from</td>
                <td class="export-td">英:/frɒm/ 美:/frʌm/ </td>
                <td class="export-td">prep. 来自，从；今后；由于</td>
            </tr>
            
             <tr>
                <td class="export-td">1691</td>
                <td class="export-td">explore</td>
                <td class="export-td">英:/ɪk'splɔː/ 美:/ɪk'splɔr/ </td>
                <td class="export-td">1. vt. 探测；探索；探险
2. vi. 探测；探险；探索</td>
            </tr>
            
             <tr>
                <td class="export-td">1692</td>
                <td class="export-td">cold</td>
                <td class="export-td">英:/kəʊld/ 美:/kold/ </td>
                <td class="export-td">1. adj. 寒冷的；冷淡的，不热情的；失去知觉的
2. n. 寒冷；感冒</td>
            </tr>
            
             <tr>
                <td class="export-td">1693</td>
                <td class="export-td">drunk</td>
                <td class="export-td">英:/drʌŋk/ 美:/drʌŋk/ </td>
                <td class="export-td">1. v. 喝酒（drink的过去分词）
2. adj. 喝醉了的</td>
            </tr>
            
             <tr>
                <td class="export-td">1694</td>
                <td class="export-td">bush</td>
                <td class="export-td">英:/bʊʃ/ 美:/bʊʃ/ </td>
                <td class="export-td">1. n. 矮树丛；灌木
2. vt. 以灌木装饰；使…精疲力竭</td>
            </tr>
            
             <tr>
                <td class="export-td">1695</td>
                <td class="export-td">front</td>
                <td class="export-td">英:/frʌnt/ 美:/frʌnt/ </td>
                <td class="export-td">1. n. 前面；前线；正面
2. vt. 面对；朝向；对付</td>
            </tr>
            
             <tr>
                <td class="export-td">1696</td>
                <td class="export-td">grid</td>
                <td class="export-td">英:/grɪd/ 美:/ɡrɪd/ </td>
                <td class="export-td">n. [计]网格；格子，栅格；输电网</td>
            </tr>
            
             <tr>
                <td class="export-td">1697</td>
                <td class="export-td">bore</td>
                <td class="export-td">英:/bɔː/ 美:/bɔr/ </td>
                <td class="export-td">忍受</td>
            </tr>
            
             <tr>
                <td class="export-td">1698</td>
                <td class="export-td">banana</td>
                <td class="export-td">英:/bə'nɑːnə/ 美:/bə'nænə/ </td>
                <td class="export-td">n. 香蕉；喜剧演员；大鹰钩鼻</td>
            </tr>
            
             <tr>
                <td class="export-td">1699</td>
                <td class="export-td">brilliant</td>
                <td class="export-td">英:/'brɪlj(ə)nt/ 美:/'brɪljənt/ </td>
                <td class="export-td">辉煌</td>
            </tr>
            
             <tr>
                <td class="export-td">1700</td>
                <td class="export-td">explorer</td>
                <td class="export-td">英:/ek'splɔːrə(r)/ 美:/ɪk'splɔrɚ/ </td>
                <td class="export-td">n. 探测者，探测器；探险家</td>
            </tr>
            
             <tr>
                <td class="export-td">1701</td>
                <td class="export-td">closed</td>
                <td class="export-td">英:/kləʊzd/ 美:/klozd/ </td>
                <td class="export-td">1. adj. 关着的；不公开的
2. v. 关；结束；接近（close的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1702</td>
                <td class="export-td">brilliantly</td>
                <td class="export-td">英:/'briljəntli/ 美:/ˈbrɪljəntlɪ/ </td>
                <td class="export-td">出色</td>
            </tr>
            
             <tr>
                <td class="export-td">1703</td>
                <td class="export-td">entry</td>
                <td class="export-td">英:/'entri/ 美:/ˈɛntri/ </td>
                <td class="export-td">n. 入口；进入；登记；条目；对土地的侵占；[商]报关手续</td>
            </tr>
            
             <tr>
                <td class="export-td">1704</td>
                <td class="export-td">explosion</td>
                <td class="export-td">英:/ɪk'spləʊʒ(ə)n/ 美:/ɪk'sploʒən/ </td>
                <td class="export-td">爆炸,爆发,激增</td>
            </tr>
            
             <tr>
                <td class="export-td">1705</td>
                <td class="export-td">grief</td>
                <td class="export-td">英:/griːf/ 美:/ɡrif/ </td>
                <td class="export-td">n. 悲痛；忧伤；不幸</td>
            </tr>
            
             <tr>
                <td class="export-td">1706</td>
                <td class="export-td">boring</td>
                <td class="export-td">英:/'bɔːrɪŋ/ 美:/'bɔrɪŋ/ </td>
                <td class="export-td">1. adj. 令人厌烦的；无聊的
2. n. 钻孔</td>
            </tr>
            
             <tr>
                <td class="export-td">1707</td>
                <td class="export-td">band</td>
                <td class="export-td">英:/bænd/ 美:/bænd/ </td>
                <td class="export-td">1. n. 带；松紧带；传送带；乐队；一帮
2. vi. 联合；聚焦</td>
            </tr>
            
             <tr>
                <td class="export-td">1708</td>
                <td class="export-td">explosive</td>
                <td class="export-td">英:/ɪk'spləʊsɪv/ 美:/ɪk'splosɪv/ </td>
                <td class="export-td">爆炸 的; 炸药</td>
            </tr>
            
             <tr>
                <td class="export-td">1709</td>
                <td class="export-td">cheetah</td>
                <td class="export-td">英:/'tʃiːtə/ 美:/'tʃitə/ </td>
                <td class="export-td">n. 猎豹</td>
            </tr>
            
             <tr>
                <td class="export-td">1710</td>
                <td class="export-td">brim</td>
                <td class="export-td">英:/brɪm/ 美:/brɪm/ </td>
                <td class="export-td">1. n. 边；边缘
2. vi. 满溢；溢出</td>
            </tr>
            
             <tr>
                <td class="export-td">1711</td>
                <td class="export-td">direction</td>
                <td class="export-td">英:/dɪ'rekʃ(ə)n/ 美:/daɪ'rɛkʃən/ </td>
                <td class="export-td">方向</td>
            </tr>
            
             <tr>
                <td class="export-td">1712</td>
                <td class="export-td">crooked</td>
                <td class="export-td">英:/'krʊkɪd/ 美:/'krʊkɪd/ </td>
                <td class="export-td">adj. 弯曲的；歪的；不正当的</td>
            </tr>
            
             <tr>
                <td class="export-td">1713</td>
                <td class="export-td">frontier</td>
                <td class="export-td">英:/'frʌntɪə/ 美:/frʌn'tɪr/ </td>
                <td class="export-td">1. n. 边界；国境；前沿
2. adj. 边界的；开拓的</td>
            </tr>
            
             <tr>
                <td class="export-td">1714</td>
                <td class="export-td">closet</td>
                <td class="export-td">英:/'klɒzɪt/ 美:/'klɑzət/ </td>
                <td class="export-td">1. n. 壁橱；议事室，密室；小房间
2. adj. 秘密的，私下的；空谈的</td>
            </tr>
            
             <tr>
                <td class="export-td">1715</td>
                <td class="export-td">chemical</td>
                <td class="export-td">英:/'kemɪk(ə)l/ 美:/'kɛmɪkl/ </td>
                <td class="export-td">1. n. 化学制品，化学药品
2. adj. 化学的</td>
            </tr>
            
             <tr>
                <td class="export-td">1716</td>
                <td class="export-td">dry</td>
                <td class="export-td">英:/draɪ/ 美:/draɪ/ </td>
                <td class="export-td">1. adj. 干的；口渴的；禁酒的；枯燥无味的
2. vt. 把…弄干</td>
            </tr>
            
             <tr>
                <td class="export-td">1717</td>
                <td class="export-td">connect</td>
                <td class="export-td">英:/kə'nekt/ 美:/kə'nɛkt/ </td>
                <td class="export-td">1. vt. 连接；联合；关连
2. vi. 连接，连结；联合</td>
            </tr>
            
             <tr>
                <td class="export-td">1718</td>
                <td class="export-td">export</td>
                <td class="export-td">英:/ɪk'spɔːt/ 美:/ɪk'spɔrt/ </td>
                <td class="export-td">1. n. 输出，出口；出口商品
2. vi. 输出物资</td>
            </tr>
            
             <tr>
                <td class="export-td">1719</td>
                <td class="export-td">born</td>
                <td class="export-td">英:/bɔ:n/ 美:/bɔrn/ </td>
                <td class="export-td">1. v. 出世（bear的过去分词）
2. adj. 天生的</td>
            </tr>
            
             <tr>
                <td class="export-td">1720</td>
                <td class="export-td">directly</td>
                <td class="export-td">英:/dɪ'rektlɪ/ 美:/daɪ'rɛktli/ </td>
                <td class="export-td">1. adv. 直接地；立即；马上；坦率地；正好地
2. conj. 一…就</td>
            </tr>
            
             <tr>
                <td class="export-td">1721</td>
                <td class="export-td">frost</td>
                <td class="export-td">英:/frɔst/ 美:/frɔst/ </td>
                <td class="export-td">1. vt. 结霜于；冻坏
2. vi. 结霜；受冻</td>
            </tr>
            
             <tr>
                <td class="export-td">1722</td>
                <td class="export-td">envelope</td>
                <td class="export-td">英:/'envələʊp/ 美:/ˈɛnvəˌlop/ </td>
                <td class="export-td">n. 信封，封皮；[生]包膜；[天]包层；[数]包迹</td>
            </tr>
            
             <tr>
                <td class="export-td">1723</td>
                <td class="export-td">crop</td>
                <td class="export-td">英:/krɒp/ 美:/krɑp/ </td>
                <td class="export-td">1. n. 农作物；庄稼；产量；平头
2. vt. 种植；收割；修剪；剪短</td>
            </tr>
            
             <tr>
                <td class="export-td">1724</td>
                <td class="export-td">her</td>
                <td class="export-td">英:/hɜː(r)/ 美:/hɚ/ </td>
                <td class="export-td">pron. 她的；她</td>
            </tr>
            
             <tr>
                <td class="export-td">1725</td>
                <td class="export-td">director</td>
                <td class="export-td">英:/dɪ'rektə/ 美:/də'rɛktɚ/ </td>
                <td class="export-td">n. 人事助理；导演；主任，主管</td>
            </tr>
            
             <tr>
                <td class="export-td">1726</td>
                <td class="export-td">business</td>
                <td class="export-td">英:/'bɪznɪs/ 美:/'bɪznəs/ </td>
                <td class="export-td">n. 商业；生意；交易；事情</td>
            </tr>
            
             <tr>
                <td class="export-td">1727</td>
                <td class="export-td">hers</td>
                <td class="export-td">英:/hɜːz/ 美:/hɝz/ </td>
                <td class="export-td">pron. 她的（所有格）</td>
            </tr>
            
             <tr>
                <td class="export-td">1728</td>
                <td class="export-td">grill</td>
                <td class="export-td">英:/grɪl/ 美:/ɡrɪl/ </td>
                <td class="export-td">1. vt. 烧，烤；烤问
2. vi. 烧，烤；严加盘问</td>
            </tr>
            
             <tr>
                <td class="export-td">1729</td>
                <td class="export-td">borne</td>
                <td class="export-td">英:/bɔːn/ 美:/bɔrn/ </td>
                <td class="export-td">v. 忍受；负荷；结果实；生子女（bear的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1730</td>
                <td class="export-td">cloth</td>
                <td class="export-td">英:/klɒθ/ 美:/klɔθ/ </td>
                <td class="export-td">n. 布，织物；餐巾</td>
            </tr>
            
             <tr>
                <td class="export-td">1731</td>
                <td class="export-td">expose</td>
                <td class="export-td">英:/ɪk'spəʊz/ 美:/ɪk'spoz/ </td>
                <td class="export-td">vt. 使曝光；揭露，揭发；显示</td>
            </tr>
            
             <tr>
                <td class="export-td">1732</td>
                <td class="export-td">bring</td>
                <td class="export-td">英:/brɪŋ/ 美:/brɪŋ/ </td>
                <td class="export-td">vt. 带来；引起；促使；使某人处于某种情况或境地</td>
            </tr>
            
             <tr>
                <td class="export-td">1733</td>
                <td class="export-td">grim</td>
                <td class="export-td">英:/grɪm/ 美:/ɡrɪm/ </td>
                <td class="export-td">adj. 冷酷的；残忍的；糟糕的</td>
            </tr>
            
             <tr>
                <td class="export-td">1734</td>
                <td class="export-td">clothes</td>
                <td class="export-td">英:/kləʊ(ð)z/ 美:/kloðz/ </td>
                <td class="export-td">n. 衣服</td>
            </tr>
            
             <tr>
                <td class="export-td">1735</td>
                <td class="export-td">bandage</td>
                <td class="export-td">英:/'bændɪdʒ/ 美:/'bændɪdʒ/ </td>
                <td class="export-td">1. n. 绷带
2. vt. 用绷带包扎</td>
            </tr>
            
             <tr>
                <td class="export-td">1736</td>
                <td class="export-td">chemist</td>
                <td class="export-td">英:/'kemɪst/ 美:/'kɛmɪst/ </td>
                <td class="export-td">n. 药剂师；化学家</td>
            </tr>
            
             <tr>
                <td class="export-td">1737</td>
                <td class="export-td">frosting</td>
                <td class="export-td">英:/'frɒstɪŋ/ 美:/'frɔstɪŋ/ </td>
                <td class="export-td">1. n. 霜状白糖；无光泽面；结霜；去光泽
2. v. 以霜覆盖；冻坏；起霜（frost的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">1738</td>
                <td class="export-td">envious</td>
                <td class="export-td">英:/'envɪəs/ 美:/'ɛnvɪəs/ </td>
                <td class="export-td">adj. 羡慕的；嫉妒的</td>
            </tr>
            
             <tr>
                <td class="export-td">1739</td>
                <td class="export-td">chemistry</td>
                <td class="export-td">英:/'kemɪstrɪ/ 美:/'kɛmɪstri/ </td>
                <td class="export-td">化学</td>
            </tr>
            
             <tr>
                <td class="export-td">1740</td>
                <td class="export-td">herb</td>
                <td class="export-td">英:/hɜːb/ 美:/ɝb/ </td>
                <td class="export-td">n. 香草，药草</td>
            </tr>
            
             <tr>
                <td class="export-td">1741</td>
                <td class="export-td">belly</td>
                <td class="export-td">英:/'belɪ/ 美:/'bɛli/ </td>
                <td class="export-td">1. n. 腹部；胃；食欲
2. vi. 涨满；鼓起</td>
            </tr>
            
             <tr>
                <td class="export-td">1742</td>
                <td class="export-td">borrow</td>
                <td class="export-td">英:/'bɒrəʊ/ 美:/'bɑro/ </td>
                <td class="export-td">1. vi. 借；借用；从其他语言中引入
2. vt. 借用；借</td>
            </tr>
            
             <tr>
                <td class="export-td">1743</td>
                <td class="export-td">directory</td>
                <td class="export-td">英:/dɪ'rekt(ə)rɪ/ 美:/daɪ'rɛktəri/ </td>
                <td class="export-td">目录</td>
            </tr>
            
             <tr>
                <td class="export-td">1744</td>
                <td class="export-td">cross</td>
                <td class="export-td">英:/krɒs/ 美:/krɔs/ </td>
                <td class="export-td">1. n. 十字架，十字形物；交叉，十字
2. vi. 交叉；横过；杂交</td>
            </tr>
            
             <tr>
                <td class="export-td">1745</td>
                <td class="export-td">environment</td>
                <td class="export-td">英:/ɪn'vaɪrənm(ə)nt/ 美:/ɪn'vaɪrənmənt/ </td>
                <td class="export-td">环境,外界</td>
            </tr>
            
             <tr>
                <td class="export-td">1746</td>
                <td class="export-td">bloodstream</td>
                <td class="export-td">英:/'blʌdstriːm/ 美:/'blʌdstrim/ </td>
                <td class="export-td">血流</td>
            </tr>
            
             <tr>
                <td class="export-td">1747</td>
                <td class="export-td">bandit</td>
                <td class="export-td">英:/'bændɪt/ 美:/'bændɪt/ </td>
                <td class="export-td">强盗</td>
            </tr>
            
             <tr>
                <td class="export-td">1748</td>
                <td class="export-td">businessman</td>
                <td class="export-td">英:/'bɪznɪsmən/ 美:/'bɪznəsmæn/ </td>
                <td class="export-td">商人</td>
            </tr>
            
             <tr>
                <td class="export-td">1749</td>
                <td class="export-td">express</td>
                <td class="export-td">英:/ɪk'spres/ 美:/ɪk'sprɛs/ </td>
                <td class="export-td">1. vt. 表达；快递
2. adj. 明确的；迅速的；专门的</td>
            </tr>
            
             <tr>
                <td class="export-td">1750</td>
                <td class="export-td">grin</td>
                <td class="export-td">英:/grɪn/ 美:/ɡrɪn/ </td>
                <td class="export-td">1. v. 露齿而笑，咧着嘴笑
2. n. 露齿笑</td>
            </tr>
            
             <tr>
                <td class="export-td">1751</td>
                <td class="export-td">grind</td>
                <td class="export-td">英:/graɪnd/ 美:/ɡraɪnd/ </td>
                <td class="export-td">1. vt. 磨碎；磨快
2. vi. 磨碎；折磨</td>
            </tr>
            
             <tr>
                <td class="export-td">1752</td>
                <td class="export-td">disorganized</td>
                <td class="export-td">英:/dɪsˈɔ:gənaɪzd/ 美:/dɪs'ɔrɡənaɪzd/ </td>
                <td class="export-td">disorganised<br /><br />杂乱无章</td>
            </tr>
            
             <tr>
                <td class="export-td">1753</td>
                <td class="export-td">dirt</td>
                <td class="export-td">英:/dɜːt/ 美:/dɝt/ </td>
                <td class="export-td">n. 污垢，泥土；灰尘，尘土；下流话</td>
            </tr>
            
             <tr>
                <td class="export-td">1754</td>
                <td class="export-td">collapse</td>
                <td class="export-td">英:/kə'læps/ 美:/kə'læps/ </td>
                <td class="export-td">1. vi. 倒塌；瓦解；暴跌
2. vt. 使倒塌，使崩溃；使萎陷</td>
            </tr>
            
             <tr>
                <td class="export-td">1755</td>
                <td class="export-td">envy</td>
                <td class="export-td">英:/'envɪ/ 美:/'ɛnvi/ </td>
                <td class="export-td">1. n. 羡慕；嫉妒，妒忌
2. vt. 羡慕；嫉妒，妒忌</td>
            </tr>
            
             <tr>
                <td class="export-td">1756</td>
                <td class="export-td">frown</td>
                <td class="export-td">英:/fraʊn/ 美:/fraʊn/ </td>
                <td class="export-td">1. vi. 皱眉；不同意
2. vt. 皱眉，蹙额</td>
            </tr>
            
             <tr>
                <td class="export-td">1757</td>
                <td class="export-td">grip</td>
                <td class="export-td">英:/grɪp/ 美:/ɡrɪp/ </td>
                <td class="export-td">1. n. 紧握；柄；支配；握拍方式；拍柄绷带
2. vt. 紧握；夹紧</td>
            </tr>
            
             <tr>
                <td class="export-td">1758</td>
                <td class="export-td">clothing</td>
                <td class="export-td">英:/'kləʊðɪŋ/ 美:/'kloðɪŋ/ </td>
                <td class="export-td">1. n. （总称）服装；[航海]帆装
2. v. 给…穿衣；覆盖（clothe的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">1759</td>
                <td class="export-td">expression</td>
                <td class="export-td">英:/ɪk'spreʃ(ə)n/ 美:/ɪk'sprɛʃən/ </td>
                <td class="export-td">表达</td>
            </tr>
            
             <tr>
                <td class="export-td">1760</td>
                <td class="export-td">collar</td>
                <td class="export-td">英:/'kɒlə/ 美:/'kɑlɚ/ </td>
                <td class="export-td">1. n. 衣领；颈圈
2. vt. 给…上领子；给…套上颈圈；[口]抓住</td>
            </tr>
            
             <tr>
                <td class="export-td">1761</td>
                <td class="export-td">gripping</td>
                <td class="export-td">英:/'ɡripiŋ/ 美:/ˈɡrɪpɪŋ/ </td>
                <td class="export-td">1. adj. 引人注意的；令人全神贯注的；扣人心弦的
2. v. 握紧；扣人心弦（grip的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">1762</td>
                <td class="export-td">belong</td>
                <td class="export-td">英:/bɪ'lɒŋ/ 美:/bɪ'lɔŋ/ </td>
                <td class="export-td">vi. 属于，应归入；适宜；应被放置；居住</td>
            </tr>
            
             <tr>
                <td class="export-td">1763</td>
                <td class="export-td">belongings</td>
                <td class="export-td">英:/biˈlɔŋiŋz/ 美:/bə'lɔŋɪŋz/ </td>
                <td class="export-td">财产, 所有物</td>
            </tr>
            
             <tr>
                <td class="export-td">1764</td>
                <td class="export-td">herd</td>
                <td class="export-td">英:/hɜːd/ 美:/hɝd/ </td>
                <td class="export-td">1. n. 兽群，畜群；放牧人
2. vi. 成群，聚在一起</td>
            </tr>
            
             <tr>
                <td class="export-td">1765</td>
                <td class="export-td">froze</td>
                <td class="export-td">英:/frəʊz/ 美:/froz/ </td>
                <td class="export-td">v. 冻结；凝固；冻住（freeze的过去式形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">1766</td>
                <td class="export-td">cloud</td>
                <td class="export-td">英:/klaʊd/ 美:/klaʊd/ </td>
                <td class="export-td">1. n. 云；云状物；一大群；阴云；黑斑
2. vt. 以云遮敝；使混乱；使忧郁；玷污</td>
            </tr>
            
             <tr>
                <td class="export-td">1767</td>
                <td class="export-td">bloody</td>
                <td class="export-td">英:/'blʌdɪ/ 美:/'blʌdi/ </td>
                <td class="export-td">1. adj. 嗜杀的，残忍的；血腥的；非常的；血色的
2. vt. 使流血</td>
            </tr>
            
             <tr>
                <td class="export-td">1768</td>
                <td class="export-td">dirty</td>
                <td class="export-td">英:/'dɜːtɪ/ 美:/'dɝti/ </td>
                <td class="export-td">1. adj. 污秽的；下流的，卑鄙的；恶劣的；暗淡的
2. vi. 变脏</td>
            </tr>
            
             <tr>
                <td class="export-td">1769</td>
                <td class="export-td">boss</td>
                <td class="export-td">英:/bɒs/ 美:/bɔs/ </td>
                <td class="export-td">1. n. 老板；工头；首领
2. vt. 指挥，调遣；当…的领导</td>
            </tr>
            
             <tr>
                <td class="export-td">1770</td>
                <td class="export-td">frozen</td>
                <td class="export-td">英:/'frəʊzn/ 美:/ˈfrozən/ </td>
                <td class="export-td">1. adj. 冻结的；冷酷的
2. v. 凝固；变得刻板；结冰（freeze的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1771</td>
                <td class="export-td">below</td>
                <td class="export-td">英:/bɪ'ləʊ/ 美:/bɪ'lo/ </td>
                <td class="export-td">1. adv. 在下面，在较低处；在本页下面
2. prep. 在…下面</td>
            </tr>
            
             <tr>
                <td class="export-td">1772</td>
                <td class="export-td">conscience</td>
                <td class="export-td">英:/'kɒnʃ(ə)ns/ 美:/'kɑnʃəns/ </td>
                <td class="export-td">良心</td>
            </tr>
            
             <tr>
                <td class="export-td">1773</td>
                <td class="export-td">cherry</td>
                <td class="export-td">英:/ˈtʃeri/ 美:/ˈtʃɛri/ </td>
                <td class="export-td">n. 樱桃；樱桃树；如樱桃的鲜红色；[俚，鄙]处女膜，处女</td>
            </tr>
            
             <tr>
                <td class="export-td">1774</td>
                <td class="export-td">belt</td>
                <td class="export-td">英:/belt/ 美:/bɛlt/ </td>
                <td class="export-td">1. n. 地带；带；腰带
2. vt. 用带子系住；用皮带抽打</td>
            </tr>
            
             <tr>
                <td class="export-td">1775</td>
                <td class="export-td">bossy</td>
                <td class="export-td">英:/'bɒsɪ/ 美:/'bɔsi/ </td>
                <td class="export-td">1. adj. 专横的；浮雕装饰的；爱指挥他人的
2. n. 母牛；牛犊</td>
            </tr>
            
             <tr>
                <td class="export-td">1776</td>
                <td class="export-td">cloudy</td>
                <td class="export-td">英:/'klaʊdɪ/ 美:/'klaʊdi/ </td>
                <td class="export-td">adj. 多云的；阴天的；愁容满面的</td>
            </tr>
            
             <tr>
                <td class="export-td">1777</td>
                <td class="export-td">bang</td>
                <td class="export-td">英:/bæŋ/ 美:/bæŋ/ </td>
                <td class="export-td">砰</td>
            </tr>
            
             <tr>
                <td class="export-td">1778</td>
                <td class="export-td">bloom</td>
                <td class="export-td">英:/bluːm/ 美:/blum/ </td>
                <td class="export-td">1. n. 花；青春；旺盛
2. vt. 使开花；使茂盛</td>
            </tr>
            
             <tr>
                <td class="export-td">1779</td>
                <td class="export-td">disability</td>
                <td class="export-td">英:/dɪsə'bɪlɪtɪ/ 美:/ˌdɪsə'bɪləti/ </td>
                <td class="export-td">无力, 无能, 残疾</td>
            </tr>
            
             <tr>
                <td class="export-td">1780</td>
                <td class="export-td">here</td>
                <td class="export-td">英:/hɪə/ 美:/hɪr/ </td>
                <td class="export-td">1. adv. 在这里；此时
2. int. 嘿！；喂！</td>
            </tr>
            
             <tr>
                <td class="export-td">1781</td>
                <td class="export-td">disable</td>
                <td class="export-td">英:/dɪs'eɪb(ə)l/ 美:/dɪs'ebl/ </td>
                <td class="export-td">vt. 使残废；使失去能力；使无资格</td>
            </tr>
            
             <tr>
                <td class="export-td">1782</td>
                <td class="export-td">conscientious</td>
                <td class="export-td">英:/ˌkɒnʃɪ'enʃəs/ 美:/'kɑnʃɪ'ɛnʃəs/ </td>
                <td class="export-td">有良心</td>
            </tr>
            
             <tr>
                <td class="export-td">1783</td>
                <td class="export-td">busy</td>
                <td class="export-td">英:/'bɪzɪ/ 美:/'bɪzi/ </td>
                <td class="export-td">1. adj. 忙碌的；热闹的；正被占用的
2. vt. 使忙于</td>
            </tr>
            
             <tr>
                <td class="export-td">1784</td>
                <td class="export-td">colleague</td>
                <td class="export-td">英:/'kɒliːg/ 美:/'kɑliɡ/ </td>
                <td class="export-td">同事</td>
            </tr>
            
             <tr>
                <td class="export-td">1785</td>
                <td class="export-td">collect</td>
                <td class="export-td">英:/kə'lekt/ 美:/kə'lɛkt/ </td>
                <td class="export-td">1. vt. 收集；募捐
2. vi. 收集；聚集；募捐</td>
            </tr>
            
             <tr>
                <td class="export-td">1786</td>
                <td class="export-td">chess</td>
                <td class="export-td">英:/tʃes/ 美:/tʃɛs/ </td>
                <td class="export-td">n. 国际象棋，西洋棋</td>
            </tr>
            
             <tr>
                <td class="export-td">1787</td>
                <td class="export-td">but</td>
                <td class="export-td">英:/bʌt/ 美:/bʌt,bət/ </td>
                <td class="export-td">1. conj. 但是；然而；而是
2. adv. 仅仅，只</td>
            </tr>
            
             <tr>
                <td class="export-td">1788</td>
                <td class="export-td">exquisite</td>
                <td class="export-td">英:/'ekskwɪzɪt/ 美:/ɪk'skwɪzɪt/ </td>
                <td class="export-td">玲珑</td>
            </tr>
            
             <tr>
                <td class="export-td">1789</td>
                <td class="export-td">disadvantage</td>
                <td class="export-td">英:/dɪsəd'vɑːntɪdʒ/ 美:/ˌdɪsəd'væntɪdʒ/ </td>
                <td class="export-td">坏处</td>
            </tr>
            
             <tr>
                <td class="export-td">1790</td>
                <td class="export-td">collection</td>
                <td class="export-td">英:/kə'lekʃ(ə)n/ 美:/kə'lɛkʃən/ </td>
                <td class="export-td">集</td>
            </tr>
            
             <tr>
                <td class="export-td">1791</td>
                <td class="export-td">grit</td>
                <td class="export-td">英:/grɪt/ 美:/ɡrɪt/ </td>
                <td class="export-td">1. vt. 研磨；在…上铺砂砾
2. vi. 摩擦作声</td>
            </tr>
            
             <tr>
                <td class="export-td">1792</td>
                <td class="export-td">doubt</td>
                <td class="export-td">英:/daʊt/ 美:/daʊt/ </td>
                <td class="export-td">1. n. 怀疑；疑问；疑惑
2. v. 怀疑；不信；[古]恐怕；拿不准</td>
            </tr>
            
             <tr>
                <td class="export-td">1793</td>
                <td class="export-td">bench</td>
                <td class="export-td">英:/ben(t)ʃ/ 美:/bɛntʃ/ </td>
                <td class="export-td">1. n. 长凳；工作台；替补队员
2. vt. 给…以席位；为…设置条凳</td>
            </tr>
            
             <tr>
                <td class="export-td">1794</td>
                <td class="export-td">conscious</td>
                <td class="export-td">英:/'kɒnʃəs/ 美:/'kɑnʃəs/ </td>
                <td class="export-td">意识</td>
            </tr>
            
             <tr>
                <td class="export-td">1795</td>
                <td class="export-td">butcher</td>
                <td class="export-td">英:/'bʊtʃə/ 美:/'bʊtʃɚ/ </td>
                <td class="export-td">1. vt. 屠杀
2. n. 屠夫</td>
            </tr>
            
             <tr>
                <td class="export-td">1796</td>
                <td class="export-td">clove</td>
                <td class="export-td">英:/kləʊv/ 美:/klov/ </td>
                <td class="export-td">1. n. 丁香
2. v. 劈开（cleave的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">1797</td>
                <td class="export-td">chest</td>
                <td class="export-td">英:/tʃest/ 美:/tʃɛst/ </td>
                <td class="export-td">n. 胸，胸部；箱子；衣柜；金库</td>
            </tr>
            
             <tr>
                <td class="export-td">1798</td>
                <td class="export-td">brisk</td>
                <td class="export-td">英:/brɪsk/ 美:/brɪsk/ </td>
                <td class="export-td">1. adj. 敏锐的，活泼的，轻快的；凛冽的
2. vi. 活跃起来；变得轻快</td>
            </tr>
            
             <tr>
                <td class="export-td">1799</td>
                <td class="export-td">consciousness</td>
                <td class="export-td">英:/'kɒnʃəsnɪs/ 美:/'kɑnʃəsnəs/ </td>
                <td class="export-td">意识</td>
            </tr>
            
             <tr>
                <td class="export-td">1800</td>
                <td class="export-td">fruit</td>
                <td class="export-td">英:/fruːt/ 美:/frut/ </td>
                <td class="export-td">1. n. 水果；产物
2. vi. 结果实</td>
            </tr>
            
             <tr>
                <td class="export-td">1801</td>
                <td class="export-td">banister</td>
                <td class="export-td">英:/'bænɪstə/ 美:/'bænɪstɚ/ </td>
                <td class="export-td">n. 栏杆的支柱；楼梯的扶栏</td>
            </tr>
            
             <tr>
                <td class="export-td">1802</td>
                <td class="export-td">doubtful</td>
                <td class="export-td">英:/'daʊtfʊl/ 美:/'daʊtfəl/ </td>
                <td class="export-td">adj. 可疑的；令人生疑的；疑心的；不能确定的</td>
            </tr>
            
             <tr>
                <td class="export-td">1803</td>
                <td class="export-td">bend</td>
                <td class="export-td">英:/bend/ 美:/bɛnd/ </td>
                <td class="export-td">1. vt. 使弯曲；使屈服；使致力；使朝向
2. vi. 弯曲，转弯；屈服；专心于；倾向</td>
            </tr>
            
             <tr>
                <td class="export-td">1804</td>
                <td class="export-td">doubtless</td>
                <td class="export-td">英:/'daʊtlɪs/ 美:/'daʊtləs/ </td>
                <td class="export-td">无疑的, 确定的</td>
            </tr>
            
             <tr>
                <td class="export-td">1805</td>
                <td class="export-td">bank</td>
                <td class="export-td">英:/bæŋk/ 美:/bæŋk/ </td>
                <td class="export-td">1. n. 银行；岸；储库；浅滩
2. vt. 将…存入银行；倾斜转弯</td>
            </tr>
            
             <tr>
                <td class="export-td">1806</td>
                <td class="export-td">bristle</td>
                <td class="export-td">英:/'brisl/ 美:/ˈbrɪsəl/ </td>
                <td class="export-td">1. n. 猪鬃；刚毛
2. vi. 发怒；竖起</td>
            </tr>
            
             <tr>
                <td class="export-td">1807</td>
                <td class="export-td">both</td>
                <td class="export-td">英:/bəʊθ/ 美:/boθ/ </td>
                <td class="export-td">1. adj. 两者的；两个的
2. adv. 又；并；两者皆</td>
            </tr>
            
             <tr>
                <td class="export-td">1808</td>
                <td class="export-td">butter</td>
                <td class="export-td">英:/'bʌtə/ 美:/'bʌtɚ/ </td>
                <td class="export-td">1. vt. 涂黄油于；[口]讨好
2. n. 黄油；奶油；奉承话</td>
            </tr>
            
             <tr>
                <td class="export-td">1809</td>
                <td class="export-td">cotton</td>
                <td class="export-td">英:/ˈkɔtn/ 美:/ˈkɑtn/ </td>
                <td class="export-td">1. n. 棉花；棉线；棉布
2. vi. 和谐；一致；理解；亲近</td>
            </tr>
            
             <tr>
                <td class="export-td">1810</td>
                <td class="export-td">dough</td>
                <td class="export-td">英:/dəʊ/ 美:/do/ </td>
                <td class="export-td">n. 生面团；[美俚]金钱</td>
            </tr>
            
             <tr>
                <td class="export-td">1811</td>
                <td class="export-td">extend</td>
                <td class="export-td">英:/ɪk'stend/ 美:/ɪk'stɛnd/ </td>
                <td class="export-td">1. vt. 延伸；扩大；伸出；给予；推广；使竭尽全力；[律]对…估价
2. vi. 伸展；延伸；扩大；[军]使疏开</td>
            </tr>
            
             <tr>
                <td class="export-td">1812</td>
                <td class="export-td">clown</td>
                <td class="export-td">英:/klaʊn/ 美:/klaʊn/ </td>
                <td class="export-td">1. n. 小丑；乡下人；粗鲁笨拙的人
2. vi. 扮小丑；装傻</td>
            </tr>
            
             <tr>
                <td class="export-td">1813</td>
                <td class="export-td">blouse</td>
                <td class="export-td">英:/'blaʊz/ 美:/blaʊs/ </td>
                <td class="export-td">1. n. 宽松的上衣；女装衬衫
2. vt. 使…宽松下垂</td>
            </tr>
            
             <tr>
                <td class="export-td">1814</td>
                <td class="export-td">disagree</td>
                <td class="export-td">英:/dɪsə'griː/ 美:/ˌdɪsə'ɡri/ </td>
                <td class="export-td">vi. 不一致；不适宜；不同意；争执</td>
            </tr>
            
             <tr>
                <td class="export-td">1815</td>
                <td class="export-td">chew</td>
                <td class="export-td">英:/tʃuː/ 美:/tʃʊ/ </td>
                <td class="export-td">1. n. 咀嚼；咀嚼物
2. vt. 嚼碎，咀嚼</td>
            </tr>
            
             <tr>
                <td class="export-td">1816</td>
                <td class="export-td">doughnut</td>
                <td class="export-td">英:/'dəʊnʌt/ 美:/'do'nʌt/ </td>
                <td class="export-td">n. [计]圆环图；油炸圈饼；电子回旋加速器环状真空室</td>
            </tr>
            
             <tr>
                <td class="export-td">1817</td>
                <td class="export-td">extension</td>
                <td class="export-td">英:/ɪk'stenʃ(ə)n/ 美:/ɪk'stɛnʃən/ </td>
                <td class="export-td">延期</td>
            </tr>
            
             <tr>
                <td class="export-td">1818</td>
                <td class="export-td">blow</td>
                <td class="export-td">英:/bləʊ/ 美:/blo/ </td>
                <td class="export-td">1. n. 吹；殴打；打击
2. vi. 风吹；喘气</td>
            </tr>
            
             <tr>
                <td class="export-td">1819</td>
                <td class="export-td">collector</td>
                <td class="export-td">英:/kə'lektə/ 美:/kə'lɛktɚ/ </td>
                <td class="export-td">收集家, 收税员</td>
            </tr>
            
             <tr>
                <td class="export-td">1820</td>
                <td class="export-td">beneath</td>
                <td class="export-td">英:/bɪ'niːθ/ 美:/bɪ'niθ/ </td>
                <td class="export-td">1. prep. 在…之下
2. adv. 在下方</td>
            </tr>
            
             <tr>
                <td class="export-td">1821</td>
                <td class="export-td">extensive</td>
                <td class="export-td">英:/ɪk'stensɪv/ 美:/ɪk'stɛnsɪv/ </td>
                <td class="export-td">广泛的,广阔的</td>
            </tr>
            
             <tr>
                <td class="export-td">1822</td>
                <td class="export-td">groan</td>
                <td class="export-td">英:/grəʊn/ 美:/ɡron/ </td>
                <td class="export-td">1. vi. 呻吟；抱怨；发吱嘎声
2. vt. 呻吟；抱怨</td>
            </tr>
            
             <tr>
                <td class="export-td">1823</td>
                <td class="export-td">consent</td>
                <td class="export-td">英:/kən'sent/ 美:/kən'sɛnt/ </td>
                <td class="export-td">1. vi. 同意；答应；赞成
2. n. 同意；赞成；（意见等的）一致</td>
            </tr>
            
             <tr>
                <td class="export-td">1824</td>
                <td class="export-td">consequence</td>
                <td class="export-td">英:/'kɒnsɪkw(ə)ns/ 美:/'kɑnsəkwɛns/ </td>
                <td class="export-td">结果,后果</td>
            </tr>
            
             <tr>
                <td class="export-td">1825</td>
                <td class="export-td">grocer</td>
                <td class="export-td">英:/'grəʊsə/ 美:/'ɡrosɚ/ </td>
                <td class="export-td">n. 杂货店；食品商</td>
            </tr>
            
             <tr>
                <td class="export-td">1826</td>
                <td class="export-td">disagreement</td>
                <td class="export-td">英:/dɪsə'ɡriːmənt/ 美:/ˌdɪsə'ɡrimənt/ </td>
                <td class="export-td">异议</td>
            </tr>
            
             <tr>
                <td class="export-td">1827</td>
                <td class="export-td">college</td>
                <td class="export-td">英:/'kɒlɪdʒ/ 美:/'kɑlɪdʒ/ </td>
                <td class="export-td">n. 学院；学会；大学</td>
            </tr>
            
             <tr>
                <td class="export-td">1828</td>
                <td class="export-td">groceries</td>
                <td class="export-td"></td>
                <td class="export-td">杂货店</td>
            </tr>
            
             <tr>
                <td class="export-td">1829</td>
                <td class="export-td">bottle</td>
                <td class="export-td">英:/'bɒt(ə)l/ 美:/'bɑtl/ </td>
                <td class="export-td">1. n. 瓶子；一瓶的容量
2. vt. 把…装入瓶中；控制</td>
            </tr>
            
             <tr>
                <td class="export-td">1830</td>
                <td class="export-td">club</td>
                <td class="export-td">英:/klʌb/ 美:/klʌb/ </td>
                <td class="export-td">1. n. 俱乐部，社团；夜总会；（扑克牌中的）梅花；棍棒
2. vt. 用棍棒打；募集</td>
            </tr>
            
             <tr>
                <td class="export-td">1831</td>
                <td class="export-td">consequently</td>
                <td class="export-td">英:/'kɒnsɪkw(ə)ntlɪ/ 美:/'kɑnsəkwɛntli/ </td>
                <td class="export-td">所以, 因此</td>
            </tr>
            
             <tr>
                <td class="export-td">1832</td>
                <td class="export-td">disappear</td>
                <td class="export-td">英:/dɪsə'pɪə/ 美:/'dɪsə'pɪr/ </td>
                <td class="export-td">消失,灭绝</td>
            </tr>
            
             <tr>
                <td class="export-td">1833</td>
                <td class="export-td">dove</td>
                <td class="export-td">英:/dʌv/ 美:/dov/ </td>
                <td class="export-td">1. n. 鸽子；鸽派人士
2. v. 潜水（dive的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">1834</td>
                <td class="export-td">extent</td>
                <td class="export-td">英:/ɪk'stent/ 美:/ɪk'stɛnt/ </td>
                <td class="export-td">n. 范围；程度；长度</td>
            </tr>
            
             <tr>
                <td class="export-td">1835</td>
                <td class="export-td">collide</td>
                <td class="export-td">英:/kə'laɪd/ 美:/kə'laɪd/ </td>
                <td class="export-td">1. vi. 碰撞；抵触，冲突
2. vt. 使碰撞；使相撞</td>
            </tr>
            
             <tr>
                <td class="export-td">1836</td>
                <td class="export-td">couch</td>
                <td class="export-td">英:/kaʊtʃ/ 美:/kaʊtʃ/ </td>
                <td class="export-td">1. n. 睡椅，长沙发；卧榻；床
2. vi. 蹲伏，埋伏；躺着</td>
            </tr>
            
             <tr>
                <td class="export-td">1837</td>
                <td class="export-td">disappoint</td>
                <td class="export-td">英:/dɪsə'pɒɪnt/ 美:/'dɪsə'pɔɪnt/ </td>
                <td class="export-td">使...失望</td>
            </tr>
            
             <tr>
                <td class="export-td">1838</td>
                <td class="export-td">butterfly</td>
                <td class="export-td">英:/'bʌtəflaɪ/ 美:/'bʌtɚflaɪ/ </td>
                <td class="export-td">蝴蝶,蝶状物,蝶泳</td>
            </tr>
            
             <tr>
                <td class="export-td">1839</td>
                <td class="export-td">disappointed</td>
                <td class="export-td">英:/dɪsə'pɒɪntɪd/ 美:/'dɪsə'pɔɪntɪd/ </td>
                <td class="export-td">失望的</td>
            </tr>
            
             <tr>
                <td class="export-td">1840</td>
                <td class="export-td">buttock</td>
                <td class="export-td">英:/'bʌtək/ 美:/'bʌtək/ </td>
                <td class="export-td">1. n. 半边臀部；船尾
2. vt. 用腰摔</td>
            </tr>
            
             <tr>
                <td class="export-td">1841</td>
                <td class="export-td">chicken</td>
                <td class="export-td">英:/'tʃɪkɪn/ 美:/'tʃɪkɪn/ </td>
                <td class="export-td">1. n. 小鸡；鸡肉；胆小鬼，懦夫
2. adj. 鸡肉的；幼小的；胆怯的</td>
            </tr>
            
             <tr>
                <td class="export-td">1842</td>
                <td class="export-td">conservation</td>
                <td class="export-td">英:/kɒnsə'veɪʃ(ə)n/ 美:/ˌkɑnsɚ'veʃən/ </td>
                <td class="export-td">保护</td>
            </tr>
            
             <tr>
                <td class="export-td">1843</td>
                <td class="export-td">exterior</td>
                <td class="export-td">英:/ɪk'stɪərɪə/ 美:/ɪk'stɪrɪɚ/ </td>
                <td class="export-td">1. adj. 外部的；表面的；外在的
2. n. 外部；表面；外型；外貌</td>
            </tr>
            
             <tr>
                <td class="export-td">1844</td>
                <td class="export-td">disappointing</td>
                <td class="export-td">英:/ˌdɪsəˈpɔɪntɪŋ/ 美:/ˌdɪsə'pɔɪntɪŋ/ </td>
                <td class="export-td">令人失望</td>
            </tr>
            
             <tr>
                <td class="export-td">1845</td>
                <td class="export-td">button</td>
                <td class="export-td">英:/'bʌt(ə)n/ 美:/'bʌtn/ </td>
                <td class="export-td">1. n. [计]按钮；钮扣
2. vt. 扣紧；扣住；在…上装钮扣</td>
            </tr>
            
             <tr>
                <td class="export-td">1846</td>
                <td class="export-td">banker</td>
                <td class="export-td">英:/'bæŋkə/ 美:/'bæŋkɚ/ </td>
                <td class="export-td">n. 银行家；银行业者；掘土工</td>
            </tr>
            
             <tr>
                <td class="export-td">1847</td>
                <td class="export-td">disappointment</td>
                <td class="export-td">英:/dɪsə'pɒɪntm(ə)nt/ 美:/ˌdɪsə'pɔɪntmənt/ </td>
                <td class="export-td">失望</td>
            </tr>
            
             <tr>
                <td class="export-td">1848</td>
                <td class="export-td">crossing</td>
                <td class="export-td">英:/'krɒsɪŋ/ 美:/'krɔsɪŋ/ </td>
                <td class="export-td">1. n. 杂交；十字路口；横渡；横道
2. v. 横越（cross的现在分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1849</td>
                <td class="export-td">bottom</td>
                <td class="export-td">英:/'bɒtəm/ 美:/'bɑtəm/ </td>
                <td class="export-td">1. n. 底部；臀部；末端；尽头
2. adj. 底部的</td>
            </tr>
            
             <tr>
                <td class="export-td">1850</td>
                <td class="export-td">banking</td>
                <td class="export-td">英:/'bæŋkɪŋ/ 美:/'bæŋkɪŋ/ </td>
                <td class="export-td">1. n. 银行业；银行业务；银行家的职业；筑堤
2. v. 把钱存入银行；做银行家；在…边筑堤（bank的现在分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1851</td>
                <td class="export-td">crossroads</td>
                <td class="export-td">英:/ˈkrɔsrəʊdz/ 美:/'krɔsrodz/ </td>
                <td class="export-td">交叉路口, 十字路</td>
            </tr>
            
             <tr>
                <td class="export-td">1852</td>
                <td class="export-td">collision</td>
                <td class="export-td">英:/kə'lɪʒ(ə)n/ 美:/kə'lɪʒən/ </td>
                <td class="export-td">碰撞, 冲突</td>
            </tr>
            
             <tr>
                <td class="export-td">1853</td>
                <td class="export-td">crosswalk</td>
                <td class="export-td">英:/'krɒswɔːk/ 美:/'krɔs'wɔk/ </td>
                <td class="export-td">人行横道</td>
            </tr>
            
             <tr>
                <td class="export-td">1854</td>
                <td class="export-td">bankrupt</td>
                <td class="export-td">英:/'bæŋkrʌpt/ 美:/'bæŋkrʌpt/ </td>
                <td class="export-td">1. adj. 破产的
2. vt. 使破产</td>
            </tr>
            
             <tr>
                <td class="export-td">1855</td>
                <td class="export-td">disapprove</td>
                <td class="export-td">英:/dɪsə'pruːv/ 美:/'dɪsə'prʊv/ </td>
                <td class="export-td">不赞成</td>
            </tr>
            
             <tr>
                <td class="export-td">1856</td>
                <td class="export-td">brittle</td>
                <td class="export-td">英:/'brɪt(ə)l/ 美:/'brɪtl/ </td>
                <td class="export-td">adj. 易碎的，脆弱的；易生气的</td>
            </tr>
            
             <tr>
                <td class="export-td">1857</td>
                <td class="export-td">down</td>
                <td class="export-td">英:/daʊn/ 美:/daʊn/ </td>
                <td class="export-td">1. adv. 向下，下去；在下面
2. adj. 向下的</td>
            </tr>
            
             <tr>
                <td class="export-td">1858</td>
                <td class="export-td">groom</td>
                <td class="export-td">英:/gruːm/ 美:/ɡrum/ </td>
                <td class="export-td">1. vt. 推荐；喂马；整饰
2. n. 马夫；新郎；男仆</td>
            </tr>
            
             <tr>
                <td class="export-td">1859</td>
                <td class="export-td">disapproval</td>
                <td class="export-td">英:/dɪsə'pruːvl/ 美:/'dɪsə'prʊvl/ </td>
                <td class="export-td">不赞成</td>
            </tr>
            
             <tr>
                <td class="export-td">1860</td>
                <td class="export-td">cough</td>
                <td class="export-td">英:/kɔf/ 美:/kɔf/ </td>
                <td class="export-td">1. n. 咳嗽，咳嗽声；咳嗽病
2. vt. 咳出</td>
            </tr>
            
             <tr>
                <td class="export-td">1861</td>
                <td class="export-td">crossword</td>
                <td class="export-td">/'krɔs,wə:d/ </td>
                <td class="export-td">填字游戏</td>
            </tr>
            
             <tr>
                <td class="export-td">1862</td>
                <td class="export-td">could</td>
                <td class="export-td">英:/kəd/ 美:/kəd/ </td>
                <td class="export-td">1. aux. 能够
2. v. 能（can的过去式）</td>
            </tr>
            
             <tr>
                <td class="export-td">1863</td>
                <td class="export-td">groove</td>
                <td class="export-td">英:/gruːv/ 美:/ɡruv/ </td>
                <td class="export-td">1. n. 凹槽，槽；最佳状态；惯例
2. vt. 开槽于</td>
            </tr>
            
             <tr>
                <td class="export-td">1864</td>
                <td class="export-td">conservative</td>
                <td class="export-td">英:/kənˈsə:vətiv/ 美:/kən'sɝvətɪv/ </td>
                <td class="export-td">保守的,守旧的</td>
            </tr>
            
             <tr>
                <td class="export-td">1865</td>
                <td class="export-td">external</td>
                <td class="export-td">英:/ɪk'stɜːn(ə)l/ 美:/ɪk'stɝnl/ </td>
                <td class="export-td">1. adj. 外部的；表面的；外面的；[药]外用的；外国的
2. n. 外部；外面；外观</td>
            </tr>
            
             <tr>
                <td class="export-td">1866</td>
                <td class="export-td">broad</td>
                <td class="export-td">英:/brɔːd/ 美:/brɔd/ </td>
                <td class="export-td">1. adj. 宽的，辽阔的；显著的；大概的
2. n. 宽阔部分</td>
            </tr>
            
             <tr>
                <td class="export-td">1867</td>
                <td class="export-td">colloquial</td>
                <td class="export-td">英:/kə'ləʊkwɪəl/ 美:/kə'lokwɪəl/ </td>
                <td class="export-td">口语的,会话的</td>
            </tr>
            
             <tr>
                <td class="export-td">1868</td>
                <td class="export-td">frustrating</td>
                <td class="export-td">英:/frʌˈstreɪtɪŋ/ 美:/'frʌstretɪŋ/ </td>
                <td class="export-td">泄气</td>
            </tr>
            
             <tr>
                <td class="export-td">1869</td>
                <td class="export-td">banner</td>
                <td class="export-td">英:/'bænə/ 美:/'bænɚ/ </td>
                <td class="export-td">n. 旗帜，横幅；标语</td>
            </tr>
            
             <tr>
                <td class="export-td">1870</td>
                <td class="export-td">clue</td>
                <td class="export-td">英:/kluː/ 美:/klʊ/ </td>
                <td class="export-td">1. n. 线索；（故事等的）情节
2. vt. 为…提供线索；[口]为…提供情况</td>
            </tr>
            
             <tr>
                <td class="export-td">1871</td>
                <td class="export-td">council</td>
                <td class="export-td">英:/'kaʊns(ə)l/ 美:/'kaʊnsl/ </td>
                <td class="export-td">n. 理事会；会议；委员会；顾问班子；地方议会</td>
            </tr>
            
             <tr>
                <td class="export-td">1872</td>
                <td class="export-td">hero</td>
                <td class="export-td">英:/'hɪərəʊ/ 美:/'hɪro/ </td>
                <td class="export-td">n. 英雄；男主角，男主人公</td>
            </tr>
            
             <tr>
                <td class="export-td">1873</td>
                <td class="export-td">fry</td>
                <td class="export-td">英:/fraɪ/ 美:/fraɪ/ </td>
                <td class="export-td">1. n. 鱼苗；油炸食物
2. vt. 油炸；油煎</td>
            </tr>
            
             <tr>
                <td class="export-td">1874</td>
                <td class="export-td">benefit</td>
                <td class="export-td">英:/'benɪfɪt/ 美:/'bɛnɪfɪt/ </td>
                <td class="export-td">1. n. 利益，好处；救济金
2. vt. 有益于，对…有益</td>
            </tr>
            
             <tr>
                <td class="export-td">1875</td>
                <td class="export-td">heroine</td>
                <td class="export-td">英:/'herəʊɪn/ 美:/'hɛroɪn/ </td>
                <td class="export-td">1. n. 女英雄；女杰
2. adj. 英雄式的</td>
            </tr>
            
             <tr>
                <td class="export-td">1876</td>
                <td class="export-td">grope</td>
                <td class="export-td">英:/grəʊp/ 美:/ɡrop/ </td>
                <td class="export-td">1. vi. 摸索；探索
2. vt. 摸索</td>
            </tr>
            
             <tr>
                <td class="export-td">1877</td>
                <td class="export-td">buy</td>
                <td class="export-td">英:/baɪ/ 美:/baɪ/ </td>
                <td class="export-td">1. vt. 购买；获得；贿赂
2. vi. 买，采购</td>
            </tr>
            
             <tr>
                <td class="export-td">1878</td>
                <td class="export-td">chief</td>
                <td class="export-td">英:/tʃiːf/ 美:/tʃif/ </td>
                <td class="export-td">1. n. 酋长；首领；主要部分
2. adj. 主要的；首席的；主任的</td>
            </tr>
            
             <tr>
                <td class="export-td">1879</td>
                <td class="export-td">crouch</td>
                <td class="export-td">英:/kraʊtʃ/ 美:/kraʊtʃ/ </td>
                <td class="export-td">1. vi. 蹲伏，蜷伏；卑躬屈膝
2. vt. 低头；屈膝</td>
            </tr>
            
             <tr>
                <td class="export-td">1880</td>
                <td class="export-td">consider</td>
                <td class="export-td">英:/kən'sɪdə/ 美:/kən'sɪdɚ/ </td>
                <td class="export-td">1. vt. 认为；考虑；细想；考虑到
2. vi. 认为；考虑；细想</td>
            </tr>
            
             <tr>
                <td class="export-td">1881</td>
                <td class="export-td">extinct</td>
                <td class="export-td">英:/ɪk'stɪŋkt/ 美:/ɪk'stɪŋkt/ </td>
                <td class="export-td">1. adj. 灭绝的，绝种的；熄灭的
2. vt. [古]使熄灭</td>
            </tr>
            
             <tr>
                <td class="export-td">1882</td>
                <td class="export-td">buzz</td>
                <td class="export-td">英:/bʌz/ 美:/bʌz/ </td>
                <td class="export-td">1. vt. 使嗡嗡叫；暗中散布
2. vi. 作嗡嗡声；东奔西忙</td>
            </tr>
            
             <tr>
                <td class="export-td">1883</td>
                <td class="export-td">clumsy</td>
                <td class="export-td">英:/'klʌmzɪ/ 美:/'klʌmzi/ </td>
                <td class="export-td">adj. 笨拙的</td>
            </tr>
            
             <tr>
                <td class="export-td">1884</td>
                <td class="export-td">considerable</td>
                <td class="export-td">英:/kən'sɪd(ə)rəb(ə)l/ 美:/kən'sɪdərəbl/ </td>
                <td class="export-td">相当大的</td>
            </tr>
            
             <tr>
                <td class="export-td">1885</td>
                <td class="export-td">extinguish</td>
                <td class="export-td">英:/ɪk'stɪŋgwɪʃ/ 美:/ɪk'stɪŋɡwɪʃ/ </td>
                <td class="export-td">熄减, 消减, 偿清</td>
            </tr>
            
             <tr>
                <td class="export-td">1886</td>
                <td class="export-td">disaster</td>
                <td class="export-td">英:/dɪ'zɑːstə/ 美:/dɪ'zæstɚ/ </td>
                <td class="export-td">n. 不幸；灾难，灾祸</td>
            </tr>
            
             <tr>
                <td class="export-td">1887</td>
                <td class="export-td">bought</td>
                <td class="export-td">英:/bɔːt/ 美:/bɔt/ </td>
                <td class="export-td">v. 买（buy的过去式和过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1888</td>
                <td class="export-td">disastrous</td>
                <td class="export-td">英:/dɪ'zɑːstrəs/ 美:/dɪ'zæstrəs/ </td>
                <td class="export-td">灾难性的</td>
            </tr>
            
             <tr>
                <td class="export-td">1889</td>
                <td class="export-td">heroic</td>
                <td class="export-td">英:/hɪ'rəʊɪk/ 美:/hə'roɪk/ </td>
                <td class="export-td">1. adj. 英勇的；英雄的；记叙英雄及其事迹的；夸张的
2. n. 史诗；英勇行为</td>
            </tr>
            
             <tr>
                <td class="export-td">1890</td>
                <td class="export-td">clung</td>
                <td class="export-td">英:/klʌŋ/ 美:/klʌŋ/ </td>
                <td class="export-td">v. 紧握；贴近；坚持（cling的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1891</td>
                <td class="export-td">crow</td>
                <td class="export-td">英:/krəʊ/ 美:/kro/ </td>
                <td class="export-td">1. vi. 报晓；啼叫
2. n. 乌鸦；鸡鸣；撬棍</td>
            </tr>
            
             <tr>
                <td class="export-td">1892</td>
                <td class="export-td">considerate</td>
                <td class="export-td">英:/kən'sɪd(ə)rət/ 美:/kən'sɪdərət/ </td>
                <td class="export-td">考虑周到的,体谅的</td>
            </tr>
            
             <tr>
                <td class="export-td">1893</td>
                <td class="export-td">count</td>
                <td class="export-td">英:/kaʊnt/ 美:/kaʊnt/ </td>
                <td class="export-td">1. vt. 计算；认为
2. vi. 计数；有价值</td>
            </tr>
            
             <tr>
                <td class="export-td">1894</td>
                <td class="export-td">bent</td>
                <td class="export-td">英:/bent/ 美:/bɛnt/ </td>
                <td class="export-td">1. n. 爱好，嗜好
2. adj. 弯曲的；决心的</td>
            </tr>
            
             <tr>
                <td class="export-td">1895</td>
                <td class="export-td">countable</td>
                <td class="export-td">英:/'kauntəbl/ 美:/ˈkaʊntəbəl/ </td>
                <td class="export-td">可数</td>
            </tr>
            
             <tr>
                <td class="export-td">1896</td>
                <td class="export-td">consideration</td>
                <td class="export-td">英:/kənsɪdə'reɪʃ(ə)n/ 美:/kən,sɪdə'reʃən/ </td>
                <td class="export-td">考虑</td>
            </tr>
            
             <tr>
                <td class="export-td">1897</td>
                <td class="export-td">downhill</td>
                <td class="export-td">英:/daʊn'hɪl/ 美:/ˌdaʊn'hɪl/ </td>
                <td class="export-td">1. adv. 下坡；向下；每况愈下
2. adj. 下坡的；容易的</td>
            </tr>
            
             <tr>
                <td class="export-td">1898</td>
                <td class="export-td">bounce</td>
                <td class="export-td">英:/baʊns/ 美:/baʊns/ </td>
                <td class="export-td">1. n. 弹力；活力；跳
2. vt. 弹跳；使弹起</td>
            </tr>
            
             <tr>
                <td class="export-td">1899</td>
                <td class="export-td">clutch</td>
                <td class="export-td">英:/klʌtʃ/ 美:/klʌtʃ/ </td>
                <td class="export-td">1. n. 控制；手；离合器；紧急关头
2. vi. 攫；企图抓住</td>
            </tr>
            
             <tr>
                <td class="export-td">1900</td>
                <td class="export-td">colonel</td>
                <td class="export-td">英:/'kɜːn(ə)l/ 美:/'kɝnl/ </td>
                <td class="export-td">n. 陆军上校</td>
            </tr>
            
             <tr>
                <td class="export-td">1901</td>
                <td class="export-td">broadcast</td>
                <td class="export-td">英:/'brɔːdkɑːst/ 美:/'brɔdkæst/ </td>
                <td class="export-td">n. 广播; 播音; 广播节目; vt. & vi. 广播, 播放; vt. 传播, 乱传时 态: ...</td>
            </tr>
            
             <tr>
                <td class="export-td">1902</td>
                <td class="export-td">heroin</td>
                <td class="export-td">英:/'herəʊɪn/ 美:/'hɛroɪn/ </td>
                <td class="export-td">n. 海洛因，吗啡</td>
            </tr>
            
             <tr>
                <td class="export-td">1903</td>
                <td class="export-td">download</td>
                <td class="export-td">英:/ˏdaunˈləud/ 美:/ˈdaʊnˌlod/ </td>
                <td class="export-td">vt. 下载</td>
            </tr>
            
             <tr>
                <td class="export-td">1904</td>
                <td class="export-td">child</td>
                <td class="export-td">英:/tʃaɪld/ 美:/tʃaɪld/ </td>
                <td class="export-td">n. 儿童，孩子；子孙；产物</td>
            </tr>
            
             <tr>
                <td class="export-td">1905</td>
                <td class="export-td">crowd</td>
                <td class="export-td">英:/kraʊd/ 美:/kraʊd/ </td>
                <td class="export-td">1. n. 群众,一伙;一堆,许多,大众
2. v. 拥挤,挤满,挤进</td>
            </tr>
            
             <tr>
                <td class="export-td">1906</td>
                <td class="export-td">baptism</td>
                <td class="export-td">英:/'bæptɪz(ə)m/ 美:/'bæptɪzəm/ </td>
                <td class="export-td">n. [宗]洗礼；[喻]严峻考验</td>
            </tr>
            
             <tr>
                <td class="export-td">1907</td>
                <td class="export-td">childhood</td>
                <td class="export-td">英:/'tʃaɪldhʊd/ 美:/'tʃaɪldhʊd/ </td>
                <td class="export-td">童年，幼年</td>
            </tr>
            
             <tr>
                <td class="export-td">1908</td>
                <td class="export-td">counter</td>
                <td class="export-td">英:/'kaʊntə/ 美:/'kaʊntɚ/ </td>
                <td class="export-td">1. n. 柜台；计数器，计算器；计算者
2. adv. 相反地</td>
            </tr>
            
             <tr>
                <td class="export-td">1909</td>
                <td class="export-td">ground</td>
                <td class="export-td">英:/graʊnd/ 美:/ɡraʊnd/ </td>
                <td class="export-td">1. n. 地面；土地；范围；战场
2. vt. 打基础；使搁浅；使接触地面</td>
            </tr>
            
             <tr>
                <td class="export-td">1910</td>
                <td class="export-td">bound</td>
                <td class="export-td">英:/baʊnd/ 美:/baʊnd/ </td>
                <td class="export-td">1. adj. 受约束的；装有封面的；有义务的
2. vt. 束缚；使跳跃</td>
            </tr>
            
             <tr>
                <td class="export-td">1911</td>
                <td class="export-td">broadcloth</td>
                <td class="export-td">英:/'brɔːdklɒθ/ 美:/'brɔd,klɔθ/ </td>
                <td class="export-td">各色细平布</td>
            </tr>
            
             <tr>
                <td class="export-td">1912</td>
                <td class="export-td">downstairs</td>
                <td class="export-td">英:/daʊn'steəz/ 美:/'daʊn'stɛrz/ </td>
                <td class="export-td">楼下的</td>
            </tr>
            
             <tr>
                <td class="export-td">1913</td>
                <td class="export-td">bar</td>
                <td class="export-td">英:/bɑː/ 美:/bɑr/ </td>
                <td class="export-td">1. n. 酒吧；条，棒；障碍
2. vt. 禁止；阻拦</td>
            </tr>
            
             <tr>
                <td class="export-td">1914</td>
                <td class="export-td">crown</td>
                <td class="export-td">英:/kraʊn/ 美:/kraʊn/ </td>
                <td class="export-td">1. n. 王冠；王权；花冠；顶点
2. vt. 加冕；居…之顶；表彰；使圆满完成</td>
            </tr>
            
             <tr>
                <td class="export-td">1915</td>
                <td class="export-td">downtown</td>
                <td class="export-td">英:/'daʊntaʊn/ 美:/'daʊn'taʊn/ </td>
                <td class="export-td">1. adv. 往闹市区；在市区
2. adj. 市中心的</td>
            </tr>
            
             <tr>
                <td class="export-td">1916</td>
                <td class="export-td">consist</td>
                <td class="export-td">英:/kən'sɪst/ 美:/kən'sɪst/ </td>
                <td class="export-td">vi. 组成；在于；符合</td>
            </tr>
            
             <tr>
                <td class="export-td">1917</td>
                <td class="export-td">boundary</td>
                <td class="export-td">英:/'baʊnd(ə)rɪ/ 美:/'baʊndri/ </td>
                <td class="export-td">n. 分界线；边界；范围</td>
            </tr>
            
             <tr>
                <td class="export-td">1918</td>
                <td class="export-td">downward</td>
                <td class="export-td">英:/'daʊnwəd/ 美:/'daʊnwɚd/ </td>
                <td class="export-td">1. adj. 向下的，下降的
2. adv. 向下</td>
            </tr>
            
             <tr>
                <td class="export-td">1919</td>
                <td class="export-td">bar code</td>
                <td class="export-td"></td>
                <td class="export-td"></td>
            </tr>
            
             <tr>
                <td class="export-td">1920</td>
                <td class="export-td">broccoli</td>
                <td class="export-td">英:/'brɒkəlɪ/ 美:/'brɑkəli/ </td>
                <td class="export-td">n. 花椰菜；西兰花</td>
            </tr>
            
             <tr>
                <td class="export-td">1921</td>
                <td class="export-td">barmaid</td>
                <td class="export-td">英:/'bɑːmeɪd/ 美:/'bɑrmed/ </td>
                <td class="export-td">n. 酒吧女侍</td>
            </tr>
            
             <tr>
                <td class="export-td">1922</td>
                <td class="export-td">brochure</td>
                <td class="export-td">英:/'brəʊʃə/ 美:/bro'ʃʊr/ </td>
                <td class="export-td">n. 手册，小册子</td>
            </tr>
            
             <tr>
                <td class="export-td">1923</td>
                <td class="export-td">consistent</td>
                <td class="export-td">英:/kən'sɪst(ə)nt/ 美:/kən'sɪstənt/ </td>
                <td class="export-td">一贯</td>
            </tr>
            
             <tr>
                <td class="export-td">1924</td>
                <td class="export-td">barman</td>
                <td class="export-td">英:/'bɑːmən/ 美:/'bɑrmən/ </td>
                <td class="export-td">n. 酒吧店主；酒吧间招待员</td>
            </tr>
            
             <tr>
                <td class="export-td">1925</td>
                <td class="export-td">bartender</td>
                <td class="export-td">英:/'bɑːtendə/ 美:/'bɑrtɛndɚ/ </td>
                <td class="export-td">酒保</td>
            </tr>
            
             <tr>
                <td class="export-td">1926</td>
                <td class="export-td">colony</td>
                <td class="export-td">英:/'kɒlənɪ/ 美:/'kɑləni/ </td>
                <td class="export-td">n. 殖民地；移民队</td>
            </tr>
            
             <tr>
                <td class="export-td">1927</td>
                <td class="export-td">childish</td>
                <td class="export-td">英:/'tʃaɪldɪʃ/ 美:/'tʃaɪldɪʃ/ </td>
                <td class="export-td">adj. 幼稚的，孩子气的</td>
            </tr>
            
             <tr>
                <td class="export-td">1928</td>
                <td class="export-td">console</td>
                <td class="export-td">英:/kən'səʊl/ 美:/'kɑnsol/ </td>
                <td class="export-td">1. n. 操纵台；控制台
2. vt. 慰藉；安慰</td>
            </tr>
            
             <tr>
                <td class="export-td">1929</td>
                <td class="export-td">herself</td>
                <td class="export-td">英:/hɜː'self/ 美:/hɝ'sɛlf/ </td>
                <td class="export-td">pron. 她自己（she的反身代词）；她亲自</td>
            </tr>
            
             <tr>
                <td class="export-td">1930</td>
                <td class="export-td">beret</td>
                <td class="export-td">英:/'bereɪ/ 美:/bə're/ </td>
                <td class="export-td">n. 贝雷帽</td>
            </tr>
            
             <tr>
                <td class="export-td">1931</td>
                <td class="export-td">chill</td>
                <td class="export-td">英:/tʃɪl/ 美:/tʃɪl/ </td>
                <td class="export-td">1. n. 寒冷；寒心；寒意
2. adj. 寒冷的；冷漠的；扫兴的</td>
            </tr>
            
             <tr>
                <td class="export-td">1932</td>
                <td class="export-td">crucial</td>
                <td class="export-td">英:/'kruːʃ(ə)l/ 美:/'krʊʃəl/ </td>
                <td class="export-td">adj. 决定性的；重要的；定局的；决断的</td>
            </tr>
            
             <tr>
                <td class="export-td">1933</td>
                <td class="export-td">berry</td>
                <td class="export-td">英:/'berɪ/ 美:/'bɛri/ </td>
                <td class="export-td">1. n. 浆果（葡萄，番茄等）
2. vi. 采集浆果</td>
            </tr>
            
             <tr>
                <td class="export-td">1934</td>
                <td class="export-td">extraordinary</td>
                <td class="export-td">英:/ˌɛkstrə'ɔdɪri/ 美:/ɪk'strɔːd(ə)n(ə)rɪ/ </td>
                <td class="export-td">非凡</td>
            </tr>
            
             <tr>
                <td class="export-td">1935</td>
                <td class="export-td">broken</td>
                <td class="export-td">英:/'brəʊk(ə)n/ 美:/'brokən/ </td>
                <td class="export-td">1. adj. 坏掉的；破碎的
2. v. 打碎；折断；损坏（break的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1936</td>
                <td class="export-td">extraordinarily</td>
                <td class="export-td">英:/iks'trɔ:dnrili/ 美:/ɪkˈstr ɔrd n..ˌ ɛrɪlɪ/ </td>
                <td class="export-td">非常</td>
            </tr>
            
             <tr>
                <td class="export-td">1937</td>
                <td class="export-td">hesitate</td>
                <td class="export-td">英:/'hezɪteɪt/ 美:/'hɛzɪtet/ </td>
                <td class="export-td">1. vi. 踌躇，犹豫；不愿
2. vt. 踌躇，犹豫；有疑虑，不愿意</td>
            </tr>
            
             <tr>
                <td class="export-td">1938</td>
                <td class="export-td">bouquet</td>
                <td class="export-td">英:/bʊ'keɪ/ 美:/bu'ke/ </td>
                <td class="export-td">n. 酒香；花束</td>
            </tr>
            
             <tr>
                <td class="export-td">1939</td>
                <td class="export-td">doze</td>
                <td class="export-td">英:/dəʊz/ 美:/doz/ </td>
                <td class="export-td">1. vi. 打瞌睡；假寐
2. vt. 打瞌睡度过</td>
            </tr>
            
             <tr>
                <td class="export-td">1940</td>
                <td class="export-td">discipline</td>
                <td class="export-td">英:/'dɪsɪplɪn/ 美:/'dɪsəplɪn/ </td>
                <td class="export-td">学科</td>
            </tr>
            
             <tr>
                <td class="export-td">1941</td>
                <td class="export-td">chilli</td>
                <td class="export-td">英:/'tʃɪlɪ/ 美:/'tʃɪli/ </td>
                <td class="export-td">n. 红辣椒</td>
            </tr>
            
             <tr>
                <td class="export-td">1942</td>
                <td class="export-td">dozen</td>
                <td class="export-td">英:/'dʌz(ə)n/ 美:/'dʌzn/ </td>
                <td class="export-td">1. n. 十二个，一打
2. adj. 一打的</td>
            </tr>
            
             <tr>
                <td class="export-td">1943</td>
                <td class="export-td">extravagant</td>
                <td class="export-td">英:/ɪk'strævəg(ə)nt/ 美:/ɪk'strævəgənt/ </td>
                <td class="export-td">奢华</td>
            </tr>
            
             <tr>
                <td class="export-td">1944</td>
                <td class="export-td">chime</td>
                <td class="export-td">英:/tʃaɪm/ 美:/tʃaɪm/ </td>
                <td class="export-td">1. vi. 鸣响；和谐
2. vt. 打钟报时；敲出和谐的声音</td>
            </tr>
            
             <tr>
                <td class="export-td">1945</td>
                <td class="export-td">barbecue</td>
                <td class="export-td">英:/'bɑːbɪkjuː/ 美:/'bɑrbɪkju/ </td>
                <td class="export-td">1. n. 烤肉；吃烤肉的野宴
2. vt. 烤肉；烧烤</td>
            </tr>
            
             <tr>
                <td class="export-td">1946</td>
                <td class="export-td">group</td>
                <td class="export-td">英:/gruːp/ 美:/ɡrup/ </td>
                <td class="export-td">1. n. 组；团体
2. adj. 群的；团体的</td>
            </tr>
            
             <tr>
                <td class="export-td">1947</td>
                <td class="export-td">barber</td>
                <td class="export-td">英:/ˈbɑ:bə/ 美:/ˈbɑrbɚ/ </td>
                <td class="export-td">1. vt. 为…理发；修整
2. n. 理发师</td>
            </tr>
            
             <tr>
                <td class="export-td">1948</td>
                <td class="export-td">consonant</td>
                <td class="export-td">英:/'kɒns(ə)nənt/ 美:/'kɑnsənənt/ </td>
                <td class="export-td">辅音</td>
            </tr>
            
             <tr>
                <td class="export-td">1949</td>
                <td class="export-td">blunt</td>
                <td class="export-td">英:/blʌnt/ 美:/blʌnt/ </td>
                <td class="export-td">1. adj. 钝的，不锋利的；生硬的；直率的
2. vt. 使迟钝</td>
            </tr>
            
             <tr>
                <td class="export-td">1950</td>
                <td class="export-td">beside</td>
                <td class="export-td">英:/bɪ'saɪd/ 美:/bɪ'saɪd/ </td>
                <td class="export-td">prep. 在旁边；与…相比；和…无关</td>
            </tr>
            
             <tr>
                <td class="export-td">1951</td>
                <td class="export-td">disco</td>
                <td class="export-td">英:/'dɪskəʊ/ 美:/'dɪsko/ </td>
                <td class="export-td">n. 的士高；迪斯科舞厅</td>
            </tr>
            
             <tr>
                <td class="export-td">1952</td>
                <td class="export-td">chimney</td>
                <td class="export-td">英:/'tʃɪmnɪ/ 美:/'tʃɪmni/ </td>
                <td class="export-td">n. 烟囱</td>
            </tr>
            
             <tr>
                <td class="export-td">1953</td>
                <td class="export-td">besides</td>
                <td class="export-td">英:/bɪ'saɪdz/ 美:/bɪ'saɪdz/ </td>
                <td class="export-td">1. adv. 而且；此外
2. prep. 除…之外</td>
            </tr>
            
             <tr>
                <td class="export-td">1954</td>
                <td class="export-td">extremely</td>
                <td class="export-td">英:/iksˈtri:mli/ 美:/ɪk'strimli/ </td>
                <td class="export-td">极其, 非常</td>
            </tr>
            
             <tr>
                <td class="export-td">1955</td>
                <td class="export-td">crude</td>
                <td class="export-td">英:/kruːd/ 美:/krud/ </td>
                <td class="export-td">1. adj. 粗糙的；粗鲁的；天然的，未加工的
2. n. 天然的物质；原油</td>
            </tr>
            
             <tr>
                <td class="export-td">1956</td>
                <td class="export-td">bow</td>
                <td class="export-td">英:/bəʊ/ 美:/baʊ/ </td>
                <td class="export-td">1. n. 弓；鞠躬；船首
2. vi. 鞠躬；弯腰</td>
            </tr>
            
             <tr>
                <td class="export-td">1957</td>
                <td class="export-td">blush</td>
                <td class="export-td">英:/blʌʃ/ 美:/blʌʃ/ </td>
                <td class="export-td">1. vi. 脸红；感到惭愧
2. n. 脸红；红色；羞愧</td>
            </tr>
            
             <tr>
                <td class="export-td">1958</td>
                <td class="export-td">cruel</td>
                <td class="export-td">英:/krʊəl/ 美:/'kruəl/ </td>
                <td class="export-td">adj. 残酷的，残忍的；使人痛苦的</td>
            </tr>
            
             <tr>
                <td class="export-td">1959</td>
                <td class="export-td">cruelty</td>
                <td class="export-td">英:/'krʊəltɪ/ 美:/'krʊəlti/ </td>
                <td class="export-td">n. 残酷；残酷的行为；残忍</td>
            </tr>
            
             <tr>
                <td class="export-td">1960</td>
                <td class="export-td">column</td>
                <td class="export-td">英:/'kɒləm/ 美:/'kɑləm/ </td>
                <td class="export-td">n. 圆柱，柱形物；纵队，列；专栏</td>
            </tr>
            
             <tr>
                <td class="export-td">1961</td>
                <td class="export-td">bare</td>
                <td class="export-td">英:/beə/ 美:/bɛr/ </td>
                <td class="export-td">1. adj. 空的；赤裸的，无遮蔽的
2. vt. 露出，使赤裸</td>
            </tr>
            
             <tr>
                <td class="export-td">1962</td>
                <td class="export-td">barely</td>
                <td class="export-td">英:/'beəlɪ/ 美:/'bɛrli/ </td>
                <td class="export-td">adv. 仅仅，勉强；几乎不；公开地；贫乏地</td>
            </tr>
            
             <tr>
                <td class="export-td">1963</td>
                <td class="export-td">chimpanzee</td>
                <td class="export-td">英:/tʃɪmpæn'ziː/ 美:/ˌtʃɪmpæn'zi/ </td>
                <td class="export-td">黑猩猩</td>
            </tr>
            
             <tr>
                <td class="export-td">1964</td>
                <td class="export-td">chin</td>
                <td class="export-td">英:/tʃɪn/ 美:/tʃɪn/ </td>
                <td class="export-td">1. n. 下巴；聊天；引体向上动作
2. vt. 用下巴夹住；与…聊天；在单杠上作引体向上动作</td>
            </tr>
            
             <tr>
                <td class="export-td">1965</td>
                <td class="export-td">cruise</td>
                <td class="export-td">英:/kruːz/ 美:/krʊz/ </td>
                <td class="export-td">1. vi. 巡航，巡游；漫游
2. vt. 巡航，巡游；漫游</td>
            </tr>
            
             <tr>
                <td class="export-td">1966</td>
                <td class="export-td">grow</td>
                <td class="export-td">英:/grəʊ/ 美:/ɡro/ </td>
                <td class="export-td">1. vi. 生长；发展；渐渐变得…
2. vt. 种植；使生长；扩展</td>
            </tr>
            
             <tr>
                <td class="export-td">1967</td>
                <td class="export-td">comb</td>
                <td class="export-td">英:/kəʊm/ 美:/kom/ </td>
                <td class="export-td">1. n. 鸡冠；梳子；蜂巢
2. vt. 梳头发；梳毛</td>
            </tr>
            
             <tr>
                <td class="export-td">1968</td>
                <td class="export-td">bronze</td>
                <td class="export-td">英:/brɒnz/ 美:/brɑnz/ </td>
                <td class="export-td">1. n. 青铜；青铜制品；古铜色
2. adj. 青铜色的；青铜制的</td>
            </tr>
            
             <tr>
                <td class="export-td">1969</td>
                <td class="export-td">best</td>
                <td class="export-td">英:/best/ 美:/bɛst/ </td>
                <td class="export-td">1. n. 最好的人，最好的事物；最佳状态
2. adj. 最好的</td>
            </tr>
            
             <tr>
                <td class="export-td">1970</td>
                <td class="export-td">crumb</td>
                <td class="export-td">英:/krʌm/ 美:/krʌm/ </td>
                <td class="export-td">1. n. 面包屑，碎屑；少许
2. vt. 弄碎；捏碎</td>
            </tr>
            
             <tr>
                <td class="export-td">1971</td>
                <td class="export-td">China</td>
                <td class="export-td"></td>
                <td class="export-td">1. n. 瓷器
2. adj. 瓷制的</td>
            </tr>
            
             <tr>
                <td class="export-td">1972</td>
                <td class="export-td">crumble</td>
                <td class="export-td">英:/'krʌmb(ə)l/ 美:/'krʌmbl/ </td>
                <td class="export-td">1. vi. 崩溃；破碎，粉碎
2. vt. 弄碎，粉碎；崩溃</td>
            </tr>
            
             <tr>
                <td class="export-td">1973</td>
                <td class="export-td">hexagon</td>
                <td class="export-td">英:/'heksəg(ə)n/ 美:/'hɛksəɡɑn/ </td>
                <td class="export-td">1. n. 六角形，六边形
2. adj. 成六角的；成六边的</td>
            </tr>
            
             <tr>
                <td class="export-td">1974</td>
                <td class="export-td">crumbly</td>
                <td class="export-td">英:/'krʌmblɪ/ 美:/'krʌmbli/ </td>
                <td class="export-td">adj. 脆的；易碎的</td>
            </tr>
            
             <tr>
                <td class="export-td">1975</td>
                <td class="export-td">bargain</td>
                <td class="export-td">英:/'bɑːgɪn/ 美:/'bɑrɡən/ </td>
                <td class="export-td">1. n. 交易；契约；特价商品
2. vi. 讨价还价；成交</td>
            </tr>
            
             <tr>
                <td class="export-td">1976</td>
                <td class="export-td">brooch</td>
                <td class="export-td">英:/brəʊtʃ/ 美:/brotʃ/ </td>
                <td class="export-td">n. （女用的）胸针，领针</td>
            </tr>
            
             <tr>
                <td class="export-td">1977</td>
                <td class="export-td">countless</td>
                <td class="export-td">英:/'kaʊntlɪs/ 美:/'kaʊntləs/ </td>
                <td class="export-td">无数的，数不尽的</td>
            </tr>
            
             <tr>
                <td class="export-td">1978</td>
                <td class="export-td">disconnect</td>
                <td class="export-td">英:/dɪskə'nekt/ 美:/ˌdɪskə'nɛkt/ </td>
                <td class="export-td">使分离</td>
            </tr>
            
             <tr>
                <td class="export-td">1979</td>
                <td class="export-td">combination</td>
                <td class="export-td">英:/kɒmbɪ'neɪʃ(ə)n/ 美:/ˌkɑmbɪ'neʃən/ </td>
                <td class="export-td">结合,联合，联合体</td>
            </tr>
            
             <tr>
                <td class="export-td">1980</td>
                <td class="export-td">crunch</td>
                <td class="export-td">英:/krʌn(t)ʃ/ 美:/krʌntʃ/ </td>
                <td class="export-td">1. n. 咬碎，咬碎声；扎扎地踏
2. vt. 压碎；嘎扎嘎扎的咬嚼；扎扎地踏过</td>
            </tr>
            
             <tr>
                <td class="export-td">1981</td>
                <td class="export-td">hey</td>
                <td class="export-td">英:/heɪ/ 美:/he/ </td>
                <td class="export-td">1. int. 喂！（引起注意等）；你好！（表示问候）
2. n. 干草（等于hay）</td>
            </tr>
            
             <tr>
                <td class="export-td">1982</td>
                <td class="export-td">country</td>
                <td class="export-td">英:/'kʌntrɪ/ 美:/'kʌntri/ </td>
                <td class="export-td">1. n. 国家；故乡
2. adj. 乡下的；粗野的</td>
            </tr>
            
             <tr>
                <td class="export-td">1983</td>
                <td class="export-td">growth</td>
                <td class="export-td">英:/grəʊθ/ 美:/ɡroθ/ </td>
                <td class="export-td">n. 生长；增长；发展；种植</td>
            </tr>
            
             <tr>
                <td class="export-td">1984</td>
                <td class="export-td">bowl</td>
                <td class="export-td">英:/bəʊl/ 美:/bol/ </td>
                <td class="export-td">1. n. 碗；木球；大酒杯
2. vi. 玩保龄球；滑动；平稳快速移动</td>
            </tr>
            
             <tr>
                <td class="export-td">1985</td>
                <td class="export-td">combine</td>
                <td class="export-td">英:/kəm'baɪn/ 美:/kəm'baɪn/ </td>
                <td class="export-td">1. vt. 使联合，使结合；使化合
2. vi. 联合，结合；化合</td>
            </tr>
            
             <tr>
                <td class="export-td">1986</td>
                <td class="export-td">grub</td>
                <td class="export-td">英:/grʌb/ 美:/ɡrʌb/ </td>
                <td class="export-td">1. vi. 翻掘；搜寻；挖土
2. vt. 挖掘寻找；将某物挖出；根除</td>
            </tr>
            
             <tr>
                <td class="export-td">1987</td>
                <td class="export-td">barge</td>
                <td class="export-td">英:/bɑːdʒ/ 美:/bɑrdʒ/ </td>
                <td class="export-td">1. vi. 蹒跚；闯入
2. n. 驳船；游艇</td>
            </tr>
            
             <tr>
                <td class="export-td">1988</td>
                <td class="export-td">bowling</td>
                <td class="export-td">英:/'bəʊlɪŋ/ 美:/'bolɪŋ/ </td>
                <td class="export-td">1. n. 滚木球戏；保龄球戏
2. v. 打保龄球（bowl的现在分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">1989</td>
                <td class="export-td">grubby</td>
                <td class="export-td">英:/'grʌbɪ/ 美:/'ɡrʌbi/ </td>
                <td class="export-td">adj. 肮脏的；生蛆的；卑鄙的；[方]矮小的</td>
            </tr>
            
             <tr>
                <td class="export-td">1990</td>
                <td class="export-td">chip</td>
                <td class="export-td">英:/tʃɪp/ 美:/tʃɪp/ </td>
                <td class="export-td">1. vt. 削，凿；削成碎片
2. vi. 碎裂；剥落</td>
            </tr>
            
             <tr>
                <td class="export-td">1991</td>
                <td class="export-td">crush</td>
                <td class="export-td">英:/krʌʃ/ 美:/krʌʃ/ </td>
                <td class="export-td">1. vt. 压碎；弄皱，变形；使…挤入
2. vi. 挤；被压碎</td>
            </tr>
            
             <tr>
                <td class="export-td">1992</td>
                <td class="export-td">broom</td>
                <td class="export-td">英:/bruːm/ 美:/brum/ </td>
                <td class="export-td">1. n. 金雀花；扫帚
2. vt. 扫除</td>
            </tr>
            
             <tr>
                <td class="export-td">1993</td>
                <td class="export-td">bet</td>
                <td class="export-td">英:/bet/ 美:/bɛt/ </td>
                <td class="export-td">1. n. 打赌，赌注；被打赌的事物
2. vt. 打赌；敢断定，确信</td>
            </tr>
            
             <tr>
                <td class="export-td">1994</td>
                <td class="export-td">grudge</td>
                <td class="export-td">英:/grʌdʒ/ 美:/ɡrʌdʒ/ </td>
                <td class="export-td">1. vt. 怀恨；吝惜；妒忌；不情愿做
2. n. 怨恨；恶意；妒忌</td>
            </tr>
            
             <tr>
                <td class="export-td">1995</td>
                <td class="export-td">eye</td>
                <td class="export-td">英:/aɪ/ 美:/aɪ/ </td>
                <td class="export-td">1. n. 眼睛；视力；见解，观点；眼光
2. vt. 注视，看</td>
            </tr>
            
             <tr>
                <td class="export-td">1996</td>
                <td class="export-td">constituency</td>
                <td class="export-td">英:/kən'stɪtjʊənsɪ/ 美:/kən'stʃuənsi/ </td>
                <td class="export-td">选区</td>
            </tr>
            
             <tr>
                <td class="export-td">1997</td>
                <td class="export-td">come</td>
                <td class="export-td">英:/kʌm/ 美:/kʌm/ </td>
                <td class="export-td">1. vi. 来；出现；到达；变成；开始；发生
2. vt. 做；假装；将满（…岁）</td>
            </tr>
            
             <tr>
                <td class="export-td">1998</td>
                <td class="export-td">countryside</td>
                <td class="export-td">英:/'kʌntrɪsaɪd/ 美:/'kʌntrɪsaɪd/ </td>
                <td class="export-td">乡下, 农村</td>
            </tr>
            
             <tr>
                <td class="export-td">1999</td>
                <td class="export-td">brother</td>
                <td class="export-td">英:/'brʌðə/ 美:/'brʌðɚ/ </td>
                <td class="export-td">1. n. 兄弟；战友；同事
2. int. [俚]我的老兄！</td>
            </tr>
            
             <tr>
                <td class="export-td">2000</td>
                <td class="export-td">bark</td>
                <td class="export-td">英:/bɑːk/ 美:/bɑrk/ </td>
                <td class="export-td">1. vt. 咆哮；吠叫；[口]咳嗽
2. vi. 厉声说出；高声叫卖</td>
            </tr>
            
             <tr>
                <td class="export-td">2001</td>
                <td class="export-td">box</td>
                <td class="export-td">英:/bɒks/ 美:/bɑks/ </td>
                <td class="export-td">1. n. 箱，盒子；包厢；一拳
2. vi. 拳击</td>
            </tr>
            
             <tr>
                <td class="export-td">2002</td>
                <td class="export-td">gruesome</td>
                <td class="export-td">英:/'gruːs(ə)m/ 美:/ˈɡrusəm/ </td>
                <td class="export-td">adj. 可怕的；阴森的</td>
            </tr>
            
             <tr>
                <td class="export-td">2003</td>
                <td class="export-td">barley</td>
                <td class="export-td">英:/'bɑːlɪ/ 美:/'bɑrli/ </td>
                <td class="export-td">n. [植]大麦</td>
            </tr>
            
             <tr>
                <td class="export-td">2004</td>
                <td class="export-td">constitution</td>
                <td class="export-td">英:/kɒnstɪ'tjuːʃ(ə)n/ 美:/'kɑnstə'tʊʃən/ </td>
                <td class="export-td">组织,宪法,体格</td>
            </tr>
            
             <tr>
                <td class="export-td">2005</td>
                <td class="export-td">cry</td>
                <td class="export-td">英:/kraɪ/ 美:/kraɪ/ </td>
                <td class="export-td">1. vt. 叫喊；哭出；大声说
2. n. 叫喊；叫声；口号；呼叫</td>
            </tr>
            
             <tr>
                <td class="export-td">2006</td>
                <td class="export-td">betray</td>
                <td class="export-td">英:/bɪ'treɪ/ 美:/bɪ'tre/ </td>
                <td class="export-td">vt. 背叛；出卖；泄露（秘密）；露出…迹象</td>
            </tr>
            
             <tr>
                <td class="export-td">2007</td>
                <td class="export-td">couple</td>
                <td class="export-td">英:/'kʌp(ə)l/ 美:/'kʌpl/ </td>
                <td class="export-td">1. n. 数个；对；夫妇
2. vi. 结合；成婚</td>
            </tr>
            
             <tr>
                <td class="export-td">2008</td>
                <td class="export-td">grumble</td>
                <td class="export-td">英:/'grʌmb(ə)l/ 美:/'ɡrʌmbl/ </td>
                <td class="export-td">1. vi. 抱怨；嘟囔
2. n. 怨言</td>
            </tr>
            
             <tr>
                <td class="export-td">2009</td>
                <td class="export-td">chirp</td>
                <td class="export-td">英:/tʃɜːp/ 美:/tʃɝp/ </td>
                <td class="export-td">1. n. 唧唧声；喳喳声；啁啾声
2. vi. 吱喳而鸣；尖声地说；咂嘴打招呼</td>
            </tr>
            
             <tr>
                <td class="export-td">2010</td>
                <td class="export-td">barn</td>
                <td class="export-td">英:/bɑːn/ 美:/bɑrn/ </td>
                <td class="export-td">1. n. 谷仓；车库；畜棚；靶（核反应截面单位）
2. vt. 把…贮存入仓</td>
            </tr>
            
             <tr>
                <td class="export-td">2011</td>
                <td class="export-td">discount</td>
                <td class="export-td">英:/'dɪskaʊnt/ 美:/dɪs'kaʊnt/ </td>
                <td class="export-td">1. n. 折扣；贴现率
2. vi. 打折扣出售商品；贴现</td>
            </tr>
            
             <tr>
                <td class="export-td">2012</td>
                <td class="export-td">brow</td>
                <td class="export-td">英:/braʊ/ 美:/braʊ/ </td>
                <td class="export-td">n. 眉，眉毛；表情；额</td>
            </tr>
            
             <tr>
                <td class="export-td">2013</td>
                <td class="export-td">coupon</td>
                <td class="export-td">英:/'kuːpɒn/ 美:/'kupɑn/ </td>
                <td class="export-td">n. 息票；赠券；联票；配给券</td>
            </tr>
            
             <tr>
                <td class="export-td">2014</td>
                <td class="export-td">courage</td>
                <td class="export-td">英:/'kʌrɪdʒ/ 美:/'kɝɪdʒ/ </td>
                <td class="export-td">n. 勇气；胆量</td>
            </tr>
            
             <tr>
                <td class="export-td">2015</td>
                <td class="export-td">better</td>
                <td class="export-td">英:/'betə/ 美:/'bɛtɚ/ </td>
                <td class="export-td">1. n. 较好者；打赌的人（等于bettor）；长辈
2. adv. 更多的；更好的；较大程度地</td>
            </tr>
            
             <tr>
                <td class="export-td">2016</td>
                <td class="export-td">boxer</td>
                <td class="export-td">英:/'bɒksə/ 美:/'bɑksɚ/ </td>
                <td class="export-td">n. 拳师，拳击手</td>
            </tr>
            
             <tr>
                <td class="export-td">2017</td>
                <td class="export-td">grumpy</td>
                <td class="export-td">英:/'grʌmpɪ/ 美:/ˈɡrʌmpi/ </td>
                <td class="export-td">1. adj. 脾气暴躁的；性情乖戾的
2. n. 脾气坏的人；爱抱怨的人</td>
            </tr>
            
             <tr>
                <td class="export-td">2018</td>
                <td class="export-td">boxing</td>
                <td class="export-td">英:/'bɒksɪŋ/ 美:/'bɑksɪŋ/ </td>
                <td class="export-td">1. n. 拳击；装箱；围模；做箱的材料
2. v. 将…装入盒中（box的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">2019</td>
                <td class="export-td">brown</td>
                <td class="export-td">英:/braun/ 美:/braʊn/ </td>
                <td class="export-td">1. adj. 棕色的，褐色的；太阳晒黑的
2. vi. 变成褐色</td>
            </tr>
            
             <tr>
                <td class="export-td">2020</td>
                <td class="export-td">courgette</td>
                <td class="export-td">英:/kʊə'ʒet/ 美:/kʊr'ʒɛt/ </td>
                <td class="export-td">n. 小胡瓜；一种密生西葫芦</td>
            </tr>
            
             <tr>
                <td class="export-td">2021</td>
                <td class="export-td">discourage</td>
                <td class="export-td">英:/dɪs'kʌrɪdʒ/ 美:/dɪs'kɝɪdʒ/ </td>
                <td class="export-td">使气馁,阻碍</td>
            </tr>
            
             <tr>
                <td class="export-td">2022</td>
                <td class="export-td">between</td>
                <td class="export-td">英:/bɪ'twiːn/ 美:/bɪ'twin/ </td>
                <td class="export-td">1. prep. 在…之间
2. adv. 在中间</td>
            </tr>
            
             <tr>
                <td class="export-td">2023</td>
                <td class="export-td">grunt</td>
                <td class="export-td">英:/grʌnt/ 美:/ɡrʌnt/ </td>
                <td class="export-td">1. n. 呼噜声；咕哝
2. vi. 作呼噜声；发哼声</td>
            </tr>
            
             <tr>
                <td class="export-td">2024</td>
                <td class="export-td">crystal</td>
                <td class="export-td">英:/'krɪst(ə)l/ 美:/'krɪstl/ </td>
                <td class="export-td">1. n. 水晶；结晶，晶体；水晶饰品
2. adj. 水晶的；透明的，清澈的</td>
            </tr>
            
             <tr>
                <td class="export-td">2025</td>
                <td class="export-td">course</td>
                <td class="export-td">英:/kɔːs/ 美:/kɔrs/ </td>
                <td class="export-td">1. n. 进程；过程；道路；一道菜
2. vt. 跑过；追赶</td>
            </tr>
            
             <tr>
                <td class="export-td">2026</td>
                <td class="export-td">eyesight</td>
                <td class="export-td">英:/'aɪsaɪt/ 美:/'aɪsaɪt/ </td>
                <td class="export-td">n. 视力；目力</td>
            </tr>
            
             <tr>
                <td class="export-td">2027</td>
                <td class="export-td">construction</td>
                <td class="export-td">英:/kən'strʌkʃ(ə)n/ 美:/kən'strʌkʃən/ </td>
                <td class="export-td">施工</td>
            </tr>
            
             <tr>
                <td class="export-td">2028</td>
                <td class="export-td">court</td>
                <td class="export-td">英:/kɔːt/ 美:/kɔrt/ </td>
                <td class="export-td">1. n. 法院；朝廷；球场；奉承
2. vt. 向…献殷勤；设法获得；招致（失败、危险等）</td>
            </tr>
            
             <tr>
                <td class="export-td">2029</td>
                <td class="export-td">consul</td>
                <td class="export-td">英:/'kɒns(ə)l/ 美:/'kɑnsl/ </td>
                <td class="export-td">n. 领事；（古罗马的）两执政官之一</td>
            </tr>
            
             <tr>
                <td class="export-td">2030</td>
                <td class="export-td">discover</td>
                <td class="export-td">英:/dɪ'skʌvə/ 美:/dɪ'skʌvɚ/ </td>
                <td class="export-td">1. vt. 发现；发觉
2. vi. 发现</td>
            </tr>
            
             <tr>
                <td class="export-td">2031</td>
                <td class="export-td">beware</td>
                <td class="export-td">英:/bɪ'weə/ 美:/bɪ'wɛr/ </td>
                <td class="export-td">1. vi. 当心，小心
2. vt. 提防；注意，当心</td>
            </tr>
            
             <tr>
                <td class="export-td">2032</td>
                <td class="export-td">discovery</td>
                <td class="export-td">英:/dɪ'skʌv(ə)rɪ/ 美:/dɪ'skʌvəri/ </td>
                <td class="export-td">发现, 发现物</td>
            </tr>
            
             <tr>
                <td class="export-td">2033</td>
                <td class="export-td">bruise</td>
                <td class="export-td">英:/bruːz/ 美:/bruz/ </td>
                <td class="export-td">1. n. 擦伤；挫伤；青肿
2. vt. 使受瘀伤；使受挫伤</td>
            </tr>
            
             <tr>
                <td class="export-td">2034</td>
                <td class="export-td">consult</td>
                <td class="export-td">英:/kən'sʌlt/ 美:/kən'sʌlt/ </td>
                <td class="export-td">1. vt. 商量；查阅；向…请教
2. vi. 请教；商议；当顾问</td>
            </tr>
            
             <tr>
                <td class="export-td">2035</td>
                <td class="export-td">courteous</td>
                <td class="export-td">英:/'kɜːtjəs/ 美:/'kɝtɪəs/ </td>
                <td class="export-td">有礼貌的，殷勤的</td>
            </tr>
            
             <tr>
                <td class="export-td">2036</td>
                <td class="export-td">consultant</td>
                <td class="export-td">英:/kən'sʌlt(ə)nt/ 美:/kən'sʌltənt/ </td>
                <td class="export-td">顾问, 咨询专家</td>
            </tr>
            
             <tr>
                <td class="export-td">2037</td>
                <td class="export-td">barracks</td>
                <td class="export-td">/'bærəks/ </td>
                <td class="export-td">1. n. 兵营，营房；简陋的房子；警察所（barrack的复数）
2. v. 使驻扎军营里；住在工房、棚屋里；（澳）大声鼓噪（barrack的三单形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">2038</td>
                <td class="export-td">courtesy</td>
                <td class="export-td">英:/'kɜːtɪsɪ/ 美:/'kɝtəsi/ </td>
                <td class="export-td">1. n. 礼貌；好意；恩惠
2. adj. 殷勤的；被承认的；出于礼节的</td>
            </tr>
            
             <tr>
                <td class="export-td">2039</td>
                <td class="export-td">beyond</td>
                <td class="export-td">英:/bɪ'jɒnd/ 美:/bɪ'jɑnd/ </td>
                <td class="export-td">1. prep. 超过；越过；在...较远的一边；那一边
2. adv. 在更远处；在远处</td>
            </tr>
            
             <tr>
                <td class="export-td">2040</td>
                <td class="export-td">consume</td>
                <td class="export-td">英:/kən'sjuːm/ 美:/kən'sʊm/ </td>
                <td class="export-td">1. vt. 消耗，消费；使…著迷；挥霍
2. vi. 耗尽，毁灭；耗尽生命</td>
            </tr>
            
             <tr>
                <td class="export-td">2041</td>
                <td class="export-td">comedian</td>
                <td class="export-td">英:/kə'miːdɪən/ 美:/kə'midɪən/ </td>
                <td class="export-td">n. 喜剧演员；滑稽人物</td>
            </tr>
            
             <tr>
                <td class="export-td">2042</td>
                <td class="export-td">comedy</td>
                <td class="export-td">英:/'kɒmɪdɪ/ 美:/'kɑmədi/ </td>
                <td class="export-td">n. 喜剧；喜剧性；有趣的事情</td>
            </tr>
            
             <tr>
                <td class="export-td">2043</td>
                <td class="export-td">consumer</td>
                <td class="export-td">英:/kən'sjuːmə/ 美:/kən'sumɚ/ </td>
                <td class="export-td">n. 用户，顾客；消费者</td>
            </tr>
            
             <tr>
                <td class="export-td">2044</td>
                <td class="export-td">barrel</td>
                <td class="export-td">英:/'bær(ə)l/ 美:/'bærəl/ </td>
                <td class="export-td">1. vt. 把……装入桶内
2. n. 桶；枪管，炮管</td>
            </tr>
            
             <tr>
                <td class="export-td">2045</td>
                <td class="export-td">brush</td>
                <td class="export-td">英:/brʌʃ/ 美:/brʌʃ/ </td>
                <td class="export-td">1. n. 刷子；画笔；毛笔；争吵
2. vt. 刷；画</td>
            </tr>
            
             <tr>
                <td class="export-td">2046</td>
                <td class="export-td">discriminate</td>
                <td class="export-td">英:/dɪ'skrɪmɪneɪt/ 美:/dɪ'skrɪmɪnet/ </td>
                <td class="export-td">区分，区别对待</td>
            </tr>
            
             <tr>
                <td class="export-td">2047</td>
                <td class="export-td">courtyard</td>
                <td class="export-td">英:/'kɔːtjɑːd/ 美:/'kɔrtjɑrd/ </td>
                <td class="export-td">庭院, 院子</td>
            </tr>
            
             <tr>
                <td class="export-td">2048</td>
                <td class="export-td">comfort</td>
                <td class="export-td">英:/ˈkʌmfət/ 美:/ˈkʌmfət/ </td>
                <td class="export-td">1. n. 安慰；舒适；安慰者
2. vt. 安慰；使（痛苦等）缓和</td>
            </tr>
            
             <tr>
                <td class="export-td">2049</td>
                <td class="export-td">barricade</td>
                <td class="export-td">英:/ˌbærɪ'keɪd/ 美:/'bærɪ'ked/ </td>
                <td class="export-td">壅</td>
            </tr>
            
             <tr>
                <td class="export-td">2050</td>
                <td class="export-td">consumption</td>
                <td class="export-td">英:/kən'sʌm(p)ʃ(ə)n/ 美:/kən'sʌmpʃən/ </td>
                <td class="export-td">消费</td>
            </tr>
            
             <tr>
                <td class="export-td">2051</td>
                <td class="export-td">barrier</td>
                <td class="export-td">英:/'bærɪə/ 美:/'bærɪɚ/ </td>
                <td class="export-td">1. n. 障碍物，屏障；界线
2. vt. 把…关入栅栏</td>
            </tr>
            
             <tr>
                <td class="export-td">2052</td>
                <td class="export-td">chocolate</td>
                <td class="export-td">英:/'tʃɒk(ə)lət/ 美:/'tʃɑklət/ </td>
                <td class="export-td">巧克力</td>
            </tr>
            
             <tr>
                <td class="export-td">2053</td>
                <td class="export-td">comfortable</td>
                <td class="export-td">英:/'kʌmf(ə)təb(ə)l/ 美:/'kʌmftəbl/ </td>
                <td class="export-td">舒适的,充裕的</td>
            </tr>
            
             <tr>
                <td class="export-td">2054</td>
                <td class="export-td">discuss</td>
                <td class="export-td">英:/dɪ'skʌs/ 美:/dɪ'skʌs/ </td>
                <td class="export-td">vt. 讨论；论述，辩论</td>
            </tr>
            
             <tr>
                <td class="export-td">2055</td>
                <td class="export-td">choice</td>
                <td class="export-td">英:/tʃɒɪs/ 美:/tʃɔɪs/ </td>
                <td class="export-td">1. n. 选择；选择权；精选品
2. adj. 精选的；仔细推敲的</td>
            </tr>
            
             <tr>
                <td class="export-td">2056</td>
                <td class="export-td">discussion</td>
                <td class="export-td">英:/dɪ'skʌʃ(ə)n/ 美:/dɪ'skʌʃən/ </td>
                <td class="export-td">讨论,辩论</td>
            </tr>
            
             <tr>
                <td class="export-td">2057</td>
                <td class="export-td">contact</td>
                <td class="export-td">英:/'kɒntækt/ 美:/'kəntækt/ </td>
                <td class="export-td">1. n. 接触，联系
2. vt. 使接触</td>
            </tr>
            
             <tr>
                <td class="export-td">2058</td>
                <td class="export-td">brutal</td>
                <td class="export-td">英:/'bruːt(ə)l/ 美:/'brutl/ </td>
                <td class="export-td">adj. 残忍的；野蛮的，不讲理的</td>
            </tr>
            
             <tr>
                <td class="export-td">2059</td>
                <td class="export-td">choir</td>
                <td class="export-td">英:/'kwaɪə/ 美:/'kwaɪɚ/ </td>
                <td class="export-td">1. n. 合唱队；唱诗班；舞蹈队
2. vt. 合唱</td>
            </tr>
            
             <tr>
                <td class="export-td">2060</td>
                <td class="export-td">comic</td>
                <td class="export-td">英:/'kɒmɪk/ 美:/'kɑmɪk/ </td>
                <td class="export-td">1. adj. 喜剧的；有趣的；滑稽的
2. n. 喜剧演员；连环漫画；滑稽人物</td>
            </tr>
            
             <tr>
                <td class="export-td">2061</td>
                <td class="export-td">contagious</td>
                <td class="export-td">英:/kən'teɪdʒəs/ 美:/kən'tedʒəs/ </td>
                <td class="export-td">传染性的</td>
            </tr>
            
             <tr>
                <td class="export-td">2062</td>
                <td class="export-td">cover</td>
                <td class="export-td">英:/'kʌvə/ 美:/'kʌvɚ/ </td>
                <td class="export-td">1. vt. 包括；涉及；采访，报导
2. n. 盖子；封面，封皮；掩蔽物</td>
            </tr>
            
             <tr>
                <td class="export-td">2063</td>
                <td class="export-td">command</td>
                <td class="export-td">英:/kə'mɑːnd/ 美:/kə'mænd/ </td>
                <td class="export-td">1. vi. 命令，指挥；控制
2. vt. 命令，指挥；控制；远望</td>
            </tr>
            
             <tr>
                <td class="export-td">2064</td>
                <td class="export-td">choke</td>
                <td class="export-td">英:/tʃəʊk/ 美:/tʃok/ </td>
                <td class="export-td">1. vt. 使窒息；呛；阻塞；扑灭；抑制
2. vi. 窒息；阻塞；[口]说不出话来</td>
            </tr>
            
             <tr>
                <td class="export-td">2065</td>
                <td class="export-td">covering</td>
                <td class="export-td">英:/'kʌv(ə)rɪŋ/ 美:/'kʌvərɪŋ/ </td>
                <td class="export-td">1. adj. 掩盖的，掩护的
2. n. 遮盖物，覆盖物</td>
            </tr>
            
             <tr>
                <td class="export-td">2066</td>
                <td class="export-td">contain</td>
                <td class="export-td">英:/kən'teɪn/ 美:/kən'ten/ </td>
                <td class="export-td">1. vt. 包含；容纳；控制；牵制（敌军）
2. vi. 含有；自制</td>
            </tr>
            
             <tr>
                <td class="export-td">2067</td>
                <td class="export-td">container</td>
                <td class="export-td">英:/kən'teɪnə/ 美:/kən'tenɚ/ </td>
                <td class="export-td">容器, 集装箱</td>
            </tr>
            
             <tr>
                <td class="export-td">2068</td>
                <td class="export-td">base</td>
                <td class="export-td">英:/beɪs/ 美:/bes/ </td>
                <td class="export-td">1. n. 底部；垒；基础
2. adj. 卑鄙的；低劣的</td>
            </tr>
            
             <tr>
                <td class="export-td">2069</td>
                <td class="export-td">choose</td>
                <td class="export-td">英:/tʃuːz/ 美:/tʃuz/ </td>
                <td class="export-td">1. vt. 选择，决定
2. vi. 选择，挑选</td>
            </tr>
            
             <tr>
                <td class="export-td">2070</td>
                <td class="export-td">coveralls</td>
                <td class="export-td">/'kʌvɚ'ɔlz/ </td>
                <td class="export-td">工作服</td>
            </tr>
            
             <tr>
                <td class="export-td">2071</td>
                <td class="export-td">chop</td>
                <td class="export-td">英:/tʃɒp/ 美:/tʃɑp/ </td>
                <td class="export-td">1. n. 砍；排骨；商标；[网]削球
2. vt. 剁碎；砍</td>
            </tr>
            
             <tr>
                <td class="export-td">2072</td>
                <td class="export-td">baseball</td>
                <td class="export-td">英:/ˈbeisbɔ:l/ 美:/'besbɔl/ </td>
                <td class="export-td">n. 棒球运动；棒球</td>
            </tr>
            
             <tr>
                <td class="export-td">2073</td>
                <td class="export-td">basement</td>
                <td class="export-td">英:/'beɪsm(ə)nt/ 美:/'besmənt/ </td>
                <td class="export-td">n. 地下室；地窖</td>
            </tr>
            
             <tr>
                <td class="export-td">2074</td>
                <td class="export-td">bases</td>
                <td class="export-td">英:/'beɪsiːz/ 美:/'besiz/ </td>
                <td class="export-td">n. 主要成分；根据；基础（base的复数形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">2075</td>
                <td class="export-td">contemporary</td>
                <td class="export-td">英:/kən'temp(ə)r(ər)ɪ/ 美:/kən'tɛmpərɛri/ </td>
                <td class="export-td">同时代的人</td>
            </tr>
            
             <tr>
                <td class="export-td">2076</td>
                <td class="export-td">cow</td>
                <td class="export-td">英:/kaʊ/ 美:/kaʊ/ </td>
                <td class="export-td">1. n. 奶牛，母牛；母兽
2. vt. 威胁，恐吓</td>
            </tr>
            
             <tr>
                <td class="export-td">2077</td>
                <td class="export-td">basic</td>
                <td class="export-td">英:/'beɪsɪk/ 美:/'besɪk/ </td>
                <td class="export-td">1. adj. 基本的；基础的
2. n. 基础；要素</td>
            </tr>
            
             <tr>
                <td class="export-td">2078</td>
                <td class="export-td">basically</td>
                <td class="export-td">英:/ˈbeisikəli/ 美:/'besɪkli/ </td>
                <td class="export-td">基本上, 主要地</td>
            </tr>
            
             <tr>
                <td class="export-td">2079</td>
                <td class="export-td">disgrace</td>
                <td class="export-td">英:/dɪs'greɪs/ 美:/dɪs'ɡres/ </td>
                <td class="export-td">1. n. 耻辱；丢脸的人或事；失宠
2. vt. 使……失宠；给……丢脸；使……蒙受耻辱；贬黜</td>
            </tr>
            
             <tr>
                <td class="export-td">2080</td>
                <td class="export-td">comment</td>
                <td class="export-td">英:/'kɒment/ 美:/'kɑmɛnt/ </td>
                <td class="export-td">1. n. 评论；意见；批评
2. vi. 发表评论；发表意见</td>
            </tr>
            
             <tr>
                <td class="export-td">2081</td>
                <td class="export-td">content</td>
                <td class="export-td">英:/kən'tent/ 美:/'kɑntɛnt/ </td>
                <td class="export-td">1. n. 内容，目录；容量；满足
2. adj. 满意的</td>
            </tr>
            
             <tr>
                <td class="export-td">2082</td>
                <td class="export-td">disgraceful</td>
                <td class="export-td">英:/dɪs'greɪsfʊl/ 美:/dɪs'ɡresfl/ </td>
                <td class="export-td">可耻的, 不名誉的</td>
            </tr>
            
             <tr>
                <td class="export-td">2083</td>
                <td class="export-td">commentary</td>
                <td class="export-td">英:/ˈkɔmentəri/ 美:/'kɑməntɛri/ </td>
                <td class="export-td">评论</td>
            </tr>
            
             <tr>
                <td class="export-td">2084</td>
                <td class="export-td">commentator</td>
                <td class="export-td">英:/'kɒmənteɪtə/ 美:/'kɑmən'tetɚ/ </td>
                <td class="export-td">评论员</td>
            </tr>
            
             <tr>
                <td class="export-td">2085</td>
                <td class="export-td">disguise</td>
                <td class="export-td">英:/dɪs'gaɪz/ 美:/dɪs'ɡaɪz/ </td>
                <td class="export-td">1. vt. 假装；掩饰；隐瞒
2. n. 伪装；假装；用作伪装的东西</td>
            </tr>
            
             <tr>
                <td class="export-td">2086</td>
                <td class="export-td">basin</td>
                <td class="export-td">英:/'beɪs(ə)n/ 美:/'besn/ </td>
                <td class="export-td">n. 盆地；盆；水池；流域</td>
            </tr>
            
             <tr>
                <td class="export-td">2087</td>
                <td class="export-td">disgust</td>
                <td class="export-td">英:/dɪs'gʌst/ 美:/dɪs'ɡʌst/ </td>
                <td class="export-td">1. n. 厌恶，嫌恶
2. vt. 使作呕；使厌恶</td>
            </tr>
            
             <tr>
                <td class="export-td">2088</td>
                <td class="export-td">chorus</td>
                <td class="export-td">英:/'kɔːrəs/ 美:/'kɔrəs/ </td>
                <td class="export-td">1. n. 合唱队；齐声；歌舞队
2. vt. 合唱；异口同声地说</td>
            </tr>
            
             <tr>
                <td class="export-td">2089</td>
                <td class="export-td">commerce</td>
                <td class="export-td">英:/'kɒmɜːs/ 美:/'kɑmɝs/ </td>
                <td class="export-td">n. 贸易，商业</td>
            </tr>
            
             <tr>
                <td class="export-td">2090</td>
                <td class="export-td">disgusted</td>
                <td class="export-td">英:/dɪsˈgʌstɪd/ 美:/dɪs'ɡʌstɪd/ </td>
                <td class="export-td">厌恶的</td>
            </tr>
            
             <tr>
                <td class="export-td">2091</td>
                <td class="export-td">commercial</td>
                <td class="export-td">英:/kə'mɜːʃ(ə)l/ 美:/kə'mɝʃəl/ </td>
                <td class="export-td">商业的; 商业广告</td>
            </tr>
            
             <tr>
                <td class="export-td">2092</td>
                <td class="export-td">basis</td>
                <td class="export-td">英:/'beɪsɪs/ 美:/'besɪs/ </td>
                <td class="export-td">n. 底部；基础；主要成分；基本原则或原理</td>
            </tr>
            
             <tr>
                <td class="export-td">2093</td>
                <td class="export-td">basket</td>
                <td class="export-td">英:/'bɑːskɪt/ 美:/'bæskɪt/ </td>
                <td class="export-td">1. n. 篮子；（篮球比赛的）得分；一篮之量；篮筐
2. vt. 装入篮</td>
            </tr>
            
             <tr>
                <td class="export-td">2094</td>
                <td class="export-td">disgusting</td>
                <td class="export-td">英:/dɪsˈgʌstɪŋ/ 美:/dɪs'ɡʌstɪŋ/ </td>
                <td class="export-td">令人厌恶的</td>
            </tr>
            
             <tr>
                <td class="export-td">2095</td>
                <td class="export-td">dish</td>
                <td class="export-td">英:/dɪʃ/ 美:/dɪʃ/ </td>
                <td class="export-td">1. n. 碟，盘；一道菜
2. vt. 把…装盘；使成碟状</td>
            </tr>
            
             <tr>
                <td class="export-td">2096</td>
                <td class="export-td">coward</td>
                <td class="export-td">英:/'kaʊəd/ 美:/'kaʊɚd/ </td>
                <td class="export-td">1. n. 懦夫，懦弱的人
2. adj. 胆小的，懦怯的</td>
            </tr>
            
             <tr>
                <td class="export-td">2097</td>
                <td class="export-td">continent</td>
                <td class="export-td">英:/'kɒntɪnənt/ 美:/'kɑntɪnənt/ </td>
                <td class="export-td">大陆</td>
            </tr>
            
             <tr>
                <td class="export-td">2098</td>
                <td class="export-td">dishcloth</td>
                <td class="export-td">英:/'dɪʃklɒθ/ 美:/'dɪʃklɔθ/ </td>
                <td class="export-td">抹布</td>
            </tr>
            
             <tr>
                <td class="export-td">2099</td>
                <td class="export-td">cowboy</td>
                <td class="export-td">英:/'kaʊbɒɪ/ 美:/'kaʊbɔɪ/ </td>
                <td class="export-td">n. 牧童；牛仔；莽撞的人</td>
            </tr>
            
             <tr>
                <td class="export-td">2100</td>
                <td class="export-td">dishwasher</td>
                <td class="export-td">英:/'dɪʃwɒʃə/ 美:/'dɪʃwɔʃɚ/ </td>
                <td class="export-td">洗碗机</td>
            </tr>
            
             <tr>
                <td class="export-td">2101</td>
                <td class="export-td">bass</td>
                <td class="export-td">英:/bæs/ 美:/bæs/ </td>
                <td class="export-td">1. n. [音]男低音；低音部；[鱼]鲈鱼；[植]椴树
2. adj. 低音的</td>
            </tr>
            
             <tr>
                <td class="export-td">2102</td>
                <td class="export-td">Christ</td>
                <td class="export-td">/kraɪst/ </td>
                <td class="export-td">1. n. 基督；救世主
2. int. 天啊！</td>
            </tr>
            
             <tr>
                <td class="export-td">2103</td>
                <td class="export-td">continual</td>
                <td class="export-td">英:/kən'tɪnjʊəl/ 美:/kən'tɪnjuəl/ </td>
                <td class="export-td">不断的, 频繁的</td>
            </tr>
            
             <tr>
                <td class="export-td">2104</td>
                <td class="export-td">christening</td>
                <td class="export-td">英:/'krisəniŋ/ 美:/ˈkrɪsənɪŋ/ </td>
                <td class="export-td">洗礼</td>
            </tr>
            
             <tr>
                <td class="export-td">2105</td>
                <td class="export-td">Christian</td>
                <td class="export-td">英:/'krɪstɪən/ 美:/'krɪstʃən/ </td>
                <td class="export-td">基督教</td>
            </tr>
            
             <tr>
                <td class="export-td">2106</td>
                <td class="export-td">commit</td>
                <td class="export-td">英:/kə'mɪt/ 美:/kə'mɪt/ </td>
                <td class="export-td">vt. 把...交托给；指派…作战；使…承担义务；犯罪，做错事</td>
            </tr>
            
             <tr>
                <td class="export-td">2107</td>
                <td class="export-td">continue</td>
                <td class="export-td">英:/kən'tɪnjuː/ 美:/kən'tɪnju/ </td>
                <td class="export-td">1. vi. 仍旧，连续；继续，延续
2. vt. 继续说…；使…继续；使…延长</td>
            </tr>
            
             <tr>
                <td class="export-td">2108</td>
                <td class="export-td">Christianity</td>
                <td class="export-td">/ˌkristi'ænəti/ </td>
                <td class="export-td">基督教, 基督教精神</td>
            </tr>
            
             <tr>
                <td class="export-td">2109</td>
                <td class="export-td">committed</td>
                <td class="export-td">英:/kə'mɪtɪd/ 美:/ kəˈmɪtɪd/ </td>
                <td class="export-td">承诺</td>
            </tr>
            
             <tr>
                <td class="export-td">2110</td>
                <td class="export-td">dishonest</td>
                <td class="export-td">英:/dɪs'ɒnɪst/ 美:/dɪs'ɑnɪst/ </td>
                <td class="export-td">不诚实的</td>
            </tr>
            
             <tr>
                <td class="export-td">2111</td>
                <td class="export-td">committee</td>
                <td class="export-td">英:/kə'mɪtɪ/ 美:/kə'mɪti/ </td>
                <td class="export-td">委员会</td>
            </tr>
            
             <tr>
                <td class="export-td">2112</td>
                <td class="export-td">continuous</td>
                <td class="export-td">英:/kən'tɪnjʊəs/ 美:/kən'tɪnjʊəs/ </td>
                <td class="export-td">连续</td>
            </tr>
            
             <tr>
                <td class="export-td">2113</td>
                <td class="export-td">bat</td>
                <td class="export-td">英:/bæt/ 美:/bæt/ </td>
                <td class="export-td">1. n. 蝙蝠；球棒；批处理文件的扩展名
2. vt. 用球棒击球；击球率达…</td>
            </tr>
            
             <tr>
                <td class="export-td">2114</td>
                <td class="export-td">Christmas</td>
                <td class="export-td">英:/ˈkrisməs/ 美:/ˈkrɪsməs/ </td>
                <td class="export-td">圣诞节</td>
            </tr>
            
             <tr>
                <td class="export-td">2115</td>
                <td class="export-td">batch</td>
                <td class="export-td">英:/bætʃ/ 美:/bætʃ/ </td>
                <td class="export-td">1. n. 一批；一炉；一次所制之量
2. vt. 分批处理</td>
            </tr>
            
             <tr>
                <td class="export-td">2116</td>
                <td class="export-td">common</td>
                <td class="export-td">英:/'kɒmən/ 美:/'kɑmən/ </td>
                <td class="export-td">1. adj. 普通的；共同的；通常的；一般的
2. n. 平民；普通；公有地</td>
            </tr>
            
             <tr>
                <td class="export-td">2117</td>
                <td class="export-td">cozy</td>
                <td class="export-td">英:/ˈkəuzi/ 美:/'kozi/ </td>
                <td class="export-td">adj. 舒适的，惬意的</td>
            </tr>
            
             <tr>
                <td class="export-td">2118</td>
                <td class="export-td">bathroom</td>
                <td class="export-td">英:/'bɑːθruːm/ 美:/'bæθrum/ </td>
                <td class="export-td">n. 浴室；厕所；盥洗室</td>
            </tr>
            
             <tr>
                <td class="export-td">2119</td>
                <td class="export-td">disinfectant</td>
                <td class="export-td">英:/dɪsɪn'fekt(ə)nt/ 美:/'dɪsɪn'fɛktənt/ </td>
                <td class="export-td">消毒的; 消毒剂</td>
            </tr>
            
             <tr>
                <td class="export-td">2120</td>
                <td class="export-td">contraceptive</td>
                <td class="export-td">英:/kɒntrə'septɪv/ 美:/'kɑntrə'sɛptɪv/ </td>
                <td class="export-td">避孕的</td>
            </tr>
            
             <tr>
                <td class="export-td">2121</td>
                <td class="export-td">contract</td>
                <td class="export-td">英:/'kɒntrækt/ 美:/'kɑntrækt/ </td>
                <td class="export-td">1. vi. 感染；订约；收缩
2. vt. 感染；订约；使缩短</td>
            </tr>
            
             <tr>
                <td class="export-td">2122</td>
                <td class="export-td">bathe</td>
                <td class="export-td">英:/beɪð/ 美:/beð/ </td>
                <td class="export-td">1. vt. 沐浴；用水洗
2. vi. 洗澡；沐浴</td>
            </tr>
            
             <tr>
                <td class="export-td">2123</td>
                <td class="export-td">contradict</td>
                <td class="export-td">英:/kɒntrə'dɪkt/ 美:/'kɑntrə'dɪkt/ </td>
                <td class="export-td">反驳,与...矛盾</td>
            </tr>
            
             <tr>
                <td class="export-td">2124</td>
                <td class="export-td">communicate</td>
                <td class="export-td">英:/kə'mjuːnɪkeɪt/ 美:/kə'mjunɪket/ </td>
                <td class="export-td">传达, 传播</td>
            </tr>
            
             <tr>
                <td class="export-td">2125</td>
                <td class="export-td">communication</td>
                <td class="export-td">英:/kəmjuːnɪ'keɪʃ(ə)n/ 美:/kə,mjunɪ'keʃən/ </td>
                <td class="export-td">通讯</td>
            </tr>
            
             <tr>
                <td class="export-td">2126</td>
                <td class="export-td">contrary</td>
                <td class="export-td">英:/'kɒntrərɪ/ 美:/'kɑntrɛri/ </td>
                <td class="export-td">1. adj. 相反的；对立的
2. adv. 相反地</td>
            </tr>
            
             <tr>
                <td class="export-td">2127</td>
                <td class="export-td">battery</td>
                <td class="export-td">英:/'bæt(ə)rɪ/ 美:/'bætri/ </td>
                <td class="export-td">n. 电池，蓄电池</td>
            </tr>
            
             <tr>
                <td class="export-td">2128</td>
                <td class="export-td">disk</td>
                <td class="export-td">英:/dɪsk/ 美:/dɪsk/ </td>
                <td class="export-td">n. 磁盘，磁碟片；圆盘，盘状物；唱片</td>
            </tr>
            
             <tr>
                <td class="export-td">2129</td>
                <td class="export-td">community</td>
                <td class="export-td">英:/kə'mjuːnɪtɪ/ 美:/kə'mjʊnəti/ </td>
                <td class="export-td">社区, 团体 群落</td>
            </tr>
            
             <tr>
                <td class="export-td">2130</td>
                <td class="export-td">contrast</td>
                <td class="export-td">英:/'kɒntrɑːst/ 美:/'kɑntræst/ </td>
                <td class="export-td">1. vi. 对比；形成对照
2. vt. 使对比；使与…对照</td>
            </tr>
            
             <tr>
                <td class="export-td">2131</td>
                <td class="export-td">diskette</td>
                <td class="export-td">英:/dɪ'sket/ 美:/dɪs'kɛt/ </td>
                <td class="export-td">n. 磁盘；软磁盘</td>
            </tr>
            
             <tr>
                <td class="export-td">2132</td>
                <td class="export-td">battle</td>
                <td class="export-td">英:/'bæt(ə)l/ 美:/'bætl/ </td>
                <td class="export-td">1. n. 战役；斗争
2. vi. 作战；斗争</td>
            </tr>
            
             <tr>
                <td class="export-td">2133</td>
                <td class="export-td">chubby</td>
                <td class="export-td">英:/'tʃʌbɪ/ 美:/'tʃʌbi/ </td>
                <td class="export-td">adj. 圆胖的，丰满的</td>
            </tr>
            
             <tr>
                <td class="export-td">2134</td>
                <td class="export-td">dislike</td>
                <td class="export-td">英:/dɪs'laɪk/ 美:/dɪs'laɪk/ </td>
                <td class="export-td">1. vt. 不喜欢，厌恶
2. n. 嫌恶，反感，不喜爱</td>
            </tr>
            
             <tr>
                <td class="export-td">2135</td>
                <td class="export-td">contribute</td>
                <td class="export-td">英:/kən'trɪbjuːt/ 美:/kən'trɪbjut/ </td>
                <td class="export-td">捐助,投稿</td>
            </tr>
            
             <tr>
                <td class="export-td">2136</td>
                <td class="export-td">contribution</td>
                <td class="export-td">英:/kɒntrɪ'bjuːʃ(ə)n/ 美:/ˌkɑntrɪ'bjuʃən/ </td>
                <td class="export-td">贡献,捐款</td>
            </tr>
            
             <tr>
                <td class="export-td">2137</td>
                <td class="export-td">disloyal</td>
                <td class="export-td">英:/dɪs'lɒɪ(ə)l/ 美:/dɪs'lɔɪəl/ </td>
                <td class="export-td">adj. 不忠诚的；不忠的；背叛的</td>
            </tr>
            
             <tr>
                <td class="export-td">2138</td>
                <td class="export-td">commute</td>
                <td class="export-td">英:/kə'mjuːt/ 美:/kə'mjʊt/ </td>
                <td class="export-td">1. vt. 交换；减刑；用……交换；使……变成
2. vi. 通勤；代偿</td>
            </tr>
            
             <tr>
                <td class="export-td">2139</td>
                <td class="export-td">dismal</td>
                <td class="export-td">英:/'dɪzm(ə)l/ 美:/'dɪzməl/ </td>
                <td class="export-td">1. adj. 凄凉的，忧郁的；阴沉的，沉闷的；可怕的
2. n. 低落的情绪</td>
            </tr>
            
             <tr>
                <td class="export-td">2140</td>
                <td class="export-td">dismay</td>
                <td class="export-td">英:/dɪs'meɪ/ 美:/dɪs'me/ </td>
                <td class="export-td">1. n. 沮丧，灰心；惊慌
2. vt. 使惊慌；使沮丧</td>
            </tr>
            
             <tr>
                <td class="export-td">2141</td>
                <td class="export-td">control</td>
                <td class="export-td">英:/kənˈtrəul/ 美:/kənˈtrol/ </td>
                <td class="export-td">1. n. 控制；管理；抑制；操纵装置
2. vt. 控制；管理；抑制</td>
            </tr>
            
             <tr>
                <td class="export-td">2142</td>
                <td class="export-td">dismiss</td>
                <td class="export-td">英:/dɪs'mɪs/ 美:/dɪs'mɪs/ </td>
                <td class="export-td">1. vt. 让...离开；开除；解散；解雇
2. vi. 解散</td>
            </tr>
            
             <tr>
                <td class="export-td">2143</td>
                <td class="export-td">companion</td>
                <td class="export-td">英:/kəm'pænjən/ 美:/kəm'pænɪən/ </td>
                <td class="export-td">同伴</td>
            </tr>
            
             <tr>
                <td class="export-td">2144</td>
                <td class="export-td">chunk</td>
                <td class="export-td">英:/tʃʌŋk/ 美:/tʃʌŋk/ </td>
                <td class="export-td">n. 大块；矮胖的人或物</td>
            </tr>
            
             <tr>
                <td class="export-td">2145</td>
                <td class="export-td">controversial</td>
                <td class="export-td">英:/kɒntrə'vɜːʃ(ə)l/ 美:/ˌkɑntrə'vɝʃl/ </td>
                <td class="export-td">引起争论的,有争议的</td>
            </tr>
            
             <tr>
                <td class="export-td">2146</td>
                <td class="export-td">bay</td>
                <td class="export-td">英:/beɪ/ 美:/be/ </td>
                <td class="export-td">1. n. 海湾；狗吠声
2. vt. 向…吠叫</td>
            </tr>
            
             <tr>
                <td class="export-td">2147</td>
                <td class="export-td">disobedient</td>
                <td class="export-td">英:/dɪsə'biːdɪənt/ 美:/'dɪsə'bidɪənt/ </td>
                <td class="export-td">不服从的, 不顺从的</td>
            </tr>
            
             <tr>
                <td class="export-td">2148</td>
                <td class="export-td">company</td>
                <td class="export-td">英:/'kʌmp(ə)nɪ/ 美:/'kʌmpəni/ </td>
                <td class="export-td">1. n. 公司；陪伴，同伴；连队
2. vi. 交往</td>
            </tr>
            
             <tr>
                <td class="export-td">2149</td>
                <td class="export-td">church</td>
                <td class="export-td">英:/tʃɜːtʃ/ 美:/tʃɝtʃ/ </td>
                <td class="export-td">1. n. 教堂；礼拜；教派
2. adj. 教会的；礼拜的</td>
            </tr>
            
             <tr>
                <td class="export-td">2150</td>
                <td class="export-td">comparable</td>
                <td class="export-td">英:/'kɒmp(ə)rəb(ə)l/ 美:/'kɑmpərəbl/ </td>
                <td class="export-td">可比较的, 比得上的</td>
            </tr>
            
             <tr>
                <td class="export-td">2151</td>
                <td class="export-td">controversy</td>
                <td class="export-td">英:/'kɒntrəvɜːsɪ/ 美:/'kɑntrə'vɝsi/ </td>
                <td class="export-td">争论,争议</td>
            </tr>
            
             <tr>
                <td class="export-td">2152</td>
                <td class="export-td">comparative</td>
                <td class="export-td">英:/kəm'pærətɪv/ 美:/kəm'pærətɪv/ </td>
                <td class="export-td">比较的,相当的</td>
            </tr>
            
             <tr>
                <td class="export-td">2153</td>
                <td class="export-td">disobey</td>
                <td class="export-td">英:/dɪsə'beɪ/ 美:/'dɪsə'be/ </td>
                <td class="export-td">v. 不服从；违反</td>
            </tr>
            
             <tr>
                <td class="export-td">2154</td>
                <td class="export-td">churchyard</td>
                <td class="export-td">英:/'tʃɜːtʃjɑːd/ 美:/'tʃɝtʃ'jɑrd/ </td>
                <td class="export-td">墓地, 境内</td>
            </tr>
            
             <tr>
                <td class="export-td">2155</td>
                <td class="export-td">comparison</td>
                <td class="export-td">英:/kəm'pærɪs(ə)n/ 美:/kəm'pærɪsn/ </td>
                <td class="export-td">比较</td>
            </tr>
            
             <tr>
                <td class="export-td">2156</td>
                <td class="export-td">compartment</td>
                <td class="export-td">英:/kəm'pɑːtm(ə)nt/ 美:/kəm'pɑrtmənt/ </td>
                <td class="export-td">包房</td>
            </tr>
            
             <tr>
                <td class="export-td">2157</td>
                <td class="export-td">compass</td>
                <td class="export-td">英:/'kʌmpəs/ 美:/'kʌmpəs/ </td>
                <td class="export-td">1. n. 指南针，罗盘；圆规
2. vt. 包围</td>
            </tr>
            
             <tr>
                <td class="export-td">2158</td>
                <td class="export-td">convenience</td>
                <td class="export-td">英:/kən'viːnɪəns/ 美:/kən'vinɪəns/ </td>
                <td class="export-td">方便</td>
            </tr>
            
             <tr>
                <td class="export-td">2159</td>
                <td class="export-td">convenient</td>
                <td class="export-td">英:/kən'viːnɪənt/ 美:/kən'vinɪənt/ </td>
                <td class="export-td">方便的</td>
            </tr>
            
             <tr>
                <td class="export-td">2160</td>
                <td class="export-td">convent</td>
                <td class="export-td">英:/'kɒnv(ə)nt/ 美:/'kɑnvɛnt/ </td>
                <td class="export-td">n. 女修道院</td>
            </tr>
            
             <tr>
                <td class="export-td">2161</td>
                <td class="export-td">compete</td>
                <td class="export-td">英:/kəm'piːt/ 美:/kəm'pit/ </td>
                <td class="export-td">vi. 竞争；比赛；对抗</td>
            </tr>
            
             <tr>
                <td class="export-td">2162</td>
                <td class="export-td">competition</td>
                <td class="export-td">英:/kɒmpɪ'tɪʃ(ə)n/ 美:/ˌkɑmpə'tɪʃən/ </td>
                <td class="export-td">比赛,竞争</td>
            </tr>
            
             <tr>
                <td class="export-td">2163</td>
                <td class="export-td">dispenser</td>
                <td class="export-td">英:/dɪ'spensə/ 美:/dɪ'spɛnsɚ/ </td>
                <td class="export-td">饮水机</td>
            </tr>
            
             <tr>
                <td class="export-td">2164</td>
                <td class="export-td">competitive</td>
                <td class="export-td">英:/kəm'petɪtɪv/ 美:/kəm'pɛtətɪv/ </td>
                <td class="export-td">竞争的, 比赛的</td>
            </tr>
            
             <tr>
                <td class="export-td">2165</td>
                <td class="export-td">conversation</td>
                <td class="export-td">英:/kɒnvə'seɪʃ(ə)n/ 美:/ˌkɑnvɚ'seʃən/ </td>
                <td class="export-td">会话,谈话</td>
            </tr>
            
             <tr>
                <td class="export-td">2166</td>
                <td class="export-td">competitor</td>
                <td class="export-td">英:/kəm'petɪtə/ 美:/kəm'pɛtɪtɚ/ </td>
                <td class="export-td">竞争者,对手</td>
            </tr>
            
             <tr>
                <td class="export-td">2167</td>
                <td class="export-td">compile</td>
                <td class="export-td">英:/kəm'paɪl/ 美:/kəm'paɪl/ </td>
                <td class="export-td">vt. 编译；编辑；汇编；编制</td>
            </tr>
            
             <tr>
                <td class="export-td">2168</td>
                <td class="export-td">conversion</td>
                <td class="export-td">英:/kən'vɜːʃ(ə)n/ 美:/kən'vɝʒn/ </td>
                <td class="export-td">转变</td>
            </tr>
            
             <tr>
                <td class="export-td">2169</td>
                <td class="export-td">convert</td>
                <td class="export-td">英:/kən'vɜːt/ 美:/kən'vɝt/ </td>
                <td class="export-td">1. vt. 使转变；转换…；使…改变信仰
2. vi. 转变，变换；皈依；改变信仰</td>
            </tr>
            
             <tr>
                <td class="export-td">2170</td>
                <td class="export-td">complain</td>
                <td class="export-td">英:/kəm'pleɪn/ 美:/kəm'plen/ </td>
                <td class="export-td">1. vi. 发牢骚；投诉；诉说
2. vt. 抱怨；控诉</td>
            </tr>
            
             <tr>
                <td class="export-td">2171</td>
                <td class="export-td">display</td>
                <td class="export-td">英:/dɪ'spleɪ/ 美:/dɪ'sple/ </td>
                <td class="export-td">1. n. 显示；炫耀
2. vt. 显示；陈列；表现</td>
            </tr>
            
             <tr>
                <td class="export-td">2172</td>
                <td class="export-td">complaint</td>
                <td class="export-td">英:/kəm'pleɪnt/ 美:/kəm'plent/ </td>
                <td class="export-td">抱怨</td>
            </tr>
            
             <tr>
                <td class="export-td">2173</td>
                <td class="export-td">convict</td>
                <td class="export-td">英:/kən'vɪkt/ 美:/kən'vɪkt/ </td>
                <td class="export-td">1. vt. 证明…有罪；宣告…有罪
2. n. 罪犯</td>
            </tr>
            
             <tr>
                <td class="export-td">2174</td>
                <td class="export-td">convince</td>
                <td class="export-td">英:/kən'vɪns/ 美:/kən'vɪns/ </td>
                <td class="export-td">vt. 使确信，使信服；说服</td>
            </tr>
            
             <tr>
                <td class="export-td">2175</td>
                <td class="export-td">convinced</td>
                <td class="export-td">英:/kənˈvɪnst/ 美:/kən'vɪnst/ </td>
                <td class="export-td">信服的</td>
            </tr>
            
             <tr>
                <td class="export-td">2176</td>
                <td class="export-td">complete</td>
                <td class="export-td">英:/kəm'pliːt/ 美:/kəm'plit/ </td>
                <td class="export-td">1. adj. 完全的；完整的；彻底的
2. vt. 完成</td>
            </tr>
            
             <tr>
                <td class="export-td">2177</td>
                <td class="export-td">completely</td>
                <td class="export-td">/kəm'pli:tli/ </td>
                <td class="export-td">全然</td>
            </tr>
            
             <tr>
                <td class="export-td">2178</td>
                <td class="export-td">dispose</td>
                <td class="export-td">英:/dɪ'spəʊz/ 美:/dɪ'spoz/ </td>
                <td class="export-td">1. vt. 处理；处置；安排
2. vi. 处理；安排；（能够）决定</td>
            </tr>
            
             <tr>
                <td class="export-td">2179</td>
                <td class="export-td">complex</td>
                <td class="export-td">英:/'kɒmpleks/ 美:/kəm'plɛks/ </td>
                <td class="export-td">1. adj. 复杂的；合成的
2. n. 复合体；综合设施</td>
            </tr>
            
             <tr>
                <td class="export-td">2180</td>
                <td class="export-td">complicated</td>
                <td class="export-td">英:/'kɒmplɪkeɪtɪd/ 美:/'kɑmplɪketɪd/ </td>
                <td class="export-td">复杂的, 难懂的</td>
            </tr>
            
             <tr>
                <td class="export-td">2181</td>
                <td class="export-td">complication</td>
                <td class="export-td">英:/kɒmplɪ'keɪʃ(ə)n/ 美:/ˌkɑmplɪ'keʃən/ </td>
                <td class="export-td">复杂，并发症，纠纷</td>
            </tr>
            
             <tr>
                <td class="export-td">2182</td>
                <td class="export-td">compliment</td>
                <td class="export-td">英:/'kɒmplɪm(ə)nt/ 美:/'kɑmpləmənt/ </td>
                <td class="export-td">称赞,恭维, 致意</td>
            </tr>
            
             <tr>
                <td class="export-td">2183</td>
                <td class="export-td">dispute</td>
                <td class="export-td">英:/dɪ'spjuːt/ 美:/'dɪs'pjʊt/ </td>
                <td class="export-td">1. vt. 辩论；阻止；抗拒；怀疑
2. vi. 争论</td>
            </tr>
            
             <tr>
                <td class="export-td">2184</td>
                <td class="export-td">compose</td>
                <td class="export-td">英:/kəm'pəʊz/ 美:/kəm'poz/ </td>
                <td class="export-td">1. vt. 使平静；构成；写作；排…的版
2. vi. 排字；组成；作曲</td>
            </tr>
            
             <tr>
                <td class="export-td">2185</td>
                <td class="export-td">composer</td>
                <td class="export-td">英:/kəm'pəʊzə/ 美:/kəm'pozɚ/ </td>
                <td class="export-td">n. 作曲家；作家，著作者；设计者</td>
            </tr>
            
             <tr>
                <td class="export-td">2186</td>
                <td class="export-td">composition</td>
                <td class="export-td">英:/kɒmpə'zɪʃ(ə)n/ 美:/ˌkɑmpə'zɪʃən/ </td>
                <td class="export-td">组成</td>
            </tr>
            
             <tr>
                <td class="export-td">2187</td>
                <td class="export-td">compound</td>
                <td class="export-td">英:/'kɒmpaʊnd/ 美:/'kɑmpaʊnd/ </td>
                <td class="export-td">1. vt. 混合；合成；和解妥协；搀合
2. vi. 妥协；和解</td>
            </tr>
            
             <tr>
                <td class="export-td">2188</td>
                <td class="export-td">dissatisfied</td>
                <td class="export-td">英:/dɪs'sætɪsfaɪd/ 美:/dɪs'sætɪsfaɪd/ </td>
                <td class="export-td">不满</td>
            </tr>
            
             <tr>
                <td class="export-td">2189</td>
                <td class="export-td">comprehensive</td>
                <td class="export-td">英:/kɒmprɪ'hensɪv/ 美:/ˌkɑmprɪ'hɛnsɪv/ </td>
                <td class="export-td">全面</td>
            </tr>
            
             <tr>
                <td class="export-td">2190</td>
                <td class="export-td">compression</td>
                <td class="export-td">英:/kəm'preʃ(ə)n/ 美:/kəm'prɛʃən/ </td>
                <td class="export-td">压缩, 压榨, 缩小</td>
            </tr>
            
             <tr>
                <td class="export-td">2191</td>
                <td class="export-td">compromise</td>
                <td class="export-td">英:/'kɒmprəmaɪz/ 美:/'kɑmprəmaɪz/ </td>
                <td class="export-td">妥协</td>
            </tr>
            
             <tr>
                <td class="export-td">2192</td>
                <td class="export-td">compulsory</td>
                <td class="export-td">英:/kəm'pʌls(ə)rɪ/ 美:/kəm'pʌlsəri/ </td>
                <td class="export-td">义务</td>
            </tr>
            
             <tr>
                <td class="export-td">2193</td>
                <td class="export-td">computer</td>
                <td class="export-td">英:/kəm'pjuːtə/ 美:/kəm'pjutɚ/ </td>
                <td class="export-td">n. 电脑；计算机；电子计算机</td>
            </tr>
            
             <tr>
                <td class="export-td">2194</td>
                <td class="export-td">dissolve</td>
                <td class="export-td">英:/dɪ'zɒlv/ 美:/dɪ'zɑlv/ </td>
                <td class="export-td">1. vt. 使溶解；使液化；使分解
2. vi. 溶解；解散；消失</td>
            </tr>
            
             <tr>
                <td class="export-td">2195</td>
                <td class="export-td">distance</td>
                <td class="export-td">英:/'dɪst(ə)ns/ 美:/'dɪstəns/ </td>
                <td class="export-td">1. n. 距离；远方；疏远；间隔
2. vt. 把…远远甩在后面；疏远</td>
            </tr>
            
             <tr>
                <td class="export-td">2196</td>
                <td class="export-td">distant</td>
                <td class="export-td">英:/'dɪst(ə)nt/ 美:/'dɪstənt/ </td>
                <td class="export-td">adj. 遥远的；冷漠的；远隔的</td>
            </tr>
            
             <tr>
                <td class="export-td">2197</td>
                <td class="export-td">distinct</td>
                <td class="export-td">英:/dɪ'stɪŋ(k)t/ 美:/dɪ'stɪŋkt/ </td>
                <td class="export-td">adj. 清楚的；明显的；独特的；有区别的</td>
            </tr>
            
             <tr>
                <td class="export-td">2198</td>
                <td class="export-td">distinguish</td>
                <td class="export-td">英:/dɪ'stɪŋgwɪʃ/ 美:/dɪ'stɪŋɡwɪʃ/ </td>
                <td class="export-td">区分</td>
            </tr>
            
             <tr>
                <td class="export-td">2199</td>
                <td class="export-td">distinguished</td>
                <td class="export-td">英:/dɪ'stɪŋgwɪʃt/ 美:/dɪˈstɪŋɡwɪʃt/ </td>
                <td class="export-td">卓著的</td>
            </tr>
            
             <tr>
                <td class="export-td">2200</td>
                <td class="export-td">distract</td>
                <td class="export-td">英:/dɪ'strækt/ 美:/dɪ'strækt/ </td>
                <td class="export-td">vt. 转移；分心</td>
            </tr>
            
             <tr>
                <td class="export-td">2201</td>
                <td class="export-td">distress</td>
                <td class="export-td">英:/dɪ'stres/ 美:/dɪ'strɛs/ </td>
                <td class="export-td">1. n. 危难，不幸；贫困；悲痛
2. vt. 使悲痛；使贫困</td>
            </tr>
            
             <tr>
                <td class="export-td">2202</td>
                <td class="export-td">distribute</td>
                <td class="export-td">英:/dɪ'strɪbjuːt/ 美:/dɪ'strɪbjut/ </td>
                <td class="export-td">分配,散布</td>
            </tr>
            
             <tr>
                <td class="export-td">2203</td>
                <td class="export-td">district</td>
                <td class="export-td">英:/'dɪstrɪkt/ 美:/'dɪstrɪkt/ </td>
                <td class="export-td">n. 区域；行政区；地方</td>
            </tr>
            
             <tr>
                <td class="export-td">2204</td>
                <td class="export-td">disturb</td>
                <td class="export-td">英:/dɪ'stɜːb/ 美:/dɪ'stɝb/ </td>
                <td class="export-td">1. vt. 打扰；妨碍；弄乱；使不安；使恼怒
2. vi. 打扰；妨碍</td>
            </tr>
            
             <tr>
                <td class="export-td">2205</td>
                <td class="export-td">disturbance</td>
                <td class="export-td">英:/dɪ'stɜːb(ə)ns/ 美:/dɪ'stɝbəns/ </td>
                <td class="export-td">扰乱,骚动</td>
            </tr>
            
             <tr>
                <td class="export-td">2206</td>
                <td class="export-td">disused</td>
                <td class="export-td">/dis'ju:zd/ </td>
                <td class="export-td">1. adj. 废弃不用的
2. v. 废弃（disuse的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">2207</td>
                <td class="export-td">ditch</td>
                <td class="export-td">英:/dɪtʃ/ 美:/dɪtʃ/ </td>
                <td class="export-td">1. vt. 在…上掘沟；把…开入沟里；[俚]丢弃
2. vi. 开沟；掘沟</td>
            </tr>
            
             <tr>
                <td class="export-td">2208</td>
                <td class="export-td">dive</td>
                <td class="export-td">英:/daɪv/ 美:/daɪv/ </td>
                <td class="export-td">1. vi. 跳水；潜水；俯冲；急剧下降
2. n. 潜水；跳水；俯冲；扑</td>
            </tr>
            
             <tr>
                <td class="export-td">2209</td>
                <td class="export-td">diver</td>
                <td class="export-td">英:/'daɪvə/ 美:/'daɪvɚ/ </td>
                <td class="export-td">n. 潜水者；跳水的选手；潜鸟</td>
            </tr>
            
             <tr>
                <td class="export-td">2210</td>
                <td class="export-td">divert</td>
                <td class="export-td">英:/daɪ'vɜːt/ 美:/daɪ'vɝt/ </td>
                <td class="export-td">1. vt. 转移；使…欢娱；使…转向
2. vi. 转移</td>
            </tr>
            
             <tr>
                <td class="export-td">2211</td>
                <td class="export-td">divide</td>
                <td class="export-td">英:/dɪ'vaɪd/ 美:/dɪ'vaɪd/ </td>
                <td class="export-td">1. vt. 分开；划分；除；使产生分歧
2. vi. 分开；意见分歧</td>
            </tr>
            
             <tr>
                <td class="export-td">2212</td>
                <td class="export-td">divine</td>
                <td class="export-td">英:/dɪ'vaɪn/ 美:/dɪ'vaɪn/ </td>
                <td class="export-td">1. adj. 神圣的；非凡的；天赐的；极好的
2. vt. 占卜；预言；用占卜勘探</td>
            </tr>
            
             <tr>
                <td class="export-td">2213</td>
                <td class="export-td">division</td>
                <td class="export-td">英:/dɪ'vɪʒ(ə)n/ 美:/də'vɪʒən/ </td>
                <td class="export-td">n. 除法；部门；分割；师（军队）；[体]赛区</td>
            </tr>
            
             <tr>
                <td class="export-td">2214</td>
                <td class="export-td">divorce</td>
                <td class="export-td">英:/dɪ'vɔːs/ 美:/dɪ'vɔrs/ </td>
                <td class="export-td">1. vt. 使离婚，使分离；与…离婚
2. n. 离婚；分离</td>
            </tr>
            
             <tr>
                <td class="export-td">2215</td>
                <td class="export-td">dizzy</td>
                <td class="export-td">英:/'dɪzɪ/ 美:/'dɪzi/ </td>
                <td class="export-td">1. adj. 晕眩的；昏乱的；使人头晕的；心不在焉的；[口]愚蠢的
2. vt. 使头晕眼花；使混乱；使茫然</td>
            </tr>
            
             <tr>
                <td class="export-td">2216</td>
                <td class="export-td">future</td>
                <td class="export-td">英:/'fjuːtʃə/ 美:/'fjʊtʃɚ/ </td>
                <td class="export-td">1. n. 未来；期货；前途；将来时
2. adj. 将来的，未来的</td>
            </tr>
            
             <tr>
                <td class="export-td">2217</td>
                <td class="export-td">career</td>
                <td class="export-td">英:/kə'rɪə/ 美:/kə'rɪr/ </td>
                <td class="export-td">n. 事业，职业；生涯</td>
            </tr>
            
             <tr>
                <td class="export-td">2218</td>
                <td class="export-td">avoid</td>
                <td class="export-td">英:/ə'vɒɪd/ 美:/ə'vɔɪd/ </td>
                <td class="export-td">vt. 避免；避开，躲避；消除</td>
            </tr>
            
             <tr>
                <td class="export-td">2219</td>
                <td class="export-td">definition</td>
                <td class="export-td">英:/defɪ'nɪʃ(ə)n/ 美:/ˌdɛfɪ'nɪʃən/ </td>
                <td class="export-td">定义, 阐释，清晰度</td>
            </tr>
            
             <tr>
                <td class="export-td">2220</td>
                <td class="export-td">anxious</td>
                <td class="export-td">英:/'æŋ(k)ʃəs/ 美:/'æŋkʃəs/ </td>
                <td class="export-td">adj. 渴望的；担忧的；焦虑的；急切的</td>
            </tr>
            
             <tr>
                <td class="export-td">2221</td>
                <td class="export-td">advanced</td>
                <td class="export-td">英:/æd'vɑːnst/ 美:/əd'vænst/ </td>
                <td class="export-td">1. adj. 高级的；先进的；晚期的；年老的
2. v. 前进；增加；上涨（advance的过去式和过去分词形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">2222</td>
                <td class="export-td">aid</td>
                <td class="export-td">英:/eɪd/ 美:/ed/ </td>
                <td class="export-td">1. n. 帮助；援助；助手；帮助者
2. vt. 帮助；援助；有助于</td>
            </tr>
            
             <tr>
                <td class="export-td">2223</td>
                <td class="export-td">aim</td>
                <td class="export-td">英:/eɪm/ 美:/em/ </td>
                <td class="export-td">1. vt. 把…对准；目的在于；引导
2. vi. 对准目标；打算</td>
            </tr>
            
             <tr>
                <td class="export-td">2224</td>
                <td class="export-td">air</td>
                <td class="export-td">英:/eə/ 美:/ɛr/ </td>
                <td class="export-td">1. n. 空气，大气；曲调；天空；样子
2. vt. 使通风，晾干；夸耀</td>
            </tr>
            
             <tr>
                <td class="export-td">2225</td>
                <td class="export-td">aircraft</td>
                <td class="export-td">英:/'eəkrɑːft/ 美:/'ɛr'kræft/ </td>
                <td class="export-td">n. 飞机，航空器</td>
            </tr>
            
             <tr>
                <td class="export-td">2226</td>
                <td class="export-td">airline</td>
                <td class="export-td">英:/'eəlaɪn/ 美:/'ɛrlaɪn/ </td>
                <td class="export-td">1. n. 航空公司；航线
2. adj. 航线的</td>
            </tr>
            
             <tr>
                <td class="export-td">2227</td>
                <td class="export-td">airplane</td>
                <td class="export-td">英:/'eəpleɪn/ 美:/'ɛr'plen/ </td>
                <td class="export-td">n. 飞机</td>
            </tr>
            
             <tr>
                <td class="export-td">2228</td>
                <td class="export-td">airport</td>
                <td class="export-td">英:/'eəpɔːt/ 美:/'ɛr'pɔrt/ </td>
                <td class="export-td">n. 机场；航空站</td>
            </tr>
            
             <tr>
                <td class="export-td">2229</td>
                <td class="export-td">ambition</td>
                <td class="export-td">英:/æm'bɪʃ(ə)n/ 美:/æm'bɪʃən/ </td>
                <td class="export-td">1. n. 野心，雄心；抱负，志向
2. vt. 有…野心；追求</td>
            </tr>
            
             <tr>
                <td class="export-td">2230</td>
                <td class="export-td">ambulance</td>
                <td class="export-td">英:/'æmbjʊl(ə)ns/ 美:/'æmbjələns/ </td>
                <td class="export-td">救护车</td>
            </tr>
            
             <tr>
                <td class="export-td">2231</td>
                <td class="export-td">among</td>
                <td class="export-td">英:/ə'mʌŋ/ 美:/ə'mʌŋ/ </td>
                <td class="export-td">prep. 在…中间；在…之中</td>
            </tr>
            
             <tr>
                <td class="export-td">2232</td>
                <td class="export-td">amount</td>
                <td class="export-td">英:/ə'maʊnt/ 美:/ə'maʊnt/ </td>
                <td class="export-td">1. vi. 总计，合计；共计；相当于；产生…结果
2. n. 数量；总额，总数</td>
            </tr>
            
             <tr>
                <td class="export-td">2233</td>
                <td class="export-td">amuse</td>
                <td class="export-td">英:/ə'mjuːz/ 美:/ə'mjuz/ </td>
                <td class="export-td">vt. 使发笑；消遣；娱乐；使愉快</td>
            </tr>
            
             <tr>
                <td class="export-td">2234</td>
                <td class="export-td">analyse</td>
                <td class="export-td">英:/'æn(ə)laɪz/ 美:/ˈænəˌlaɪz/ </td>
                <td class="export-td">vt. 分析；分解；细察</td>
            </tr>
            
             <tr>
                <td class="export-td">2235</td>
                <td class="export-td">analysis</td>
                <td class="export-td">英:/ə'nælɪsɪs/ 美:/ə'næləsɪs/ </td>
                <td class="export-td">n. 分析；分解；验定</td>
            </tr>
            
             <tr>
                <td class="export-td">2236</td>
                <td class="export-td">ancestor</td>
                <td class="export-td">英:/'ænsestə/ 美:/'ænsɛstɚ/ </td>
                <td class="export-td">n. 始祖，祖先；被继承人</td>
            </tr>
            
             <tr>
                <td class="export-td">2237</td>
                <td class="export-td">anchor</td>
                <td class="export-td">英:/'æŋkə/ 美:/'æŋkɚ/ </td>
                <td class="export-td">1. n. 锚；靠山；新闻节目主播；抛锚停泊
2. vt. 抛锚；使固定；主持节目</td>
            </tr>
            
             <tr>
                <td class="export-td">2238</td>
                <td class="export-td">ancient</td>
                <td class="export-td">英:/'eɪnʃ(ə)nt/ 美:/'enʃənt/ </td>
                <td class="export-td">1. adj. 古代的；古老的，过时的；年老的
2. n. 老人；古代人</td>
            </tr>
            
             <tr>
                <td class="export-td">2239</td>
                <td class="export-td">and</td>
                <td class="export-td">英:/ənd/ 美:/ənd/ </td>
                <td class="export-td">conj. 和，与；而且；然后；就；但是</td>
            </tr>
            
             <tr>
                <td class="export-td">2240</td>
                <td class="export-td">angel</td>
                <td class="export-td">英:/ˈeɪndʒl/ 美:/ˈendʒəl/ </td>
                <td class="export-td">1. n. 天使；守护神；善人
2. vt. [美俚]出钱支持</td>
            </tr>
            
             <tr>
                <td class="export-td">2241</td>
                <td class="export-td">anger</td>
                <td class="export-td">英:/'æŋgə/ 美:/'æŋɡɚ/ </td>
                <td class="export-td">1. n. 怒，愤怒；忿怒
2. vt. 使发怒，激怒；恼火</td>
            </tr>
            
             <tr>
                <td class="export-td">2242</td>
                <td class="export-td">angle</td>
                <td class="export-td">英:/ˈæŋɡl/ 美:/ˈæŋɡəl/ </td>
                <td class="export-td">1. vi. 钓鱼；谋取
2. n. 角度，角</td>
            </tr>
            
             <tr>
                <td class="export-td">2243</td>
                <td class="export-td">angry</td>
                <td class="export-td">英:/'æŋgrɪ/ 美:/'æŋɡri/ </td>
                <td class="export-td">adj. 生气的；愤怒的；狂暴的；（伤口等）发炎的</td>
            </tr>
            
             <tr>
                <td class="export-td">2244</td>
                <td class="export-td">ankle</td>
                <td class="export-td">英:/'æŋk(ə)l/ 美:/'æŋkl/ </td>
                <td class="export-td">n. 踝关节，踝</td>
            </tr>
            
             <tr>
                <td class="export-td">2245</td>
                <td class="export-td">announce</td>
                <td class="export-td">英:/ə'naʊns/ 美:/ə'naʊns/ </td>
                <td class="export-td">1. vt. 宣布；述说；预示；播报
2. vi. 宣布参加竞选；当播音员</td>
            </tr>
            
             <tr>
                <td class="export-td">2246</td>
                <td class="export-td">announcer</td>
                <td class="export-td">英:/ə'naʊnsə/ 美:/ə'naʊnsɚ/ </td>
                <td class="export-td">广播员, 告知者</td>
            </tr>
            
             <tr>
                <td class="export-td">2247</td>
                <td class="export-td">annoy</td>
                <td class="export-td">英:/ə'nɒɪ/ 美:/ə'nɔɪ/ </td>
                <td class="export-td">1. vt. 骚扰；打搅；惹恼
2. vi. 令人讨厌；打搅；惹恼</td>
            </tr>
            
             <tr>
                <td class="export-td">2248</td>
                <td class="export-td">annual</td>
                <td class="export-td">英:/'ænjʊəl/ 美:/'ænjuəl/ </td>
                <td class="export-td">1. adj. 年度的；每年的
2. n. 年刊，年鉴；一年生植物</td>
            </tr>
            
             <tr>
                <td class="export-td">2249</td>
                <td class="export-td">anticipate</td>
                <td class="export-td">英:/æn'tɪsɪpeɪt/ 美:/æn'tɪsə'pet/ </td>
                <td class="export-td">预料</td>
            </tr>
            
             <tr>
                <td class="export-td">2250</td>
                <td class="export-td">anxiety</td>
                <td class="export-td">英:/æŋ'zaɪətɪ/ 美:/æŋ'zaɪəti/ </td>
                <td class="export-td">n. 焦虑；挂念；渴望；令人焦虑的事</td>
            </tr>
            
             <tr>
                <td class="export-td">2251</td>
                <td class="export-td">any</td>
                <td class="export-td">英:/'enɪ/ 美:/'ɛni/ </td>
                <td class="export-td">1. adj. 任何的；所有的；丝毫
2. pron. 任何；任何一个；若干</td>
            </tr>
            
             <tr>
                <td class="export-td">2252</td>
                <td class="export-td">anybody</td>
                <td class="export-td">英:/'enɪbɒdɪ/ 美:/'ɛnɪbɑdi/ </td>
                <td class="export-td">1. pron. 任何人
2. n. 重要人物</td>
            </tr>
            
             <tr>
                <td class="export-td">2253</td>
                <td class="export-td">anyone</td>
                <td class="export-td">英:/'enɪwʌn/ 美:/'ɛnɪ'wʌn/ </td>
                <td class="export-td">pron. 任何人；任何一个</td>
            </tr>
            
             <tr>
                <td class="export-td">2254</td>
                <td class="export-td">anything</td>
                <td class="export-td">英:/'enɪθɪŋ/ 美:/'ɛnɪ'θɪŋ/ </td>
                <td class="export-td">pron. 任何事</td>
            </tr>
            
             <tr>
                <td class="export-td">2255</td>
                <td class="export-td">anyway</td>
                <td class="export-td">英:/'enɪweɪ/ 美:/'ɛnɪ'we/ </td>
                <td class="export-td">adv. 无论如何，不管怎样；总之</td>
            </tr>
            
             <tr>
                <td class="export-td">2256</td>
                <td class="export-td">argue</td>
                <td class="export-td">英:/'ɑːgjuː/ 美:/'ɑrgjʊ/ </td>
                <td class="export-td">1. vi. 争论，辩论；提出理由
2. vt. 辩论，争论；说服；证明</td>
            </tr>
            
             <tr>
                <td class="export-td">2257</td>
                <td class="export-td">argument</td>
                <td class="export-td">英:/'ɑːgjʊm(ə)nt/ 美:/'ɑrɡjumənt/ </td>
                <td class="export-td">n. 争吵；论据；内容提要；论证</td>
            </tr>
            
             <tr>
                <td class="export-td">2258</td>
                <td class="export-td">arise</td>
                <td class="export-td">英:/ə'raɪz/ 美:/ə'raɪz/ </td>
                <td class="export-td">vi. 出现；起立；上升</td>
            </tr>
            
             <tr>
                <td class="export-td">2259</td>
                <td class="export-td">arithmetic</td>
                <td class="export-td">英:/ə'rɪθmətɪk/ 美:/ə'rɪθmətɪk/ </td>
                <td class="export-td">算术</td>
            </tr>
            
             <tr>
                <td class="export-td">2260</td>
                <td class="export-td">arm</td>
                <td class="export-td">英:/ɑːm/ 美:/ɑrm/ </td>
                <td class="export-td">1. n. 手臂；袖子；武器；装备
2. vi. 武装起来</td>
            </tr>
            
             <tr>
                <td class="export-td">2261</td>
                <td class="export-td">army</td>
                <td class="export-td">英:/'ɑːmɪ/ 美:/'ɑrmi/ </td>
                <td class="export-td">n. 陆军，军队</td>
            </tr>
            
             <tr>
                <td class="export-td">2262</td>
                <td class="export-td">around</td>
                <td class="export-td">英:/ə'raʊnd/ 美:/ə'raʊnd/ </td>
                <td class="export-td">1. adv. 到处；大约；在附近
2. prep. 四处；在…周围</td>
            </tr>
            
             <tr>
                <td class="export-td">2263</td>
                <td class="export-td">arouse</td>
                <td class="export-td">英:/ə'raʊz/ 美:/ə'raʊz/ </td>
                <td class="export-td">1. vt. 引起；鼓励；唤醒
2. vi. 醒来；发奋；激发</td>
            </tr>
            
             <tr>
                <td class="export-td">2264</td>
                <td class="export-td">arrange</td>
                <td class="export-td">英:/ə'reɪn(d)ʒ/ 美:/ə'rendʒ/ </td>
                <td class="export-td">1. vt. 排列；安排；整理
2. vi. 安排；排列；协商</td>
            </tr>
            
             <tr>
                <td class="export-td">2265</td>
                <td class="export-td">arrangement</td>
                <td class="export-td">英:/ə'reɪn(d)ʒm(ə)nt/ 美:/ə'rendʒmənt/ </td>
                <td class="export-td">安排,商议,整理</td>
            </tr>
            
             <tr>
                <td class="export-td">2266</td>
                <td class="export-td">arrest</td>
                <td class="export-td">英:/ə'rest/ 美:/ə'rɛst/ </td>
                <td class="export-td">1. vt. 吸引；逮捕；阻止
2. n. 逮捕；监禁</td>
            </tr>
            
             <tr>
                <td class="export-td">2267</td>
                <td class="export-td">arrival</td>
                <td class="export-td">英:/ə'raɪv(ə)l/ 美:/ə'raɪvəl/ </td>
                <td class="export-td">n. 到达；到达者；到来</td>
            </tr>
            
             <tr>
                <td class="export-td">2268</td>
                <td class="export-td">arrive</td>
                <td class="export-td">英:/ə'raɪv/ 美:/ə'raɪv/ </td>
                <td class="export-td">vi. 到达；成功；出生；达成</td>
            </tr>
            
             <tr>
                <td class="export-td">2269</td>
                <td class="export-td">arrow</td>
                <td class="export-td">英:/'ærəʊ/ 美:/'æro/ </td>
                <td class="export-td">1. n. 箭状物；箭头记号；箭，箭头
2. vt. 以箭头指示；箭一般地飞向</td>
            </tr>
            
             <tr>
                <td class="export-td">2270</td>
                <td class="export-td">art</td>
                <td class="export-td">英:/ɑːt/ 美:/ɑrt/ </td>
                <td class="export-td">1. n. 艺术；美术；艺术品
2. adj. 艺术的；艺术品的</td>
            </tr>
            
             <tr>
                <td class="export-td">2271</td>
                <td class="export-td">article</td>
                <td class="export-td">英:/'ɑːtɪk(ə)l/ 美:/'ɑrtɪkl/ </td>
                <td class="export-td">1. n. 物品；文章；冠词；条款
2. vt. 订约将…收为学徒或见习生；使…受协议条款的约束</td>
            </tr>
            
             <tr>
                <td class="export-td">2272</td>
                <td class="export-td">artificial</td>
                <td class="export-td">英:/ɑːtɪ'fɪʃ(ə)l/ 美:/ˌɑrtɪ'fɪʃl/ </td>
                <td class="export-td">人造的</td>
            </tr>
            
             <tr>
                <td class="export-td">2273</td>
                <td class="export-td">artist</td>
                <td class="export-td">英:/'ɑːtɪst/ 美:/'ɑrtɪst/ </td>
                <td class="export-td">n. 艺术家；美术家（尤指画家）；大师</td>
            </tr>
            
             <tr>
                <td class="export-td">2274</td>
                <td class="export-td">artistic</td>
                <td class="export-td">英:/ɑː'tɪstɪk/ 美:/ɑr'tɪstɪk/ </td>
                <td class="export-td">adj. 艺术的；有美感的；风雅的</td>
            </tr>
            
             <tr>
                <td class="export-td">2275</td>
                <td class="export-td">as</td>
                <td class="export-td">英:/æz/ 美:/əz/ </td>
                <td class="export-td">1. conj. 因为；依照；当…时；随着；虽然
2. prep. 当作；以…的身份；如同</td>
            </tr>
            
             <tr>
                <td class="export-td">2276</td>
                <td class="export-td">ash</td>
                <td class="export-td">英:/æʃ/ 美:/æʃ/ </td>
                <td class="export-td">n. 灰；灰烬</td>
            </tr>
            
             <tr>
                <td class="export-td">2277</td>
                <td class="export-td">ashamed</td>
                <td class="export-td">英:/ə'ʃeɪmd/ 美:/ə'ʃemd/ </td>
                <td class="export-td">adj. 惭愧的，感到难为情的；耻于……的</td>
            </tr>
            
             <tr>
                <td class="export-td">2278</td>
                <td class="export-td">aside</td>
                <td class="export-td">英:/ə'saɪd/ 美:/ə'saɪd/ </td>
                <td class="export-td">1. adv. 在旁边；离开，撇开
2. n. 旁白；私语，悄悄话；离题的话</td>
            </tr>
            
             <tr>
                <td class="export-td">2279</td>
                <td class="export-td">ask</td>
                <td class="export-td">英:/ɑːsk/ 美:/æsk/ </td>
                <td class="export-td">1. vt. 问，询问；邀请；要求；需要；讨价
2. vi. 要求；问，询问</td>
            </tr>
            
             <tr>
                <td class="export-td">2280</td>
                <td class="export-td">asleep</td>
                <td class="export-td">英:/ə'sliːp/ 美:/ə'slip/ </td>
                <td class="export-td">1. adj. 睡着的；麻木的；长眠的
2. adv. 进入睡眠状态；熟睡地</td>
            </tr>
            
             <tr>
                <td class="export-td">2281</td>
                <td class="export-td">assignment</td>
                <td class="export-td">英:/ə'saɪnm(ə)nt/ 美:/ə'saɪnmənt/ </td>
                <td class="export-td">分配</td>
            </tr>
            
             <tr>
                <td class="export-td">2282</td>
                <td class="export-td">assist</td>
                <td class="export-td">英:/ə'sɪst/ 美:/ə'sɪst/ </td>
                <td class="export-td">1. n. 帮助；助攻
2. vi. 参加；出席</td>
            </tr>
            
             <tr>
                <td class="export-td">2283</td>
                <td class="export-td">assistant</td>
                <td class="export-td">英:/ə'sɪst(ə)nt/ 美:/ə'sɪstənt/ </td>
                <td class="export-td">副的; 助手</td>
            </tr>
            
             <tr>
                <td class="export-td">2284</td>
                <td class="export-td">associate</td>
                <td class="export-td">英:/ə'səʊʃɪeɪt/ 美:/ə'soʃɪet/ </td>
                <td class="export-td">关联</td>
            </tr>
            
             <tr>
                <td class="export-td">2285</td>
                <td class="export-td">assume</td>
                <td class="export-td">英:/ə'sjuːm/ 美:/ə'sum/ </td>
                <td class="export-td">1. vt. 假定；承担；呈现；采取
2. vi. 装腔作势；多管闲事</td>
            </tr>
            
             <tr>
                <td class="export-td">2286</td>
                <td class="export-td">assure</td>
                <td class="export-td">英:/ə'ʃʊə/ 美:/ə'ʃʊr/ </td>
                <td class="export-td">vt. 保证；担保；使确信；弄清楚</td>
            </tr>
            
             <tr>
                <td class="export-td">2287</td>
                <td class="export-td">astonish</td>
                <td class="export-td">英:/ə'stɒnɪʃ/ 美:/ə'stɑnɪʃ/ </td>
                <td class="export-td">vt. 使惊讶</td>
            </tr>
            
             <tr>
                <td class="export-td">2288</td>
                <td class="export-td">at</td>
                <td class="export-td">英:/æt/ 美:/ət/ </td>
                <td class="export-td">prep. 在（表示存在或出现的地点、场所、位置、空间）；向；朝；因为；忙于；以（某种价格、速度等）</td>
            </tr>
            
             <tr>
                <td class="export-td">2289</td>
                <td class="export-td">athlete</td>
                <td class="export-td">英:/'æθliːt/ 美:/'æθlit/ </td>
                <td class="export-td">n. 运动员，体育家；身强力壮的人</td>
            </tr>
            
             <tr>
                <td class="export-td">2290</td>
                <td class="export-td">atmosphere</td>
                <td class="export-td">英:/'ætməsfɪə/ 美:/'ætməsfɪr/ </td>
                <td class="export-td">气氛</td>
            </tr>
            
             <tr>
                <td class="export-td">2291</td>
                <td class="export-td">atom</td>
                <td class="export-td">英:/'ætəm/ 美:/'ætəm/ </td>
                <td class="export-td">n. 原子</td>
            </tr>
            
             <tr>
                <td class="export-td">2292</td>
                <td class="export-td">atomic</td>
                <td class="export-td">英:/ə'tɒmɪk/ 美:/ə'tɑmɪk/ </td>
                <td class="export-td">adj. 原子的，原子能的；微粒子的</td>
            </tr>
            
             <tr>
                <td class="export-td">2293</td>
                <td class="export-td">attach</td>
                <td class="export-td">英:/ə'tætʃ/ 美:/ə'tætʃ/ </td>
                <td class="export-td">1. vt. 系上；贴上；使依附；使依恋
2. vi. 附加；附属；伴随</td>
            </tr>
            
             <tr>
                <td class="export-td">2294</td>
                <td class="export-td">attack</td>
                <td class="export-td">英:/ə'tæk/ 美:/ə'tæk/ </td>
                <td class="export-td">1. n. 攻击；抨击；疾病发作
2. vt. 抨击；攻击；动手干</td>
            </tr>
            
             <tr>
                <td class="export-td">2295</td>
                <td class="export-td">attempt</td>
                <td class="export-td">英:/ə'tem(p)t/ 美:/ə'tɛmpt/ </td>
                <td class="export-td">1. n. 企图，试图；攻击
2. vt. 企图，试图；尝试</td>
            </tr>
            
             <tr>
                <td class="export-td">2296</td>
                <td class="export-td">attend</td>
                <td class="export-td">英:/ə'tend/ 美:/ə'tɛnd/ </td>
                <td class="export-td">1. vt. 出席；上（大学等）；照料；招待；陪伴
2. vi. 出席；照料；照顾；致力于</td>
            </tr>
            
             <tr>
                <td class="export-td">2297</td>
                <td class="export-td">attention</td>
                <td class="export-td">英:/ə'tenʃ(ə)n/ 美:/ə'tɛnʃən/ </td>
                <td class="export-td">注意 ,关心,立正</td>
            </tr>
            
             <tr>
                <td class="export-td">2298</td>
                <td class="export-td">attitude</td>
                <td class="export-td">英:/'ætɪtjuːd/ 美:/'ætɪtʊd/ </td>
                <td class="export-td">n. 态度；姿势；看法；意见</td>
            </tr>
            
             <tr>
                <td class="export-td">2299</td>
                <td class="export-td">attract</td>
                <td class="export-td">英:/ə'trækt/ 美:/ə'trækt/ </td>
                <td class="export-td">1. vt. 吸引；引起
2. vi. 吸引；有吸引力</td>
            </tr>
            
             <tr>
                <td class="export-td">2300</td>
                <td class="export-td">attraction</td>
                <td class="export-td">英:/ə'trækʃ(ə)n/ 美:/ə'trækʃən/ </td>
                <td class="export-td">引力</td>
            </tr>
            
             <tr>
                <td class="export-td">2301</td>
                <td class="export-td">attractive</td>
                <td class="export-td">英:/ə'træktɪv/ 美:/ə'træktɪv/ </td>
                <td class="export-td">吸引力</td>
            </tr>
            
             <tr>
                <td class="export-td">2302</td>
                <td class="export-td">audience</td>
                <td class="export-td">英:/'ɔːdɪəns/ 美:/'ɔdɪəns/ </td>
                <td class="export-td">n. 观众；听众；接见；读者</td>
            </tr>
            
             <tr>
                <td class="export-td">2303</td>
                <td class="export-td">August</td>
                <td class="export-td">英:/ɔː'gʌst/ 美:/ɔˈɡʌst/ </td>
                <td class="export-td">1. adj. 威严的；令人敬畏的
2. n. 八月（简写为Aug）</td>
            </tr>
            
             <tr>
                <td class="export-td">2304</td>
                <td class="export-td">aunt</td>
                <td class="export-td">英:/ɑːnt/ 美:/ænt/ </td>
                <td class="export-td">n. 伯母；阿姨；舅妈；姑妈</td>
            </tr>
            
             <tr>
                <td class="export-td">2305</td>
                <td class="export-td">author</td>
                <td class="export-td">英:/'ɔːθə/ 美:/'ɔθɚ/ </td>
                <td class="export-td">1. n. 作者；作家；创始人
2. vt. 创作出版</td>
            </tr>
            
             <tr>
                <td class="export-td">2306</td>
                <td class="export-td">authority</td>
                <td class="export-td">英:/ɔː'θɒrɪtɪ/ 美:/ə'θɔrəti/ </td>
                <td class="export-td">权力, 权威</td>
            </tr>
            
             <tr>
                <td class="export-td">2307</td>
                <td class="export-td">automatic</td>
                <td class="export-td">英:/ɔːtə'mætɪk/ 美:/'ɔtə'mætɪk/ </td>
                <td class="export-td">自动</td>
            </tr>
            
             <tr>
                <td class="export-td">2308</td>
                <td class="export-td">automobile</td>
                <td class="export-td">英:/'ɔːtəməbiːl/ 美:/ˌɔtəmə'bil/ </td>
                <td class="export-td">汽车; 汽车的</td>
            </tr>
            
             <tr>
                <td class="export-td">2309</td>
                <td class="export-td">autumn</td>
                <td class="export-td">英:/'ɔːtəm/ 美:/'ɔtəm/ </td>
                <td class="export-td">1. n. 秋天；成熟期；渐衰期，凋落期
2. adj. 秋天的，秋季的</td>
            </tr>
            
             <tr>
                <td class="export-td">2310</td>
                <td class="export-td">available</td>
                <td class="export-td">英:/ə'veɪləb(ə)l/ 美:/ə'veləbl/ </td>
                <td class="export-td">可用的</td>
            </tr>
            
             <tr>
                <td class="export-td">2311</td>
                <td class="export-td">avenue</td>
                <td class="export-td">英:/'æv(ə)njuː/ 美:/'ævənu/ </td>
                <td class="export-td">n. 林荫大道；大街</td>
            </tr>
            
             <tr>
                <td class="export-td">2312</td>
                <td class="export-td">average</td>
                <td class="export-td">英:/'æv(ə)rɪdʒ/ 美:/'ævərɪdʒ/ </td>
                <td class="export-td">1. n. 平均；平均数；[商]海损
2. adj. 平均的；普通的</td>
            </tr>
            
             <tr>
                <td class="export-td">2313</td>
                <td class="export-td">awake</td>
                <td class="export-td">英:/ə'weɪk/ 美:/ə'wek/ </td>
                <td class="export-td">1. vi. 觉醒，意识到；醒来；被唤起
2. vt. 唤醒；激起，唤起；使觉醒</td>
            </tr>
            
             <tr>
                <td class="export-td">2314</td>
                <td class="export-td">award</td>
                <td class="export-td">英:/ə'wɔ:d/ 美:/əˈwɔrd/ </td>
                <td class="export-td">1. vt. 授予；判定
2. n. 奖品；判决</td>
            </tr>
            
             <tr>
                <td class="export-td">2315</td>
                <td class="export-td">aware</td>
                <td class="export-td">英:/ə'weə/ 美:/ə'wɛr/ </td>
                <td class="export-td">adj. 知道的；意识到的；有…方面知识的；懂世故的</td>
            </tr>
            
             <tr>
                <td class="export-td">2316</td>
                <td class="export-td">away</td>
                <td class="export-td">英:/ə'weɪ/ 美:/ə'we/ </td>
                <td class="export-td">adv. 离去，离开；在远处</td>
            </tr>
            
             <tr>
                <td class="export-td">2317</td>
                <td class="export-td">awful</td>
                <td class="export-td">英:/'ɔːfʊl/ 美:/'ɔfl/ </td>
                <td class="export-td">a.可怕的，庄严的</td>
            </tr>
            
             <tr>
                <td class="export-td">2318</td>
                <td class="export-td">awfully</td>
                <td class="export-td">英:/'ɔːfʊlɪ/ 美:/'ɔfli/ </td>
                <td class="export-td">adv. 非常；很；十分；可怕地</td>
            </tr>
            
             <tr>
                <td class="export-td">2319</td>
                <td class="export-td">awkward</td>
                <td class="export-td">英:/'ɔːkwəd/ 美:/'ɔkwɚd/ </td>
                <td class="export-td">adj. 笨拙的；尴尬的；棘手的；不合适的</td>
            </tr>
            
             <tr>
                <td class="export-td">2320</td>
                <td class="export-td">ceiling</td>
                <td class="export-td">英:/'siːlɪŋ/ 美:/'silɪŋ/ </td>
                <td class="export-td">n. 天花板；上限</td>
            </tr>
            
             <tr>
                <td class="export-td">2321</td>
                <td class="export-td">become</td>
                <td class="export-td">英:/bɪ'kʌm/ 美:/bɪ'kʌm/ </td>
                <td class="export-td">1. vi. 变成；变得；成为
2. vt. 适合；相称</td>
            </tr>
            
             <tr>
                <td class="export-td">2322</td>
                <td class="export-td">bicycle</td>
                <td class="export-td">英:/'baɪsɪkl/ 美:/'baɪsɪkl/ </td>
                <td class="export-td">1. n. 自行车
2. vi. 骑脚踏车</td>
            </tr>
            
             <tr>
                <td class="export-td">2323</td>
                <td class="export-td">big</td>
                <td class="export-td">英:/bɪg/ 美:/bɪɡ/ </td>
                <td class="export-td">1. adj. 大的；重要的；量大的
2. adv. 大量地；夸大地；顺利</td>
            </tr>
            
             <tr>
                <td class="export-td">2324</td>
                <td class="export-td">bike</td>
                <td class="export-td">英:/baɪk/ 美:/baɪk/ </td>
                <td class="export-td">1. n. 自行车；脚踏车
2. vi. 骑自行车（或摩托车）</td>
            </tr>
            
             <tr>
                <td class="export-td">2325</td>
                <td class="export-td">bill</td>
                <td class="export-td">英:/bɪl/ 美:/bɪl/ </td>
                <td class="export-td">1. n. 帐单；法案；广告；钞票；票据；清单
2. vt. 宣布；开帐单；用海报宣传</td>
            </tr>
            
             <tr>
                <td class="export-td">2326</td>
                <td class="export-td">billion</td>
                <td class="export-td">英:/'bɪljən/ 美:/'bɪljən/ </td>
                <td class="export-td">1. n. 十亿；大量
2. num. 十亿</td>
            </tr>
            
             <tr>
                <td class="export-td">2327</td>
                <td class="export-td">bind</td>
                <td class="export-td">英:/baɪnd/ 美:/baɪnd/ </td>
                <td class="export-td">1. vi. 装订；结合；过紧；有约束力
2. vt. 装订；约束；绑；包扎；凝固</td>
            </tr>
            
             <tr>
                <td class="export-td">2328</td>
                <td class="export-td">biology</td>
                <td class="export-td">英:/baɪ'ɒlədʒɪ/ 美:/baɪ'ɑlədʒi/ </td>
                <td class="export-td">n. 生物学；（一个地区全部的）生物</td>
            </tr>
            
             <tr>
                <td class="export-td">2329</td>
                <td class="export-td">bird</td>
                <td class="export-td">英:/bɜːd/ 美:/bɝd/ </td>
                <td class="export-td">1. n. 鸟；家伙；羽毛球
2. vt. 向…喝倒彩；起哄</td>
            </tr>
            
             <tr>
                <td class="export-td">2330</td>
                <td class="export-td">birth</td>
                <td class="export-td">英:/bɜːθ/ 美:/bɝθ/ </td>
                <td class="export-td">n. 出生；血统，出身；起源</td>
            </tr>
            
             <tr>
                <td class="export-td">2331</td>
                <td class="export-td">birthday</td>
                <td class="export-td">英:/'bɜːθdeɪ/ 美:/'bɝθde/ </td>
                <td class="export-td">n. 生日，诞辰；诞生的日子</td>
            </tr>
            
             <tr>
                <td class="export-td">2332</td>
                <td class="export-td">biscuit</td>
                <td class="export-td">英:/'bɪskɪt/ 美:/'bɪskɪt/ </td>
                <td class="export-td">n. 小点心，饼干</td>
            </tr>
            
             <tr>
                <td class="export-td">2333</td>
                <td class="export-td">bit</td>
                <td class="export-td">英:/bɪt/ 美:/bɪt/ </td>
                <td class="export-td">1. n. 少量；马嚼子；比特（二进位制信息单位）；辅币；[口]老一套
2. vt. 控制</td>
            </tr>
            
             <tr>
                <td class="export-td">2334</td>
                <td class="export-td">bite</td>
                <td class="export-td">英:/baɪt/ 美:/baɪt/ </td>
                <td class="export-td">咬</td>
            </tr>
            
             <tr>
                <td class="export-td">2335</td>
                <td class="export-td">bitter</td>
                <td class="export-td">英:/'bɪtə/ 美:/'bɪtɚ/ </td>
                <td class="export-td">1. adj. 苦的；痛苦的；充满仇恨的；尖刻的
2. n. 苦味；苦啤酒</td>
            </tr>
            
             <tr>
                <td class="export-td">2336</td>
                <td class="export-td">cabbage</td>
                <td class="export-td">英:/'kæbɪdʒ/ 美:/'kæbɪdʒ/ </td>
                <td class="export-td">n. 卷心菜，甘蓝菜，（俚)脑袋</td>
            </tr>
            
             <tr>
                <td class="export-td">2337</td>
                <td class="export-td">cabin</td>
                <td class="export-td">英:/'kæbɪn/ 美:/'kæbɪn/ </td>
                <td class="export-td">1. n. 小屋；客舱；船舱
2. vt. 把…关在小屋里</td>
            </tr>
            
             <tr>
                <td class="export-td">2338</td>
                <td class="export-td">cabinet</td>
                <td class="export-td">英:/'kæbɪnɪt/ 美:/'kæbɪnət/ </td>
                <td class="export-td">1. n. 内阁；橱柜；展览艺术品的小陈列室
2. adj. 内阁的；私下的，秘密的</td>
            </tr>
            
             <tr>
                <td class="export-td">2339</td>
                <td class="export-td">cable</td>
                <td class="export-td">英:/ˈkeibl/ 美:/ˈkebəl/ </td>
                <td class="export-td">1. n. 电缆；海底电报
2. vt. 打电报</td>
            </tr>
            
             <tr>
                <td class="export-td">2340</td>
                <td class="export-td">cafe</td>
                <td class="export-td">/'kafeɪ/ </td>
                <td class="export-td">n. 咖啡馆；小餐馆</td>
            </tr>
            
             <tr>
                <td class="export-td">2341</td>
                <td class="export-td">cafeteria</td>
                <td class="export-td">英:/kæfɪ'tɪərɪə/ 美:/ˌkæfə'tɪrɪə/ </td>
                <td class="export-td">自助餐厅</td>
            </tr>
            
             <tr>
                <td class="export-td">2342</td>
                <td class="export-td">cage</td>
                <td class="export-td">英:/keɪdʒ/ 美:/kedʒ/ </td>
                <td class="export-td">1. n. 笼，兽笼；牢房，监狱
2. vt. 把…关进笼子；把…囚禁起来</td>
            </tr>
            
             <tr>
                <td class="export-td">2343</td>
                <td class="export-td">cake</td>
                <td class="export-td">英:/keɪk/ 美:/kek/ </td>
                <td class="export-td">1. n. 蛋糕；块状物；利益总额
2. vt. 使结块</td>
            </tr>
            
             <tr>
                <td class="export-td">2344</td>
                <td class="export-td">calculation</td>
                <td class="export-td">英:/kælkjʊ'leɪʃ(ə)n/ 美:/ˌkælkju'leʃən/ </td>
                <td class="export-td">计算</td>
            </tr>
            
             <tr>
                <td class="export-td">2345</td>
                <td class="export-td">calculate</td>
                <td class="export-td">英:/'kælkjʊleɪt/ 美:/'kælkjulet/ </td>
                <td class="export-td">计算</td>
            </tr>
            
             <tr>
                <td class="export-td">2346</td>
                <td class="export-td">calculator</td>
                <td class="export-td">英:/'kælkjʊleɪtə/ 美:/'kælkjuletɚ/ </td>
                <td class="export-td">计算器</td>
            </tr>
            
             <tr>
                <td class="export-td">2347</td>
                <td class="export-td">calendar</td>
                <td class="export-td">英:/'kælɪndə/ 美:/'kæləndɚ/ </td>
                <td class="export-td">1. n. 日历；历法；日程表
2. vt. 将…列入表中；将…排入日程表</td>
            </tr>
            
             <tr>
                <td class="export-td">2348</td>
                <td class="export-td">call</td>
                <td class="export-td">英:/kɔːl/ 美:/kɔl/ </td>
                <td class="export-td">1. vi. 呼叫；拜访；叫牌
2. vt. 呼叫；召集；称呼</td>
            </tr>
            
             <tr>
                <td class="export-td">2349</td>
                <td class="export-td">calm</td>
                <td class="export-td">英:/kɑːm/ 美:/kɑm/ </td>
                <td class="export-td">1. adj. 静的，平静的；沉着的
2. vt. 使平静；使镇定</td>
            </tr>
            
             <tr>
                <td class="export-td">2350</td>
                <td class="export-td">camel</td>
                <td class="export-td">英:/'kæm(ə)l/ 美:/'kæml/ </td>
                <td class="export-td">1. n. 骆驼；打捞浮筒；工作作风官僚
2. adj. 驼色的；暗棕色的</td>
            </tr>
            
             <tr>
                <td class="export-td">2351</td>
                <td class="export-td">camera</td>
                <td class="export-td">英:/'kæm(ə)rə/ 美:/'kæmərə/ </td>
                <td class="export-td">n. 照相机；摄影机</td>
            </tr>
            
             <tr>
                <td class="export-td">2352</td>
                <td class="export-td">camp</td>
                <td class="export-td">英:/kæmp/ 美:/kæmp/ </td>
                <td class="export-td">1. vi. 扎营；露营
2. vt. 扎营；使扎营</td>
            </tr>
            
             <tr>
                <td class="export-td">2353</td>
                <td class="export-td">campaign</td>
                <td class="export-td">英:/kæm'peɪn/ 美:/kæm'pen/ </td>
                <td class="export-td">1. vi. 作战；参加活动；参加竞选
2. n. 战役；运动；活动</td>
            </tr>
            
             <tr>
                <td class="export-td">2354</td>
                <td class="export-td">campus</td>
                <td class="export-td">英:/'kæmpəs/ 美:/'kæmpəs/ </td>
                <td class="export-td">n. （大学）校园；大学，大学生活；校园内的草地</td>
            </tr>
            
             <tr>
                <td class="export-td">2355</td>
                <td class="export-td">can</td>
                <td class="export-td">英:/kæn/ 美:/kən/ </td>
                <td class="export-td">能,可以</td>
            </tr>
            
             <tr>
                <td class="export-td">2356</td>
                <td class="export-td">canal</td>
                <td class="export-td">英:/kə'næl/ 美:/kə'næl/ </td>
                <td class="export-td">1. n. 运河；水道；灌溉水渠；管道
2. vt. 在…开凿运河</td>
            </tr>
            
             <tr>
                <td class="export-td">2357</td>
                <td class="export-td">cancel</td>
                <td class="export-td">英:/'kæns(ə)l/ 美:/'kænsl/ </td>
                <td class="export-td">1. vt. 取消；删去
2. vi. 取消；相互抵销</td>
            </tr>
            
             <tr>
                <td class="export-td">2358</td>
                <td class="export-td">candidate</td>
                <td class="export-td">英:/'kændɪdeɪt/ 美:/'kændɪdət/ </td>
                <td class="export-td">候选人, 求职者</td>
            </tr>
            
             <tr>
                <td class="export-td">2359</td>
                <td class="export-td">candle</td>
                <td class="export-td">英:/'kænd(ə)l/ 美:/'kændl/ </td>
                <td class="export-td">1. n. 蜡烛；烛光；烛形物
2. vt. 对着光检查</td>
            </tr>
            
             <tr>
                <td class="export-td">2360</td>
                <td class="export-td">candy</td>
                <td class="export-td">英:/'kændɪ/ 美:/'kændi/ </td>
                <td class="export-td">1. vt. 用糖煮；使结晶为砂糖；美化
2. vi. 糖煮；成为结晶</td>
            </tr>
            
             <tr>
                <td class="export-td">2361</td>
                <td class="export-td">cannon</td>
                <td class="export-td">英:/'kænən/ 美:/'kænən/ </td>
                <td class="export-td">1. n. 大炮；加农炮；榴弹炮；机关炮
2. vi. 炮轰；开炮</td>
            </tr>
            
             <tr>
                <td class="export-td">2362</td>
                <td class="export-td">canoe</td>
                <td class="export-td">英:/kə'nuː/ 美:/kə'nu/ </td>
                <td class="export-td">1. n. 独木舟；轻舟
2. vi. 乘独木舟</td>
            </tr>
            
             <tr>
                <td class="export-td">2363</td>
                <td class="export-td">cap</td>
                <td class="export-td">英:/kæp/ 美:/kæp/ </td>
                <td class="export-td">1. n. 帽子；盖
2. vi. 脱帽致意</td>
            </tr>
            
             <tr>
                <td class="export-td">2364</td>
                <td class="export-td">capable</td>
                <td class="export-td">英:/'keɪpəb(ə)l/ 美:/'kepəbl/ </td>
                <td class="export-td">adj. 能干的，能胜任的；有才华的</td>
            </tr>
            
             <tr>
                <td class="export-td">2365</td>
                <td class="export-td">capacity</td>
                <td class="export-td">英:/kə'pæsɪtɪ/ 美:/kə'pæsəti/ </td>
                <td class="export-td">n. 能力；容量；生产力；资格，地位</td>
            </tr>
            
             <tr>
                <td class="export-td">2366</td>
                <td class="export-td">capital</td>
                <td class="export-td">英:/'kæpɪt(ə)l/ 美:/'kæpɪtl/ </td>
                <td class="export-td">1. n. 首都，省会；大写字母；资金；资本家
2. adj. 重要的；大写的；首都的</td>
            </tr>
            
             <tr>
                <td class="export-td">2367</td>
                <td class="export-td">capture</td>
                <td class="export-td">英:/'kæptʃə/ 美:/'kæptʃɚ/ </td>
                <td class="export-td">1. vt. 俘获；夺得
2. n. 战利品，俘虏；捕获</td>
            </tr>
            
             <tr>
                <td class="export-td">2368</td>
                <td class="export-td">car</td>
                <td class="export-td">英:/kɑː/ 美:/kɑr/ </td>
                <td class="export-td">n. 汽车；车厢</td>
            </tr>
            
             <tr>
                <td class="export-td">2369</td>
                <td class="export-td">carbon</td>
                <td class="export-td">英:/'kɑːb(ə)n/ 美:/'kɑrbən/ </td>
                <td class="export-td">1. n. 碳；碳棒；复写纸
2. adj. 碳的；碳处理的</td>
            </tr>
            
             <tr>
                <td class="export-td">2370</td>
                <td class="export-td">card</td>
                <td class="export-td">英:/kɑːd/ 美:/kɑrd/ </td>
                <td class="export-td">1. n. 卡片；纸牌；明信片
2. vt. 记于卡片上</td>
            </tr>
            
             <tr>
                <td class="export-td">2371</td>
                <td class="export-td">care</td>
                <td class="export-td">英:/keə/ 美:/kɛr/ </td>
                <td class="export-td">1. n. 照料；忧虑；关怀；谨慎
2. vi. 关心；喜爱；照顾；顾虑</td>
            </tr>
            
             <tr>
                <td class="export-td">2372</td>
                <td class="export-td">careful</td>
                <td class="export-td">英:/'keəfʊl/ 美:/'kɛrfl/ </td>
                <td class="export-td">adj. 仔细的，小心的</td>
            </tr>
            
             <tr>
                <td class="export-td">2373</td>
                <td class="export-td">careless</td>
                <td class="export-td">英:/'keəlɪs/ 美:/'kɛrləs/ </td>
                <td class="export-td">adj. 粗心的；无忧无虑的；淡漠的</td>
            </tr>
            
             <tr>
                <td class="export-td">2374</td>
                <td class="export-td">cargo</td>
                <td class="export-td">英:/'kɑːgəʊ/ 美:/'kɑrɡo/ </td>
                <td class="export-td">n. 货物，船货</td>
            </tr>
            
             <tr>
                <td class="export-td">2375</td>
                <td class="export-td">carpenter</td>
                <td class="export-td">英:/ˈkɑ:pintə/ 美:/ˈkɑrpəntɚ/ </td>
                <td class="export-td">木匠; 做木工活</td>
            </tr>
            
             <tr>
                <td class="export-td">2376</td>
                <td class="export-td">carpet</td>
                <td class="export-td">英:/'kɑːpɪt/ 美:/'kɑrpɪt/ </td>
                <td class="export-td">1. vt. 在…上铺地毯，把地毯铺在…上；斥责
2. n. 地毯；地毯状覆盖物</td>
            </tr>
            
             <tr>
                <td class="export-td">2377</td>
                <td class="export-td">carriage</td>
                <td class="export-td">英:/'kærɪdʒ/ 美:/'kærɪdʒ/ </td>
                <td class="export-td">n. 四轮马车；客车厢；运费；运输；举止</td>
            </tr>
            
             <tr>
                <td class="export-td">2378</td>
                <td class="export-td">carrot</td>
                <td class="export-td">英:/'kærət/ 美:/'kærət/ </td>
                <td class="export-td">n. 胡萝卜</td>
            </tr>
            
             <tr>
                <td class="export-td">2379</td>
                <td class="export-td">carry</td>
                <td class="export-td">英:/'kærɪ/ 美:/'kæri/ </td>
                <td class="export-td">1. vt. 拿，扛；搬运；携带；支持
2. vi. 被携带；被搬运；能达到</td>
            </tr>
            
             <tr>
                <td class="export-td">2380</td>
                <td class="export-td">cart</td>
                <td class="export-td">英:/kɑːt/ 美:/kɑrt/ </td>
                <td class="export-td">1. n. 二轮运货马车
2. vt. 用车装载</td>
            </tr>
            
             <tr>
                <td class="export-td">2381</td>
                <td class="export-td">carve</td>
                <td class="export-td">英:/kɑːv/ 美:/kɑrv/ </td>
                <td class="export-td">1. vt. 雕刻；切开；开创
2. vi. 切开；做雕刻工作</td>
            </tr>
            
             <tr>
                <td class="export-td">2382</td>
                <td class="export-td">case</td>
                <td class="export-td">英:/keɪs/ 美:/kes/ </td>
                <td class="export-td">1. n. 情况；实例；箱
2. vt. 把…装于容器中；包围</td>
            </tr>
            
             <tr>
                <td class="export-td">2383</td>
                <td class="export-td">cash</td>
                <td class="export-td">英:/kæʃ/ 美:/kæʃ/ </td>
                <td class="export-td">1. n. 现款，现金
2. vt. 将…兑现；支付现款</td>
            </tr>
            
             <tr>
                <td class="export-td">2384</td>
                <td class="export-td">cassette</td>
                <td class="export-td">英:/kə'set/ 美:/kə'sɛt/ </td>
                <td class="export-td">n. 盒式磁带；暗盒；珠宝箱；片匣</td>
            </tr>
            
             <tr>
                <td class="export-td">2385</td>
                <td class="export-td">cast</td>
                <td class="export-td">英:/kɑːst/ 美:/kæst/ </td>
                <td class="export-td">1. vt. 投，抛；投射（光、影、视线等）；浇铸；计算
2. n. 投掷，抛；铸件，铸型；演员阵容；脱落物</td>
            </tr>
            
             <tr>
                <td class="export-td">2386</td>
                <td class="export-td">castle</td>
                <td class="export-td">英:/'kɑːs(ə)l/ 美:/'kæsl/ </td>
                <td class="export-td">1. n. 城堡；象棋中的车
2. vt. 置…于城堡中；筑城堡防御</td>
            </tr>
            
             <tr>
                <td class="export-td">2387</td>
                <td class="export-td">casual</td>
                <td class="export-td">英:/'kæʒjʊəl/ 美:/'kæʒʊəl/ </td>
                <td class="export-td">1. adj. 偶然的；随便的；临时的；非正式的
2. n. 临时工人；便装；待命士兵</td>
            </tr>
            
             <tr>
                <td class="export-td">2388</td>
                <td class="export-td">cat</td>
                <td class="export-td">英:/kæt/ 美:/kæt/ </td>
                <td class="export-td">n. 猫；猫科动物</td>
            </tr>
            
             <tr>
                <td class="export-td">2389</td>
                <td class="export-td">catch</td>
                <td class="export-td">英:/kætʃ/ 美:/kætʃ/ </td>
                <td class="export-td">1. vt. 赶上；抓住；感染；了解
2. vi. 赶上；抓住</td>
            </tr>
            
             <tr>
                <td class="export-td">2390</td>
                <td class="export-td">cathedral</td>
                <td class="export-td">英:/kə'θiːdr(ə)l/ 美:/kə'θidrəl/ </td>
                <td class="export-td">大教堂</td>
            </tr>
            
             <tr>
                <td class="export-td">2391</td>
                <td class="export-td">cause</td>
                <td class="export-td">英:/kɔːz/ 美:/kɔz/ </td>
                <td class="export-td">1. n. 原因；事业；目标
2. vt. 引起；使遭受</td>
            </tr>
            
             <tr>
                <td class="export-td">2392</td>
                <td class="export-td">cave</td>
                <td class="export-td">英:/keɪv/ 美:/kev/ </td>
                <td class="export-td">1. vt. 使凹陷，使塌落；在…挖洞穴
2. vi. 凹陷，塌落；投降</td>
            </tr>
            
             <tr>
                <td class="export-td">2393</td>
                <td class="export-td">cease</td>
                <td class="export-td">英:/siːs/ 美:/sis/ </td>
                <td class="export-td">1. vi. 停止；终了
2. vt. 停止；结束</td>
            </tr>
            
             <tr>
                <td class="export-td">2394</td>
                <td class="export-td">celebrate</td>
                <td class="export-td">英:/'selɪbreɪt/ 美:/'sɛlɪbret/ </td>
                <td class="export-td">名人,名誉,社会名流</td>
            </tr>
            
             <tr>
                <td class="export-td">2395</td>
                <td class="export-td">cell</td>
                <td class="export-td">英:/sel/ 美:/sɛl/ </td>
                <td class="export-td">1. n. 细胞；电池；蜂房的巢室；单人小室
2. vi. 住在牢房或小室中</td>
            </tr>
            
             <tr>
                <td class="export-td">2396</td>
                <td class="export-td">cellar</td>
                <td class="export-td">英:/'selə/ 美:/'sɛlɚ/ </td>
                <td class="export-td">1. n. 地窖；酒窖；地下室
2. vt. 把…藏入地窖</td>
            </tr>
            
             <tr>
                <td class="export-td">2397</td>
                <td class="export-td">cement</td>
                <td class="export-td">英:/sɪ'ment/ 美:/sə'mɛnt/ </td>
                <td class="export-td">1. vt. 巩固，加强；用水泥涂；接合
2. vi. 粘牢</td>
            </tr>
            
             <tr>
                <td class="export-td">2398</td>
                <td class="export-td">cent</td>
                <td class="export-td">英:/sent/ 美:/sɛnt/ </td>
                <td class="export-td">n. 分；一分的硬币；森特（等于半音程的百分之一）</td>
            </tr>
            
             <tr>
                <td class="export-td">2399</td>
                <td class="export-td">centigrade</td>
                <td class="export-td">英:/'sentɪgreɪd/ 美:/'sɛntɪɡred/ </td>
                <td class="export-td">摄氏的，百分度的</td>
            </tr>
            
             <tr>
                <td class="export-td">2400</td>
                <td class="export-td">central</td>
                <td class="export-td">英:/'sentr(ə)l/ 美:/'sɛntrəl/ </td>
                <td class="export-td">1. adj. 中心的；主要的；中枢的
2. n. 电话总机</td>
            </tr>
            
             <tr>
                <td class="export-td">2401</td>
                <td class="export-td">centre</td>
                <td class="export-td">英:/'sentə/ 美:/ˈsɛntɚ/ </td>
                <td class="export-td">1. vi. 以…为中心
2. vt. 集中；将…放在中央</td>
            </tr>
            
             <tr>
                <td class="export-td">2402</td>
                <td class="export-td">century</td>
                <td class="export-td">英:/'sentʃʊrɪ/ 美:/'sɛntʃəri/ </td>
                <td class="export-td">n. 世纪，百年；（板球）一百分</td>
            </tr>
            
             <tr>
                <td class="export-td">2403</td>
                <td class="export-td">ceremony</td>
                <td class="export-td">英:/'serɪmənɪ/ 美:/'sɛrə'moni/ </td>
                <td class="export-td">n. 典礼，仪式；礼节，礼仪；客套，虚礼</td>
            </tr>
            
             <tr>
                <td class="export-td">2404</td>
                <td class="export-td">certain</td>
                <td class="export-td">英:/'sɜːt(ə)n/ 美:/'sɝtn/ </td>
                <td class="export-td">1. adj. 某一；确信；无疑的；有把握的；必然的
2. pron. 某些；某几个</td>
            </tr>
            
             <tr>
                <td class="export-td">2405</td>
                <td class="export-td">certainly</td>
                <td class="export-td">英:/'sɜːt(ə)nlɪ/ 美:/'sɝtnli/ </td>
                <td class="export-td">当然</td>
            </tr>
            
             <tr>
                <td class="export-td">2406</td>
                <td class="export-td">certificate</td>
                <td class="export-td">英:/sə'tɪfɪkət/ 美:/sɚ'tɪfɪkət/ </td>
                <td class="export-td">证 书,执照</td>
            </tr>
            
             <tr>
                <td class="export-td">2407</td>
                <td class="export-td">cigarette</td>
                <td class="export-td">英:/sɪgə'ret/ 美:/'sɪɡərɛt/ </td>
                <td class="export-td">香烟</td>
            </tr>
            
             <tr>
                <td class="export-td">2408</td>
                <td class="export-td">cinema</td>
                <td class="export-td">英:/'sɪnɪmə/ 美:/'sɪnəmə/ </td>
                <td class="export-td">n. 电影院；电影；电影业，电影制作术</td>
            </tr>
            
             <tr>
                <td class="export-td">2409</td>
                <td class="export-td">circle</td>
                <td class="export-td">英:/'sɜːk(ə)l/ 美:/'sɝkl/ </td>
                <td class="export-td">1. n. 圆；圆形物；循环，周期；圈子
2. vi. 盘旋，旋转；环行</td>
            </tr>
            
             <tr>
                <td class="export-td">2410</td>
                <td class="export-td">circular</td>
                <td class="export-td">英:/'sɜːkjʊlə/ 美:/'sɝkjəlɚ/ </td>
                <td class="export-td">1. adj. 圆形的；循环的；间接的
2. n. 通知，传单</td>
            </tr>
            
             <tr>
                <td class="export-td">2411</td>
                <td class="export-td">circulate</td>
                <td class="export-td">英:/'sɜːkjʊleɪt/ 美:/'sɝkjəlet/ </td>
                <td class="export-td">流通,循环,传播</td>
            </tr>
            
             <tr>
                <td class="export-td">2412</td>
                <td class="export-td">circumference</td>
                <td class="export-td">英:/sə'kʌmf(ə)r(ə)ns/ 美:/sɚ'kʌmfərəns/ </td>
                <td class="export-td">圆周, 周围, 胸围</td>
            </tr>
            
             <tr>
                <td class="export-td">2413</td>
                <td class="export-td">circumstance</td>
                <td class="export-td">英:/'sɜːkəmst(ə)ns/ 美:/'sɝkəmstæns/ </td>
                <td class="export-td">环境</td>
            </tr>
            
             <tr>
                <td class="export-td">2414</td>
                <td class="export-td">citizen</td>
                <td class="export-td">英:/'sɪtɪz(ə)n/ 美:/'sɪtɪzn/ </td>
                <td class="export-td">n. 公民；市民；老百姓</td>
            </tr>
            
             <tr>
                <td class="export-td">2415</td>
                <td class="export-td">city</td>
                <td class="export-td">英:/'sɪtɪ/ 美:/'sɪti/ </td>
                <td class="export-td">1. n. 城市，都市
2. adj. 都会的；城市的</td>
            </tr>
            
             <tr>
                <td class="export-td">2416</td>
                <td class="export-td">civil</td>
                <td class="export-td">英:/'sɪv(ə)l/ 美:/'sɪvl/ </td>
                <td class="export-td">adj. 公民的；民间的；文职的；有礼貌的；根据民法的</td>
            </tr>
            
             <tr>
                <td class="export-td">2417</td>
                <td class="export-td">civilization</td>
                <td class="export-td">英:/ˌsivilaiˈzeiʃən/ 美:/ˌsɪvələ'zeʃən/ </td>
                <td class="export-td">文明,开化</td>
            </tr>
            
             <tr>
                <td class="export-td">2418</td>
                <td class="export-td">classmate</td>
                <td class="export-td">英:/'klɑːsmeɪt/ 美:/'klæsmet/ </td>
                <td class="export-td">同班同学</td>
            </tr>
            
             <tr>
                <td class="export-td">2419</td>
                <td class="export-td">classroom</td>
                <td class="export-td">英:/'klɑːsruːm/ 美:/'klæs'rʊm/ </td>
                <td class="export-td">教室，课堂</td>
            </tr>
            
             <tr>
                <td class="export-td">2420</td>
                <td class="export-td">connection</td>
                <td class="export-td">英:/kəˈnekʃən/ 美:/kə'nɛkʃən/ </td>
                <td class="export-td">连接</td>
            </tr>
            
             <tr>
                <td class="export-td">2421</td>
                <td class="export-td">contest</td>
                <td class="export-td">英:/'kɒntest/ 美:/kən'tɛst/ </td>
                <td class="export-td">1. vt. 争辩；提出质疑
2. vi. 竞争；争辩</td>
            </tr>
            
             <tr>
                <td class="export-td">2422</td>
                <td class="export-td">cooperate</td>
                <td class="export-td">英:/kəuˈɔpəreit/ 美:/ko'ɑpəret/ </td>
                <td class="export-td">合作,协力</td>
            </tr>
            
             <tr>
                <td class="export-td">2423</td>
                <td class="export-td">dead</td>
                <td class="export-td">英:/ded/ 美:/dɛd/ </td>
                <td class="export-td">1. adj. 无生命的；废弃了的；呆板的
2. adv. 完全地</td>
            </tr>
            
             <tr>
                <td class="export-td">2424</td>
                <td class="export-td">deadly</td>
                <td class="export-td">英:/'dedlɪ/ 美:/'dɛdli/ </td>
                <td class="export-td">1. adj. 致命的；死一般的；非常的
2. adv. 非常；如死一般地</td>
            </tr>
            
             <tr>
                <td class="export-td">2425</td>
                <td class="export-td">deaf</td>
                <td class="export-td">英:/def/ 美:/dɛf/ </td>
                <td class="export-td">adj. 聋的</td>
            </tr>
            
             <tr>
                <td class="export-td">2426</td>
                <td class="export-td">deal</td>
                <td class="export-td">英:/diːl/ 美:/dil/ </td>
                <td class="export-td">1. vt. 发牌；处理；给予；分配
2. vi. 处理；做生意；对待；讨论</td>
            </tr>
            
             <tr>
                <td class="export-td">2427</td>
                <td class="export-td">dear</td>
                <td class="export-td">英:/dɪə/ 美:/dɪr/ </td>
                <td class="export-td">1. adj. 亲爱的；昂贵的；尊敬的
2. adv. 高价地；疼爱地</td>
            </tr>
            
             <tr>
                <td class="export-td">2428</td>
                <td class="export-td">death</td>
                <td class="export-td">英:/deθ/ 美:/dɛθ/ </td>
                <td class="export-td">n. 死；死亡；死神；毁灭</td>
            </tr>
            
             <tr>
                <td class="export-td">2429</td>
                <td class="export-td">debate</td>
                <td class="export-td">英:/dɪ'beɪt/ 美:/dɪ'bet/ </td>
                <td class="export-td">1. vt. 辩论，争论，讨论
2. vi. 辩论，争论，讨论</td>
            </tr>
            
             <tr>
                <td class="export-td">2430</td>
                <td class="export-td">debt</td>
                <td class="export-td">英:/det/ 美:/dɛt/ </td>
                <td class="export-td">n. 债务；借款；罪过</td>
            </tr>
            
             <tr>
                <td class="export-td">2431</td>
                <td class="export-td">decade</td>
                <td class="export-td">英:/'dekeɪd/ 美:/'dɛked/ </td>
                <td class="export-td">n. 十年，十年期；十</td>
            </tr>
            
             <tr>
                <td class="export-td">2432</td>
                <td class="export-td">decay</td>
                <td class="export-td">英:/dɪ'keɪ/ 美:/dɪ'ke/ </td>
                <td class="export-td">1. vi. 腐烂，腐朽；衰退，衰减
2. n. 衰退，衰减；腐烂，腐朽</td>
            </tr>
            
             <tr>
                <td class="export-td">2433</td>
                <td class="export-td">deceive</td>
                <td class="export-td">英:/dɪ'siːv/ 美:/dɪ'siv/ </td>
                <td class="export-td">v. 欺骗；行骗</td>
            </tr>
            
             <tr>
                <td class="export-td">2434</td>
                <td class="export-td">December</td>
                <td class="export-td">英:/diˈsembə/ 美:/dɪˈsɛmbɚ/ </td>
                <td class="export-td">n. 十二月</td>
            </tr>
            
             <tr>
                <td class="export-td">2435</td>
                <td class="export-td">decent</td>
                <td class="export-td">英:/'diːs(ə)nt/ 美:/'disnt/ </td>
                <td class="export-td">adj. 得体的；正派的；相当好的</td>
            </tr>
            
             <tr>
                <td class="export-td">2436</td>
                <td class="export-td">decide</td>
                <td class="export-td">英:/dɪ'saɪd/ 美:/dɪ'saɪd/ </td>
                <td class="export-td">1. vt. 决定；判决；解决
2. vi. 决定，下决心</td>
            </tr>
            
             <tr>
                <td class="export-td">2437</td>
                <td class="export-td">decision</td>
                <td class="export-td">英:/dɪ'sɪʒ(ə)n/ 美:/dɪ'sɪʒn/ </td>
                <td class="export-td">n. 决定，决心；决议</td>
            </tr>
            
             <tr>
                <td class="export-td">2438</td>
                <td class="export-td">deck</td>
                <td class="export-td">英:/dek/ 美:/dɛk/ </td>
                <td class="export-td">1. n. 甲板；行李仓；露天平台
2. vt. 装甲板；装饰；打扮</td>
            </tr>
            
             <tr>
                <td class="export-td">2439</td>
                <td class="export-td">declare</td>
                <td class="export-td">英:/dɪ'kleə/ 美:/dɪ'klɛr/ </td>
                <td class="export-td">1. vt. 宣布，声明；断言，宣称
2. vi. 声明，宣布</td>
            </tr>
            
             <tr>
                <td class="export-td">2440</td>
                <td class="export-td">decorate</td>
                <td class="export-td">英:/'dekəreɪt/ 美:/'dɛkəret/ </td>
                <td class="export-td">1. vt. 装饰；布置；授勋给
2. vi. 装饰；布置</td>
            </tr>
            
             <tr>
                <td class="export-td">2441</td>
                <td class="export-td">decrease</td>
                <td class="export-td">英:/dɪ'kriːs/ 美:/dɪ'kris/ </td>
                <td class="export-td">1. n. 减少，减小；减少量
2. vi. 减少，减小</td>
            </tr>
            
             <tr>
                <td class="export-td">2442</td>
                <td class="export-td">deed</td>
                <td class="export-td">英:/diːd/ 美:/did/ </td>
                <td class="export-td">1. n. 行动；证书；[法]契据
2. vt. 立契转让</td>
            </tr>
            
             <tr>
                <td class="export-td">2443</td>
                <td class="export-td">deep</td>
                <td class="export-td">英:/di:p/ 美:/dip/ </td>
                <td class="export-td">1. n. 深处；深渊
2. adj. 深的；深奥的；低沉的</td>
            </tr>
            
             <tr>
                <td class="export-td">2444</td>
                <td class="export-td">deer</td>
                <td class="export-td">英:/dɪə/ 美:/dɪr/ </td>
                <td class="export-td">鹿</td>
            </tr>
            
             <tr>
                <td class="export-td">2445</td>
                <td class="export-td">defeat</td>
                <td class="export-td">英:/dɪ'fiːt/ 美:/dɪ'fit/ </td>
                <td class="export-td">1. vt. 击败，战胜；使…失败；挫败
2. n. 失败；战胜</td>
            </tr>
            
             <tr>
                <td class="export-td">2446</td>
                <td class="export-td">defence</td>
                <td class="export-td">英:/dɪ'fens/ 美:/dɪˈfɛns/ </td>
                <td class="export-td">n. 防御；防卫；防卫设备；答辩</td>
            </tr>
            
             <tr>
                <td class="export-td">2447</td>
                <td class="export-td">defend</td>
                <td class="export-td">英:/dɪ'fend/ 美:/dɪ'fɛnd/ </td>
                <td class="export-td">1. vt. 防护；辩护
2. vi. 防守；保卫</td>
            </tr>
            
             <tr>
                <td class="export-td">2448</td>
                <td class="export-td">define</td>
                <td class="export-td">英:/dɪ'faɪn/ 美:/dɪ'faɪn/ </td>
                <td class="export-td">vt. 定义；使明确；规定</td>
            </tr>
            
             <tr>
                <td class="export-td">2449</td>
                <td class="export-td">definite</td>
                <td class="export-td">英:/'defɪnɪt/ 美:/'dɛfɪnət/ </td>
                <td class="export-td">adj. 确切的；一定的</td>
            </tr>
            
             <tr>
                <td class="export-td">2450</td>
                <td class="export-td">definitely</td>
                <td class="export-td">/'dɛfɪnətli/ </td>
                <td class="export-td">明确地, 确切地</td>
            </tr>
            
             <tr>
                <td class="export-td">2451</td>
                <td class="export-td">delay</td>
                <td class="export-td">英:/dɪ'leɪ/ 美:/dɪ'le/ </td>
                <td class="export-td">1. vi. 耽搁；延期
2. vt. 延期；耽搁</td>
            </tr>
            
             <tr>
                <td class="export-td">2452</td>
                <td class="export-td">delete</td>
                <td class="export-td">英:/dɪ'liːt/ 美:/dɪ'lit/ </td>
                <td class="export-td">vt. 删除</td>
            </tr>
            
             <tr>
                <td class="export-td">2453</td>
                <td class="export-td">delicate</td>
                <td class="export-td">英:/'delɪkət/ 美:/'dɛləkət/ </td>
                <td class="export-td">adj. 微妙的；易碎的；清淡可口的；柔和的；精美的，雅致的；纤弱的</td>
            </tr>
            
             <tr>
                <td class="export-td">2454</td>
                <td class="export-td">delicious</td>
                <td class="export-td">英:/dɪ'lɪʃəs/ 美:/dɪ'lɪʃəs/ </td>
                <td class="export-td">可口的, 美味的</td>
            </tr>
            
             <tr>
                <td class="export-td">2455</td>
                <td class="export-td">delight</td>
                <td class="export-td">英:/dɪ'laɪt/ 美:/dɪ'laɪt/ </td>
                <td class="export-td">1. n. 高兴
2. vi. 高兴</td>
            </tr>
            
             <tr>
                <td class="export-td">2456</td>
                <td class="export-td">deliver</td>
                <td class="export-td">英:/dɪ'lɪvə/ 美:/dɪ'lɪvɚ/ </td>
                <td class="export-td">1. vt. 发表；递送；释放；给予（打击）；交付；给…接生
2. vi. 传送；投递；履行；实现</td>
            </tr>
            
             <tr>
                <td class="export-td">2457</td>
                <td class="export-td">demand</td>
                <td class="export-td">英:/dɪ'mɑːnd/ 美:/dɪ'mænd/ </td>
                <td class="export-td">1. vt. 要求；需要；查询
2. vi. 请求；查问；需要</td>
            </tr>
            
             <tr>
                <td class="export-td">2458</td>
                <td class="export-td">democracy</td>
                <td class="export-td">英:/dɪ'mɒkrəsɪ/ 美:/də'mɑkrəsi/ </td>
                <td class="export-td">民主</td>
            </tr>
            
             <tr>
                <td class="export-td">2459</td>
                <td class="export-td">democratic</td>
                <td class="export-td">英:/demə'krætɪk/ 美:/'dɛmə'krætɪk/ </td>
                <td class="export-td">民主的</td>
            </tr>
            
             <tr>
                <td class="export-td">2460</td>
                <td class="export-td">demonstrate</td>
                <td class="export-td">英:/'demənstreɪt/ 美:/'dɛmən'stret/ </td>
                <td class="export-td">演示</td>
            </tr>
            
             <tr>
                <td class="export-td">2461</td>
                <td class="export-td">dense</td>
                <td class="export-td">英:/dens/ 美:/dɛns/ </td>
                <td class="export-td">adj. 浓厚的；稠密的；愚钝的</td>
            </tr>
            
             <tr>
                <td class="export-td">2462</td>
                <td class="export-td">deny</td>
                <td class="export-td">英:/dɪ'naɪ/ 美:/dɪ'nai/ </td>
                <td class="export-td">1. vt. 否定，否认；拒绝给予；拒绝…的要求
2. vi. 否认；拒绝</td>
            </tr>
            
             <tr>
                <td class="export-td">2463</td>
                <td class="export-td">depart</td>
                <td class="export-td">英:/dɪ'pɑːt/ 美:/dɪ'pɑrt/ </td>
                <td class="export-td">1. vi. 离开；出发，起程；违反；去世
2. adj. 逝世的</td>
            </tr>
            
             <tr>
                <td class="export-td">2464</td>
                <td class="export-td">department</td>
                <td class="export-td">英:/dɪ'pɑːtm(ə)nt/ 美:/dɪ'pɑrtmənt/ </td>
                <td class="export-td">部门,系,省</td>
            </tr>
            
             <tr>
                <td class="export-td">2465</td>
                <td class="export-td">departure</td>
                <td class="export-td">英:/dɪ'pɑːtʃə/ 美:/dɪ'pɑrtʃɚ/ </td>
                <td class="export-td">离开,出发,分歧</td>
            </tr>
            
             <tr>
                <td class="export-td">2466</td>
                <td class="export-td">depend</td>
                <td class="export-td">英:/dɪ'pend/ 美:/dɪ'pɛnd/ </td>
                <td class="export-td">vi. 依赖，依靠；相信，信赖；取决于</td>
            </tr>
            
             <tr>
                <td class="export-td">2467</td>
                <td class="export-td">dependent</td>
                <td class="export-td">英:/diˈpendənt/ 美:/dɪ'pɛndənt/ </td>
                <td class="export-td">依赖的</td>
            </tr>
            
             <tr>
                <td class="export-td">2468</td>
                <td class="export-td">deposit</td>
                <td class="export-td">英:/dɪ'pɒzɪt/ 美:/dɪ'pɑzɪt/ </td>
                <td class="export-td">1. n. 存款；保证金；沉淀物
2. vt. 存放；使沉积</td>
            </tr>
            
             <tr>
                <td class="export-td">2469</td>
                <td class="export-td">depress</td>
                <td class="export-td">英:/dɪ'pres/ 美:/dɪˈprɛs/ </td>
                <td class="export-td">vt. 使沮丧；压低；使萧条</td>
            </tr>
            
             <tr>
                <td class="export-td">2470</td>
                <td class="export-td">depth</td>
                <td class="export-td">英:/depθ/ 美:/dɛpθ/ </td>
                <td class="export-td">n. 深度；深奥</td>
            </tr>
            
             <tr>
                <td class="export-td">2471</td>
                <td class="export-td">descend</td>
                <td class="export-td">英:/dɪ'send/ 美:/dɪ'sɛnd/ </td>
                <td class="export-td">1. vi. 下降；下来；遗传；屈尊；下去
2. vt. 下去；沿…向下</td>
            </tr>
            
             <tr>
                <td class="export-td">2472</td>
                <td class="export-td">describe</td>
                <td class="export-td">英:/dɪ'skraɪb/ 美:/dɪ'skraɪb/ </td>
                <td class="export-td">vt. 描述，形容；描绘</td>
            </tr>
            
             <tr>
                <td class="export-td">2473</td>
                <td class="export-td">description</td>
                <td class="export-td">英:/dɪ'skrɪpʃ(ə)n/ 美:/dɪ'skrɪpʃən/ </td>
                <td class="export-td">描述</td>
            </tr>
            
             <tr>
                <td class="export-td">2474</td>
                <td class="export-td">desert</td>
                <td class="export-td">英:/dɪ'zɜːt/ 美:/ˈdɛzət/ </td>
                <td class="export-td">1. vt. 遗弃；放弃；逃跑
2. vi. 遗弃；逃掉；开小差</td>
            </tr>
            
             <tr>
                <td class="export-td">2475</td>
                <td class="export-td">deserve</td>
                <td class="export-td">英:/dɪ'zɜːv/ 美:/dɪ'zɝv/ </td>
                <td class="export-td">1. vi. 应受，应得
2. vt. 应受，应得</td>
            </tr>
            
             <tr>
                <td class="export-td">2476</td>
                <td class="export-td">design</td>
                <td class="export-td">英:/dɪ'zaɪn/ 美:/dɪ'zaɪn/ </td>
                <td class="export-td">1. vt. 设计；计划；构思
2. n. 设计；图案</td>
            </tr>
            
             <tr>
                <td class="export-td">2477</td>
                <td class="export-td">desire</td>
                <td class="export-td">英:/dɪ'zaɪə/ 美:/dɪ'zaɪɚ/ </td>
                <td class="export-td">1. n. 欲望；要求，心愿；性欲
2. vt. 要求；想要；希望得到…</td>
            </tr>
            
             <tr>
                <td class="export-td">2478</td>
                <td class="export-td">desk</td>
                <td class="export-td">英:/desk/ 美:/dɛsk/ </td>
                <td class="export-td">1. n. 办公桌；服务台；编辑部；（美）讲道台；乐谱架
2. adj. 书桌的；桌上用的；伏案做的</td>
            </tr>
            
             <tr>
                <td class="export-td">2479</td>
                <td class="export-td">despair</td>
                <td class="export-td">英:/dɪ'speə/ 美:/dɪ'spɛr/ </td>
                <td class="export-td">1. n. 绝望；令人绝望的人或事
2. vi. 绝望，丧失信心</td>
            </tr>
            
             <tr>
                <td class="export-td">2480</td>
                <td class="export-td">desperate</td>
                <td class="export-td">英:/'desp(ə)rət/ 美:/'dɛspərət/ </td>
                <td class="export-td">危急</td>
            </tr>
            
             <tr>
                <td class="export-td">2481</td>
                <td class="export-td">despise</td>
                <td class="export-td">英:/dɪ'spaɪz/ 美:/dɪ'spaɪz/ </td>
                <td class="export-td">vt. 轻视，鄙视</td>
            </tr>
            
             <tr>
                <td class="export-td">2482</td>
                <td class="export-td">despite</td>
                <td class="export-td">英:/dɪ'spaɪt/ 美:/dɪ'spaɪt/ </td>
                <td class="export-td">1. prep. 尽管，不管
2. n. 轻视；憎恨；侮辱</td>
            </tr>
            
             <tr>
                <td class="export-td">2483</td>
                <td class="export-td">destination</td>
                <td class="export-td">英:/ˌdestɪ'neɪʃ(ə)n/ 美:/ˌdɛstɪ'neʃən/ </td>
                <td class="export-td">目的地,终点,景点</td>
            </tr>
            
             <tr>
                <td class="export-td">2484</td>
                <td class="export-td">destroy</td>
                <td class="export-td">英:/dɪ'strɒɪ/ 美:/dɪ'strɔɪ/ </td>
                <td class="export-td">vt. 毁坏；破坏；消灭</td>
            </tr>
            
             <tr>
                <td class="export-td">2485</td>
                <td class="export-td">destruction</td>
                <td class="export-td">英:/dɪ'strʌkʃ(ə)n/ 美:/dɪ'strʌkʃən/ </td>
                <td class="export-td">破坏,毁灭,破坏者</td>
            </tr>
            
             <tr>
                <td class="export-td">2486</td>
                <td class="export-td">detail</td>
                <td class="export-td">英:/'diːteɪl/ 美:/'ditel/ </td>
                <td class="export-td">1. n. 细节，详情
2. vt. 详述；选派</td>
            </tr>
            
             <tr>
                <td class="export-td">2487</td>
                <td class="export-td">detect</td>
                <td class="export-td">英:/dɪ'tekt/ 美:/dɪ'tɛkt/ </td>
                <td class="export-td">vt. 发现；察觉；探测</td>
            </tr>
            
             <tr>
                <td class="export-td">2488</td>
                <td class="export-td">determination</td>
                <td class="export-td">英:/dɪ,tɜːmɪ'neɪʃ(ə)n/ 美:/dɪ,tɝmɪ'neʃən/ </td>
                <td class="export-td">决心</td>
            </tr>
            
             <tr>
                <td class="export-td">2489</td>
                <td class="export-td">develop</td>
                <td class="export-td">英:/dɪ'veləp/ 美:/dɪ'vɛləp/ </td>
                <td class="export-td">1. vt. 开发；使成长；进步；使显影
2. vi. 发育；生长；显露；进化</td>
            </tr>
            
             <tr>
                <td class="export-td">2490</td>
                <td class="export-td">development</td>
                <td class="export-td">英:/dɪ'veləpm(ə)nt/ 美:/dɪ'vɛləpmənt/ </td>
                <td class="export-td">发育</td>
            </tr>
            
             <tr>
                <td class="export-td">2491</td>
                <td class="export-td">device</td>
                <td class="export-td">英:/dɪ'vaɪs/ 美:/dɪ'vaɪs/ </td>
                <td class="export-td">n. 装置；策略；图案</td>
            </tr>
            
             <tr>
                <td class="export-td">2492</td>
                <td class="export-td">devil</td>
                <td class="export-td">英:/'dev(ə)l/ 美:/'dɛvl/ </td>
                <td class="export-td">1. n. 撒旦；魔鬼；恶棍；家伙
2. vt. 折磨</td>
            </tr>
            
             <tr>
                <td class="export-td">2493</td>
                <td class="export-td">devote</td>
                <td class="export-td">英:/dɪ'vəʊt/ 美:/dɪ'vot/ </td>
                <td class="export-td">vt. 奉献；致力于</td>
            </tr>
            
             <tr>
                <td class="export-td">2494</td>
                <td class="export-td">dew</td>
                <td class="export-td">英:/'djuː/ 美:/du/ </td>
                <td class="export-td">1. n. 露水；清新；珠，滴
2. vt. （露水等）弄湿</td>
            </tr>
            
             <tr>
                <td class="export-td">2495</td>
                <td class="export-td">eighteen</td>
                <td class="export-td">英:/eɪ'tiːn/ 美:/ˌe'tin/ </td>
                <td class="export-td">1. n. 十八，十八个
2. adj. 十八个的，十八的</td>
            </tr>
            
             <tr>
                <td class="export-td">2496</td>
                <td class="export-td">eighty</td>
                <td class="export-td">英:/'eɪtɪ/ 美:/ˈeti/ </td>
                <td class="export-td">1. n. 八十；八十岁；八十年代
2. adj. 八十的，八十个的；八十岁的</td>
            </tr>
            
             <tr>
                <td class="export-td">2497</td>
                <td class="export-td">either</td>
                <td class="export-td">英:/'aɪðə/ 美:/'iðɚ/ </td>
                <td class="export-td">1. adj. 两者之中任一的；两者之中每一的
2. prep. 任何一个</td>
            </tr>
            
             <tr>
                <td class="export-td">2498</td>
                <td class="export-td">elaborate</td>
                <td class="export-td">英:/ɪ'læb(ə)rət/ 美:/ɪ'læbəret/ </td>
                <td class="export-td">vi. 详尽说明; vt. 详细制定; adj. 复杂的; 精心制作的时 态:   elaborat...</td>
            </tr>
            
             <tr>
                <td class="export-td">2499</td>
                <td class="export-td">elastic</td>
                <td class="export-td">英:/ɪ'læstɪk/ 美:/ɪ'læstɪk/ </td>
                <td class="export-td">1. adj. 有弹性的；易伸缩的；灵活的
2. n. 松紧带；橡皮圈</td>
            </tr>
            
             <tr>
                <td class="export-td">2500</td>
                <td class="export-td">elbow</td>
                <td class="export-td">英:/'elbəʊ/ 美:/'ɛlbo/ </td>
                <td class="export-td">1. n. 弯头；肘部；扶手
2. vt. 推挤；用手肘推开</td>
            </tr>
            
             <tr>
                <td class="export-td">2501</td>
                <td class="export-td">elder</td>
                <td class="export-td">英:/'eldə/ 美:/'ɛldɚ/ </td>
                <td class="export-td">1. n. 年长者；长辈；老人；父辈
2. adj. 年长的；年龄较大的；资格老的</td>
            </tr>
            
             <tr>
                <td class="export-td">2502</td>
                <td class="export-td">elect</td>
                <td class="export-td">英:/ɪ'lekt/ 美:/ɪ'lɛkt/ </td>
                <td class="export-td">1. adj. 选出的；当选的；卓越的
2. n. 被选的人；特殊阶层；上帝的选民</td>
            </tr>
            
             <tr>
                <td class="export-td">2503</td>
                <td class="export-td">election</td>
                <td class="export-td">英:/ɪ'lekʃ(ə)n/ 美:/ɪ'lɛkʃən/ </td>
                <td class="export-td">n. 选举；当选；选择权；[宗]上帝的选拔</td>
            </tr>
            
             <tr>
                <td class="export-td">2504</td>
                <td class="export-td">electric</td>
                <td class="export-td">英:/ɪ'lektrɪk/ 美:/ɪˈlɛktrɪk/ </td>
                <td class="export-td">1. adj. 电的；导电的；电动的；发电的；令人震惊的
2. n. [美口]电气车辆；电；带电体</td>
            </tr>
            
             <tr>
                <td class="export-td">2505</td>
                <td class="export-td">electrical</td>
                <td class="export-td">英:/ɪ'lektrɪk(ə)l/ 美:/ɪ'lɛktrɪkl/ </td>
                <td class="export-td">电的,与电有关的</td>
            </tr>
            
             <tr>
                <td class="export-td">2506</td>
                <td class="export-td">electricity</td>
                <td class="export-td">英:/ˌɪlek'trɪsɪtɪ/ 美:/ɪ'lɛk'trɪsəti/ </td>
                <td class="export-td">电,电学</td>
            </tr>
            
             <tr>
                <td class="export-td">2507</td>
                <td class="export-td">electronic</td>
                <td class="export-td">英:/ɪlek'trɒnɪk/ 美:/ɪ,lɛk'trɑnɪk/ </td>
                <td class="export-td">电子的</td>
            </tr>
            
             <tr>
                <td class="export-td">2508</td>
                <td class="export-td">electronics</td>
                <td class="export-td">英:/ɪlek'trɒnɪks/ 美:/ɪ,lɛk'trɑnɪks/ </td>
                <td class="export-td">电子学，电子器件</td>
            </tr>
            
             <tr>
                <td class="export-td">2509</td>
                <td class="export-td">element</td>
                <td class="export-td">英:/'elɪm(ə)nt/ 美:/ˈɛləmənt/ </td>
                <td class="export-td">n. 元素；成分；要素；原理；自然环境</td>
            </tr>
            
             <tr>
                <td class="export-td">2510</td>
                <td class="export-td">elementary</td>
                <td class="export-td">英:/elɪ'ment(ə)rɪ/ 美:/ˌɛlɪ'mɛntri/ </td>
                <td class="export-td">初级</td>
            </tr>
            
             <tr>
                <td class="export-td">2511</td>
                <td class="export-td">elephant</td>
                <td class="export-td">英:/'elɪf(ə)nt/ 美:/'ɛlɪfənt/ </td>
                <td class="export-td">n. 象；大号图画纸</td>
            </tr>
            
             <tr>
                <td class="export-td">2512</td>
                <td class="export-td">elevator</td>
                <td class="export-td">英:/'elɪveɪtə/ 美:/'ɛlɪvetɚ/ </td>
                <td class="export-td">n. 电梯；升降舵；升降机；起卸机</td>
            </tr>
            
             <tr>
                <td class="export-td">2513</td>
                <td class="export-td">eleven</td>
                <td class="export-td">英:/ɪ'lev(ə)n/ 美:/ɪ'lɛvn/ </td>
                <td class="export-td">1. n. 十一；十一个
2. adj. 十一的；十一个的</td>
            </tr>
            
             <tr>
                <td class="export-td">2514</td>
                <td class="export-td">eliminate</td>
                <td class="export-td">英:/ɪ'lɪmɪneɪt/ 美:/ɪ'lɪmɪnet/ </td>
                <td class="export-td">除去, 剔除; 忽略</td>
            </tr>
            
             <tr>
                <td class="export-td">2515</td>
                <td class="export-td">else</td>
                <td class="export-td">英:/els/ 美:/ɛls/ </td>
                <td class="export-td">1. adv. 另外；其他；否则
2. adj. 别的；其他的</td>
            </tr>
            
             <tr>
                <td class="export-td">2516</td>
                <td class="export-td">elsewhere</td>
                <td class="export-td">英:/els'weə/ 美:/ˈɛlsˌhwɛr/ </td>
                <td class="export-td">在别处, 到别处</td>
            </tr>
            
             <tr>
                <td class="export-td">2517</td>
                <td class="export-td">embrace</td>
                <td class="export-td">英:/ɪm'breɪs/ 美:/ɪm'bres/ </td>
                <td class="export-td">1. vt. 包含；信奉，皈依；拥抱
2. vi. 拥抱</td>
            </tr>
            
             <tr>
                <td class="export-td">2518</td>
                <td class="export-td">ensure</td>
                <td class="export-td">英:/ɪn'ʃɔː/ 美:/ɪn'ʃʊr/ </td>
                <td class="export-td">vt. 保证，确保；使安全</td>
            </tr>
            
             <tr>
                <td class="export-td">2519</td>
                <td class="export-td">European</td>
                <td class="export-td">英:/jʊərə'piːən/ 美:/'jʊrə'piən/ </td>
                <td class="export-td">1. adj. 欧洲的；欧洲人的
2. n. 欧洲人</td>
            </tr>
            
             <tr>
                <td class="export-td">2520</td>
                <td class="export-td">evaporate</td>
                <td class="export-td">英:/ɪ'væpəreɪt/ 美:/ɪ'væpəret/ </td>
                <td class="export-td">蒸发</td>
            </tr>
            
             <tr>
                <td class="export-td">2521</td>
                <td class="export-td">eve</td>
                <td class="export-td">英:/iːv/ 美:/iv/ </td>
                <td class="export-td">n. 前夕；傍晚；重大事件关头</td>
            </tr>
            
             <tr>
                <td class="export-td">2522</td>
                <td class="export-td">even</td>
                <td class="export-td">英:/'iːv(ə)n/ 美:/'ivən/ </td>
                <td class="export-td">1. adj. 偶数的；相等的；平坦的
2. adv. 甚至；还；实际上；即使</td>
            </tr>
            
             <tr>
                <td class="export-td">2523</td>
                <td class="export-td">evening</td>
                <td class="export-td">英:/'iːv(ə)nɪŋ/ 美:/'ivnɪŋ/ </td>
                <td class="export-td">1. n. 傍晚；晚上；后期；（联欢性的）晚会
2. adj. 在晚上的；为晚上的；晚上用的</td>
            </tr>
            
             <tr>
                <td class="export-td">2524</td>
                <td class="export-td">event</td>
                <td class="export-td">英:/ɪ'vent/ 美:/ɪ'vɛnt/ </td>
                <td class="export-td">n. 事件，大事；结果；项目</td>
            </tr>
            
             <tr>
                <td class="export-td">2525</td>
                <td class="export-td">eventually</td>
                <td class="export-td">英:/ɪ'ventʃʊəlɪ/ 美:/ɪ'vɛntʃuəli/ </td>
                <td class="export-td">终于, 最后</td>
            </tr>
            
             <tr>
                <td class="export-td">2526</td>
                <td class="export-td">ever</td>
                <td class="export-td">英:/'evə/ 美:/'ɛvɚ/ </td>
                <td class="export-td">adv. 曾经；究竟；永远</td>
            </tr>
            
             <tr>
                <td class="export-td">2527</td>
                <td class="export-td">every</td>
                <td class="export-td">英:/'evrɪ/ 美:/'ɛvri/ </td>
                <td class="export-td">adj. 每一的，每个的；每隔…的</td>
            </tr>
            
             <tr>
                <td class="export-td">2528</td>
                <td class="export-td">everybody</td>
                <td class="export-td">英:/'evrɪbɒdɪ/ 美:/'ɛvrɪbɑdi/ </td>
                <td class="export-td">柴米油盐</td>
            </tr>
            
             <tr>
                <td class="export-td">2529</td>
                <td class="export-td">everyday</td>
                <td class="export-td">英:/'evrɪdeɪ/ 美:/'ɛvrɪde/ </td>
                <td class="export-td">1. adj. 每天的，日常的
2. n. 寻常日子；平时</td>
            </tr>
            
             <tr>
                <td class="export-td">2530</td>
                <td class="export-td">everyone</td>
                <td class="export-td">英:/'evrɪwʌn/ 美:/'ɛvrɪwʌn/ </td>
                <td class="export-td">1. pron. 人人；每个人
2. n. 每个人</td>
            </tr>
            
             <tr>
                <td class="export-td">2531</td>
                <td class="export-td">everything</td>
                <td class="export-td">英:/'evrɪθɪŋ/ 美:/'ɛvrɪ'θɪŋ/ </td>
                <td class="export-td">pron. 每件事，一切</td>
            </tr>
            
             <tr>
                <td class="export-td">2532</td>
                <td class="export-td">everywhere</td>
                <td class="export-td">英:/'evrɪweə/ 美:/'ɛvrɪwɛr/ </td>
                <td class="export-td">到处, 无论何处</td>
            </tr>
            
             <tr>
                <td class="export-td">2533</td>
                <td class="export-td">evidence</td>
                <td class="export-td">英:/'evɪd(ə)ns/ 美:/'ɛvɪdəns/ </td>
                <td class="export-td">1. n. 证据，证明；迹象；明显
2. vt. 证明</td>
            </tr>
            
             <tr>
                <td class="export-td">2534</td>
                <td class="export-td">evident</td>
                <td class="export-td">英:/'evɪd(ə)nt/ 美:/'ɛvɪdənt/ </td>
                <td class="export-td">adj. 明显的；明白的</td>
            </tr>
            
             <tr>
                <td class="export-td">2535</td>
                <td class="export-td">evil</td>
                <td class="export-td">英:/'iːv(ə)l/ 美:/'ivl/ </td>
                <td class="export-td">1. adj. 邪恶的；有害的；不幸的；讨厌的
2. n. 罪恶，邪恶；不幸</td>
            </tr>
            
             <tr>
                <td class="export-td">2536</td>
                <td class="export-td">factor</td>
                <td class="export-td">英:/'fæktə/ 美:/'fæktɚ/ </td>
                <td class="export-td">1. n. 因素；因数；要素；代理人
2. vi. 做代理商</td>
            </tr>
            
             <tr>
                <td class="export-td">2537</td>
                <td class="export-td">fade</td>
                <td class="export-td">英:/feɪd/ 美:/fad/ </td>
                <td class="export-td">1. vi. 褪色；凋谢；逐渐消失
2. vt. 使褪色</td>
            </tr>
            
             <tr>
                <td class="export-td">2538</td>
                <td class="export-td">Fahrenheit</td>
                <td class="export-td">/'færən'haɪt/ </td>
                <td class="export-td">华氏的</td>
            </tr>
            
             <tr>
                <td class="export-td">2539</td>
                <td class="export-td">fail</td>
                <td class="export-td">英:/feɪl/ 美:/fel/ </td>
                <td class="export-td">1. vi. 失败，不及格；衰退；缺乏；破产
2. vt. 不及格；忘记；使失望；舍弃</td>
            </tr>
            
             <tr>
                <td class="export-td">2540</td>
                <td class="export-td">failure</td>
                <td class="export-td">英:/'feɪljə/ 美:/'feljɚ/ </td>
                <td class="export-td">n. 失败；故障；失败者；破产</td>
            </tr>
            
             <tr>
                <td class="export-td">2541</td>
                <td class="export-td">faint</td>
                <td class="export-td">英:/feɪnt/ 美:/fent/ </td>
                <td class="export-td">1. adj. 头晕的；虚弱的；模糊的；衰弱的
2. vi. 昏倒；变得微弱；变得没气力</td>
            </tr>
            
             <tr>
                <td class="export-td">2542</td>
                <td class="export-td">fair</td>
                <td class="export-td">英:/feə/ 美:/fɛr/ </td>
                <td class="export-td">1. adj. 公平的；美丽的，白皙的；晴朗的
2. adv. 公平地；清楚地；直接地</td>
            </tr>
            
             <tr>
                <td class="export-td">2543</td>
                <td class="export-td">fairly</td>
                <td class="export-td">英:/'feəlɪ/ 美:/'fɛrli/ </td>
                <td class="export-td">adv. 公平地；相当地；简直</td>
            </tr>
            
             <tr>
                <td class="export-td">2544</td>
                <td class="export-td">faith</td>
                <td class="export-td">英:/feɪθ/ 美:/feθ/ </td>
                <td class="export-td">n. 信任；信念；信仰；忠实</td>
            </tr>
            
             <tr>
                <td class="export-td">2545</td>
                <td class="export-td">faithful</td>
                <td class="export-td">英:/'feɪθfʊl/ 美:/'feθfəl/ </td>
                <td class="export-td">adj. 忠实的，忠诚的；如实的；准确可靠的</td>
            </tr>
            
             <tr>
                <td class="export-td">2546</td>
                <td class="export-td">fall</td>
                <td class="export-td">英:/fɔːl/ 美:/fɔl/ </td>
                <td class="export-td">1. vi. 落下；变成；来临；减弱
2. n. 秋天；瀑布；下降</td>
            </tr>
            
             <tr>
                <td class="export-td">2547</td>
                <td class="export-td">false</td>
                <td class="export-td">英:/fɔːls/ 美:/fɔls/ </td>
                <td class="export-td">1. adj. 伪造的；错误的；虚伪的
2. adv. 欺诈地</td>
            </tr>
            
             <tr>
                <td class="export-td">2548</td>
                <td class="export-td">fame</td>
                <td class="export-td">英:/feɪm/ 美:/fem/ </td>
                <td class="export-td">1. n. 名声，名望；[古]传闻，传说
2. vt. 使闻名，使有名望</td>
            </tr>
            
             <tr>
                <td class="export-td">2549</td>
                <td class="export-td">familiar</td>
                <td class="export-td">英:/fə'mɪlɪə/ 美:/fə'mɪljɚ/ </td>
                <td class="export-td">1. adj. 熟悉的；常见的；亲近的
2. n. 常客；密友</td>
            </tr>
            
             <tr>
                <td class="export-td">2550</td>
                <td class="export-td">family</td>
                <td class="export-td">英:/'fæmɪlɪ/ 美:/'fæməli/ </td>
                <td class="export-td">1. n. 家庭；家族；家属；亲属；子女；僚属
2. adj. 家庭的，家族的</td>
            </tr>
            
             <tr>
                <td class="export-td">2551</td>
                <td class="export-td">famine</td>
                <td class="export-td">英:/'fæmɪn/ 美:/'fæmɪn/ </td>
                <td class="export-td">n. 饥荒；饥饿，奇缺</td>
            </tr>
            
             <tr>
                <td class="export-td">2552</td>
                <td class="export-td">famous</td>
                <td class="export-td">英:/'feɪməs/ 美:/'feməs/ </td>
                <td class="export-td">adj. 著名的；[口]极好的，非常令人满意的</td>
            </tr>
            
             <tr>
                <td class="export-td">2553</td>
                <td class="export-td">fan</td>
                <td class="export-td">英:/fæn/ 美:/fæn/ </td>
                <td class="export-td">风扇</td>
            </tr>
            
             <tr>
                <td class="export-td">2554</td>
                <td class="export-td">fancy</td>
                <td class="export-td">英:/'fænsɪ/ 美:/'fænsi/ </td>
                <td class="export-td">1. n. 想像力；爱好；幻想
2. adj. 想象的；奇特的；精选的；昂贵的</td>
            </tr>
            
             <tr>
                <td class="export-td">2555</td>
                <td class="export-td">far</td>
                <td class="export-td">英:/fɑː/ 美:/fɑr/ </td>
                <td class="export-td">1. adv. 很；到很远的距离；遥远地；到很深的程度；久远地
2. adj. 远的；久远的</td>
            </tr>
            
             <tr>
                <td class="export-td">2556</td>
                <td class="export-td">fare</td>
                <td class="export-td">英:/feə/ 美:/fɛr/ </td>
                <td class="export-td">费用,食物</td>
            </tr>
            
             <tr>
                <td class="export-td">2557</td>
                <td class="export-td">farewell</td>
                <td class="export-td">英:/feə'wel/ 美:/ˌfɛr'wɛl/ </td>
                <td class="export-td">1. n. 告别，辞别；再会；再见
2. int. 别了！（常含有永别或不容易再见面的意思）；再会！</td>
            </tr>
            
             <tr>
                <td class="export-td">2558</td>
                <td class="export-td">farm</td>
                <td class="export-td">英:/fɑːm/ 美:/fɑrm/ </td>
                <td class="export-td">1. vi. 种田，务农；经营农场
2. n. 农场；畜牧场；农家</td>
            </tr>
            
             <tr>
                <td class="export-td">2559</td>
                <td class="export-td">farmer</td>
                <td class="export-td">英:/'fɑːmə/ 美:/ˈfɑrmɚ/ </td>
                <td class="export-td">n. 农夫，农民</td>
            </tr>
            
             <tr>
                <td class="export-td">2560</td>
                <td class="export-td">farther</td>
                <td class="export-td">英:/'fɑːðə/ 美:/'fɑrðɚ/ </td>
                <td class="export-td">1. adv. 此外；更远地；更进一步地
2. adj. 更远的（far的比较级）；进一步的</td>
            </tr>
            
             <tr>
                <td class="export-td">2561</td>
                <td class="export-td">fashion</td>
                <td class="export-td">英:/'fæʃ(ə)n/ 美:/'fæʃən/ </td>
                <td class="export-td">1. n. 样式；时尚；时装；时髦人物
2. vt. 做成…的形状；使用；改变</td>
            </tr>
            
             <tr>
                <td class="export-td">2562</td>
                <td class="export-td">fashionable</td>
                <td class="export-td">英:/'fæʃ(ə)nəb(ə)l/ 美:/'fæʃnəbl/ </td>
                <td class="export-td">流行的, 时髦的</td>
            </tr>
            
             <tr>
                <td class="export-td">2563</td>
                <td class="export-td">fast</td>
                <td class="export-td">英:/fɑːst/ 美:/fæst/ </td>
                <td class="export-td">1. adj. 快速的，迅速的；紧的，稳固的
2. adv. 紧紧地；彻底地；迅速地</td>
            </tr>
            
             <tr>
                <td class="export-td">2564</td>
                <td class="export-td">fasten</td>
                <td class="export-td">英:/'fɑːs(ə)n/ 美:/'fæsən/ </td>
                <td class="export-td">1. vt. 扎牢；使固定；集中于；强加于
2. vi. 扣紧；抓住；集中注意力</td>
            </tr>
            
             <tr>
                <td class="export-td">2565</td>
                <td class="export-td">fatal</td>
                <td class="export-td">英:/'feɪt(ə)l/ 美:/'fetl/ </td>
                <td class="export-td">adj. 致命的；重大的；毁灭性的；命中注定的</td>
            </tr>
            
             <tr>
                <td class="export-td">2566</td>
                <td class="export-td">fate</td>
                <td class="export-td">英:/feɪt/ 美:/fet/ </td>
                <td class="export-td">1. n. 命运
2. vt. 注定</td>
            </tr>
            
             <tr>
                <td class="export-td">2567</td>
                <td class="export-td">father</td>
                <td class="export-td">英:/'fɑːðə/ 美:/'fɑðɚ/ </td>
                <td class="export-td">1. n. 父亲，爸爸；神父；祖先；前辈
2. vt. 发明，创立；当…的父亲</td>
            </tr>
            
             <tr>
                <td class="export-td">2568</td>
                <td class="export-td">fault</td>
                <td class="export-td">英:/fɔːlt/ 美:/fɔlt/ </td>
                <td class="export-td">1. n. 故障；毛病；缺点；错误；[地]断层；（网球等）发球失误
2. vi. 弄错；[地]产生断层</td>
            </tr>
            
             <tr>
                <td class="export-td">2569</td>
                <td class="export-td">faulty</td>
                <td class="export-td">英:/'fɔːltɪ/ 美:/ˈfɔlti/ </td>
                <td class="export-td">adj. 有缺点的；有错误的</td>
            </tr>
            
             <tr>
                <td class="export-td">2570</td>
                <td class="export-td">favour</td>
                <td class="export-td">英:/'feɪvə/ 美:/ˈfevɚ/ </td>
                <td class="export-td">1. n. 偏爱；赞同；善行
2. vt. 赞成；喜爱；有助于</td>
            </tr>
            
             <tr>
                <td class="export-td">2571</td>
                <td class="export-td">favourite</td>
                <td class="export-td">/'feivərit/ </td>
                <td class="export-td">特别喜爱的</td>
            </tr>
            
             <tr>
                <td class="export-td">2572</td>
                <td class="export-td">fear</td>
                <td class="export-td">英:/fɪə/ 美:/fɪr/ </td>
                <td class="export-td">1. n. 害怕；担心；恐惧；敬畏
2. vt. 害怕；敬畏；为…担心</td>
            </tr>
            
             <tr>
                <td class="export-td">2573</td>
                <td class="export-td">feast</td>
                <td class="export-td">英:/fiːst/ 美:/fist/ </td>
                <td class="export-td">1. vt. 款待，宴请；享受
2. n. 节日；筵席，宴会</td>
            </tr>
            
             <tr>
                <td class="export-td">2574</td>
                <td class="export-td">feather</td>
                <td class="export-td">英:/'feðə/ 美:/'fɛðɚ/ </td>
                <td class="export-td">1. n. 羽毛
2. vt. 用羽毛装饰</td>
            </tr>
            
             <tr>
                <td class="export-td">2575</td>
                <td class="export-td">feature</td>
                <td class="export-td">英:/'fiːtʃə/ 美:/'fitʃɚ/ </td>
                <td class="export-td">1. n. 容貌；特色，特征；特写或专题节目
2. vi. 起重要作用</td>
            </tr>
            
             <tr>
                <td class="export-td">2576</td>
                <td class="export-td">February</td>
                <td class="export-td">英:/'febrʊərɪ/ 美:/'fɛbrʊ'ɛri/ </td>
                <td class="export-td">n. 二月</td>
            </tr>
            
             <tr>
                <td class="export-td">2577</td>
                <td class="export-td">federal</td>
                <td class="export-td">英:/'fed(ə)r(ə)l/ 美:/'fɛdərəl/ </td>
                <td class="export-td">1. adj. 联邦的；同盟的
2. n. 北部联邦同盟盟员；北京连邦软件产业发展公司，国内主要的正版软件经销商</td>
            </tr>
            
             <tr>
                <td class="export-td">2578</td>
                <td class="export-td">fee</td>
                <td class="export-td">英:/fiː/ 美:/fi/ </td>
                <td class="export-td">1. n. 酬金；小费；费用
2. vt. 付费给……</td>
            </tr>
            
             <tr>
                <td class="export-td">2579</td>
                <td class="export-td">feeble</td>
                <td class="export-td">英:/'fiːb(ə)l/ 美:/'fibl/ </td>
                <td class="export-td">adj. 微弱的，无力的；虚弱的；薄弱的</td>
            </tr>
            
             <tr>
                <td class="export-td">2580</td>
                <td class="export-td">feed</td>
                <td class="export-td">英:/fiːd/ 美:/fid/ </td>
                <td class="export-td">1. vt. 喂养；放牧；供给；抚养（家庭等）；靠…为生
2. vi. 吃东西；流入</td>
            </tr>
            
             <tr>
                <td class="export-td">2581</td>
                <td class="export-td">feedback</td>
                <td class="export-td">英:/'fiːdbæk/ 美:/'fidbæk/ </td>
                <td class="export-td">n. 反馈；回复；成果，资料</td>
            </tr>
            
             <tr>
                <td class="export-td">2582</td>
                <td class="export-td">feel</td>
                <td class="export-td">英:/fiːl/ 美:/fil/ </td>
                <td class="export-td">1. vt. 感觉；试探；触摸；认为
2. vi. 觉得；摸索</td>
            </tr>
            
             <tr>
                <td class="export-td">2583</td>
                <td class="export-td">feeling</td>
                <td class="export-td">英:/'fiːlɪŋ/ 美:/'filɪŋ/ </td>
                <td class="export-td">1. n. 感觉，触觉；感情，情绪；同情
2. adj. 有同情心的；富于感情的；有感觉的</td>
            </tr>
            
             <tr>
                <td class="export-td">2584</td>
                <td class="export-td">fellow</td>
                <td class="export-td">英:/'feləʊ/ 美:/'fɛlo/ </td>
                <td class="export-td">1. n. 同事；家伙；朋友；会员
2. adj. 同伴的，同事的；同道的</td>
            </tr>
            
             <tr>
                <td class="export-td">2585</td>
                <td class="export-td">fertile</td>
                <td class="export-td">英:/'fɜːtaɪl/ 美:/'fɝtl/ </td>
                <td class="export-td">1. adj. 富饶的，肥沃的；能生育的
2. n. 肥沃，多产</td>
            </tr>
            
             <tr>
                <td class="export-td">2586</td>
                <td class="export-td">fertilizer</td>
                <td class="export-td">英:/'fɜːtɪlaɪzə/ 美:/'fɝtəlaɪzɚ/ </td>
                <td class="export-td">肥料</td>
            </tr>
            
             <tr>
                <td class="export-td">2587</td>
                <td class="export-td">festival</td>
                <td class="export-td">英:/'festɪv(ə)l/ 美:/'fɛstɪvl/ </td>
                <td class="export-td">1. n. 节日；庆祝，纪念活动；欢乐
2. adj. 节日的，喜庆的；快乐的</td>
            </tr>
            
             <tr>
                <td class="export-td">2588</td>
                <td class="export-td">fetch</td>
                <td class="export-td">英:/fetʃ/ 美:/fɛtʃ/ </td>
                <td class="export-td">1. vt. 接来；到达；取来；吸引
2. vi. 取物；卖得；拿</td>
            </tr>
            
             <tr>
                <td class="export-td">2589</td>
                <td class="export-td">fever</td>
                <td class="export-td">英:/'fiːvə/ 美:/'fivɚ/ </td>
                <td class="export-td">1. n. 发烧，发热；狂热
2. vt. 使发烧；使狂热；使患热病</td>
            </tr>
            
             <tr>
                <td class="export-td">2590</td>
                <td class="export-td">few</td>
                <td class="export-td">英:/fjuː/ 美:/fju/ </td>
                <td class="export-td">1. adj. 很少的；几乎没有的
2. pron. 很少</td>
            </tr>
            
             <tr>
                <td class="export-td">2591</td>
                <td class="export-td">fibre</td>
                <td class="export-td">英:/'faibə/ 美:/ˈfaɪbɚ/ </td>
                <td class="export-td">n. 纤维；纤维制品</td>
            </tr>
            
             <tr>
                <td class="export-td">2592</td>
                <td class="export-td">fiction</td>
                <td class="export-td">英:/'fɪkʃ(ə)n/ 美:/'fɪkʃən/ </td>
                <td class="export-td">n. 小说；虚构，编造；谎言</td>
            </tr>
            
             <tr>
                <td class="export-td">2593</td>
                <td class="export-td">field</td>
                <td class="export-td">英:/fi:ld/ 美:/fild/ </td>
                <td class="export-td">1. n. 领域，牧场，旷野，战场，运动场
2. vi. 担任场外队员</td>
            </tr>
            
             <tr>
                <td class="export-td">2594</td>
                <td class="export-td">fierce</td>
                <td class="export-td">英:/fɪəs/ 美:/fɪrs/ </td>
                <td class="export-td">adj. 凶猛的；暴躁的；猛烈的</td>
            </tr>
            
             <tr>
                <td class="export-td">2595</td>
                <td class="export-td">fifteen</td>
                <td class="export-td">英:/fɪf'tiːn/ 美:/ˌfɪf'tin/ </td>
                <td class="export-td">1. n. 十五；十五个；十五人组成的橄榄球队
2. adj. 十五的</td>
            </tr>
            
             <tr>
                <td class="export-td">2596</td>
                <td class="export-td">fifth</td>
                <td class="export-td">英:/fɪfθ/ 美:/fɪfθ/ </td>
                <td class="export-td">1. adj. 第五的；五分之一的
2. n. 第五；五分之一</td>
            </tr>
            
             <tr>
                <td class="export-td">2597</td>
                <td class="export-td">fifty</td>
                <td class="export-td">英:/'fɪftɪ/ 美:/'fɪfti/ </td>
                <td class="export-td">1. n. 五十；五十个；编号为50的东西
2. adj. 五十的；五十个的；众多的</td>
            </tr>
            
             <tr>
                <td class="export-td">2598</td>
                <td class="export-td">fight</td>
                <td class="export-td">英:/faɪt/ 美:/faɪt/ </td>
                <td class="export-td">1. vi. 打架；打仗；搏斗，斗争
2. vt. 打架；与…打仗，与…斗争；反对…提案</td>
            </tr>
            
             <tr>
                <td class="export-td">2599</td>
                <td class="export-td">figure</td>
                <td class="export-td">英:/'fɪgə/ 美:/'fɪɡjɚ/ </td>
                <td class="export-td">1. n. 图形；数字；（人的）体形；人物；画像；价格
2. vi. 出现；计算；扮演角色</td>
            </tr>
            
             <tr>
                <td class="export-td">2600</td>
                <td class="export-td">file</td>
                <td class="export-td">英:/faɪl/ 美:/faɪl/ </td>
                <td class="export-td">1. n. 文件；档案；锉刀；文件夹
2. vt. 锉；琢磨；把…归档；提出</td>
            </tr>
            
             <tr>
                <td class="export-td">2601</td>
                <td class="export-td">fill</td>
                <td class="export-td">英:/fɪl/ 美:/fɪl/ </td>
                <td class="export-td">1. vt. 装满，使充满；满足；堵塞；任职
2. vi. 被充满，膨胀</td>
            </tr>
            
             <tr>
                <td class="export-td">2602</td>
                <td class="export-td">film</td>
                <td class="export-td">英:/fɪlm/ 美:/fɪlm/ </td>
                <td class="export-td">1. n. 胶卷；电影；薄膜；轻烟
2. vt. 在…上覆以薄膜；把…拍成电影</td>
            </tr>
            
             <tr>
                <td class="export-td">2603</td>
                <td class="export-td">filter</td>
                <td class="export-td">英:/'fɪltə/ 美:/'fɪltɚ/ </td>
                <td class="export-td">1. vi. 慢慢传开；滤过；渗入
2. n. 滤波器；过滤器；滤光器；筛选</td>
            </tr>
            
             <tr>
                <td class="export-td">2604</td>
                <td class="export-td">final</td>
                <td class="export-td">英:/'faɪn(ə)l/ 美:/'faɪnl/ </td>
                <td class="export-td">1. adj. 最终的；决定性的；不可更改的
2. n. 决赛；期末考试；当日报纸的末版</td>
            </tr>
            
             <tr>
                <td class="export-td">2605</td>
                <td class="export-td">finally</td>
                <td class="export-td">英:/'faɪnəlɪ/ 美:/'faɪnəli/ </td>
                <td class="export-td">adv. 终于；最后；决定性地</td>
            </tr>
            
             <tr>
                <td class="export-td">2606</td>
                <td class="export-td">finance</td>
                <td class="export-td">英:/faɪ'næns/ 美:/'faɪnæns/ </td>
                <td class="export-td">1. n. 财政，财政学；金融
2. vt. 负担经费，供给…经费</td>
            </tr>
            
             <tr>
                <td class="export-td">2607</td>
                <td class="export-td">financial</td>
                <td class="export-td">英:/faɪ'nænʃ(ə)l/ 美:/faɪ'nænʃl/ </td>
                <td class="export-td">金融的,财政的</td>
            </tr>
            
             <tr>
                <td class="export-td">2608</td>
                <td class="export-td">find</td>
                <td class="export-td">英:/faɪnd/ 美:/faɪnd/ </td>
                <td class="export-td">1. vt. 发现；认为；感到；获得
2. vi. 裁决</td>
            </tr>
            
             <tr>
                <td class="export-td">2609</td>
                <td class="export-td">finger</td>
                <td class="export-td">英:/'fɪŋgə/ 美:/'fɪŋɡɚ/ </td>
                <td class="export-td">1. n. 手指；指针，指状物
2. vt. 用手指拨弄；伸出</td>
            </tr>
            
             <tr>
                <td class="export-td">2610</td>
                <td class="export-td">fine</td>
                <td class="export-td">英:/faɪn/ 美:/faɪn/ </td>
                <td class="export-td">1. adj. 好的；优良的；晴朗的；健康的；细小的，精美的
2. n. 罚款</td>
            </tr>
            
             <tr>
                <td class="export-td">2611</td>
                <td class="export-td">finish</td>
                <td class="export-td">英:/'fɪnɪʃ/ 美:/'fɪnɪʃ/ </td>
                <td class="export-td">1. vt. 完成；结束；用完
2. vi. 结束，终止；完成；终结</td>
            </tr>
            
             <tr>
                <td class="export-td">2612</td>
                <td class="export-td">fire</td>
                <td class="export-td">英:/'faɪə/ 美:/faɪr/ </td>
                <td class="export-td">1. n. 火；火灾；炉火；热情；炮火；激情；磨难
2. vt. 解雇；点燃；烧制；使发光；开除；放枪；激动</td>
            </tr>
            
             <tr>
                <td class="export-td">2613</td>
                <td class="export-td">firm</td>
                <td class="export-td">英:/fɜːm/ 美:/fɝm/ </td>
                <td class="export-td">1. adj. 坚定的；结实的；牢固的；严格的
2. vt. 使牢固；使坚定</td>
            </tr>
            
             <tr>
                <td class="export-td">2614</td>
                <td class="export-td">first</td>
                <td class="export-td">英:/fɜːst/ 美:/fɝst/ </td>
                <td class="export-td">1. adv. 第一；首先；优先；宁愿
2. n. 第一；开始；冠军</td>
            </tr>
            
             <tr>
                <td class="export-td">2615</td>
                <td class="export-td">fish</td>
                <td class="export-td">英:/fɪʃ/ 美:/fɪʃ/ </td>
                <td class="export-td">1. vi. 捕鱼，钓鱼；用钩捞取
2. n. 鱼，鱼类</td>
            </tr>
            
             <tr>
                <td class="export-td">2616</td>
                <td class="export-td">fist</td>
                <td class="export-td">英:/fɪst/ 美:/fɪst/ </td>
                <td class="export-td">1. n. 拳头；掌握；笔迹
2. vt. 紧握；拳打；握成拳</td>
            </tr>
            
             <tr>
                <td class="export-td">2617</td>
                <td class="export-td">fit</td>
                <td class="export-td">英:/fɪt/ 美:/fɪt/ </td>
                <td class="export-td">1. vt. 安装；使……适应；使……合身；与……相符
2. vi. 适合；合身；符合，配合</td>
            </tr>
            
             <tr>
                <td class="export-td">2618</td>
                <td class="export-td">five</td>
                <td class="export-td">英:/faɪv/ 美:/faɪv/ </td>
                <td class="export-td">1. n. 五，五个；[口]五美元钞票
2. num. 五，五个</td>
            </tr>
            
             <tr>
                <td class="export-td">2619</td>
                <td class="export-td">fix</td>
                <td class="export-td">英:/fɪks/ 美:/fɪks/ </td>
                <td class="export-td">1. vt. 安装；修理；使固定；准备
2. vi. 固定；注视</td>
            </tr>
            
             <tr>
                <td class="export-td">2620</td>
                <td class="export-td">flag</td>
                <td class="export-td">英:/flæg/ 美:/flæg/ </td>
                <td class="export-td">1. vi. 标记；枯萎；衰退
2. vt. 标记；插旗</td>
            </tr>
            
             <tr>
                <td class="export-td">2621</td>
                <td class="export-td">flame</td>
                <td class="export-td">英:/fleɪm/ 美:/flem/ </td>
                <td class="export-td">1. n. 火焰；热情；光辉
2. v. 泛红；焚烧</td>
            </tr>
            
             <tr>
                <td class="export-td">2622</td>
                <td class="export-td">flare</td>
                <td class="export-td">英:/fleə/ 美:/flɛr/ </td>
                <td class="export-td">1. vt. 使张开；使闪耀；用发光信号发出；使外倾
2. vi. 闪耀，闪光；燃烧；突然发怒</td>
            </tr>
            
             <tr>
                <td class="export-td">2623</td>
                <td class="export-td">flash</td>
                <td class="export-td">英:/flæʃ/ 美:/flæʃ/ </td>
                <td class="export-td">1. vt. 使闪光；反射
2. n. 闪光，闪现；一瞬间</td>
            </tr>
            
             <tr>
                <td class="export-td">2624</td>
                <td class="export-td">flat</td>
                <td class="export-td">英:/flæt/ 美:/flæt/ </td>
                <td class="export-td">1. adj. 平坦的；单调的；浅的；扁平的
2. adv. 断然地；平直地</td>
            </tr>
            
             <tr>
                <td class="export-td">2625</td>
                <td class="export-td">flavour</td>
                <td class="export-td">英:/'fleɪvə/ 美:/ˈflevɚ/ </td>
                <td class="export-td">1. n. 香味；滋味
2. vt. 给……调味；给……增添风趣</td>
            </tr>
            
             <tr>
                <td class="export-td">2626</td>
                <td class="export-td">fleet</td>
                <td class="export-td">英:/fliːt/ 美:/flit/ </td>
                <td class="export-td">1. adj. 快速的，敏捷的
2. n. 舰队；小河；港湾</td>
            </tr>
            
             <tr>
                <td class="export-td">2627</td>
                <td class="export-td">flesh</td>
                <td class="export-td">英:/fleʃ/ 美:/flɛʃ/ </td>
                <td class="export-td">1. n. 肉体；肉
2. vt. 喂肉给…；使发胖</td>
            </tr>
            
             <tr>
                <td class="export-td">2628</td>
                <td class="export-td">flexible</td>
                <td class="export-td">英:/'fleksɪb(ə)l/ 美:/'flɛksəbl/ </td>
                <td class="export-td">adj. 灵活的；柔韧的；易弯曲的</td>
            </tr>
            
             <tr>
                <td class="export-td">2629</td>
                <td class="export-td">flight</td>
                <td class="export-td">英:/flaɪt/ 美:/flaɪt/ </td>
                <td class="export-td">1. n. 飞行；班机；逃走
2. vt. 使惊飞；射击</td>
            </tr>
            
             <tr>
                <td class="export-td">2630</td>
                <td class="export-td">float</td>
                <td class="export-td">英:/fləʊt/ 美:/flot/ </td>
                <td class="export-td">1. vt. 使漂浮；实行
2. vi. 浮动；摇摆；飘动，散播；付诸实施</td>
            </tr>
            
             <tr>
                <td class="export-td">2631</td>
                <td class="export-td">flock</td>
                <td class="export-td">英:/flɔk/ 美:/flɑk/ </td>
                <td class="export-td">1. n. 群；棉束（等于floc）
2. vt. 用棉束填满</td>
            </tr>
            
             <tr>
                <td class="export-td">2632</td>
                <td class="export-td">flood</td>
                <td class="export-td">英:/flʌd/ 美:/flʌd/ </td>
                <td class="export-td">1. vt. 淹没；充满；溢出
2. vi. 为水淹没；涌出；涌进</td>
            </tr>
            
             <tr>
                <td class="export-td">2633</td>
                <td class="export-td">floor</td>
                <td class="export-td">英:/flɔː/ 美:/flɔr/ </td>
                <td class="export-td">1. n. 地板，地面；楼层；基底；议员席
2. vt. 铺地板；打倒，击倒；（被困难）难倒</td>
            </tr>
            
             <tr>
                <td class="export-td">2634</td>
                <td class="export-td">flour</td>
                <td class="export-td">英:/'flaʊə/ 美:/'flaʊɚ/ </td>
                <td class="export-td">1. n. 面粉；粉状物质
2. vt. 撒粉于；把…磨成粉</td>
            </tr>
            
             <tr>
                <td class="export-td">2635</td>
                <td class="export-td">flourish</td>
                <td class="export-td">英:/'flʌrɪʃ/ 美:/'flɝɪʃ/ </td>
                <td class="export-td">1. n. 兴旺；茂盛；挥舞；炫耀；华饰
2. vt. 夸耀；挥舞</td>
            </tr>
            
             <tr>
                <td class="export-td">2636</td>
                <td class="export-td">flow</td>
                <td class="export-td">英:/fləʊ/ 美:/flo/ </td>
                <td class="export-td">1. vi. 流动，涌流；飘扬；川流不息
2. vt. 淹没，溢过</td>
            </tr>
            
             <tr>
                <td class="export-td">2637</td>
                <td class="export-td">flower</td>
                <td class="export-td">英:/'flaʊə/ 美:/'flaʊɚ/ </td>
                <td class="export-td">1. n. 花；精华；开花植物
2. vi. 开花；成熟，发育；繁荣；旺盛</td>
            </tr>
            
             <tr>
                <td class="export-td">2638</td>
                <td class="export-td">flu</td>
                <td class="export-td">英:/fluː/ 美:/flu/ </td>
                <td class="export-td">n. 流感</td>
            </tr>
            
             <tr>
                <td class="export-td">2639</td>
                <td class="export-td">fluent</td>
                <td class="export-td">英:/'fluːənt/ 美:/'fluənt/ </td>
                <td class="export-td">adj. 流畅的，流利的；液态的；畅流的</td>
            </tr>
            
             <tr>
                <td class="export-td">2640</td>
                <td class="export-td">fluid</td>
                <td class="export-td">英:/'fluːɪd/ 美:/'fluɪd/ </td>
                <td class="export-td">1. adj. 流动的；不固定的；流畅的
2. n. 流体；液体</td>
            </tr>
            
             <tr>
                <td class="export-td">2641</td>
                <td class="export-td">flush</td>
                <td class="export-td">英:/flʌʃ/ 美:/flʌʃ/ </td>
                <td class="export-td">1. n. 激动，洋溢；面红；萌芽；旺盛；奔流
2. vt. 使齐平；用水冲洗；使激动；发红，使发亮</td>
            </tr>
            
             <tr>
                <td class="export-td">2642</td>
                <td class="export-td">fly</td>
                <td class="export-td">英:/flaɪ/ 美:/flaɪ/ </td>
                <td class="export-td">1. vi. 飞；飘扬；驾驶飞机
2. vt. 飞行；使飘扬；飞越</td>
            </tr>
            
             <tr>
                <td class="export-td">2643</td>
                <td class="export-td">focus</td>
                <td class="export-td">英:/'fəʊkəs/ 美:/'fokəs/ </td>
                <td class="export-td">1. n. 焦点；焦距；清晰；中心
2. vt. 使聚焦；使集中</td>
            </tr>
            
             <tr>
                <td class="export-td">2644</td>
                <td class="export-td">fog</td>
                <td class="export-td">英:/fɒg/ 美:/fɔɡ/ </td>
                <td class="export-td">1. n. 雾；烟雾，尘雾；迷惑
2. vt. 以雾笼罩；使模糊；使困惑</td>
            </tr>
            
             <tr>
                <td class="export-td">2645</td>
                <td class="export-td">fold</td>
                <td class="export-td">英:/fəʊld/ 美:/fold/ </td>
                <td class="export-td">1. vt. 折叠；合拢；抱住；笼罩
2. n. 折痕；羊栏；信徒</td>
            </tr>
            
             <tr>
                <td class="export-td">2646</td>
                <td class="export-td">folk</td>
                <td class="export-td">英:/fəʊk/ 美:/fok/ </td>
                <td class="export-td">1. n. 人们；民族；亲属（复数）
2. adj. 民间的</td>
            </tr>
            
             <tr>
                <td class="export-td">2647</td>
                <td class="export-td">follow</td>
                <td class="export-td">英:/'fɒləʊ/ 美:/'fɑlo/ </td>
                <td class="export-td">1. vt. 跟随；追求；遵循；密切注意
2. vi. 跟随；接着</td>
            </tr>
            
             <tr>
                <td class="export-td">2648</td>
                <td class="export-td">following</td>
                <td class="export-td">英:/'fɒləʊɪŋ/ 美:/ˈfɑloɪŋ/ </td>
                <td class="export-td">以下</td>
            </tr>
            
             <tr>
                <td class="export-td">2649</td>
                <td class="export-td">fond</td>
                <td class="export-td">英:/fɒnd/ 美:/fɑnd/ </td>
                <td class="export-td">adj. 喜欢的；温柔的；宠爱的</td>
            </tr>
            
             <tr>
                <td class="export-td">2650</td>
                <td class="export-td">food</td>
                <td class="export-td">英:/fuːd/ 美:/fud/ </td>
                <td class="export-td">n. 食物；养料</td>
            </tr>
            
             <tr>
                <td class="export-td">2651</td>
                <td class="export-td">fool</td>
                <td class="export-td">英:/fuːl/ 美:/ful/ </td>
                <td class="export-td">1. vi. 开玩笑；欺骗；戏弄
2. n. 愚人；傻瓜；受骗者</td>
            </tr>
            
             <tr>
                <td class="export-td">2652</td>
                <td class="export-td">foolish</td>
                <td class="export-td">英:/'fuːlɪʃ/ 美:/'fulɪʃ/ </td>
                <td class="export-td">adj. 愚蠢的；傻的</td>
            </tr>
            
             <tr>
                <td class="export-td">2653</td>
                <td class="export-td">foot</td>
                <td class="export-td">英:/fʊt/ 美:/fʊt/ </td>
                <td class="export-td">1. n. 脚；英尺；末尾；步调
2. vi. 步行；跳舞；总计</td>
            </tr>
            
             <tr>
                <td class="export-td">2654</td>
                <td class="export-td">football</td>
                <td class="export-td">英:/'fʊtbɔːl/ 美:/'fʊtbɔl/ </td>
                <td class="export-td">1. n. 足球，橄榄球
2. vi. 踢足球；打橄榄球</td>
            </tr>
            
             <tr>
                <td class="export-td">2655</td>
                <td class="export-td">footstep</td>
                <td class="export-td">英:/'fʊtstep/ 美:/ˈfʊtˌstɛp/ </td>
                <td class="export-td">n. 脚步声；脚步；足迹</td>
            </tr>
            
             <tr>
                <td class="export-td">2656</td>
                <td class="export-td">for</td>
                <td class="export-td">英:/fɔː/ 美:/fɔr,fə/ </td>
                <td class="export-td">1. prep. 为，为了；给；因为；对于；适合于；至于
2. conj. 因为</td>
            </tr>
            
             <tr>
                <td class="export-td">2657</td>
                <td class="export-td">forbid</td>
                <td class="export-td">英:/fə'bɪd/ 美:/fɚ'bɪd/ </td>
                <td class="export-td">vt. 禁止；妨碍，阻止</td>
            </tr>
            
             <tr>
                <td class="export-td">2658</td>
                <td class="export-td">force</td>
                <td class="export-td">英:/fɔːs/ 美:/fɔrs/ </td>
                <td class="export-td">1. n. 力量；武力；魄力；军队
2. vt. 强迫；强加；促使，推动</td>
            </tr>
            
             <tr>
                <td class="export-td">2659</td>
                <td class="export-td">forecast</td>
                <td class="export-td">英:/'fɔːkɑːst/ 美:/'fɔrkæst/ </td>
                <td class="export-td">1. vt. 预报，预测；预示
2. n. 预想；预测，预报</td>
            </tr>
            
             <tr>
                <td class="export-td">2660</td>
                <td class="export-td">forehead</td>
                <td class="export-td">英:/'fɔːhed/ 美:/'fɔr'hɛd/ </td>
                <td class="export-td">n. 额，前额</td>
            </tr>
            
             <tr>
                <td class="export-td">2661</td>
                <td class="export-td">foreign</td>
                <td class="export-td">英:/'fɒrɪn/ 美:/'fɔrən/ </td>
                <td class="export-td">adj. 外国的；[医]异质的；不相关的；外交的</td>
            </tr>
            
             <tr>
                <td class="export-td">2662</td>
                <td class="export-td">forest</td>
                <td class="export-td">英:/'fɒrɪst/ 美:/'fɔrɪst/ </td>
                <td class="export-td">1. vt. 植树于，使成为森林
2. n. 森林</td>
            </tr>
            
             <tr>
                <td class="export-td">2663</td>
                <td class="export-td">forever</td>
                <td class="export-td">英:/fə'revə/ 美:/fɚ'ɛvɚ/ </td>
                <td class="export-td">adv. 永远；常常；不断地</td>
            </tr>
            
             <tr>
                <td class="export-td">2664</td>
                <td class="export-td">forget</td>
                <td class="export-td">英:/fə'get/ 美:/fɚ'ɡɛt/ </td>
                <td class="export-td">1. vt. 忘记；忽略
2. vi. 忘记</td>
            </tr>
            
             <tr>
                <td class="export-td">2665</td>
                <td class="export-td">forgive</td>
                <td class="export-td">英:/fə'gɪv/ 美:/fɚ'ɡɪv/ </td>
                <td class="export-td">1. vt. 原谅；免除（债务、义务等）
2. vi. 表示原谅</td>
            </tr>
            
             <tr>
                <td class="export-td">2666</td>
                <td class="export-td">fork</td>
                <td class="export-td">英:/fɔːk/ 美:/fɔrk/ </td>
                <td class="export-td">1. n. 餐叉；叉；耙
2. vt. 叉起；使成叉状</td>
            </tr>
            
             <tr>
                <td class="export-td">2667</td>
                <td class="export-td">form</td>
                <td class="export-td">英:/fɔːm/ 美:/fɔrm/ </td>
                <td class="export-td">1. n. 形式，形状；形态，外形；表格；方式
2. vt. 构成，组成；排列，组织；产生，塑造</td>
            </tr>
            
             <tr>
                <td class="export-td">2668</td>
                <td class="export-td">formal</td>
                <td class="export-td">英:/'fɔːm(ə)l/ 美:/'fɔrml/ </td>
                <td class="export-td">1. adj. 正式的；拘谨的；有条理的
2. n. 正式的社交活动；夜礼服</td>
            </tr>
            
             <tr>
                <td class="export-td">2669</td>
                <td class="export-td">former</td>
                <td class="export-td">英:/'fɔːmə/ 美:/'fɔrmɚ/ </td>
                <td class="export-td">1. adj. 从前的，前者的；前任的
2. n. 模型，样板；起形成作用的人</td>
            </tr>
            
             <tr>
                <td class="export-td">2670</td>
                <td class="export-td">formula</td>
                <td class="export-td">英:/'fɔːmjʊlə/ 美:/'fɔrmjələ/ </td>
                <td class="export-td">n. 公式，准则；配方；婴儿食品</td>
            </tr>
            
             <tr>
                <td class="export-td">2671</td>
                <td class="export-td">fortnight</td>
                <td class="export-td">英:/'fɔːtnaɪt/ 美:/'fɔrtnaɪt/ </td>
                <td class="export-td">两星期，十四天</td>
            </tr>
            
             <tr>
                <td class="export-td">2672</td>
                <td class="export-td">fortunate</td>
                <td class="export-td">英:/'fɔːtʃ(ə)nət/ 美:/'fɔrtʃənət/ </td>
                <td class="export-td">幸运的,侥幸的</td>
            </tr>
            
             <tr>
                <td class="export-td">2673</td>
                <td class="export-td">fortunately</td>
                <td class="export-td">/'fɔrtʃənətli/ </td>
                <td class="export-td">幸运地,幸亏</td>
            </tr>
            
             <tr>
                <td class="export-td">2674</td>
                <td class="export-td">fortune</td>
                <td class="export-td">英:/'fɔːtʃuːn/ 美:/'fɔrtʃən/ </td>
                <td class="export-td">1. n. 运气；财富；命运
2. vt. 给予财富</td>
            </tr>
            
             <tr>
                <td class="export-td">2675</td>
                <td class="export-td">forty</td>
                <td class="export-td">英:/'fɔːtɪ/ 美:/'fɔrti/ </td>
                <td class="export-td">1. n. 四十
2. adj. 四十的；四十个的</td>
            </tr>
            
             <tr>
                <td class="export-td">2676</td>
                <td class="export-td">forward</td>
                <td class="export-td">英:/'fɔːwəd/ 美:/'fɔrwɚd/ </td>
                <td class="export-td">1. adj. 早的；向前的；迅速的
2. adv. 向将来；向前地</td>
            </tr>
            
             <tr>
                <td class="export-td">2677</td>
                <td class="export-td">found</td>
                <td class="export-td">英:/faʊnd/ 美:/faʊnd/ </td>
                <td class="export-td">1. vt. 创立，建立；创办
2. v. 找到（find的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">2678</td>
                <td class="export-td">foundation</td>
                <td class="export-td">英:/faʊn'deɪʃ(ə)n/ 美:/faʊn'deʃən/ </td>
                <td class="export-td">基础, 根据, 建立</td>
            </tr>
            
             <tr>
                <td class="export-td">2679</td>
                <td class="export-td">fountain</td>
                <td class="export-td">英:/'faʊntɪn/ 美:/'faʊntn/ </td>
                <td class="export-td">n. 喷泉，泉水；源泉</td>
            </tr>
            
             <tr>
                <td class="export-td">2680</td>
                <td class="export-td">four</td>
                <td class="export-td">英:/fɔː/ 美:/fɔr/ </td>
                <td class="export-td">1. num. 四；四个
2. adj. 四的；四个的</td>
            </tr>
            
             <tr>
                <td class="export-td">2681</td>
                <td class="export-td">fourteen</td>
                <td class="export-td">英:/fɔː'tiːn/ 美:/ˌfɔr'tin/ </td>
                <td class="export-td">1. num. 十四
2. n. 十四</td>
            </tr>
            
             <tr>
                <td class="export-td">2682</td>
                <td class="export-td">fox</td>
                <td class="export-td">英:/fɒks/ 美:/fɑks/ </td>
                <td class="export-td">1. vt. [口]欺骗；使变酸
2. n. 狐狸；狡猾的人</td>
            </tr>
            
             <tr>
                <td class="export-td">2683</td>
                <td class="export-td">ghost</td>
                <td class="export-td">英:/gəʊst/ 美:/ɡost/ </td>
                <td class="export-td">1. n. 鬼，幽灵
2. vt. 作祟于；替…捉刀；为人代笔</td>
            </tr>
            
             <tr>
                <td class="export-td">2684</td>
                <td class="export-td">giant</td>
                <td class="export-td">英:/'dʒaɪənt/ 美:/'dʒaɪənt/ </td>
                <td class="export-td">1. n. 巨人；巨大的动物；伟人
2. adj. 巨大的；巨人般的</td>
            </tr>
            
             <tr>
                <td class="export-td">2685</td>
                <td class="export-td">gift</td>
                <td class="export-td">英:/gɪft/ 美:/ɡɪft/ </td>
                <td class="export-td">1. n. 礼物；赠品；天赋
2. vt. 向…赠送；赋予</td>
            </tr>
            
             <tr>
                <td class="export-td">2686</td>
                <td class="export-td">girl</td>
                <td class="export-td">英:/gɜːl/ 美:/ɡɝl/ </td>
                <td class="export-td">n. 女孩，姑娘；女儿；女朋友</td>
            </tr>
            
             <tr>
                <td class="export-td">2687</td>
                <td class="export-td">give</td>
                <td class="export-td">英:/gɪv/ 美:/ɡɪv/ </td>
                <td class="export-td">1. vt. 给；授予；让步；产生；举办
2. n. 弹性；伸展性；弯曲</td>
            </tr>
            
             <tr>
                <td class="export-td">2688</td>
                <td class="export-td">granddaughter</td>
                <td class="export-td">英:/'grændɔːtə/ 美:/'ɡrændɔtɚ/ </td>
                <td class="export-td">孙女, 外孙女</td>
            </tr>
            
             <tr>
                <td class="export-td">2689</td>
                <td class="export-td">grandson</td>
                <td class="export-td">英:/'græn(d)sʌn/ 美:/ˈɡrændˌsʌn/ </td>
                <td class="export-td">n. 孙子；外孙</td>
            </tr>
            
             <tr>
                <td class="export-td">2690</td>
                <td class="export-td">grey</td>
                <td class="export-td">英:/greɪ/ 美:/ɡre/ </td>
                <td class="export-td">1. adj. 灰色的；灰白的
2. vt. 使变成灰色；使变老</td>
            </tr>
            
             <tr>
                <td class="export-td">2691</td>
                <td class="export-td">guarantee</td>
                <td class="export-td">英:/gær(ə)n'tiː/ 美:/ˌɡærən'ti/ </td>
                <td class="export-td">保证 , 担保</td>
            </tr>
            
             <tr>
                <td class="export-td">2692</td>
                <td class="export-td">guard</td>
                <td class="export-td">英:/gɑːd/ 美:/ɡɑrd/ </td>
                <td class="export-td">1. n. 警戒；守卫；护卫队；防护装置
2. vi. 警惕</td>
            </tr>
            
             <tr>
                <td class="export-td">2693</td>
                <td class="export-td">guess</td>
                <td class="export-td">英:/ges/ 美:/ɡɛs/ </td>
                <td class="export-td">1. vt. 猜测；推测；猜中；[美口]认为
2. vi. 推测；猜；猜中</td>
            </tr>
            
             <tr>
                <td class="export-td">2694</td>
                <td class="export-td">guest</td>
                <td class="export-td">英:/ɡest/ 美:/ɡɛst/ </td>
                <td class="export-td">1. n. 客人，宾客；顾客
2. vt. 款待，招待</td>
            </tr>
            
             <tr>
                <td class="export-td">2695</td>
                <td class="export-td">guidance</td>
                <td class="export-td">英:/'gaɪd(ə)ns/ 美:/'gaɪdns/ </td>
                <td class="export-td">n. 指导，引导；领导</td>
            </tr>
            
             <tr>
                <td class="export-td">2696</td>
                <td class="export-td">guide</td>
                <td class="export-td">英:/gaɪd/ 美:/ɡaɪd/ </td>
                <td class="export-td">1. n. 指南；向导；入门书
2. vt. 带领；引导；操纵</td>
            </tr>
            
             <tr>
                <td class="export-td">2697</td>
                <td class="export-td">guilty</td>
                <td class="export-td">英:/'gɪltɪ/ 美:/'ɡɪlti/ </td>
                <td class="export-td">adj. 有罪的；内疚的</td>
            </tr>
            
             <tr>
                <td class="export-td">2698</td>
                <td class="export-td">gulf</td>
                <td class="export-td">英:/gʌlf/ 美:/ɡʌlf/ </td>
                <td class="export-td">1. n. 海湾；深渊；漩涡；分歧
2. vt. 吞没</td>
            </tr>
            
             <tr>
                <td class="export-td">2699</td>
                <td class="export-td">gum</td>
                <td class="export-td">英:/gʌm/ 美:/ɡʌm/ </td>
                <td class="export-td">1. n. 树胶；橡皮；口香糖
2. vt. 使…有粘性；用胶粘，涂以树胶</td>
            </tr>
            
             <tr>
                <td class="export-td">2700</td>
                <td class="export-td">habit</td>
                <td class="export-td">英:/'hæbɪt/ 美:/'hæbɪt/ </td>
                <td class="export-td">1. n. 习惯，习性；嗜好
2. vt. 使穿衣</td>
            </tr>
            
             <tr>
                <td class="export-td">2701</td>
                <td class="export-td">hair</td>
                <td class="export-td">英:/heə/ 美:/hɛr/ </td>
                <td class="export-td">1. n. 头发；毛发；些微
2. vt. 除去…的毛发</td>
            </tr>
            
             <tr>
                <td class="export-td">2702</td>
                <td class="export-td">haircut</td>
                <td class="export-td">英:/'heəkʌt/ 美:/'hɛrkʌt/ </td>
                <td class="export-td">n. 理发；发型</td>
            </tr>
            
             <tr>
                <td class="export-td">2703</td>
                <td class="export-td">hall</td>
                <td class="export-td">英:/hɔːl/ 美:/hɔl/ </td>
                <td class="export-td">n. 门厅，走廊；会堂；食堂；学生宿舍</td>
            </tr>
            
             <tr>
                <td class="export-td">2704</td>
                <td class="export-td">halt</td>
                <td class="export-td">英:/hɔːlt/ 美:/hɔlt/ </td>
                <td class="export-td">1. vi. 停止；踌躇，犹豫；立定
2. n. 停止；立定；休息</td>
            </tr>
            
             <tr>
                <td class="export-td">2705</td>
                <td class="export-td">hamburger</td>
                <td class="export-td">英:/'hæmbɜːgə/ 美:/'hæmbɝɡɚ/ </td>
                <td class="export-td">汉堡包</td>
            </tr>
            
             <tr>
                <td class="export-td">2706</td>
                <td class="export-td">hand</td>
                <td class="export-td">英:/hænd/ 美:/hænd/ </td>
                <td class="export-td">1. n. 手，手艺；指针；插手；帮助
2. vt. 搀扶；传递，交给；支持</td>
            </tr>
            
             <tr>
                <td class="export-td">2707</td>
                <td class="export-td">handful</td>
                <td class="export-td">英:/'hæn(d)fʊl/ 美:/'hænd,fʊl/ </td>
                <td class="export-td">n. 一把；少数；棘手事</td>
            </tr>
            
             <tr>
                <td class="export-td">2708</td>
                <td class="export-td">handkerchief</td>
                <td class="export-td">英:/'hæŋkətʃɪf/ 美:/'hæŋkɚtʃɪf/ </td>
                <td class="export-td">手帕，方头巾、围巾</td>
            </tr>
            
             <tr>
                <td class="export-td">2709</td>
                <td class="export-td">handsome</td>
                <td class="export-td">英:/'hæns(ə)m/ 美:/'hænsəm/ </td>
                <td class="export-td">adj. （男子）英俊的；大方的，慷慨的；可观的；健美而端庄的</td>
            </tr>
            
             <tr>
                <td class="export-td">2710</td>
                <td class="export-td">handwriting</td>
                <td class="export-td">英:/'hændraɪtɪŋ/ 美:/'hænd'raɪtɪŋ/ </td>
                <td class="export-td">笔迹, 书法</td>
            </tr>
            
             <tr>
                <td class="export-td">2711</td>
                <td class="export-td">handy</td>
                <td class="export-td">英:/'hændɪ/ 美:/'hændi/ </td>
                <td class="export-td">adj. 手边的，就近的；便利的；容易取得的；敏捷的</td>
            </tr>
            
             <tr>
                <td class="export-td">2712</td>
                <td class="export-td">hang</td>
                <td class="export-td">英:/hæŋ/ 美:/hæŋ/ </td>
                <td class="export-td">挂</td>
            </tr>
            
             <tr>
                <td class="export-td">2713</td>
                <td class="export-td">happen</td>
                <td class="export-td">英:/'hæp(ə)n/ 美:/'hæpən/ </td>
                <td class="export-td">vi. 发生；碰巧；偶然遇到</td>
            </tr>
            
             <tr>
                <td class="export-td">2714</td>
                <td class="export-td">happy</td>
                <td class="export-td">英:/'hæpɪ/ 美:/'hæpi/ </td>
                <td class="export-td">adj. 高兴的；幸福的；巧妙的</td>
            </tr>
            
             <tr>
                <td class="export-td">2715</td>
                <td class="export-td">harbour</td>
                <td class="export-td">英:/'hɑːbə/ 美:/ˈhɑrbɚ/ </td>
                <td class="export-td">1. vi. 藏匿；入港停泊；庇护
2. vt. 庇护；藏匿；入港停泊</td>
            </tr>
            
             <tr>
                <td class="export-td">2716</td>
                <td class="export-td">hard</td>
                <td class="export-td">英:/hɑːd/ 美:/hɑrd/ </td>
                <td class="export-td">1. adj. 困难的；硬的；猛烈的；确实的；努力的；辛苦的；冷酷无情的；严厉的
2. adv. 努力地；猛烈地；辛苦地；牢固地；接近地；困难地</td>
            </tr>
            
             <tr>
                <td class="export-td">2717</td>
                <td class="export-td">harden</td>
                <td class="export-td">英:/ˈhɑ:dn/ 美:/ˈhɑrdn/ </td>
                <td class="export-td">1. vi. 变硬，变坚固；变坚强；变冷酷
2. vt. 使…变硬；使…坚强；使…冷酷；使…麻木不仁</td>
            </tr>
            
             <tr>
                <td class="export-td">2718</td>
                <td class="export-td">hardly</td>
                <td class="export-td">英:/'hɑːdlɪ/ 美:/'hɑrdli/ </td>
                <td class="export-td">adv. 几乎不，简直不；刚刚</td>
            </tr>
            
             <tr>
                <td class="export-td">2719</td>
                <td class="export-td">hardware</td>
                <td class="export-td">英:/'hɑːdweə/ 美:/'hɑrdwɛr/ </td>
                <td class="export-td">n. 计算机硬件；五金器具</td>
            </tr>
            
             <tr>
                <td class="export-td">2720</td>
                <td class="export-td">hare</td>
                <td class="export-td">英:/heə/ 美:/hɛr/ </td>
                <td class="export-td">n. 野兔</td>
            </tr>
            
             <tr>
                <td class="export-td">2721</td>
                <td class="export-td">harm</td>
                <td class="export-td">英:/hɑːm/ 美:/hɑrm/ </td>
                <td class="export-td">1. n. 伤害；损害
2. vt. 损害；伤害；危害</td>
            </tr>
            
             <tr>
                <td class="export-td">2722</td>
                <td class="export-td">harmful</td>
                <td class="export-td">英:/'hɑːmfʊl/ 美:/'hɑrmfəl/ </td>
                <td class="export-td">adj. 能造成损害的；有害的</td>
            </tr>
            
             <tr>
                <td class="export-td">2723</td>
                <td class="export-td">harmony</td>
                <td class="export-td">英:/'hɑːmənɪ/ 美:/'hɑrməni/ </td>
                <td class="export-td">n. 协调；融洽；调和；和睦</td>
            </tr>
            
             <tr>
                <td class="export-td">2724</td>
                <td class="export-td">harsh</td>
                <td class="export-td">英:/hɑːʃ/ 美:/hɑrʃ/ </td>
                <td class="export-td">adj. 粗糙的；刺耳的；严厉的；严酷的；刺目的</td>
            </tr>
            
             <tr>
                <td class="export-td">2725</td>
                <td class="export-td">harvest</td>
                <td class="export-td">英:/'hɑːvɪst/ 美:/'hɑrvɪst/ </td>
                <td class="export-td">1. n. 收获；产量；结果
2. vt. 收割；得到</td>
            </tr>
            
             <tr>
                <td class="export-td">2726</td>
                <td class="export-td">haste</td>
                <td class="export-td">英:/heɪst/ 美:/hest/ </td>
                <td class="export-td">1. n. 匆忙；急忙；轻率
2. vi. 匆忙；赶紧</td>
            </tr>
            
             <tr>
                <td class="export-td">2727</td>
                <td class="export-td">hasty</td>
                <td class="export-td">英:/'heɪstɪ/ 美:/'hesti/ </td>
                <td class="export-td">adj. 匆忙的；轻率的；草率的；性怠的</td>
            </tr>
            
             <tr>
                <td class="export-td">2728</td>
                <td class="export-td">hat</td>
                <td class="export-td">英:/hæt/ 美:/hæt/ </td>
                <td class="export-td">1. n. 帽子
2. vt. 给……戴上帽子</td>
            </tr>
            
             <tr>
                <td class="export-td">2729</td>
                <td class="export-td">hatch</td>
                <td class="export-td">英:/hætʃ/ 美:/hætʃ/ </td>
                <td class="export-td">1. n. 舱口；孵化
2. vt. 策划；孵</td>
            </tr>
            
             <tr>
                <td class="export-td">2730</td>
                <td class="export-td">hate</td>
                <td class="export-td">英:/heɪt/ 美:/het/ </td>
                <td class="export-td">1. vt. 憎恨；厌恶；遗憾
2. vi. 仇恨</td>
            </tr>
            
             <tr>
                <td class="export-td">2731</td>
                <td class="export-td">hatred</td>
                <td class="export-td">英:/'heɪtrɪd/ 美:/'hetrɪd/ </td>
                <td class="export-td">n. 憎恨；怨恨；敌意</td>
            </tr>
            
             <tr>
                <td class="export-td">2732</td>
                <td class="export-td">have</td>
                <td class="export-td">英:/hæv/ 美:/hæv/ </td>
                <td class="export-td">1. vt. 有；让；从事；允许；拿
2. aux. 已经</td>
            </tr>
            
             <tr>
                <td class="export-td">2733</td>
                <td class="export-td">hawk</td>
                <td class="export-td">英:/hɔːk/ 美:/hɔk/ </td>
                <td class="export-td">1. vt. 捕捉；咳出；兜售，沿街叫卖
2. vi. 清嗓；咳嗽；像鹰一般地袭击</td>
            </tr>
            
             <tr>
                <td class="export-td">2734</td>
                <td class="export-td">hay</td>
                <td class="export-td">英:/heɪ/ 美:/he/ </td>
                <td class="export-td">1. n. 干草
2. vt. 把晒干</td>
            </tr>
            
             <tr>
                <td class="export-td">2735</td>
                <td class="export-td">hi</td>
                <td class="export-td">英:/haɪ/ 美:/haɪ/ </td>
                <td class="export-td">int. 嗨！（表示问候或用以唤起注意）</td>
            </tr>
            
             <tr>
                <td class="export-td">2736</td>
                <td class="export-td">hide</td>
                <td class="export-td">英:/haɪd/ 美:/haɪd/ </td>
                <td class="export-td">1. vt. 隐藏；隐瞒；鞭打
2. vi. 隐藏</td>
            </tr>
            
             <tr>
                <td class="export-td">2737</td>
                <td class="export-td">high</td>
                <td class="export-td">英:/haɪ/ 美:/haɪ/ </td>
                <td class="export-td">1. adj. 高的；高级的；高音调的；崇高的
2. n. 高水平；天空；由麻醉品引起的快感；高压地带</td>
            </tr>
            
             <tr>
                <td class="export-td">2738</td>
                <td class="export-td">highly</td>
                <td class="export-td">英:/'haɪlɪ/ 美:/'haɪli/ </td>
                <td class="export-td">adv. 非常；高度地；非常赞许地</td>
            </tr>
            
             <tr>
                <td class="export-td">2739</td>
                <td class="export-td">highway</td>
                <td class="export-td">英:/'haɪweɪ/ 美:/'haɪwe/ </td>
                <td class="export-td">n. 公路，大路；捷径</td>
            </tr>
            
             <tr>
                <td class="export-td">2740</td>
                <td class="export-td">hill</td>
                <td class="export-td">英:/hɪl/ 美:/hɪl/ </td>
                <td class="export-td">n. 小山；丘陵；斜坡；山冈</td>
            </tr>
            
             <tr>
                <td class="export-td">2741</td>
                <td class="export-td">him</td>
                <td class="export-td">英:/hɪm/ 美:/hɪm/ </td>
                <td class="export-td">pron. 他（宾格）</td>
            </tr>
            
             <tr>
                <td class="export-td">2742</td>
                <td class="export-td">himself</td>
                <td class="export-td">英:/hɪm'self/ 美:/hɪm'sɛlf/ </td>
                <td class="export-td">pron. 他自己；他亲自，他本人</td>
            </tr>
            
             <tr>
                <td class="export-td">2743</td>
                <td class="export-td">hint</td>
                <td class="export-td">英:/hɪnt/ 美:/hɪnt/ </td>
                <td class="export-td">1. n. 暗示；线索
2. vt. 暗示；示意</td>
            </tr>
            
             <tr>
                <td class="export-td">2744</td>
                <td class="export-td">hire</td>
                <td class="export-td">英:/'haɪə/ 美:/'haɪɚ/ </td>
                <td class="export-td">1. n. 租金，工钱；雇用，租用
2. vt. 雇用；出租</td>
            </tr>
            
             <tr>
                <td class="export-td">2745</td>
                <td class="export-td">his</td>
                <td class="export-td">英:/hɪz/ 美:/hɪz/ </td>
                <td class="export-td">pron. 他的</td>
            </tr>
            
             <tr>
                <td class="export-td">2746</td>
                <td class="export-td">historical</td>
                <td class="export-td">英:/hɪ'stɒrɪk(ə)l/ 美:/hɪ'stɔrɪkl/ </td>
                <td class="export-td">与历史有关的</td>
            </tr>
            
             <tr>
                <td class="export-td">2747</td>
                <td class="export-td">history</td>
                <td class="export-td">英:/'hɪst(ə)rɪ/ 美:/'hɪstri/ </td>
                <td class="export-td">n. 历史，历史学；历史记录；来历</td>
            </tr>
            
             <tr>
                <td class="export-td">2748</td>
                <td class="export-td">hit</td>
                <td class="export-td">英:/hɪt/ 美:/hɪt/ </td>
                <td class="export-td">1. vt. 袭击；碰撞；打击；偶然发现；伤…的感情
2. vi. 打击；打；碰撞；偶然碰上</td>
            </tr>
            
             <tr>
                <td class="export-td">2749</td>
                <td class="export-td">hobby</td>
                <td class="export-td">英:/'hɒbɪ/ 美:/'hɑbi/ </td>
                <td class="export-td">n. 嗜好；业余爱好</td>
            </tr>
            
             <tr>
                <td class="export-td">2750</td>
                <td class="export-td">hold</td>
                <td class="export-td">英:/həʊld/ 美:/hold/ </td>
                <td class="export-td">1. vt. 持有；保存；拥有；拘留；约束或控制
2. vi. 持续；支持；有效</td>
            </tr>
            
             <tr>
                <td class="export-td">2751</td>
                <td class="export-td">hole</td>
                <td class="export-td">英:/həʊl/ 美:/hol/ </td>
                <td class="export-td">1. n. 洞，孔；洞穴，穴；突破口
2. vi. 凿洞，穿孔；（高尔夫球等）进洞</td>
            </tr>
            
             <tr>
                <td class="export-td">2752</td>
                <td class="export-td">holiday</td>
                <td class="export-td">英:/'hɒlɪdeɪ/ 美:/'hɑləde/ </td>
                <td class="export-td">usu at the end of May, observed in the US to commemorate troops who died in war （美国）阵亡将士纪念日（通常为五月底）.<br /><br />1. n. 假日；节日；休息日
2. vi. 外出度假</td>
            </tr>
            
             <tr>
                <td class="export-td">2753</td>
                <td class="export-td">hollow</td>
                <td class="export-td">英:/'hɒləʊ/ 美:/'hɑlo/ </td>
                <td class="export-td">1. adj. 空的；凹的；虚伪的；中空的，空腹的
2. n. 洞；山谷；窟窿</td>
            </tr>
            
             <tr>
                <td class="export-td">2754</td>
                <td class="export-td">holy</td>
                <td class="export-td">英:/'həʊlɪ/ 美:/'holi/ </td>
                <td class="export-td">1. adj. 圣洁的，神圣的；至善的
2. n. 神圣的东西</td>
            </tr>
            
             <tr>
                <td class="export-td">2755</td>
                <td class="export-td">home</td>
                <td class="export-td">英:/həʊm/ 美:/hom/ </td>
                <td class="export-td">1. n. 家，住宅；家乡；产地；避难所
2. adv. 在家，回家；深入地</td>
            </tr>
            
             <tr>
                <td class="export-td">2756</td>
                <td class="export-td">honest</td>
                <td class="export-td">英:/'ɒnɪst/ 美:/'ɑnɪst/ </td>
                <td class="export-td">adj. 诚实的，实在的；可靠的；坦率的</td>
            </tr>
            
             <tr>
                <td class="export-td">2757</td>
                <td class="export-td">honey</td>
                <td class="export-td">英:/'hʌnɪ/ 美:/'hʌni/ </td>
                <td class="export-td">1. n. 蜂蜜；甜蜜；宝贝
2. adj. 甘美的；蜂蜜似的</td>
            </tr>
            
             <tr>
                <td class="export-td">2758</td>
                <td class="export-td">honeymoon</td>
                <td class="export-td">英:/'hʌnɪmuːn/ 美:/'hʌnɪmun/ </td>
                <td class="export-td">蜜月; 度蜜月</td>
            </tr>
            
             <tr>
                <td class="export-td">2759</td>
                <td class="export-td">honour</td>
                <td class="export-td">英:/'ɒnə/ 美:/ˈɑnɚ/ </td>
                <td class="export-td">1. n. 荣誉；尊敬；勋章
2. vt. 尊敬；承兑；承兑远期票据</td>
            </tr>
            
             <tr>
                <td class="export-td">2760</td>
                <td class="export-td">hook</td>
                <td class="export-td">英:/huk/ 美:/hʊk/ </td>
                <td class="export-td">1. n. 挂钩，吊钩
2. vt. 钩住；引上钩</td>
            </tr>
            
             <tr>
                <td class="export-td">2761</td>
                <td class="export-td">hope</td>
                <td class="export-td">英:/həʊp/ 美:/hop/ </td>
                <td class="export-td">1. n. 希望；信心；期望
2. vt. 希望；期望</td>
            </tr>
            
             <tr>
                <td class="export-td">2762</td>
                <td class="export-td">hopeful</td>
                <td class="export-td">英:/'həʊpfʊl/ 美:/'hopfl/ </td>
                <td class="export-td">1. adj. 有希望的；有前途的
2. n. 有希望成功的人</td>
            </tr>
            
             <tr>
                <td class="export-td">2763</td>
                <td class="export-td">hopeless</td>
                <td class="export-td">英:/'həʊplɪs/ 美:/'hopləs/ </td>
                <td class="export-td">adj. 绝望的；不可救药的</td>
            </tr>
            
             <tr>
                <td class="export-td">2764</td>
                <td class="export-td">horizon</td>
                <td class="export-td">英:/hə'raɪz(ə)n/ 美:/hə'raɪzn/ </td>
                <td class="export-td">n. 地平线；眼界；范围；视野</td>
            </tr>
            
             <tr>
                <td class="export-td">2765</td>
                <td class="export-td">horizontal</td>
                <td class="export-td">英:/hɒrɪ'zɒnt(ə)l/ 美:/'hɔrə'zɑntl/ </td>
                <td class="export-td">水平的,横的</td>
            </tr>
            
             <tr>
                <td class="export-td">2766</td>
                <td class="export-td">horn</td>
                <td class="export-td">英:/hɔːn/ 美:/hɔrn/ </td>
                <td class="export-td">1. n. 角；喇叭，号角
2. vt. 装角于</td>
            </tr>
            
             <tr>
                <td class="export-td">2767</td>
                <td class="export-td">horror</td>
                <td class="export-td">英:/'hɒrə/ 美:/'hɔrɚ/ </td>
                <td class="export-td">n. 惊骇；惨状；极端厌恶；令人恐怖的事物</td>
            </tr>
            
             <tr>
                <td class="export-td">2768</td>
                <td class="export-td">horse</td>
                <td class="export-td">英:/hɔːs/ 美:/hɔrs/ </td>
                <td class="export-td">1. n. 马；骑兵；脚架；[俚]海洛因
2. vt. 使骑马；系马于；[口]捉弄</td>
            </tr>
            
             <tr>
                <td class="export-td">2769</td>
                <td class="export-td">hospital</td>
                <td class="export-td">英:/'hɒspɪt(ə)l/ 美:/'hɑspɪtl/ </td>
                <td class="export-td">n. 医院</td>
            </tr>
            
             <tr>
                <td class="export-td">2770</td>
                <td class="export-td">host</td>
                <td class="export-td">英:/həʊst/ 美:/host/ </td>
                <td class="export-td">1. n. 主人；主机；主持人；许多
2. vt. 主持；当主人招待</td>
            </tr>
            
             <tr>
                <td class="export-td">2771</td>
                <td class="export-td">hostess</td>
                <td class="export-td">英:/'həʊstɪs/ 美:/'hostəs/ </td>
                <td class="export-td">n. 女主人，女老板；舞女；女服务员；女房东</td>
            </tr>
            
             <tr>
                <td class="export-td">2772</td>
                <td class="export-td">hostile</td>
                <td class="export-td">英:/'hɒstaɪl/ 美:/'hɑstl/ </td>
                <td class="export-td">1. adj. 敌对的，敌方的；怀敌意的
2. n. 敌对</td>
            </tr>
            
             <tr>
                <td class="export-td">2773</td>
                <td class="export-td">hot</td>
                <td class="export-td">英:/hɒt/ 美:/hɑt/ </td>
                <td class="export-td">1. adj. 热的；辣的；热情的；激动的；紧迫的
2. adv. 热；紧迫地</td>
            </tr>
            
             <tr>
                <td class="export-td">2774</td>
                <td class="export-td">hotel</td>
                <td class="export-td">英:/həʊ'tel/ 美:/ho'tɛl/ </td>
                <td class="export-td">1. n. 旅馆，饭店；客栈
2. vt. 使…在饭店下榻</td>
            </tr>
            
             <tr>
                <td class="export-td">2775</td>
                <td class="export-td">hour</td>
                <td class="export-td">英:/'aʊə/ 美:/'aʊɚ/ </td>
                <td class="export-td">n. 小时；钟头；课时；…点钟</td>
            </tr>
            
             <tr>
                <td class="export-td">2776</td>
                <td class="export-td">house</td>
                <td class="export-td">英:/haʊs/ 美:/haʊs/ </td>
                <td class="export-td">1. n. 住宅；家庭；某种用途的建筑物；机构；议会
2. vt. 给…房子住；把…储藏在房内；覆盖</td>
            </tr>
            
             <tr>
                <td class="export-td">2777</td>
                <td class="export-td">housewife</td>
                <td class="export-td">英:/'haʊswaɪf/ 美:/'haʊs'waɪf/ </td>
                <td class="export-td">家庭主妇; 针线盒</td>
            </tr>
            
             <tr>
                <td class="export-td">2778</td>
                <td class="export-td">how</td>
                <td class="export-td">英:/haʊ/ 美:/haʊ/ </td>
                <td class="export-td">1. adv. 多么；多少；如何
2. n. 方式；方法</td>
            </tr>
            
             <tr>
                <td class="export-td">2779</td>
                <td class="export-td">however</td>
                <td class="export-td">英:/haʊ'evə/ 美:/haʊ'ɛvɚ/ </td>
                <td class="export-td">1. adv. 无论如何；不管怎样
2. conj. 可是；然而</td>
            </tr>
            
             <tr>
                <td class="export-td">2780</td>
                <td class="export-td">huge</td>
                <td class="export-td">英:/hjuːdʒ/ 美:/hjudʒ/ </td>
                <td class="export-td">巨大的,程度高的</td>
            </tr>
            
             <tr>
                <td class="export-td">2781</td>
                <td class="export-td">human</td>
                <td class="export-td">英:/'hjuːmən/ 美:/'hjumən/ </td>
                <td class="export-td">1. adj. 人的；人类的
2. n. 人；人类</td>
            </tr>
            
             <tr>
                <td class="export-td">2782</td>
                <td class="export-td">humble</td>
                <td class="export-td">英:/ˈhʌmbl/ 美:/ˈhʌmbəl/ </td>
                <td class="export-td">谦卑</td>
            </tr>
            
             <tr>
                <td class="export-td">2783</td>
                <td class="export-td">humid</td>
                <td class="export-td">英:/'hjuːmɪd/ 美:/'hjumɪd/ </td>
                <td class="export-td">adj. 潮湿的；湿润的；多湿气的</td>
            </tr>
            
             <tr>
                <td class="export-td">2784</td>
                <td class="export-td">humorous</td>
                <td class="export-td">英:/'hjuːm(ə)rəs/ 美:/'hjumərəs/ </td>
                <td class="export-td">adj. 诙谐的，幽默的；滑稽的，可笑的</td>
            </tr>
            
             <tr>
                <td class="export-td">2785</td>
                <td class="export-td">hundred</td>
                <td class="export-td">英:/'hʌndrəd/ 美:/'hʌndrəd/ </td>
                <td class="export-td">1. n. 一百；许多
2. adj. 一百的；许多的</td>
            </tr>
            
             <tr>
                <td class="export-td">2786</td>
                <td class="export-td">hunger</td>
                <td class="export-td">英:/'hʌŋgə/ 美:/'hʌŋɡɚ/ </td>
                <td class="export-td">1. n. 渴望；饿，饥饿
2. vi. 渴望；挨饿</td>
            </tr>
            
             <tr>
                <td class="export-td">2787</td>
                <td class="export-td">hungry</td>
                <td class="export-td">英:/'hʌŋgrɪ/ 美:/'hʌŋɡri/ </td>
                <td class="export-td">adj. 饥饿的；渴望的；荒年的；不毛的</td>
            </tr>
            
             <tr>
                <td class="export-td">2788</td>
                <td class="export-td">hunt</td>
                <td class="export-td">英:/hʌnt/ 美:/hʌnt/ </td>
                <td class="export-td">1. vt. 搜索；打猎
2. vi. 打猎；搜寻</td>
            </tr>
            
             <tr>
                <td class="export-td">2789</td>
                <td class="export-td">hurry</td>
                <td class="export-td">英:/'hʌrɪ/ 美:/'hɝi/ </td>
                <td class="export-td">1. n. 匆忙，急忙
2. vt. 使赶紧；使匆忙，使急忙</td>
            </tr>
            
             <tr>
                <td class="export-td">2790</td>
                <td class="export-td">hurt</td>
                <td class="export-td">英:/hɜːt/ 美:/hɝt/ </td>
                <td class="export-td">1. vt. 使受伤；使疼痛；使痛心；[口]损害
2. vi. 感到疼痛；带来痛苦；[口]有坏处</td>
            </tr>
            
             <tr>
                <td class="export-td">2791</td>
                <td class="export-td">husband</td>
                <td class="export-td">英:/'hʌzbənd/ 美:/'hʌzbənd/ </td>
                <td class="export-td">1. vt. 节约地使用（或管理）
2. n. 丈夫</td>
            </tr>
            
             <tr>
                <td class="export-td">2792</td>
                <td class="export-td">hut</td>
                <td class="export-td">英:/hʌt/ 美:/hʌt/ </td>
                <td class="export-td">1. n. 小屋；临时营房
2. vt. 使住在小屋中；驻扎</td>
            </tr>
            
             <tr>
                <td class="export-td">2793</td>
                <td class="export-td">hydrogen</td>
                <td class="export-td">英:/'haɪdrədʒ(ə)n/ 美:/'haɪdrədʒən/ </td>
                <td class="export-td">n. 氢</td>
            </tr>
            
             <tr>
                <td class="export-td">2794</td>
                <td class="export-td">ice</td>
                <td class="export-td">英:/aɪs/ 美:/aɪs/ </td>
                <td class="export-td">1. n. 冰；冰淇淋；矜持；（俚）钻石
2. vt. 冰镇；结冰</td>
            </tr>
            
             <tr>
                <td class="export-td">2795</td>
                <td class="export-td">idea</td>
                <td class="export-td">英:/aɪ'dɪə/ 美:/aɪ'diə/ </td>
                <td class="export-td">n. 主意；概念；想法</td>
            </tr>
            
             <tr>
                <td class="export-td">2796</td>
                <td class="export-td">ideal</td>
                <td class="export-td">英:/aɪ'dɪəl/ 美:/aɪ'diəl/ </td>
                <td class="export-td">1. adj. 理想的；完美的；想象的；不切实际的
2. n. 理想；典范</td>
            </tr>
            
             <tr>
                <td class="export-td">2797</td>
                <td class="export-td">identical</td>
                <td class="export-td">英:/aɪ'dentɪk(ə)l/ 美:/aɪ'dɛntɪkl/ </td>
                <td class="export-td">相同的,同一的</td>
            </tr>
            
             <tr>
                <td class="export-td">2798</td>
                <td class="export-td">identify</td>
                <td class="export-td">英:/aɪ'dentɪfaɪ/ 美:/aɪ'dɛntɪfaɪ/ </td>
                <td class="export-td">1. vt. 识别；确定；使参与；把…看成一样
2. vi. 认同；一致；确定</td>
            </tr>
            
             <tr>
                <td class="export-td">2799</td>
                <td class="export-td">idiom</td>
                <td class="export-td">英:/'ɪdɪəm/ 美:/'ɪdɪəm/ </td>
                <td class="export-td">n. 成语，习语；土话</td>
            </tr>
            
             <tr>
                <td class="export-td">2800</td>
                <td class="export-td">if</td>
                <td class="export-td">英:/ɪf/ 美:/ɪf/ </td>
                <td class="export-td">1. conj. （表条件）如果；（表假设）假如；是否；即使
2. n. 条件；设想</td>
            </tr>
            
             <tr>
                <td class="export-td">2801</td>
                <td class="export-td">ignorant</td>
                <td class="export-td">英:/'ɪgn(ə)r(ə)nt/ 美:/'ɪɡnərənt/ </td>
                <td class="export-td">adj. 无知的；愚昧的</td>
            </tr>
            
             <tr>
                <td class="export-td">2802</td>
                <td class="export-td">ignore</td>
                <td class="export-td">英:/ɪg'nɔː/ 美:/ɪɡ'nɔr/ </td>
                <td class="export-td">vt. 驳回诉讼，忽视，不理睬</td>
            </tr>
            
             <tr>
                <td class="export-td">2803</td>
                <td class="export-td">ill</td>
                <td class="export-td">英:/ɪl/ 美:/ɪl/ </td>
                <td class="export-td">1. adj. 坏的；生病的；邪恶的；不吉利的
2. adv. 几乎不；不利地；恶劣地</td>
            </tr>
            
             <tr>
                <td class="export-td">2804</td>
                <td class="export-td">illegal</td>
                <td class="export-td">英:/ɪ'liːg(ə)l/ 美:/ɪ'ligl/ </td>
                <td class="export-td">1. adj. 非法的；违法的；违反规则的
2. n. 非法移民；间谍</td>
            </tr>
            
             <tr>
                <td class="export-td">2805</td>
                <td class="export-td">illness</td>
                <td class="export-td">英:/ɪlnɪs/ 美:/'ɪlnəs/ </td>
                <td class="export-td">n. 疾病；病</td>
            </tr>
            
             <tr>
                <td class="export-td">2806</td>
                <td class="export-td">illustrate</td>
                <td class="export-td">英:/'ɪləstreɪt/ 美:/'ɪləstret/ </td>
                <td class="export-td">举例说明,作图解</td>
            </tr>
            
             <tr>
                <td class="export-td">2807</td>
                <td class="export-td">imaginary</td>
                <td class="export-td">英:/ɪ'mædʒɪn(ə)rɪ/ 美:/ɪ'mædʒɪnɛri/ </td>
                <td class="export-td">想象的, 虚构的</td>
            </tr>
            
             <tr>
                <td class="export-td">2808</td>
                <td class="export-td">imagination</td>
                <td class="export-td">英:/ɪ,mædʒɪ'neɪʃ(ə)n/ 美:/ɪ,mædʒɪ'neʃən/ </td>
                <td class="export-td">想象,想象力,空想</td>
            </tr>
            
             <tr>
                <td class="export-td">2809</td>
                <td class="export-td">imitate</td>
                <td class="export-td">英:/'ɪmɪteɪt/ 美:/'ɪmɪtet/ </td>
                <td class="export-td">vt. 模仿，仿效；仿造，仿制</td>
            </tr>
            
             <tr>
                <td class="export-td">2810</td>
                <td class="export-td">immediate</td>
                <td class="export-td">英:/ɪ'miːdɪət/ 美:/ɪ'midɪət/ </td>
                <td class="export-td">即时</td>
            </tr>
            
             <tr>
                <td class="export-td">2811</td>
                <td class="export-td">immediately</td>
                <td class="export-td">英:/ɪ'miːdɪətlɪ/ 美:/ɪ'midɪətli/ </td>
                <td class="export-td">立即,直接地</td>
            </tr>
            
             <tr>
                <td class="export-td">2812</td>
                <td class="export-td">immense</td>
                <td class="export-td">英:/ɪ'mens/ 美:/ɪ'mɛns/ </td>
                <td class="export-td">adj. 巨大的，广大的；无边无际的；[口]非常好的</td>
            </tr>
            
             <tr>
                <td class="export-td">2813</td>
                <td class="export-td">immigrant</td>
                <td class="export-td">英:/'ɪmɪgr(ə)nt/ 美:/'ɪmɪɡrənt/ </td>
                <td class="export-td">移民, 侨民</td>
            </tr>
            
             <tr>
                <td class="export-td">2814</td>
                <td class="export-td">impact</td>
                <td class="export-td">英:/'ɪmpækt/ 美:/ɪm'pækt/ </td>
                <td class="export-td">1. vt. 撞击；冲突；影响；压紧
2. vi. 冲击；产生影响</td>
            </tr>
            
             <tr>
                <td class="export-td">2815</td>
                <td class="export-td">impatient</td>
                <td class="export-td">英:/ɪm'peɪʃ(ə)nt/ 美:/ɪm'peʃnt/ </td>
                <td class="export-td">不耐烦的, 急躁的</td>
            </tr>
            
             <tr>
                <td class="export-td">2816</td>
                <td class="export-td">imply</td>
                <td class="export-td">英:/ɪm'plaɪ/ 美:/ɪm'plai/ </td>
                <td class="export-td">vt. 暗示；意味；隐含</td>
            </tr>
            
             <tr>
                <td class="export-td">2817</td>
                <td class="export-td">import</td>
                <td class="export-td">英:/ɪm'pɔːt/ 美:/'ɪmpɔt/ </td>
                <td class="export-td">1. n. 输入；进口，进口货；意思，含义；重要性
2. vt. 输入，进口；含…的意思</td>
            </tr>
            
             <tr>
                <td class="export-td">2818</td>
                <td class="export-td">importance</td>
                <td class="export-td">英:/ɪm'pɔːt(ə)ns/ 美:/ɪm'pɔrtns/ </td>
                <td class="export-td">重要,重要性</td>
            </tr>
            
             <tr>
                <td class="export-td">2819</td>
                <td class="export-td">important</td>
                <td class="export-td">英:/ɪm'pɔːt(ə)nt/ 美:/ɪm'pɔrtnt/ </td>
                <td class="export-td">重要的,影响很大的</td>
            </tr>
            
             <tr>
                <td class="export-td">2820</td>
                <td class="export-td">impossible</td>
                <td class="export-td">英:/ɪm'pɒsɪb(ə)l/ 美:/ɪm'pɑsəbl/ </td>
                <td class="export-td">不可能的</td>
            </tr>
            
             <tr>
                <td class="export-td">2821</td>
                <td class="export-td">impress</td>
                <td class="export-td">英:/ɪm'pres/ 美:/ɪmˈprɛs/ </td>
                <td class="export-td">1. vt. 盖印；强征；传送；给予某人深刻印象
2. vi. 给人印象</td>
            </tr>
            
             <tr>
                <td class="export-td">2822</td>
                <td class="export-td">impression</td>
                <td class="export-td">英:/ɪm'preʃ(ə)n/ 美:/ɪm'prɛʃən/ </td>
                <td class="export-td">印象, 效果</td>
            </tr>
            
             <tr>
                <td class="export-td">2823</td>
                <td class="export-td">impressive</td>
                <td class="export-td">英:/ɪm'presɪv/ 美:/ɪm'prɛsɪv/ </td>
                <td class="export-td">给人深刻印象的</td>
            </tr>
            
             <tr>
                <td class="export-td">2824</td>
                <td class="export-td">imprison</td>
                <td class="export-td">英:/ɪm'prɪz(ə)n/ 美:/ɪm'prɪzn/ </td>
                <td class="export-td">vt. 监禁；关押；使…下狱</td>
            </tr>
            
             <tr>
                <td class="export-td">2825</td>
                <td class="export-td">improve</td>
                <td class="export-td">英:/ɪm'pruːv/ 美:/ɪm'pruv/ </td>
                <td class="export-td">1. vt. 改善，增进；提高…的价值
2. vi. 增加；变得更好</td>
            </tr>
            
             <tr>
                <td class="export-td">2826</td>
                <td class="export-td">improvement</td>
                <td class="export-td">英:/ɪm'pruːvm(ə)nt/ 美:/ɪm'prʊvmənt/ </td>
                <td class="export-td">改进, 改善</td>
            </tr>
            
             <tr>
                <td class="export-td">2827</td>
                <td class="export-td">in</td>
                <td class="export-td">英:/ɪn/ 美:/ɪn/ </td>
                <td class="export-td">1. prep. 在…之内；从事于；按照（表示方式）
2. adv. 进入；在屋里；（服装等）时髦；当选</td>
            </tr>
            
             <tr>
                <td class="export-td">2828</td>
                <td class="export-td">resistance</td>
                <td class="export-td">英:/rɪ'zɪst(ə)ns/ 美:/rɪ'zɪstəns/ </td>
                <td class="export-td">阻力</td>
            </tr>
            
             <tr>
                <td class="export-td">2829</td>
                <td class="export-td">illusion</td>
                <td class="export-td">英:/ɪ'l(j)uːʒ(ə)n/ 美:/ɪ'luʒn/ </td>
                <td class="export-td">n. 幻觉，错觉；错误的观念或信仰</td>
            </tr>
            
             <tr>
                <td class="export-td">2830</td>
                <td class="export-td">audio</td>
                <td class="export-td">英:/'ɔːdɪəʊ/ 美:/'ɔdɪo/ </td>
                <td class="export-td">adj. 声音的；音频的，声频的</td>
            </tr>
            
             <tr>
                <td class="export-td">2831</td>
                <td class="export-td">fax</td>
                <td class="export-td">英:/fæks/ 美:/fæks/ </td>
                <td class="export-td">1. vt. 传真
2. n. 传真</td>
            </tr>
            
             <tr>
                <td class="export-td">2832</td>
                <td class="export-td">horrible</td>
                <td class="export-td">英:/'hɒrɪb(ə)l/ 美:/'hɔrəbl/ </td>
                <td class="export-td">adj. 可怕的；极讨厌的</td>
            </tr>
            
             <tr>
                <td class="export-td">2833</td>
                <td class="export-td">deputy</td>
                <td class="export-td">英:/'depjʊtɪ/ 美:/'dɛpjuti/ </td>
                <td class="export-td">1. n. 代理人，代表
2. adj. 副的；代理的</td>
            </tr>
            
             <tr>
                <td class="export-td">2834</td>
                <td class="export-td">flee</td>
                <td class="export-td">英:/fliː/ 美:/fli/ </td>
                <td class="export-td">1. vi. 消失，消散；逃走
2. vt. 逃避；逃跑，逃走</td>
            </tr>
            
             <tr>
                <td class="export-td">2835</td>
                <td class="export-td">favorable</td>
                <td class="export-td">英:/ˈfeɪvərəbəl/ 美:/'fevərəbl/ </td>
                <td class="export-td">有利</td>
            </tr>
            
             <tr>
                <td class="export-td">2836</td>
                <td class="export-td">highlight</td>
                <td class="export-td">英:/'haɪlaɪt/ 美:/'haɪlaɪt/ </td>
                <td class="export-td">突出</td>
            </tr>
            
             <tr>
                <td class="export-td">2837</td>
                <td class="export-td">aisle</td>
                <td class="export-td">英:/aɪl/ 美:/aɪl/ </td>
                <td class="export-td">n. 通道，走道；侧廊</td>
            </tr>
            
             <tr>
                <td class="export-td">2838</td>
                <td class="export-td">ambassador</td>
                <td class="export-td">英:/æm'bæsədə/ 美:/æm'bæsədɚ/ </td>
                <td class="export-td">大使</td>
            </tr>
            
             <tr>
                <td class="export-td">2839</td>
                <td class="export-td">ammunition</td>
                <td class="export-td">英:/æmjʊ'nɪʃ(ə)n/ 美:/ˌæmju'nɪʃən/ </td>
                <td class="export-td">弹药</td>
            </tr>
            
             <tr>
                <td class="export-td">2840</td>
                <td class="export-td">anniversary</td>
                <td class="export-td">英:/ænɪ'vɜːs(ə)rɪ/ 美:/ˌænɪ'vɝsəri/ </td>
                <td class="export-td">周年纪念</td>
            </tr>
            
             <tr>
                <td class="export-td">2841</td>
                <td class="export-td">anonymous</td>
                <td class="export-td">英:/ə'nɒnɪməs/ 美:/ə'nɑnəməs/ </td>
                <td class="export-td">匿名</td>
            </tr>
            
             <tr>
                <td class="export-td">2842</td>
                <td class="export-td">antique</td>
                <td class="export-td">英:/æn'tiːk/ 美:/æn'tik/ </td>
                <td class="export-td">1. adj. 古老的，年代久远的；过时的，古董的；古风的，古式的
2. n. 古董，古玩；古风，古希腊和古罗马艺术风格</td>
            </tr>
            
             <tr>
                <td class="export-td">2843</td>
                <td class="export-td">arch</td>
                <td class="export-td">英:/ɑːtʃ/ 美:/ɑrtʃ/ </td>
                <td class="export-td">1. n. 拱门；弓形，拱形
2. adj. 主要的</td>
            </tr>
            
             <tr>
                <td class="export-td">2844</td>
                <td class="export-td">arena</td>
                <td class="export-td">英:/ə'riːnə/ 美:/ə'rinə/ </td>
                <td class="export-td">n. 竞技场；舞台</td>
            </tr>
            
             <tr>
                <td class="export-td">2845</td>
                <td class="export-td">arrogant</td>
                <td class="export-td">英:/'ærəg(ə)nt/ 美:/'ærəɡənt/ </td>
                <td class="export-td">adj. 自大的，傲慢的</td>
            </tr>
            
             <tr>
                <td class="export-td">2846</td>
                <td class="export-td">artery</td>
                <td class="export-td">英:/'ɑːtərɪ/ 美:/'ɑrtəri/ </td>
                <td class="export-td">n. 动脉；干道；主流</td>
            </tr>
            
             <tr>
                <td class="export-td">2847</td>
                <td class="export-td">assault</td>
                <td class="export-td">英:/ə'sɔːlt/ 美:/ə'sɔlt/ </td>
                <td class="export-td">1. n. 攻击；袭击
2. vt. 袭击；攻击</td>
            </tr>
            
             <tr>
                <td class="export-td">2848</td>
                <td class="export-td">auction</td>
                <td class="export-td">英:/'ɔːkʃ(ə)n/ 美:/'ɔkʃən/ </td>
                <td class="export-td">1. vt. 拍卖；竞卖
2. n. 拍卖</td>
            </tr>
            
             <tr>
                <td class="export-td">2849</td>
                <td class="export-td">authentic</td>
                <td class="export-td">英:/ɔː'θentɪk/ 美:/ɔ'θɛntɪk/ </td>
                <td class="export-td">真实</td>
            </tr>
            
             <tr>
                <td class="export-td">2850</td>
                <td class="export-td">attorney</td>
                <td class="export-td">英:/ə'tɜːnɪ/ 美:/ə'tɝni/ </td>
                <td class="export-td">n. 代理人；律师</td>
            </tr>
            
             <tr>
                <td class="export-td">2851</td>
                <td class="export-td">atlas</td>
                <td class="export-td">英:/'ætləs/ 美:/ˈætləs/ </td>
                <td class="export-td">n. 地图集</td>
            </tr>
            
             <tr>
                <td class="export-td">2852</td>
                <td class="export-td">astronomy</td>
                <td class="export-td">英:/ə'strɒnəmɪ/ 美:/ə'strɑnəmi/ </td>
                <td class="export-td">天文学</td>
            </tr>
            
             <tr>
                <td class="export-td">2853</td>
                <td class="export-td">bid</td>
                <td class="export-td">英:/bɪd/ 美:/bɪd/ </td>
                <td class="export-td">1. vt. 投标；出价；吩咐；表示
2. vi. 投标；吩咐</td>
            </tr>
            
             <tr>
                <td class="export-td">2854</td>
                <td class="export-td">biography</td>
                <td class="export-td">英:/baɪ'ɒgrəfɪ/ 美:/baɪ'ɑɡrəfi/ </td>
                <td class="export-td">传记</td>
            </tr>
            
             <tr>
                <td class="export-td">2855</td>
                <td class="export-td">bizarre</td>
                <td class="export-td">英:/bɪ'zɑː/ 美:/bɪ'zɑr/ </td>
                <td class="export-td">adj. 奇异的（指态度，容貌，款式等）</td>
            </tr>
            
             <tr>
                <td class="export-td">2856</td>
                <td class="export-td">calorie</td>
                <td class="export-td">英:/'kælərɪ/ 美:/'kæləri/ </td>
                <td class="export-td">n. 卡路里（热量单位）</td>
            </tr>
            
             <tr>
                <td class="export-td">2857</td>
                <td class="export-td">cape</td>
                <td class="export-td">英:/keɪp/ 美:/kep/ </td>
                <td class="export-td">n. 披肩；海角，岬</td>
            </tr>
            
             <tr>
                <td class="export-td">2858</td>
                <td class="export-td">cartoon</td>
                <td class="export-td">英:/kɑː'tuːn/ 美:/kɑr'tun/ </td>
                <td class="export-td">1. n. 卡通片，动画片；连环漫画
2. vt. 为…画漫画</td>
            </tr>
            
             <tr>
                <td class="export-td">2859</td>
                <td class="export-td">category</td>
                <td class="export-td">英:/'kætɪg(ə)rɪ/ 美:/'kætəɡɔri/ </td>
                <td class="export-td">n. 种类，分类；范畴</td>
            </tr>
            
             <tr>
                <td class="export-td">2860</td>
                <td class="export-td">Catholic</td>
                <td class="export-td">英:/'kæθ(ə)lɪk/ 美:/'kæθlɪk/ </td>
                <td class="export-td">1. adj. 天主教的；宽宏大量的
2. n. 天主教徒；罗马天主教</td>
            </tr>
            
             <tr>
                <td class="export-td">2861</td>
                <td class="export-td">caution</td>
                <td class="export-td">英:/'kɔːʃ(ə)n/ 美:/'kɔʃən/ </td>
                <td class="export-td">1. n. 小心，谨慎；警告，警示
2. vt. 警告</td>
            </tr>
            
             <tr>
                <td class="export-td">2862</td>
                <td class="export-td">cautious</td>
                <td class="export-td">英:/'kɔːʃəs/ 美:/'kɔʃəs/ </td>
                <td class="export-td">adj. 谨慎的；十分小心的</td>
            </tr>
            
             <tr>
                <td class="export-td">2863</td>
                <td class="export-td">cemetery</td>
                <td class="export-td">英:/'semɪtrɪ/ 美:/'sɛmə'tɛri/ </td>
                <td class="export-td">n. 墓地；公墓</td>
            </tr>
            
             <tr>
                <td class="export-td">2864</td>
                <td class="export-td">cereal</td>
                <td class="export-td">英:/'sɪərɪəl/ 美:/'sɪrɪəl/ </td>
                <td class="export-td">1. n. 谷类食品；谷类，谷物；谷类植物
2. adj. 谷类的；谷类制成的</td>
            </tr>
            
             <tr>
                <td class="export-td">2865</td>
                <td class="export-td">circulation</td>
                <td class="export-td">英:/sɜːkjʊ'leɪʃ(ə)n/ 美:/ˌsɝkjə'leʃən/ </td>
                <td class="export-td">循环</td>
            </tr>
            
             <tr>
                <td class="export-td">2866</td>
                <td class="export-td">circus</td>
                <td class="export-td">英:/'sɜːkəs/ 美:/'sɝkəs/ </td>
                <td class="export-td">n. 马戏团；马戏</td>
            </tr>
            
             <tr>
                <td class="export-td">2867</td>
                <td class="export-td">civilian</td>
                <td class="export-td">英:/sɪ'vɪlj(ə)n/ 美:/sə'vɪlɪən/ </td>
                <td class="export-td">1. adj. 民用的；百姓的，平民的
2. n. 平民，百姓</td>
            </tr>
            
             <tr>
                <td class="export-td">2868</td>
                <td class="export-td">context</td>
                <td class="export-td">英:/'kɒntekst/ 美:/'kɑntɛkst/ </td>
                <td class="export-td">n. 环境；上下文；来龙去脉</td>
            </tr>
            
             <tr>
                <td class="export-td">2869</td>
                <td class="export-td">cooperative</td>
                <td class="export-td">英:/kəuˈɔpərətiv/ 美:/ko'ɑpərətɪv/ </td>
                <td class="export-td">合作的,共同的</td>
            </tr>
            
             <tr>
                <td class="export-td">2870</td>
                <td class="export-td">decimal</td>
                <td class="export-td">英:/'desɪm(ə)l/ 美:/'dɛsɪml/ </td>
                <td class="export-td">1. adj. 小数的；十进位的
2. n. 小数</td>
            </tr>
            
             <tr>
                <td class="export-td">2871</td>
                <td class="export-td">deliberate</td>
                <td class="export-td">英:/dɪ'lɪb(ə)rət/ 美:/dɪ'lɪbərət/ </td>
                <td class="export-td">故意的</td>
            </tr>
            
             <tr>
                <td class="export-td">2872</td>
                <td class="export-td">dentist</td>
                <td class="export-td">英:/'dentɪst/ 美:/'dɛntɪst/ </td>
                <td class="export-td">n. 牙科医生</td>
            </tr>
            
             <tr>
                <td class="export-td">2873</td>
                <td class="export-td">depression</td>
                <td class="export-td">英:/dɪ'preʃ(ə)n/ 美:/dɪ'prɛʃən/ </td>
                <td class="export-td">沮丧,萧条</td>
            </tr>
            
             <tr>
                <td class="export-td">2874</td>
                <td class="export-td">descendant</td>
                <td class="export-td">英:/dɪ'send(ə)nt/ 美:/dɪ'sɛndənt/ </td>
                <td class="export-td">子孙, 后代</td>
            </tr>
            
             <tr>
                <td class="export-td">2875</td>
                <td class="export-td">descent</td>
                <td class="export-td">英:/dɪ'sent/ 美:/dɪˈsɛnt/ </td>
                <td class="export-td">1. n. 下降；血统；袭击
2. vt. 除去…的气味；使…失去香味</td>
            </tr>
            
             <tr>
                <td class="export-td">2876</td>
                <td class="export-td">detach</td>
                <td class="export-td">英:/dɪ'tætʃ/ 美:/dɪ'tætʃ/ </td>
                <td class="export-td">vt. 分离；派遣；使超然</td>
            </tr>
            
             <tr>
                <td class="export-td">2877</td>
                <td class="export-td">detective</td>
                <td class="export-td">英:/dɪ'tektɪv/ 美:/dɪ'tɛktɪv/ </td>
                <td class="export-td">侦探的; 侦探</td>
            </tr>
            
             <tr>
                <td class="export-td">2878</td>
                <td class="export-td">elderly</td>
                <td class="export-td">英:/'eldəlɪ/ 美:/'ɛldɚli/ </td>
                <td class="export-td">adj. 过了中年的；稍老的；上了年纪的</td>
            </tr>
            
             <tr>
                <td class="export-td">2879</td>
                <td class="export-td">electrician</td>
                <td class="export-td">英:/ˌɪlek'trɪʃ(ə)n/ 美:/ɪ'lɛk'trɪʃən/ </td>
                <td class="export-td">电工</td>
            </tr>
            
             <tr>
                <td class="export-td">2880</td>
                <td class="export-td">elegant</td>
                <td class="export-td">英:/'elɪg(ə)nt/ 美:/'ɛləgənt/ </td>
                <td class="export-td">adj. 高雅的，优雅的；讲究的</td>
            </tr>
            
             <tr>
                <td class="export-td">2881</td>
                <td class="export-td">eternal</td>
                <td class="export-td">英:/ɪ'tɜːn(ə)l/ 美:/ɪ'tɝnl/ </td>
                <td class="export-td">adj. 永恒的；不朽的</td>
            </tr>
            
             <tr>
                <td class="export-td">2882</td>
                <td class="export-td">ethnic</td>
                <td class="export-td">英:/'eθnɪk/ 美:/'ɛθnɪk/ </td>
                <td class="export-td">adj. 种族的；人种的</td>
            </tr>
            
             <tr>
                <td class="export-td">2883</td>
                <td class="export-td">evacuate</td>
                <td class="export-td">英:/ɪ'vækjʊeɪt/ 美:/ɪ'vækjuet/ </td>
                <td class="export-td">1. vt. 排泄；疏散，撤退
2. vi. 撤退；疏散；排泄</td>
            </tr>
            
             <tr>
                <td class="export-td">2884</td>
                <td class="export-td">fabulous</td>
                <td class="export-td">英:/'fæbjʊləs/ 美:/'fæbjələs/ </td>
                <td class="export-td">adj. 难以置信的；传说的，寓言中的；极好的</td>
            </tr>
            
             <tr>
                <td class="export-td">2885</td>
                <td class="export-td">fake</td>
                <td class="export-td">英:/feɪk/ 美:/fek/ </td>
                <td class="export-td">1. n. 假货；骗子；[体]假动作
2. vt. 捏造；假装…的样子</td>
            </tr>
            
             <tr>
                <td class="export-td">2886</td>
                <td class="export-td">fantastic</td>
                <td class="export-td">英:/fæn'tæstɪk/ 美:/fæn'tæstɪk/ </td>
                <td class="export-td">奇妙</td>
            </tr>
            
             <tr>
                <td class="export-td">2887</td>
                <td class="export-td">fantasy</td>
                <td class="export-td">英:/'fæntəsɪ/ 美:/'fæntəsi/ </td>
                <td class="export-td">1. n. 幻想；幻觉；[心]白日梦
2. adj. 虚幻的</td>
            </tr>
            
             <tr>
                <td class="export-td">2888</td>
                <td class="export-td">feminine</td>
                <td class="export-td">英:/'femɪnɪn/ 美:/'fɛmənɪn/ </td>
                <td class="export-td">adj. 女性的；妇女（似）的；娇柔的；阴性的</td>
            </tr>
            
             <tr>
                <td class="export-td">2889</td>
                <td class="export-td">ferry</td>
                <td class="export-td">英:/'ferɪ/ 美:/'fɛri/ </td>
                <td class="export-td">1. n. 渡口；渡船；摆渡
2. vt. （乘渡船）渡过；用渡船运送；空运</td>
            </tr>
            
             <tr>
                <td class="export-td">2890</td>
                <td class="export-td">firework</td>
                <td class="export-td">英:/ˈfaɪəˌwɜ:k/ 美:/'faɪɚwɝk/ </td>
                <td class="export-td">n. 烟火；激烈情绪</td>
            </tr>
            
             <tr>
                <td class="export-td">2891</td>
                <td class="export-td">flap</td>
                <td class="export-td">英:/flæp/ 美:/flæp/ </td>
                <td class="export-td">1. n. 拍打，拍打声；副翼
2. vi. 鼓翼而飞；拍动；（帽边等）垂下</td>
            </tr>
            
             <tr>
                <td class="export-td">2892</td>
                <td class="export-td">flatter</td>
                <td class="export-td">英:/'flætə/ 美:/'flætɚ/ </td>
                <td class="export-td">vt. 奉承；谄媚；使高兴</td>
            </tr>
            
             <tr>
                <td class="export-td">2893</td>
                <td class="export-td">fling</td>
                <td class="export-td">英:/flɪŋ/ 美:/flɪŋ/ </td>
                <td class="export-td">1. vt. 掷，抛；嘲笑；使陷入；轻蔑地投射；猛动
2. n. 掷，抛；嘲弄；急冲</td>
            </tr>
            
             <tr>
                <td class="export-td">2894</td>
                <td class="export-td">flutter</td>
                <td class="export-td">英:/'flʌtə/ 美:/ˈflʌtɚ/ </td>
                <td class="export-td">1. vi. 飘动；鼓翼；烦扰
2. vt. 拍；使焦急；使飘动</td>
            </tr>
            
             <tr>
                <td class="export-td">2895</td>
                <td class="export-td">foam</td>
                <td class="export-td">英:/fəʊm/ 美:/fom/ </td>
                <td class="export-td">1. n. 泡沫；水沫；灭火泡沫
2. vi. 起泡沫；吐白沫；起着泡沫流动</td>
            </tr>
            
             <tr>
                <td class="export-td">2896</td>
                <td class="export-td">foil</td>
                <td class="export-td">英:/fɔil/ 美:/fɔɪl/ </td>
                <td class="export-td">1. vt. 挫败；阻止，挡开；衬托；贴箔于
2. n. 箔，金属薄片；叶形片；衬托，烘托</td>
            </tr>
            
             <tr>
                <td class="export-td">2897</td>
                <td class="export-td">foresee</td>
                <td class="export-td">英:/fɔː'siː/ 美:/fɔr'si/ </td>
                <td class="export-td">vt. 预知；预见</td>
            </tr>
            
             <tr>
                <td class="export-td">2898</td>
                <td class="export-td">fort</td>
                <td class="export-td">英:/fɔːt/ 美:/fɔrt/ </td>
                <td class="export-td">1. n. 堡垒；要塞；（美）边界贸易站
2. vt. 设要塞保卫</td>
            </tr>
            
             <tr>
                <td class="export-td">2899</td>
                <td class="export-td">fossil</td>
                <td class="export-td">英:/'fɒs(ə)l/ 美:/'fɑsl/ </td>
                <td class="export-td">1. n. 化石；僵化的事物；顽固不化的人
2. adj. 化石的；陈腐的，守旧的</td>
            </tr>
            
             <tr>
                <td class="export-td">2900</td>
                <td class="export-td">foster</td>
                <td class="export-td">英:/ˈfɔstə/ 美:/ˈfɔstɚ/ </td>
                <td class="export-td">1. vt. 养育，抚育；培养；抱（希望等）
2. adj. 收养的，养育的</td>
            </tr>
            
             <tr>
                <td class="export-td">2901</td>
                <td class="export-td">foul</td>
                <td class="export-td">英:/faʊl/ 美:/faʊl/ </td>
                <td class="export-td">1. adj. 邪恶的；污秽的；犯规的；淤塞的
2. vt. 弄脏；犯规；淤塞；缠住，妨害</td>
            </tr>
            
             <tr>
                <td class="export-td">2902</td>
                <td class="export-td">gaol</td>
                <td class="export-td">英:/dʒeɪl/ 美:/dʒel/ </td>
                <td class="export-td">1. vt. 监禁
2. n. 监狱</td>
            </tr>
            
             <tr>
                <td class="export-td">2903</td>
                <td class="export-td">gigantic</td>
                <td class="export-td">英:/dʒaɪ'gæntɪk/ 美:/dʒaɪ'ɡæntɪk/ </td>
                <td class="export-td">adj. 巨大的，庞大的</td>
            </tr>
            
             <tr>
                <td class="export-td">2904</td>
                <td class="export-td">giggle</td>
                <td class="export-td">英:/'gɪg(ə)l/ 美:/'ɡɪɡl/ </td>
                <td class="export-td">1. vi. 傻笑；咯咯地笑
2. vt. 咯咯地笑着说</td>
            </tr>
            
             <tr>
                <td class="export-td">2905</td>
                <td class="export-td">ginger</td>
                <td class="export-td">英:/'dʒɪndʒə/ 美:/'dʒɪndʒɚ/ </td>
                <td class="export-td">1. n. 姜；姜黄色；精力；有姜味
2. vt. 用姜给…调味；使某人有活力</td>
            </tr>
            
             <tr>
                <td class="export-td">2906</td>
                <td class="export-td">glamour</td>
                <td class="export-td">英:/'ɡlæmə/ 美:/ˈɡlæmɚ/ </td>
                <td class="export-td">1. n. 魅力，魔力；迷人的美
2. vt. 迷惑，迷住</td>
            </tr>
            
             <tr>
                <td class="export-td">2907</td>
                <td class="export-td">guardian</td>
                <td class="export-td">英:/'gɑːdɪən/ 美:/'ɡɑrdɪən/ </td>
                <td class="export-td">1. n. 监护人，保护人；守护者
2. adj. 守护的</td>
            </tr>
            
             <tr>
                <td class="export-td">2908</td>
                <td class="export-td">guy</td>
                <td class="export-td">英:/ˈɡai/ 美:/ɡaɪ/ </td>
                <td class="export-td">1. n. 男人，家伙
2. vt. 嘲弄，取笑</td>
            </tr>
            
             <tr>
                <td class="export-td">2909</td>
                <td class="export-td">gym</td>
                <td class="export-td">英:/dʒɪm/ 美:/dʒɪm/ </td>
                <td class="export-td">n. 体育；体育馆；健身房</td>
            </tr>
            
             <tr>
                <td class="export-td">2910</td>
                <td class="export-td">hail</td>
                <td class="export-td">英:/heɪl/ 美:/hel/ </td>
                <td class="export-td">1. n. 冰雹；致敬；招呼；一阵
2. vt. 招呼；猛发；致敬；向...欢呼；使象下雹样落下（过去式hailed，过去分词hailed，现在分词hailing，第三人称单数hails）</td>
            </tr>
            
             <tr>
                <td class="export-td">2911</td>
                <td class="export-td">handicap</td>
                <td class="export-td">英:/'hændɪkæp/ 美:/'hændɪ'kæp/ </td>
                <td class="export-td">1. n. 障碍；不利条件，不利的因素
2. vt. 妨碍，阻碍；使不利</td>
            </tr>
            
             <tr>
                <td class="export-td">2912</td>
                <td class="export-td">haul</td>
                <td class="export-td">英:/hɔːl/ 美:/hɔl/ </td>
                <td class="export-td">1. n. 用力拖拉；努力得到的结果；拖，拉；捕获物；一网捕获的鱼量；拖运距离
2. vt. 拖运；拖拉</td>
            </tr>
            
             <tr>
                <td class="export-td">2913</td>
                <td class="export-td">haunt</td>
                <td class="export-td">英:/hɔːnt/ 美:/hɔnt/ </td>
                <td class="export-td">1. vt. 常出没于…；萦绕于…；经常去…
2. vi. 出没；作祟</td>
            </tr>
            
             <tr>
                <td class="export-td">2914</td>
                <td class="export-td">hike</td>
                <td class="export-td">英:/haɪk/ 美:/haɪk/ </td>
                <td class="export-td">1. vi. 远足；上升；徒步旅行
2. vt. 提高；拉起；使…高涨</td>
            </tr>
            
             <tr>
                <td class="export-td">2915</td>
                <td class="export-td">hinder</td>
                <td class="export-td">英:/'hɪndə/ 美:/'hɪndɚ/ </td>
                <td class="export-td">1. vi. 成为阻碍
2. vt. 阻碍；打扰</td>
            </tr>
            
             <tr>
                <td class="export-td">2916</td>
                <td class="export-td">hinge</td>
                <td class="export-td">英:/hɪn(d)ʒ/ 美:/hɪndʒ/ </td>
                <td class="export-td">1. n. 铰链；枢纽；关键
2. vt. 给…安装铰链</td>
            </tr>
            
             <tr>
                <td class="export-td">2917</td>
                <td class="export-td">hospitality</td>
                <td class="export-td">英:/hɒspɪ'tælɪtɪ/ 美:/ˌhɑspɪ'tæləti/ </td>
                <td class="export-td">好客, 殷勤</td>
            </tr>
            
             <tr>
                <td class="export-td">2918</td>
                <td class="export-td">hostage</td>
                <td class="export-td">英:/'hɒstɪdʒ/ 美:/'hɑstɪdʒ/ </td>
                <td class="export-td">n. 人质；抵押品</td>
            </tr>
            
             <tr>
                <td class="export-td">2919</td>
                <td class="export-td">hover</td>
                <td class="export-td">英:/'hɒvə/ 美:/'hʌvɚ/ </td>
                <td class="export-td">1. vi. 盘旋，翱翔；徘徊
2. n. 徘徊；盘旋；犹豫</td>
            </tr>
            
             <tr>
                <td class="export-td">2920</td>
                <td class="export-td">howl</td>
                <td class="export-td">英:/haʊl/ 美:/haʊl/ </td>
                <td class="export-td">1. vi. 怒吼；咆哮；狂吠
2. vt. 狂喊着说；对…吼叫</td>
            </tr>
            
             <tr>
                <td class="export-td">2921</td>
                <td class="export-td">hurl</td>
                <td class="export-td">英:/hɜːl/ 美:/hɝl/ </td>
                <td class="export-td">1. vt. 丢下；用力投掷；愤慨地说出
2. vi. 猛投；猛掷</td>
            </tr>
            
             <tr>
                <td class="export-td">2922</td>
                <td class="export-td">hurricane</td>
                <td class="export-td">英:/'hʌrɪk(ə)n/ 美:/'hɝəkən/ </td>
                <td class="export-td">飓风</td>
            </tr>
            
             <tr>
                <td class="export-td">2923</td>
                <td class="export-td">ignite</td>
                <td class="export-td">英:/ɪg'naɪt/ 美:/ɪɡ'naɪt/ </td>
                <td class="export-td">1. vt. 点燃；使燃烧；使激动
2. vi. 点火；燃烧</td>
            </tr>
            
             <tr>
                <td class="export-td">2924</td>
                <td class="export-td">ignorance</td>
                <td class="export-td">英:/'ɪgn(ə)r(ə)ns/ 美:/'ɪɡnərəns/ </td>
                <td class="export-td">无知</td>
            </tr>
            
             <tr>
                <td class="export-td">2925</td>
                <td class="export-td">imitation</td>
                <td class="export-td">英:/ɪmɪ'teɪʃ(ə)n/ 美:/ˌɪmɪ'teʃən/ </td>
                <td class="export-td">模仿,效法</td>
            </tr>
            
             <tr>
                <td class="export-td">2926</td>
                <td class="export-td">immune</td>
                <td class="export-td">英:/i'mju:n/ 美:/ɪˈmjoon/ </td>
                <td class="export-td">1. adj. 免疫的；免于……的，免除的
2. n. 免疫者；免除者</td>
            </tr>
            
             <tr>
                <td class="export-td">2927</td>
                <td class="export-td">imperative</td>
                <td class="export-td">英:/ɪm'perətɪv/ 美:/ɪm'pɛrətɪv/ </td>
                <td class="export-td">迫切</td>
            </tr>
            
             <tr>
                <td class="export-td">2928</td>
                <td class="export-td">impulse</td>
                <td class="export-td">英:/'ɪmpʌls/ 美:/'ɪmpʌls/ </td>
                <td class="export-td">1. n. 冲动；脉冲；刺激；推动力；神经冲动
2. vt. 推动</td>
            </tr>
            
             <tr>
                <td class="export-td">2929</td>
                <td class="export-td">catastrophe</td>
                <td class="export-td">英:/kə'tæstrəfɪ/ 美:/kə'tæstrəfi/ </td>
                <td class="export-td">灾难</td>
            </tr>
            
             <tr>
                <td class="export-td">2930</td>
                <td class="export-td">antenna</td>
                <td class="export-td">英:/æn'tenə/ 美:/æn'tɛnə/ </td>
                <td class="export-td">n. 天线；触角，触须</td>
            </tr>
            
             <tr>
                <td class="export-td">2931</td>
                <td class="export-td">asthma</td>
                <td class="export-td">英:/'æsmə/ 美:/'æzmə/ </td>
                <td class="export-td">n. [医]哮喘，气喘</td>
            </tr>
            
             <tr>
                <td class="export-td">2932</td>
                <td class="export-td">attic</td>
                <td class="export-td">英:/'ætɪk/ 美:/'ætɪk/ </td>
                <td class="export-td">n. 阁楼；顶楼；[解剖学]鼓室上的隐窝</td>
            </tr>
            
             <tr>
                <td class="export-td">2933</td>
                <td class="export-td">autobiography</td>
                <td class="export-td">英:/ɔːtəbaɪ'ɒgrəfɪ/ 美:/ˌɔtəbaɪ'ɑɡrəfi/ </td>
                <td class="export-td">自传</td>
            </tr>
            
             <tr>
                <td class="export-td">2934</td>
                <td class="export-td">bead</td>
                <td class="export-td">英:/biːd/ 美:/bid/ </td>
                <td class="export-td">1. n. 珠子；念珠；滴
2. vi. 形成珠状，起泡</td>
            </tr>
            
             <tr>
                <td class="export-td">2935</td>
                <td class="export-td">bin</td>
                <td class="export-td">英:/bɪn/ 美:/bɪn/ </td>
                <td class="export-td">箱柜</td>
            </tr>
            
             <tr>
                <td class="export-td">2936</td>
                <td class="export-td">blonde</td>
                <td class="export-td">英:/blɒnd/ 美:/blɑnd/ </td>
                <td class="export-td">1. adj. 亚麻色的；白皙的；白肤金发碧眼的
2. n. 白肤金发碧眼的女人</td>
            </tr>
            
             <tr>
                <td class="export-td">2937</td>
                <td class="export-td">canyon</td>
                <td class="export-td">英:/'kænjən/ 美:/ˈkænjən/ </td>
                <td class="export-td">n. 峡谷</td>
            </tr>
            
             <tr>
                <td class="export-td">2938</td>
                <td class="export-td">caravan</td>
                <td class="export-td">英:/'kærəvæn/ 美:/'kærəvæn/ </td>
                <td class="export-td">n. 旅行队；大篷车</td>
            </tr>
            
             <tr>
                <td class="export-td">2939</td>
                <td class="export-td">carbohydrate</td>
                <td class="export-td">英:/kɑːbə'haɪdreɪt/ 美:/ˌkɑrbo'haɪdret/ </td>
                <td class="export-td">碳水化合物, 醣</td>
            </tr>
            
             <tr>
                <td class="export-td">2940</td>
                <td class="export-td">cardboard</td>
                <td class="export-td">英:/'kɑːdbɔːd/ 美:/'kɑrdbɔrd/ </td>
                <td class="export-td">厚纸板</td>
            </tr>
            
             <tr>
                <td class="export-td">2941</td>
                <td class="export-td">caretaker</td>
                <td class="export-td">英:/'keəteɪkə/ 美:/'kɛr'tekɚ/ </td>
                <td class="export-td">临时代理的</td>
            </tr>
            
             <tr>
                <td class="export-td">2942</td>
                <td class="export-td">cartridge</td>
                <td class="export-td">英:/'kɑːtrɪdʒ/ 美:/'kɑrtrɪdʒ/ </td>
                <td class="export-td">盒式磁带</td>
            </tr>
            
             <tr>
                <td class="export-td">2943</td>
                <td class="export-td">carton</td>
                <td class="export-td">英:/'kɑːt(ə)n/ 美:/'kɑrtn/ </td>
                <td class="export-td">1. n. 纸板箱；靶心白点
2. vt. 用盒包装</td>
            </tr>
            
             <tr>
                <td class="export-td">2944</td>
                <td class="export-td">celebrity</td>
                <td class="export-td">英:/sɪ'lebrɪtɪ/ 美:/sə'lɛbrəti/ </td>
                <td class="export-td">n. 名人, 名流; 名声, 名誉名 词:   celebrityhood</td>
            </tr>
            
             <tr>
                <td class="export-td">2945</td>
                <td class="export-td">contented</td>
                <td class="export-td">英:/kən'tentɪd/ 美:/kən'tɛntɪd/ </td>
                <td class="export-td">自得</td>
            </tr>
            
             <tr>
                <td class="export-td">2946</td>
                <td class="export-td">contestant</td>
                <td class="export-td">英:/kən'test(ə)nt/ 美:/kən'tɛstənt/ </td>
                <td class="export-td">选手</td>
            </tr>
            
             <tr>
                <td class="export-td">2947</td>
                <td class="export-td">cookie</td>
                <td class="export-td">英:/'kʊkɪ/ 美:/'kʊki/ </td>
                <td class="export-td">n. 小甜点；饼干</td>
            </tr>
            
             <tr>
                <td class="export-td">2948</td>
                <td class="export-td">dealer</td>
                <td class="export-td">英:/'diːlə/ 美:/'dilɚ/ </td>
                <td class="export-td">1. n. 商人；经销商
2. v. 商人</td>
            </tr>
            
             <tr>
                <td class="export-td">2949</td>
                <td class="export-td">debut</td>
                <td class="export-td">英:/'deɪbjuː/ 美:/de'bju/ </td>
                <td class="export-td">1. n. 初次登台；开张
2. vi. 初次登台</td>
            </tr>
            
             <tr>
                <td class="export-td">2950</td>
                <td class="export-td">democrat</td>
                <td class="export-td">英:/'deməkræt/ 美:/'dɛməkræt/ </td>
                <td class="export-td">n. 民主政体论者；民主主义者；民主党人</td>
            </tr>
            
             <tr>
                <td class="export-td">2951</td>
                <td class="export-td">demolish</td>
                <td class="export-td">英:/dɪ'mɒlɪʃ/ 美:/dɪ'mɑlɪʃ/ </td>
                <td class="export-td">vt. 毁坏；推翻；破坏；拆除；驳倒</td>
            </tr>
            
             <tr>
                <td class="export-td">2952</td>
                <td class="export-td">den</td>
                <td class="export-td">英:/den/ 美:/dɛn/ </td>
                <td class="export-td">1. n. 兽穴，窝巢；贼窝，私室；小房间
2. vi. 藏到洞里；住在肮脏简陋的小房间里</td>
            </tr>
            
             <tr>
                <td class="export-td">2953</td>
                <td class="export-td">depot</td>
                <td class="export-td">英:/'depəʊ/ 美:/'dipo/ </td>
                <td class="export-td">1. n. 仓库；航空站；停车场
2. vt. 把…存放在储藏处</td>
            </tr>
            
             <tr>
                <td class="export-td">2954</td>
                <td class="export-td">derivative</td>
                <td class="export-td">英:/dɪ'rɪvətɪv/ 美:/də'rɪvətɪv/ </td>
                <td class="export-td">衍生</td>
            </tr>
            
             <tr>
                <td class="export-td">2955</td>
                <td class="export-td">detergent</td>
                <td class="export-td">英:/dɪ'tɜːdʒ(ə)nt/ 美:/dɪ'tɝdʒənt/ </td>
                <td class="export-td">清洁剂</td>
            </tr>
            
             <tr>
                <td class="export-td">2956</td>
                <td class="export-td">detour</td>
                <td class="export-td">英:/'diːtʊə/ 美:/'ditʊr/ </td>
                <td class="export-td">1. vt. 使…绕道而行
2. vi. 绕道；迂回</td>
            </tr>
            
             <tr>
                <td class="export-td">2957</td>
                <td class="export-td">devastate</td>
                <td class="export-td">英:/'devəsteɪt/ 美:/'dɛvəstet/ </td>
                <td class="export-td">毁坏,使震惊</td>
            </tr>
            
             <tr>
                <td class="export-td">2958</td>
                <td class="export-td">earring</td>
                <td class="export-td">英:/'ɪərɪŋ/ 美:/'ɪrɪŋ/ </td>
                <td class="export-td">1. n. 耳环，耳饰
2. v. 抽穗；[美俚]听见（ear的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">2959</td>
                <td class="export-td">encyclopedia</td>
                <td class="export-td">英:/en,saɪklə(ʊ)'piːdɪə/ 美:/ɪn'saɪklə'pidɪə/ </td>
                <td class="export-td">百科全书</td>
            </tr>
            
             <tr>
                <td class="export-td">2960</td>
                <td class="export-td">ferocious</td>
                <td class="export-td">英:/fə'rəʊʃəs/ 美:/fə'roʃəs/ </td>
                <td class="export-td">凶猛</td>
            </tr>
            
             <tr>
                <td class="export-td">2961</td>
                <td class="export-td">fiddle</td>
                <td class="export-td">英:/'fɪd(ə)l/ 美:/'fɪdl/ </td>
                <td class="export-td">1. n. 小提琴
2. vi. 瞎搞；拉小提琴</td>
            </tr>
            
             <tr>
                <td class="export-td">2962</td>
                <td class="export-td">fin</td>
                <td class="export-td">英:/fɪn/ 美:/fɪn/ </td>
                <td class="export-td">1. n. 鳍；鱼翅；鳍状物
2. vt. 切除鳍；装上翅</td>
            </tr>
            
             <tr>
                <td class="export-td">2963</td>
                <td class="export-td">flirt</td>
                <td class="export-td">英:/flɜːt/ 美:/flɝt/ </td>
                <td class="export-td">1. vi. 调情；玩弄；轻率地对待；摆动
2. vt. 挥动；忽然弹出</td>
            </tr>
            
             <tr>
                <td class="export-td">2964</td>
                <td class="export-td">flute</td>
                <td class="export-td">英:/fluːt/ 美:/flut/ </td>
                <td class="export-td">1. n. 长笛
2. vt. 用长笛吹奏</td>
            </tr>
            
             <tr>
                <td class="export-td">2965</td>
                <td class="export-td">foreground</td>
                <td class="export-td">英:/'fɔːgraʊnd/ 美:/ˈfɔrˌɡraʊnd/ </td>
                <td class="export-td">前景, 最显著的位置</td>
            </tr>
            
             <tr>
                <td class="export-td">2966</td>
                <td class="export-td">forgery</td>
                <td class="export-td">英:/'fɔːdʒ(ə)rɪ/ 美:/'fɔrdʒəri/ </td>
                <td class="export-td">n. 伪造；伪造罪；伪造物</td>
            </tr>
            
             <tr>
                <td class="export-td">2967</td>
                <td class="export-td">guerrilla</td>
                <td class="export-td">英:/gə'rɪlə/ 美:/gə'rɪlə/ </td>
                <td class="export-td">游击</td>
            </tr>
            
             <tr>
                <td class="export-td">2968</td>
                <td class="export-td">gulp</td>
                <td class="export-td">英:/gʌlp/ 美:/ɡʌlp/ </td>
                <td class="export-td">1. vt. 狼吞虎咽地吃；大口地吸
2. vi. 哽住；喘不过气</td>
            </tr>
            
             <tr>
                <td class="export-td">2969</td>
                <td class="export-td">gush</td>
                <td class="export-td">英:/gʌʃ/ 美:/ɡʌʃ/ </td>
                <td class="export-td">1. v. 涌出；迸出
2. n. 涌出；迸发</td>
            </tr>
            
             <tr>
                <td class="export-td">2970</td>
                <td class="export-td">gust</td>
                <td class="export-td">英:/gʌst/ 美:/ɡʌst/ </td>
                <td class="export-td">1. n. 一阵狂风；风味；趣味
2. vi. 一阵阵地劲吹</td>
            </tr>
            
             <tr>
                <td class="export-td">2971</td>
                <td class="export-td">gut</td>
                <td class="export-td">英:/gʌt/ 美:/ɡʌt/ </td>
                <td class="export-td">1. n. 内脏；肠子；胆量；海峡；剧情
2. vt. 取出内脏；摧毁内部装置</td>
            </tr>
            
             <tr>
                <td class="export-td">2972</td>
                <td class="export-td">gutter</td>
                <td class="export-td">英:/'gʌtə/ 美:/'gʌtɚ/ </td>
                <td class="export-td">1. n. 排水沟；槽；贫民区
2. vi. 流；形成沟</td>
            </tr>
            
             <tr>
                <td class="export-td">2973</td>
                <td class="export-td">habitat</td>
                <td class="export-td">英:/'hæbɪtæt/ 美:/'hæbə'tæt/ </td>
                <td class="export-td">n. 栖息地，产地</td>
            </tr>
            
             <tr>
                <td class="export-td">2974</td>
                <td class="export-td">hack</td>
                <td class="export-td">英:/hæk/ 美:/hæk/ </td>
                <td class="export-td">1. n. 砍，劈；出租马车
2. vt. 砍；出租</td>
            </tr>
            
             <tr>
                <td class="export-td">2975</td>
                <td class="export-td">harp</td>
                <td class="export-td">英:/hɑːp/ 美:/hɑrp/ </td>
                <td class="export-td">1. vi. 弹奏竖琴；喋喋不休；不停地说
2. n. 竖琴</td>
            </tr>
            
             <tr>
                <td class="export-td">2976</td>
                <td class="export-td">haze</td>
                <td class="export-td">英:/heɪz/ 美:/hez/ </td>
                <td class="export-td">1. n. 疑惑；阴霾；薄雾
2. vt. 使变朦胧；使变糊涂</td>
            </tr>
            
             <tr>
                <td class="export-td">2977</td>
                <td class="export-td">hideous</td>
                <td class="export-td">英:/'hɪdɪəs/ 美:/ˈhɪdiəs/ </td>
                <td class="export-td">adj. 可怕的；丑恶的</td>
            </tr>
            
             <tr>
                <td class="export-td">2978</td>
                <td class="export-td">hijack</td>
                <td class="export-td">英:/'haɪdʒæk/ 美:/'haɪdʒæk/ </td>
                <td class="export-td">1. vt. 抢劫；揩油
2. vi. 拦路抢劫</td>
            </tr>
            
             <tr>
                <td class="export-td">2979</td>
                <td class="export-td">hiss</td>
                <td class="export-td">英:/hɪs/ 美:/hɪs/ </td>
                <td class="export-td">1. vi. 发出嘘声；发嘘声
2. n. 嘘声；嘶嘶声</td>
            </tr>
            
             <tr>
                <td class="export-td">2980</td>
                <td class="export-td">hoard</td>
                <td class="export-td">英:/hɔːd/ 美:/hɔrd/ </td>
                <td class="export-td">1. vi. 积聚钱财；贮藏货物
2. vt. 贮藏</td>
            </tr>
            
             <tr>
                <td class="export-td">2981</td>
                <td class="export-td">hoarse</td>
                <td class="export-td">英:/hɔːs/ 美:/hɔrs/ </td>
                <td class="export-td">adj. 嘶哑的</td>
            </tr>
            
             <tr>
                <td class="export-td">2982</td>
                <td class="export-td">hoof</td>
                <td class="export-td">英:/huːf/ 美:/huf/ </td>
                <td class="export-td">1. vi. 步行；踢；跳舞
2. vt. 用蹄踢；步行</td>
            </tr>
            
             <tr>
                <td class="export-td">2983</td>
                <td class="export-td">hygiene</td>
                <td class="export-td">英:/'haɪdʒiːn/ 美:/'haɪdʒin/ </td>
                <td class="export-td">n. 卫生学；卫生；保健法</td>
            </tr>
            
             <tr>
                <td class="export-td">2984</td>
                <td class="export-td">hymn</td>
                <td class="export-td">英:/hɪm/ 美:/hɪm/ </td>
                <td class="export-td">1. n. 赞美诗；圣歌；欢乐的歌
2. vt. 唱赞美歌</td>
            </tr>
            
             <tr>
                <td class="export-td">2985</td>
                <td class="export-td">hyphen</td>
                <td class="export-td">英:/'haɪf(ə)n/ 美:/'haɪfn/ </td>
                <td class="export-td">1. vt. 以连字号连接
2. n. 连字号</td>
            </tr>
            
             <tr>
                <td class="export-td">2986</td>
                <td class="export-td">hypocrisy</td>
                <td class="export-td">英:/hɪ'pɒkrɪsɪ/ 美:/hɪ'pɑkrəsi/ </td>
                <td class="export-td">伪善</td>
            </tr>
            
             <tr>
                <td class="export-td">2987</td>
                <td class="export-td">idol</td>
                <td class="export-td">英:/'aɪd(ə)l/ 美:/'aɪdl/ </td>
                <td class="export-td">n. 偶像，崇拜物；幻象；[逻]谬论</td>
            </tr>
            
             <tr>
                <td class="export-td">2988</td>
                <td class="export-td">anorexia</td>
                <td class="export-td">英:/ˌænə'reksɪə/ 美:/'ænə'rɛksɪə/ </td>
                <td class="export-td">n. 厌食；神经性厌食症</td>
            </tr>
            
             <tr>
                <td class="export-td">2989</td>
                <td class="export-td">antibiotic</td>
                <td class="export-td">英:/ˌæntɪbaɪ'ɒtɪk/ 美:/ˌæntɪbaɪ'ɑtɪk/ </td>
                <td class="export-td">抗菌的; 抗生素</td>
            </tr>
            
             <tr>
                <td class="export-td">2990</td>
                <td class="export-td">antiseptic</td>
                <td class="export-td">英:/æntɪ'septɪk/ 美:/ˌæntɪ'sɛptɪk/ </td>
                <td class="export-td">杀菌剂, 防腐剂</td>
            </tr>
            
             <tr>
                <td class="export-td">2991</td>
                <td class="export-td">archaeology</td>
                <td class="export-td">英:/ˌɑːkɪ'ɒlədʒɪ/ 美:/ˌɑrkɪ'ɑlədʒi/ </td>
                <td class="export-td">考古学，古迹，文物</td>
            </tr>
            
             <tr>
                <td class="export-td">2992</td>
                <td class="export-td">armada</td>
                <td class="export-td">英:/ɑː'mɑːdə/ 美:/ɑrˈmɑdə/ </td>
                <td class="export-td">n. （西班牙的）无敌舰队</td>
            </tr>
            
             <tr>
                <td class="export-td">2993</td>
                <td class="export-td">arthritis</td>
                <td class="export-td">英:/ɑː'θraɪtɪs/ 美:/ɑr'θraɪtɪs/ </td>
                <td class="export-td">关节炎</td>
            </tr>
            
             <tr>
                <td class="export-td">2994</td>
                <td class="export-td">asterisk</td>
                <td class="export-td">英:/'æstərɪsk/ 美:/'æstərɪsk/ </td>
                <td class="export-td">1. n. 星号
2. vt. 注上星号；用星号标出</td>
            </tr>
            
             <tr>
                <td class="export-td">2995</td>
                <td class="export-td">asteroid</td>
                <td class="export-td">英:/'æstərɒɪd/ 美:/'æstərɔɪd/ </td>
                <td class="export-td">1. n. [天文]小行星；海盘车；小游星
2. adj. 星状的</td>
            </tr>
            
             <tr>
                <td class="export-td">2996</td>
                <td class="export-td">athletics</td>
                <td class="export-td">英:/æθ'letɪks/ 美:/æθ'lɛtɪks/ </td>
                <td class="export-td">体育运动，田径</td>
            </tr>
            
             <tr>
                <td class="export-td">2997</td>
                <td class="export-td">avalanche</td>
                <td class="export-td">英:/'ævəlɑːnʃ/ 美:/'ævəlæntʃ/ </td>
                <td class="export-td">雪崩</td>
            </tr>
            
             <tr>
                <td class="export-td">2998</td>
                <td class="export-td">bilingual</td>
                <td class="export-td">英:/baɪ'lɪŋgw(ə)l/ 美:/'baɪ'lɪŋgwəl/ </td>
                <td class="export-td">双语</td>
            </tr>
            
             <tr>
                <td class="export-td">2999</td>
                <td class="export-td">blur</td>
                <td class="export-td">英:/blɜː/ 美:/blɝ/ </td>
                <td class="export-td">1. vt. 涂污；使…模糊不清；使暗淡；玷污
2. vi. 沾上污迹；变模糊</td>
            </tr>
            
             <tr>
                <td class="export-td">3000</td>
                <td class="export-td">bricklayer</td>
                <td class="export-td">英:/'brɪkleɪə/ 美:/'brɪkleɚ/ </td>
                <td class="export-td">砖匠</td>
            </tr>
            
             <tr>
                <td class="export-td">3001</td>
                <td class="export-td">canary</td>
                <td class="export-td">英:/kə'neərɪ/ 美:/kə'nɛri/ </td>
                <td class="export-td">n. 金丝雀；淡黄色</td>
            </tr>
            
             <tr>
                <td class="export-td">3002</td>
                <td class="export-td">canopy</td>
                <td class="export-td">英:/'kænəpɪ/ 美:/'kænəpi/ </td>
                <td class="export-td">1. n. 天篷；遮篷；华盖；苍穹
2. vt. 用天蓬遮盖；遮盖</td>
            </tr>
            
             <tr>
                <td class="export-td">3003</td>
                <td class="export-td">carol</td>
                <td class="export-td">英:/'kær(ə)l/ 美:/'kærəl/ </td>
                <td class="export-td">1. vi. 欢乐地歌唱；唱耶诞颂歌
2. n. 颂歌，赞美诗；欢乐之歌</td>
            </tr>
            
             <tr>
                <td class="export-td">3004</td>
                <td class="export-td">caterpillar</td>
                <td class="export-td">英:/'kætəpɪlə/ 美:/'kætɚpɪlɚ/ </td>
                <td class="export-td">毛虫 卡特彼勒</td>
            </tr>
            
             <tr>
                <td class="export-td">3005</td>
                <td class="export-td">cello</td>
                <td class="export-td">英:/'tʃeləʊ/ 美:/'tʃɛlo/ </td>
                <td class="export-td">n. 大提琴</td>
            </tr>
            
             <tr>
                <td class="export-td">3006</td>
                <td class="export-td">certification</td>
                <td class="export-td">英:/ˌsɜːtɪfɪ'keɪʃən/ 美:/ˌsɝtɪfɪ'keʃən/ </td>
                <td class="export-td">证明,保证,鉴定</td>
            </tr>
            
             <tr>
                <td class="export-td">3007</td>
                <td class="export-td">defense</td>
                <td class="export-td">英:/diˈfens/ 美:/dɪ'fɛns/ </td>
                <td class="export-td">1. n. 防卫，防护；防御措施；防守
2. vt. 谋划抵御</td>
            </tr>
            
             <tr>
                <td class="export-td">3008</td>
                <td class="export-td">dent</td>
                <td class="export-td">英:/dent/ 美:/dɛnt/ </td>
                <td class="export-td">1. n. 凹痕；削弱；减少；[机械学]齿
2. vi. 产生凹陷；凹进去；削减</td>
            </tr>
            
             <tr>
                <td class="export-td">3009</td>
                <td class="export-td">depressed</td>
                <td class="export-td">英:/dɪ'prest/ 美:/dɪ'prɛst/ </td>
                <td class="export-td">沮丧的,降低的</td>
            </tr>
            
             <tr>
                <td class="export-td">3010</td>
                <td class="export-td">detached</td>
                <td class="export-td">英:/dɪ'tætʃt/ 美:/dɪ'tætʃt/ </td>
                <td class="export-td">1. adj. 分离的，分开的；超然的
2. v. 分离</td>
            </tr>
            
             <tr>
                <td class="export-td">3011</td>
                <td class="export-td">detest</td>
                <td class="export-td">英:/dɪ'test/ 美:/dɪ'tɛst/ </td>
                <td class="export-td">vt. 憎恨；厌恶</td>
            </tr>
            
             <tr>
                <td class="export-td">3012</td>
                <td class="export-td">devoted</td>
                <td class="export-td">英:/dɪˈvəʊtɪd/ 美:/dɪ'votɪd/ </td>
                <td class="export-td">1. adj. 献身的；忠诚的
2. v. 献身于…；致力于…（devote的过去分词）</td>
            </tr>
            
             <tr>
                <td class="export-td">3013</td>
                <td class="export-td">fabric</td>
                <td class="export-td">英:/'fæbrɪk/ 美:/'fæbrɪk/ </td>
                <td class="export-td">n. 织物；构造；建筑物；组织；布</td>
            </tr>
            
             <tr>
                <td class="export-td">3014</td>
                <td class="export-td">facilities</td>
                <td class="export-td"></td>
                <td class="export-td">工具, 设施, 设备</td>
            </tr>
            
             <tr>
                <td class="export-td">3015</td>
                <td class="export-td">fanatic</td>
                <td class="export-td">英:/fə'nætɪk/ 美:/fə'nætɪk/ </td>
                <td class="export-td">1. n. 狂热入迷者；盲信者；盲信
2. adj. 狂热的；盲信的</td>
            </tr>
            
             <tr>
                <td class="export-td">3016</td>
                <td class="export-td">faucet</td>
                <td class="export-td">英:/'fɔːsɪt/ 美:/ˈfɔsɪt/ </td>
                <td class="export-td">n. 旋塞；插口</td>
            </tr>
            
             <tr>
                <td class="export-td">3017</td>
                <td class="export-td">fell</td>
                <td class="export-td">英:/fel/ 美:/fɛl/ </td>
                <td class="export-td">1. adj. 凶猛的；毁灭性的
2. vt. 击倒；砍伐；打倒</td>
            </tr>
            
             <tr>
                <td class="export-td">3018</td>
                <td class="export-td">fern</td>
                <td class="export-td">英:/fɜːn/ 美:/fɝn/ </td>
                <td class="export-td">n. 蕨类植物；蕨</td>
            </tr>
            
             <tr>
                <td class="export-td">3019</td>
                <td class="export-td">fetus</td>
                <td class="export-td">英:/'fiːtəs/ 美:/'fitəs/ </td>
                <td class="export-td">n. 胎儿，胎</td>
            </tr>
            
             <tr>
                <td class="export-td">3020</td>
                <td class="export-td">fidget</td>
                <td class="export-td">英:/'fɪdʒɪt/ 美:/'fɪdʒɪt/ </td>
                <td class="export-td">1. vi. 烦躁；坐立不安；玩弄
2. n. 烦躁；坐立不安；烦躁不安的人</td>
            </tr>
            
             <tr>
                <td class="export-td">3021</td>
                <td class="export-td">fig</td>
                <td class="export-td">英:/fɪg/ 美:/fɪɡ/ </td>
                <td class="export-td">1. n. [植]无花果；无价值的东西；无花果树；少许，一些；服装
2. vt. 打扮；使马跑快</td>
            </tr>
            
             <tr>
                <td class="export-td">3022</td>
                <td class="export-td">firefly</td>
                <td class="export-td">英:/'faɪəflaɪ/ 美:/'faɪr'flai/ </td>
                <td class="export-td">n. 萤火虫</td>
            </tr>
            
             <tr>
                <td class="export-td">3023</td>
                <td class="export-td">flatten</td>
                <td class="export-td">英:/'flæt(ə)n/ 美:/ˈflætn../ </td>
                <td class="export-td">1. vt. 使……平坦；击败，摧毁
2. vi. 变平；变单调</td>
            </tr>
            
             <tr>
                <td class="export-td">3024</td>
                <td class="export-td">fluffy</td>
                <td class="export-td">英:/'flʌfɪ/ 美:/'flʌfi/ </td>
                <td class="export-td">adj. 蓬松的；松软的；毛茸茸的；无内容的</td>
            </tr>
            
             <tr>
                <td class="export-td">3025</td>
                <td class="export-td">folder</td>
                <td class="export-td">英:/'fəʊldə/ 美:/'foldɚ/ </td>
                <td class="export-td">n. 文件夹；折叠机；折叠式印刷品</td>
            </tr>
            
             <tr>
                <td class="export-td">3026</td>
                <td class="export-td">forge</td>
                <td class="export-td">英:/fɔːdʒ/ 美:/fɔrdʒ/ </td>
                <td class="export-td">1. n. 熔炉，锻铁炉；铁工厂
2. vi. 伪造；做锻工</td>
            </tr>
            
             <tr>
                <td class="export-td">3027</td>
                <td class="export-td">guilt</td>
                <td class="export-td">英:/gɪlt/ 美:/ɡɪlt/ </td>
                <td class="export-td">n. 内疚；犯罪，过失</td>
            </tr>
            
             <tr>
                <td class="export-td">3028</td>
                <td class="export-td">hangar</td>
                <td class="export-td">英:/'hæŋə/ 美:/'hæŋɚ/ </td>
                <td class="export-td">n. 飞机库；飞机棚</td>
            </tr>
            
             <tr>
                <td class="export-td">3029</td>
                <td class="export-td">harshly</td>
                <td class="export-td">英:/'ha:ʃli/ 美:/ˈh ɑrʃlɪ/ </td>
                <td class="export-td">adv. 严厉地；刺耳地；粗糙地</td>
            </tr>
            
             <tr>
                <td class="export-td">3030</td>
                <td class="export-td">hazardous</td>
                <td class="export-td">英:/'hæzədəs/ 美:/'hæzɚdəs/ </td>
                <td class="export-td">危险</td>
            </tr>
            
             <tr>
                <td class="export-td">3031</td>
                <td class="export-td">hibernate</td>
                <td class="export-td">英:/'haɪbəneɪt/ 美:/'haɪbɚnet/ </td>
                <td class="export-td">过冬,冬眠,避寒</td>
            </tr>
            
             <tr>
                <td class="export-td">3032</td>
                <td class="export-td">hive</td>
                <td class="export-td">英:/haɪv/ 美:/haɪv/ </td>
                <td class="export-td">1. vi. 群居；入蜂房；生活在蜂房中
2. n. 蜂房，蜂巢；热闹的场所；熙攘喧闹的人群</td>
            </tr>
            
             <tr>
                <td class="export-td">3033</td>
                <td class="export-td">hoax</td>
                <td class="export-td">英:/həʊks/ 美:/hoks/ </td>
                <td class="export-td">1. vt. 愚弄；欺骗
2. n. 恶作剧；骗局</td>
            </tr>
            
             <tr>
                <td class="export-td">3034</td>
                <td class="export-td">hormone</td>
                <td class="export-td">英:/'hɔːməʊn/ 美:/'hɔrmon/ </td>
                <td class="export-td">n. 激素，荷尔蒙</td>
            </tr>
            
             <tr>
                <td class="export-td">3035</td>
                <td class="export-td">horrific</td>
                <td class="export-td">英:/hɒ'rɪfɪk/ 美:/hə'rɪfɪk/ </td>
                <td class="export-td">adj. 可怕的；令人毛骨悚然的</td>
            </tr>
            
             <tr>
                <td class="export-td">3036</td>
                <td class="export-td">hospitable</td>
                <td class="export-td">英:/hɒ'spɪtəb(ə)l/ 美:/hɑ'spɪtəbl/ </td>
                <td class="export-td">好客</td>
            </tr>
            
             <tr>
                <td class="export-td">3037</td>
                <td class="export-td">humor</td>
                <td class="export-td">英:/ˈhju:mə/ 美:/'hjʊmɚ/ </td>
                <td class="export-td">1. n. 幽默，诙谐；心情
2. vt. 迎合，迁就；顺应</td>
            </tr>
            
             <tr>
                <td class="export-td">3038</td>
                <td class="export-td">hypocrite</td>
                <td class="export-td">英:/'hɪpəkrɪt/ 美:/'hɪpə'krɪt/ </td>
                <td class="export-td">n. 伪君子；伪善者</td>
            </tr>
            
             <tr>
                <td class="export-td">3039</td>
                <td class="export-td">icon</td>
                <td class="export-td">英:/'aɪkɒn/ 美:/ˈaɪˌkɑn/ </td>
                <td class="export-td">n. 图标；肖像，画像；圣像；偶像</td>
            </tr>
            
             <tr>
                <td class="export-td">3040</td>
                <td class="export-td">illiterate</td>
                <td class="export-td">英:/ɪ'lɪt(ə)rət/ 美:/ɪ'lɪtərət/ </td>
                <td class="export-td">文盲的, 无知的</td>
            </tr>
            
             <tr>
                <td class="export-td">3041</td>
                <td class="export-td">immunize</td>
                <td class="export-td">英:/ˈɪmjəˌnaɪz/ 美:/'ɪmjʊ'naɪz/ </td>
                <td class="export-td">vt. 使免疫；赋予免疫性</td>
            </tr>
            
             <tr>
                <td class="export-td">3042</td>
                <td class="export-td">prey</td>
                <td class="export-td">英:/preɪ/ 美:/pre/ </td>
                <td class="export-td">1. vi. 捕食；掠夺；折磨
2. n. 牺牲者；被捕食的动物；捕食</td>
            </tr>
            
             <tr>
                <td class="export-td">3043</td>
                <td class="export-td">cactus</td>
                <td class="export-td">英:/'kæktəs/ 美:/'kæktəs/ </td>
                <td class="export-td">n. [植]仙人掌</td>
            </tr>
            
             <tr>
                <td class="export-td">3044</td>
                <td class="export-td">fleece</td>
                <td class="export-td">英:/fliːs/ 美:/flis/ </td>
                <td class="export-td">1. n. 羊毛，绒头织物；羊毛制的覆盖物
2. vt. 剪下羊毛；欺诈，剥削</td>
            </tr>
            
             <tr>
                <td class="export-td">3045</td>
                <td class="export-td">gull</td>
                <td class="export-td">英:/gʌl/ 美:/ɡʌl/ </td>
                <td class="export-td">1. n. [动]鸥；笨人；易受骗之人
2. vt. 骗；欺诈</td>
            </tr>
            
             <tr>
                <td class="export-td">3046</td>
                <td class="export-td">haggle</td>
                <td class="export-td">英:/'hæg(ə)l/ 美:/'hæɡl/ </td>
                <td class="export-td">1. n. 讨价还价；争论
2. vt. 乱劈；乱砍</td>
            </tr>
            
             <tr>
                <td class="export-td">3047</td>
                <td class="export-td">hassle</td>
                <td class="export-td">英:/'hæs(ə)l/ 美:/'hæsl/ </td>
                <td class="export-td">1. vt. 找麻烦，搅扰；与…争辩；使…烦恼
2. n. 困难，麻烦；激战</td>
            </tr>
            
             <tr>
                <td class="export-td">3048</td>
                <td class="export-td">hippopotamus</td>
                <td class="export-td">英:/ˌhɪpə'pɒtəməs/ 美:/ˌhɪpəˈpɑtəməs/ </td>
                <td class="export-td">n. 河马</td>
            </tr>
            
             <tr>
                <td class="export-td">3049</td>
                <td class="export-td">huddle</td>
                <td class="export-td">英:/'hʌd(ə)l/ 美:/'hʌdl/ </td>
                <td class="export-td">1. vt. 把...挤在一起；使缩成一团；草率了事
2. vi. 挤作一团；蜷缩</td>
            </tr>
            
             <tr>
                <td class="export-td">3050</td>
                <td class="export-td">icing</td>
                <td class="export-td">英:/'aɪsɪŋ/ 美:/'aɪsɪŋ/ </td>
                <td class="export-td">1. n. 结冰；糖衣；酥皮
2. v. 冰冻（ice的ing形式）</td>
            </tr>
            
             <tr>
                <td class="export-td">3051</td>
                <td class="export-td">illegible</td>
                <td class="export-td">英:/ɪ'ledʒɪb(ə)l/ 美:/ɪ'lɛdʒəbl/ </td>
                <td class="export-td">难辨认的,  模糊的</td>
            </tr>
            
             <tr>
                <td class="export-td">3052</td>
                <td class="export-td">immortal</td>
                <td class="export-td">英:/ɪ'mɔːt(ə)l/ 美:/ɪ'mɔrtl/ </td>
                <td class="export-td">1. adj. 长生的；不朽的；神仙的
2. n. 不朽人物；神仙</td>
            </tr>
"""

    items = get_word_from_html(html)
    for item in items:
        print(item)

if __name__ == "__main__":
    main()