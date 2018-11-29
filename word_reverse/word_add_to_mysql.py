import re
import pymysql
import traceback

#链接数据库
conn = pymysql.connect(host="localhost",user="root",password="root",db="dict_oxford_primary",charset="utf8")

#获取代码并用正则表达式进行解析
def get_useful_informatin(html):

        parttern = re.compile("<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>",re.S)
        items = re.findall(parttern,html)

        for item in items:
            yield {
                "number1":item[0],
                "word":item[1],
                "alphabet":item[2],
                "meaning":item[3]
            }

            sql = "insert into wrod_list(number1,word,alphabet,meaning) values ('"+item[0]+"','"+item[1]+"','"+item[2]+"','"+item[3]+"');"
            try:
                conn.query(sql)
                conn.commit()
                print("数据存储成功........................")
            except Exception:
                print("数据存储异常........................"+traceback._cause_message)
                conn.rollback()

def main():
    html = """<tr>
                    <td class="export-td">1</td>
                    <td class="export-td">chequebook</td>
                    <td class="export-td">/'tʃekbuk/ </td>
                    <td class="export-td">支票簿</td>
                </tr>

                 <tr>
                    <td class="export-td">2</td>
                    <td class="export-td">cheers</td>
                    <td class="export-td">英:/tʃɪəz/ 美:/tʃɪrz/ </td>
                    <td class="export-td">1. int. 干杯
    2. n. 喝采；欢呼</td>
                </tr>

                 <tr>
                    <td class="export-td">3</td>
                    <td class="export-td">cheerfully</td>
                    <td class="export-td">英:/'tʃiəfəli/ 美:/ˈtʃɪrfəlɪ/ </td>
                    <td class="export-td">高高兴兴地</td>
                </tr>

                 <tr>
                    <td class="export-td">4</td>
                    <td class="export-td">checkout</td>
                    <td class="export-td">英:/'tʃekaʊt/ 美:/'tʃɛkaʊt/ </td>
                    <td class="export-td">n. 检验；结帐台；签出；检出</td>
                </tr>

                 <tr>
                    <td class="export-td">5</td>
                    <td class="export-td">charmed</td>
                    <td class="export-td">英:/tʃɑ:md/ 美:/tʃɑrmd/ </td>
                    <td class="export-td">1. adj. 喜悦的；着迷的
    2. v. 迷住；对…行魔法；哄诱（charm的过去分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">6</td>
                    <td class="export-td">charge card</td>
                    <td class="export-td"></td>
                    <td class="export-td">付款卡，信用卡；签帐卡</td>
                </tr>

                 <tr>
                    <td class="export-td">7</td>
                    <td class="export-td">chair lift</td>
                    <td class="export-td"></td>
                    <td class="export-td">升降椅；架空滑车</td>
                </tr>

                 <tr>
                    <td class="export-td">8</td>
                    <td class="export-td">centimeter</td>
                    <td class="export-td">英:/ˈsentimi:tər/ 美:/'sɛntə,mitɚ/ </td>
                    <td class="export-td">厘米，公分</td>
                </tr>

                 <tr>
                    <td class="export-td">9</td>
                    <td class="export-td">centilitre</td>
                    <td class="export-td">/'senti,li:tə/ </td>
                    <td class="export-td">厘升</td>
                </tr>

                 <tr>
                    <td class="export-td">10</td>
                    <td class="export-td">Celsius</td>
                    <td class="export-td">/'selsiəs/ </td>
                    <td class="export-td">1. adj. 摄氏的
    2. n. 摄氏度</td>
                </tr>

                 <tr>
                    <td class="export-td">11</td>
                    <td class="export-td">cellphone</td>
                    <td class="export-td">/'sɛl'fon/ </td>
                    <td class="export-td">手机</td>
                </tr>

                 <tr>
                    <td class="export-td">12</td>
                    <td class="export-td">celery</td>
                    <td class="export-td">英:/'selərɪ/ 美:/'sɛləri/ </td>
                    <td class="export-td">n. 芹菜</td>
                </tr>

                 <tr>
                    <td class="export-td">13</td>
                    <td class="export-td">celebration</td>
                    <td class="export-td">英:/selɪ'breɪʃ(ə)n/ 美:/ˌsɛlɪ'breʃən/ </td>
                    <td class="export-td">典礼,宗教仪式,庆祝</td>
                </tr>

                 <tr>
                    <td class="export-td">14</td>
                    <td class="export-td">CD player</td>
                    <td class="export-td"></td>
                    <td class="export-td">激光唱机；CD播放器</td>
                </tr>

                 <tr>
                    <td class="export-td">15</td>
                    <td class="export-td">CD</td>
                    <td class="export-td">/ˌsi: 'di:/ </td>
                    <td class="export-td">abbr. 光盘，激光唱片（Compact Disc）；呼叫设备（Calling Device）；中央地区（Central District）；商务部（Commerce Department）</td>
                </tr>

                 <tr>
                    <td class="export-td">16</td>
                    <td class="export-td">CCTV</td>
                    <td class="export-td">/ˌsi: si: ti: 'vi:/ </td>
                    <td class="export-td">abbr. 闭路电视（Closed Circuit Television）；中国中央电视台（China Central Television）</td>
                </tr>

                 <tr>
                    <td class="export-td">17</td>
                    <td class="export-td">cauliflower</td>
                    <td class="export-td">英:/'kɒlɪflaʊə/ 美:/'kɔlɪ'flaʊɚ/ </td>
                    <td class="export-td">花椰菜</td>
                </tr>

                 <tr>
                    <td class="export-td">18</td>
                    <td class="export-td">caught</td>
                    <td class="export-td">英:/kɔːt/ 美:/kɔt/ </td>
                    <td class="export-td">v. 捕捉（catch的过去分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">19</td>
                    <td class="export-td">catalogue</td>
                    <td class="export-td">英:/ˈkætəlɔɡ/ 美:/'kætəlɔɡ/ </td>
                    <td class="export-td">目录,总目,系列</td>
                </tr>

                 <tr>
                    <td class="export-td">20</td>
                    <td class="export-td">casually</td>
                    <td class="export-td">英:/'kæʒjuəli/ 美:/ˈkæ ʒjʊəlɪ/ </td>
                    <td class="export-td">adv. 偶然地；随便地；临时地</td>
                </tr>

                 <tr>
                    <td class="export-td">21</td>
                    <td class="export-td">cashier</td>
                    <td class="export-td">英:/kæ'ʃɪə/ 美:/kæ'ʃɪr/ </td>
                    <td class="export-td">1. n. 出纳员；司库
    2. vt. 解雇；抛弃</td>
                </tr>

                 <tr>
                    <td class="export-td">22</td>
                    <td class="export-td">carried</td>
                    <td class="export-td">/'kærid/ </td>
                    <td class="export-td">进行</td>
                </tr>

                 <tr>
                    <td class="export-td">23</td>
                    <td class="export-td">carousel</td>
                    <td class="export-td">英:/ˌkærə'sel/ 美:/'kærə'sɛl/ </td>
                    <td class="export-td">n. 旋转木马</td>
                </tr>

                 <tr>
                    <td class="export-td">24</td>
                    <td class="export-td">carnival</td>
                    <td class="export-td">英:/'kɑːnɪv(ə)l/ 美:/'kɑrnɪvl/ </td>
                    <td class="export-td">n. 狂欢节，嘉年华会；饮宴狂欢</td>
                </tr>

                 <tr>
                    <td class="export-td">25</td>
                    <td class="export-td">cardigan</td>
                    <td class="export-td">英:/'kɑːdɪg(ə)n/ 美:/'kɑrdɪɡən/ </td>
                    <td class="export-td">n. 羊毛衫，开襟羊毛衫（等于cardigan sweater）</td>
                </tr>

                 <tr>
                    <td class="export-td">26</td>
                    <td class="export-td">captured</td>
                    <td class="export-td"></td>
                    <td class="export-td">1. adj. 被俘的；捕获的
    2. v. 捕获；占领；引起（capture的过去分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">27</td>
                    <td class="export-td">captivity</td>
                    <td class="export-td">英:/kæp'tɪvɪtɪ/ 美:/kæp'tɪvəti/ </td>
                    <td class="export-td">囚禁, 被俘虏</td>
                </tr>

                 <tr>
                    <td class="export-td">28</td>
                    <td class="export-td">captains</td>
                    <td class="export-td">/'kæptin/ </td>
                    <td class="export-td">n. 船长；军官；首领；（体育运动中的）队长（captain的复数）</td>
                </tr>

                 <tr>
                    <td class="export-td">29</td>
                    <td class="export-td">cannot</td>
                    <td class="export-td">英:/'kænɒt/ 美:/'kænɑt/ </td>
                    <td class="export-td">v. 不能；无法</td>
                </tr>

                 <tr>
                    <td class="export-td">30</td>
                    <td class="export-td">cannibal</td>
                    <td class="export-td">英:/'kænɪb(ə)l/ 美:/'kænəbl/ </td>
                    <td class="export-td">1. n. 食人者；吃同类的动物
    2. adj. 食同类的；吃人肉的；凶残的</td>
                </tr>

                 <tr>
                    <td class="export-td">31</td>
                    <td class="export-td">canned</td>
                    <td class="export-td">英:/kænd/ 美:/kænd/ </td>
                    <td class="export-td">1. adj. 录音的；罐装的
    2. v. 装于罐头（can的过去分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">32</td>
                    <td class="export-td">candlestick</td>
                    <td class="export-td">英:/'kænd(ə)lstɪk/ 美:/'kændlstɪk/ </td>
                    <td class="export-td">烛台</td>
                </tr>

                 <tr>
                    <td class="export-td">33</td>
                    <td class="export-td">cancellation</td>
                    <td class="export-td">英:/ˌkænsə'leɪʃ(ə)n/ 美:/ˌkænsə'leʃən/ </td>
                    <td class="export-td">取消</td>
                </tr>

                 <tr>
                    <td class="export-td">34</td>
                    <td class="export-td">campsite</td>
                    <td class="export-td">英:/'kæmpsaɪt/ 美:/'kæmpsaɪt/ </td>
                    <td class="export-td">n. 营地</td>
                </tr>

                 <tr>
                    <td class="export-td">35</td>
                    <td class="export-td">camping</td>
                    <td class="export-td">/'kæmpiŋ/ </td>
                    <td class="export-td">1. n. 露营；野营
    2. v. 扎营；露营；临时安顿（camp的ing形式）</td>
                </tr>

                 <tr>
                    <td class="export-td">36</td>
                    <td class="export-td">camels</td>
                    <td class="export-td">/'kæml/ </td>
                    <td class="export-td">n. 骆驼体系；骆驼（camel的复数）</td>
                </tr>

                 <tr>
                    <td class="export-td">37</td>
                    <td class="export-td">calves</td>
                    <td class="export-td">英:/kɑːvz/ 美:/kævz/ </td>
                    <td class="export-td">n. 小牛；小腿；腓；[口]呆子（calf的复数）</td>
                </tr>

                 <tr>
                    <td class="export-td">38</td>
                    <td class="export-td">caffeine</td>
                    <td class="export-td">英:/'kæfiːn/ 美:/'kæfin/ </td>
                    <td class="export-td">n. 咖啡因；茶精（兴奋剂）</td>
                </tr>

                 <tr>
                    <td class="export-td">39</td>
                    <td class="export-td">cab</td>
                    <td class="export-td">英:/kæb/ 美:/kæb/ </td>
                    <td class="export-td">1. n. 出租汽车；出租马车；驾驶室
    2. vi. 乘出租马车（或汽车）</td>
                </tr>

                 <tr>
                    <td class="export-td">40</td>
                    <td class="export-td">businesswoman</td>
                    <td class="export-td">英:/'biznis,wumən/ 美:/ˈbɪznɪsˌwʊmən/ </td>
                    <td class="export-td">女商人</td>
                </tr>

                 <tr>
                    <td class="export-td">41</td>
                    <td class="export-td">buried</td>
                    <td class="export-td">/'berid/ </td>
                    <td class="export-td">1. adj. 埋葬的；[地]埋藏的
    2. v. 埋葬（bury的过去式和过去分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">42</td>
                    <td class="export-td">burglarize</td>
                    <td class="export-td">英:/'bɜːgləraɪz/ 美:/'bɝglə,raɪz/ </td>
                    <td class="export-td">vt. 闯入…盗窃; vi. 破门盗窃时 态:   burglarized, burglarizin...</td>
                </tr>

                 <tr>
                    <td class="export-td">43</td>
                    <td class="export-td">bulldog</td>
                    <td class="export-td">英:/'bʊldɒg/ 美:/'bʊl'dɔg/ </td>
                    <td class="export-td">n. 牛头犬，恶犬；短枪管大型手枪</td>
                </tr>

                 <tr>
                    <td class="export-td">44</td>
                    <td class="export-td">buildable</td>
                    <td class="export-td">英:/'bɪldəbl/ 美:/'bɪldəbəl/ </td>
                    <td class="export-td">可建</td>
                </tr>

                 <tr>
                    <td class="export-td">45</td>
                    <td class="export-td">budgeter</td>
                    <td class="export-td">/ˌbʌdʒi'tiə/ </td>
                    <td class="export-td">n. 预算编制者</td>
                </tr>

                 <tr>
                    <td class="export-td">46</td>
                    <td class="export-td">browser</td>
                    <td class="export-td">英:/'brauzə/ 美:/ˈbraʊzɚ/ </td>
                    <td class="export-td">n. 吃嫩叶的动物；浏览书本的人；[电脑]浏览器</td>
                </tr>

                 <tr>
                    <td class="export-td">47</td>
                    <td class="export-td">breathability</td>
                    <td class="export-td">/ˌbri:ðə'biləti/ </td>
                    <td class="export-td">透气</td>
                </tr>

                 <tr>
                    <td class="export-td">48</td>
                    <td class="export-td">breaststroke</td>
                    <td class="export-td">英:/ˈbrestˌstrəuk/ 美:/'brɛststrok/ </td>
                    <td class="export-td">蛙泳</td>
                </tr>

                 <tr>
                    <td class="export-td">49</td>
                    <td class="export-td">breadcrumb</td>
                    <td class="export-td">英:/'bredkrʌm/ 美:/ˈbr ɛdkr ʌmb/ </td>
                    <td class="export-td">面包屑</td>
                </tr>

                 <tr>
                    <td class="export-td">50</td>
                    <td class="export-td">brackets</td>
                    <td class="export-td">/'brækɪt/ </td>
                    <td class="export-td">1. n. 支架；方括号；舱口围板支架（bracket的复数）
    2. v. 给…装上托架；把…容纳在内（bracket的三单形式）</td>
                </tr>

                 <tr>
                    <td class="export-td">51</td>
                    <td class="export-td">boyfriend</td>
                    <td class="export-td">英:/'bɒɪfrend/ 美:/'bɔɪfrɛnd/ </td>
                    <td class="export-td">男朋友</td>
                </tr>

                 <tr>
                    <td class="export-td">52</td>
                    <td class="export-td">bored</td>
                    <td class="export-td">英:/bɔ:d/ 美:/bɔrd/ </td>
                    <td class="export-td">1. adj. 无聊的；烦人的；无趣的
    2. v. 烦扰；使厌烦（bore的过去式）</td>
                </tr>

                 <tr>
                    <td class="export-td">53</td>
                    <td class="export-td">bookshelf</td>
                    <td class="export-td">英:/'bʊkʃelf/ 美:/ˈbʊkˌʃɛlf/ </td>
                    <td class="export-td">书架</td>
                </tr>

                 <tr>
                    <td class="export-td">54</td>
                    <td class="export-td">bookshop</td>
                    <td class="export-td">英:/'bʊkʃɒp/ 美:/'bʊkʃɑp/ </td>
                    <td class="export-td">n. 书店</td>
                </tr>

                 <tr>
                    <td class="export-td">55</td>
                    <td class="export-td">bookmark</td>
                    <td class="export-td">英:/'bʊkmɑːk/ 美:/'bʊkmɑrk/ </td>
                    <td class="export-td">n. 书签（等于bookmarker）；标记</td>
                </tr>

                 <tr>
                    <td class="export-td">56</td>
                    <td class="export-td">bookshelves</td>
                    <td class="export-td">/'bukʃelvz/ </td>
                    <td class="export-td">书架</td>
                </tr>

                 <tr>
                    <td class="export-td">57</td>
                    <td class="export-td">bodybuild</td>
                    <td class="export-td"></td>
                    <td class="export-td">健身，</td>
                </tr>

                 <tr>
                    <td class="export-td">58</td>
                    <td class="export-td">BMX</td>
                    <td class="export-td">/'bi:em'eks/ </td>
                    <td class="export-td">abbr. 自行车越野赛（bicycle motocross）</td>
                </tr>

                 <tr>
                    <td class="export-td">59</td>
                    <td class="export-td">blosson</td>
                    <td class="export-td"></td>
                    <td class="export-td"></td>
                </tr>

                 <tr>
                    <td class="export-td">60</td>
                    <td class="export-td">blog</td>
                    <td class="export-td">/blɔg/ </td>
                    <td class="export-td">网络随笔，日志 博客</td>
                </tr>

                 <tr>
                    <td class="export-td">61</td>
                    <td class="export-td">bishop</td>
                    <td class="export-td">英:/ˈbɪʃəp/ 美:/ˈbɪʃəp/ </td>
                    <td class="export-td">n. 主教</td>
                </tr>

                 <tr>
                    <td class="export-td">62</td>
                    <td class="export-td">biro</td>
                    <td class="export-td">/'baiərəu/ </td>
                    <td class="export-td">1. n. 圆珠笔的一种
    2. vt. 用圆珠笔写</td>
                </tr>

                 <tr>
                    <td class="export-td">63</td>
                    <td class="export-td">biologist</td>
                    <td class="export-td">/bai'ɔlədʒist/ </td>
                    <td class="export-td">生物学家</td>
                </tr>

                 <tr>
                    <td class="export-td">64</td>
                    <td class="export-td">biodiversity</td>
                    <td class="export-td">英:/ˌbaiəudaiˈvə:səti/ 美:/ˌbaɪodaɪ'vɝsəti/ </td>
                    <td class="export-td">生物多样性</td>
                </tr>

                 <tr>
                    <td class="export-td">65</td>
                    <td class="export-td">biodegradable</td>
                    <td class="export-td">英:/ˌbaɪə(ʊ)dɪ'greɪdəb(ə)l/ 美:/ˌbaɪodɪ'ɡredəbl/ </td>
                    <td class="export-td">可生物降解</td>
                </tr>

                 <tr>
                    <td class="export-td">66</td>
                    <td class="export-td">binoculars</td>
                    <td class="export-td">/bɪ'nɑkjəlɚz/ </td>
                    <td class="export-td">双眼望远镜</td>
                </tr>

                 <tr>
                    <td class="export-td">67</td>
                    <td class="export-td">bingo</td>
                    <td class="export-td">英:/'bɪŋgəʊ/ 美:/'bɪŋɡo/ </td>
                    <td class="export-td">n. 宾戈游戏</td>
                </tr>

                 <tr>
                    <td class="export-td">68</td>
                    <td class="export-td">billfold</td>
                    <td class="export-td">英:/'bɪlfəʊld/ 美:/'bɪlfold/ </td>
                    <td class="export-td">n. 皮夹子</td>
                </tr>

                 <tr>
                    <td class="export-td">69</td>
                    <td class="export-td">billboard</td>
                    <td class="export-td">英:/'bɪlbɔːd/ 美:/'bɪlbɔrd/ </td>
                    <td class="export-td">广告牌; 宣传</td>
                </tr>

                 <tr>
                    <td class="export-td">70</td>
                    <td class="export-td">bikini</td>
                    <td class="export-td">英:/biˈki:ni/ 美:/bɪˈkini/ </td>
                    <td class="export-td">n. 比基尼泳装；大爆炸</td>
                </tr>

                 <tr>
                    <td class="export-td">71</td>
                    <td class="export-td">bib</td>
                    <td class="export-td">英:/bɪb/ 美:/bɪb/ </td>
                    <td class="export-td">1. n. 围嘴，围涎；围裙的上部
    2. vi. 饮酒，不断地饮酒</td>
                </tr>

                 <tr>
                    <td class="export-td">72</td>
                    <td class="export-td">bewildered</td>
                    <td class="export-td"></td>
                    <td class="export-td"></td>
                </tr>

                 <tr>
                    <td class="export-td">73</td>
                    <td class="export-td">behaviour</td>
                    <td class="export-td">英:/bɪ'heɪvjə/ 美:/bɪˈhevjɚ/ </td>
                    <td class="export-td">行为</td>
                </tr>

                 <tr>
                    <td class="export-td">74</td>
                    <td class="export-td">begining</td>
                    <td class="export-td">/bi'ɡin/ </td>
                    <td class="export-td">1. n. 开始
    2. v. 开始；创办（begin的ing形式）</td>
                </tr>

                 <tr>
                    <td class="export-td">75</td>
                    <td class="export-td">bedsit</td>
                    <td class="export-td">英:/bed'sɪt/ 美:/'bɛdsɪt/ </td>
                    <td class="export-td">1. n. 卧室兼起居室
    2. vt. 租用卧室兼起居室</td>
                </tr>

                 <tr>
                    <td class="export-td">76</td>
                    <td class="export-td">bathtub</td>
                    <td class="export-td">英:/'bɑːθtʌb/ 美:/bæθtʌb/ </td>
                    <td class="export-td">n. 浴缸</td>
                </tr>

                 <tr>
                    <td class="export-td">77</td>
                    <td class="export-td">bathrobe</td>
                    <td class="export-td">英:/'bɑːθrəʊb/ 美:/'bæθrob/ </td>
                    <td class="export-td">n. 睡衣；浴衣</td>
                </tr>

                 <tr>
                    <td class="export-td">78</td>
                    <td class="export-td">Bach</td>
                    <td class="export-td">英:/bætʃ/ 美:/bɑk/ </td>
                    <td class="export-td">n. 巴赫（德国作曲家）</td>
                </tr>

                 <tr>
                    <td class="export-td">79</td>
                    <td class="export-td">barefoot</td>
                    <td class="export-td">英:/'beəfʊt/ 美:/'bɛr'fʊt/ </td>
                    <td class="export-td">1. adj. 赤脚的
    2. adv. 赤着脚地</td>
                </tr>

                 <tr>
                    <td class="export-td">80</td>
                    <td class="export-td">ballpoint</td>
                    <td class="export-td">英:/ˈbɔ:lˌpɔɪnt/ 美:/'bɔlpɔɪnt/ </td>
                    <td class="export-td">圆珠笔</td>
                </tr>

                 <tr>
                    <td class="export-td">81</td>
                    <td class="export-td">ballpiont</td>
                    <td class="export-td"></td>
                    <td class="export-td"></td>
                </tr>

                 <tr>
                    <td class="export-td">82</td>
                    <td class="export-td">bakehead</td>
                    <td class="export-td">/'beik,hed/ </td>
                    <td class="export-td">n. 〈俚〉火车司炉</td>
                </tr>

                 <tr>
                    <td class="export-td">83</td>
                    <td class="export-td">baked</td>
                    <td class="export-td">英:/'beikid/ 美:/bekt/ </td>
                    <td class="export-td">1. adj. 烘焙的；烤的
    2. v. 烘培；烧制（bake的过去分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">84</td>
                    <td class="export-td">baguette</td>
                    <td class="export-td">英:/bæ'get/ 美:/bæˈɡɛt/ </td>
                    <td class="export-td">n. 法国棍子面包；成长方形的宝石</td>
                </tr>

                 <tr>
                    <td class="export-td">85</td>
                    <td class="export-td">backwards</td>
                    <td class="export-td">英:/'bækwədz/ 美:/'bækwɚdz/ </td>
                    <td class="export-td">落后的, 向后的</td>
                </tr>

                 <tr>
                    <td class="export-td">86</td>
                    <td class="export-td">backup</td>
                    <td class="export-td">英:/'bækʌp/ 美:/'bæk,ʌp/ </td>
                    <td class="export-td">1. n. 支持；后援；阻塞
    2. adj. 候补的；支持的</td>
                </tr>

                 <tr>
                    <td class="export-td">87</td>
                    <td class="export-td">babysitter</td>
                    <td class="export-td">/'beibisitə/ </td>
                    <td class="export-td">保姆</td>
                </tr>

                 <tr>
                    <td class="export-td">88</td>
                    <td class="export-td">babysit</td>
                    <td class="export-td">/'bebɪsɪt/ </td>
                    <td class="export-td">vi. （临时代人）照看婴孩</td>
                </tr>

                 <tr>
                    <td class="export-td">89</td>
                    <td class="export-td">B.A</td>
                    <td class="export-td"></td>
                    <td class="export-td"></td>
                </tr>

                 <tr>
                    <td class="export-td">90</td>
                    <td class="export-td">Resistac</td>
                    <td class="export-td"></td>
                    <td class="export-td">瑞西斯达克铜铝合金</td>
                </tr>

                 <tr>
                    <td class="export-td">91</td>
                    <td class="export-td">resistable</td>
                    <td class="export-td">/ri'zistəbl/ </td>
                    <td class="export-td">adj. 可抵抗的</td>
                </tr>

                 <tr>
                    <td class="export-td">92</td>
                    <td class="export-td">resistless</td>
                    <td class="export-td">英:/rɪ'zɪs(t)lɪs/ 美:/rɪ'zɪstlɪs/ </td>
                    <td class="export-td">不可抗拒的</td>
                </tr>

                 <tr>
                    <td class="export-td">93</td>
                    <td class="export-td">resistent</td>
                    <td class="export-td">/ri'zistənt/ </td>
                    <td class="export-td">性能稳定的</td>
                </tr>

                 <tr>
                    <td class="export-td">94</td>
                    <td class="export-td">resistible</td>
                    <td class="export-td">英:/rɪ'zɪstəbl/ 美:/rɪ'zɪstəbl/ </td>
                    <td class="export-td">可抵抗的</td>
                </tr>

                 <tr>
                    <td class="export-td">95</td>
                    <td class="export-td">resister</td>
                    <td class="export-td">/ri'zistə/ </td>
                    <td class="export-td">n. 抵抗者；反抗者；[物]电阻器</td>
                </tr>

                 <tr>
                    <td class="export-td">96</td>
                    <td class="export-td">resistin</td>
                    <td class="export-td">/ri'zistin/ </td>
                    <td class="export-td">n. 抵抗素；一种锰铜电阻合金</td>
                </tr>

                 <tr>
                    <td class="export-td">97</td>
                    <td class="export-td">attendance</td>
                    <td class="export-td">英:/ə'tend(ə)ns/ 美:/ə'tɛndəns/ </td>
                    <td class="export-td">n.出席，到场<br /><br />护理</td>
                </tr>

                 <tr>
                    <td class="export-td">98</td>
                    <td class="export-td">attachment</td>
                    <td class="export-td">英:/ə'tætʃm(ə)nt/ 美:/ə'tætʃmənt/ </td>
                    <td class="export-td">附件</td>
                </tr>

                 <tr>
                    <td class="export-td">99</td>
                    <td class="export-td">attached</td>
                    <td class="export-td">英:/əˈtætʃt/ 美:/ə'tætʃt/ </td>
                    <td class="export-td">1. adj. 附加的；依恋的，充满爱心的
    2. v. 附上（attach的过去分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">100</td>
                    <td class="export-td">ATM</td>
                    <td class="export-td">/ˌei ti: 'em/ </td>
                    <td class="export-td">abbr. 异步传输模式（Asynchronous Transfer Mode）；自动出纳机（Automatic Teller Machine）；空中交通管理（Air Traffic Management）</td>
                </tr>

                 <tr>
                    <td class="export-td">101</td>
                    <td class="export-td">athletic</td>
                    <td class="export-td">英:/æθ'letɪk/ 美:/æθ'lɛtɪk/ </td>
                    <td class="export-td">adj. 运动的，运动员的；体格健壮的</td>
                </tr>

                 <tr>
                    <td class="export-td">102</td>
                    <td class="export-td">ate</td>
                    <td class="export-td">英:/et/ 美:/ɛt/ </td>
                    <td class="export-td">v. 吃（eat的过去式）</td>
                </tr>

                 <tr>
                    <td class="export-td">103</td>
                    <td class="export-td">astronomer</td>
                    <td class="export-td">英:/ə'strɒnəmə/ 美:/ə'strɑnəmɚ/ </td>
                    <td class="export-td">天文学家</td>
                </tr>

                 <tr>
                    <td class="export-td">104</td>
                    <td class="export-td">astonishment</td>
                    <td class="export-td">英:/ə'stɒnɪʃmənt/ 美:/ə'stɑnɪʃmənt/ </td>
                    <td class="export-td">惊讶，令人惊讶的事</td>
                </tr>

                 <tr>
                    <td class="export-td">105</td>
                    <td class="export-td">astonishing</td>
                    <td class="export-td">英:/əsˈtɔnɪʃɪŋ/ 美:/ə'stɑnɪʃɪŋ/ </td>
                    <td class="export-td">惊人</td>
                </tr>

                 <tr>
                    <td class="export-td">106</td>
                    <td class="export-td">astonished</td>
                    <td class="export-td">/ə'stɑnɪʃt/ </td>
                    <td class="export-td">惊讶</td>
                </tr>

                 <tr>
                    <td class="export-td">107</td>
                    <td class="export-td">assistance</td>
                    <td class="export-td">英:/ə'sɪst(ə)ns/ 美:/ə'sɪstəns/ </td>
                    <td class="export-td">n. 援助，帮助；辅助设备</td>
                </tr>

                 <tr>
                    <td class="export-td">108</td>
                    <td class="export-td">assassinate</td>
                    <td class="export-td">英:/ə'sæsɪneɪt/ 美:/ə'sæsn'et/ </td>
                    <td class="export-td">暗杀</td>
                </tr>

                 <tr>
                    <td class="export-td">109</td>
                    <td class="export-td">aspirin</td>
                    <td class="export-td">英:/'æsp(ə)rɪn/ 美:/'æsprɪn/ </td>
                    <td class="export-td">n. 阿司匹林（解热镇痛药）</td>
                </tr>

                 <tr>
                    <td class="export-td">110</td>
                    <td class="export-td">asparagus</td>
                    <td class="export-td">英:/ə'spærəgəs/ 美:/ə'spærəgəs/ </td>
                    <td class="export-td">芦笋</td>
                </tr>

                 <tr>
                    <td class="export-td">111</td>
                    <td class="export-td">ashtray</td>
                    <td class="export-td">英:/'æʃtreɪ/ 美:/'æʃtre/ </td>
                    <td class="export-td">n. 烟灰缸</td>
                </tr>

                 <tr>
                    <td class="export-td">112</td>
                    <td class="export-td">ASAP</td>
                    <td class="export-td">/ˌei es ei 'pi:/ </td>
                    <td class="export-td">abbr. 尽快（As Soon As Possible）</td>
                </tr>

                 <tr>
                    <td class="export-td">113</td>
                    <td class="export-td">artichoke</td>
                    <td class="export-td">英:/'ɑːtɪtʃəʊk/ 美:/'ɑrtɪtʃok/ </td>
                    <td class="export-td">洋蓟，朝鲜蓟</td>
                </tr>

                 <tr>
                    <td class="export-td">114</td>
                    <td class="export-td">arms</td>
                    <td class="export-td">/a:mz/ </td>
                    <td class="export-td">1. n. 武器；纹章；臂（arm的复数）
    2. v. 武装；配备（arm的三单形式）</td>
                </tr>

                 <tr>
                    <td class="export-td">115</td>
                    <td class="export-td">armpit</td>
                    <td class="export-td">英:/'ɑːmpɪt/ 美:/'ɑrm'pɪt/ </td>
                    <td class="export-td">n. 腋窝</td>
                </tr>

                 <tr>
                    <td class="export-td">116</td>
                    <td class="export-td">armour</td>
                    <td class="export-td">英:/'ɑːmə/ 美:/ˈɑrmɚ/ </td>
                    <td class="export-td">n. 装甲；护面；盔甲</td>
                </tr>

                 <tr>
                    <td class="export-td">117</td>
                    <td class="export-td">armed</td>
                    <td class="export-td">英:/ɑːmd/ 美:/ɑrmd/ </td>
                    <td class="export-td">adj. 武装的；有扶手的；有防卫器官的（指动物）</td>
                </tr>

                 <tr>
                    <td class="export-td">118</td>
                    <td class="export-td">armchair</td>
                    <td class="export-td">英:/ɑːm'tʃeə/ 美:/'ɑrmtʃɛr/ </td>
                    <td class="export-td">n. 扶手椅</td>
                </tr>

                 <tr>
                    <td class="export-td">119</td>
                    <td class="export-td">are</td>
                    <td class="export-td">英:/ɑː/ 美:/ɚ/ </td>
                    <td class="export-td">1. v. 是（be的第二人称单复数现在式）
    2. n. 公亩</td>
                </tr>

                 <tr>
                    <td class="export-td">120</td>
                    <td class="export-td">aquarium</td>
                    <td class="export-td">英:/ə'kweərɪəm/ 美:/ə'kwɛrɪəm/ </td>
                    <td class="export-td">n. 水族馆；养鱼池；玻璃缸</td>
                </tr>

                 <tr>
                    <td class="export-td">121</td>
                    <td class="export-td">APP</td>
                    <td class="export-td">英:/æp/ 美:/æp/ </td>
                    <td class="export-td">abbr. 穿甲试验（Armor Piercing Proof）；应用（Application）</td>
                </tr>

                 <tr>
                    <td class="export-td">122</td>
                    <td class="export-td">anyplace</td>
                    <td class="export-td">英:/'enɪpleɪs/ 美:/'ɛnɪples/ </td>
                    <td class="export-td">adv. 任何地方</td>
                </tr>

                 <tr>
                    <td class="export-td">123</td>
                    <td class="export-td">antivirus</td>
                    <td class="export-td">英:/ˌænti'vaɪrəs/ 美:/ˌæntiˈvaɪrəs/ </td>
                    <td class="export-td">杀毒软件</td>
                </tr>

                 <tr>
                    <td class="export-td">124</td>
                    <td class="export-td">anticlockwise</td>
                    <td class="export-td">英:/æntɪ'klɒkwaɪz/ 美:/'æntɪ'klɑkwaɪz/ </td>
                    <td class="export-td">逆时针</td>
                </tr>

                 <tr>
                    <td class="export-td">125</td>
                    <td class="export-td">anticipation</td>
                    <td class="export-td">英:/æntɪsɪ'peɪʃ(ə)n/ 美:/æn,tɪsɪ'peʃən/ </td>
                    <td class="export-td">预期, 预料</td>
                </tr>

                 <tr>
                    <td class="export-td">126</td>
                    <td class="export-td">anti</td>
                    <td class="export-td">英:/'æntɪ/ 美:/'æntaɪ/ </td>
                    <td class="export-td">1. adj. 反对的
    2. n. 反对者，反对论者</td>
                </tr>

                 <tr>
                    <td class="export-td">127</td>
                    <td class="export-td">antelope</td>
                    <td class="export-td">英:/'æntɪləʊp/ 美:/'æntɪlop/ </td>
                    <td class="export-td">n. 羚羊；羚羊皮革</td>
                </tr>

                 <tr>
                    <td class="export-td">128</td>
                    <td class="export-td">anorak</td>
                    <td class="export-td">英:/'ænəræk/ 美:/'ænəræk/ </td>
                    <td class="export-td">n. 厚夹克；防水布；滑雪衫</td>
                </tr>

                 <tr>
                    <td class="export-td">129</td>
                    <td class="export-td">annoying</td>
                    <td class="export-td">英:/ə'nɒɪɪŋ/ 美:/ə'nɔɪɪŋ/ </td>
                    <td class="export-td">1. adj. 恼人的；讨厌的
    2. v. 骚扰（annoy的ing形式）</td>
                </tr>

                 <tr>
                    <td class="export-td">130</td>
                    <td class="export-td">annoyed</td>
                    <td class="export-td">英:/əˈnɔɪd/ 美:/ə'nɔɪd/ </td>
                    <td class="export-td">1. adj. 恼怒的；烦闷的
    2. v. 使烦恼；打扰（annoy的过去分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">131</td>
                    <td class="export-td">annoyance</td>
                    <td class="export-td">英:/ə'nɒɪəns/ 美:/ə'nɔɪəns/ </td>
                    <td class="export-td">烦恼</td>
                </tr>

                 <tr>
                    <td class="export-td">132</td>
                    <td class="export-td">announcement</td>
                    <td class="export-td">英:/ə'naʊnsm(ə)nt/ 美:/ə'naʊnsmənt/ </td>
                    <td class="export-td">通知,发表,宣布</td>
                </tr>

                 <tr>
                    <td class="export-td">133</td>
                    <td class="export-td">animation</td>
                    <td class="export-td">英:/ænɪ'meɪʃ(ə)n/ 美:/ˌænɪ'meʃən/ </td>
                    <td class="export-td">动画</td>
                </tr>

                 <tr>
                    <td class="export-td">134</td>
                    <td class="export-td">anesthetic</td>
                    <td class="export-td">英:/ˌænɪsˈθetɪk/ 美:/ˌænɪs'θɛtɪk/ </td>
                    <td class="export-td">麻醉剂, 麻药</td>
                </tr>

                 <tr>
                    <td class="export-td">135</td>
                    <td class="export-td">anaesthetic</td>
                    <td class="export-td">英:/ˌænis'θetik/ 美:/ˌænɪsˈθɛtɪk/ </td>
                    <td class="export-td">麻醉剂</td>
                </tr>

                 <tr>
                    <td class="export-td">136</td>
                    <td class="export-td">amusing</td>
                    <td class="export-td">英:/ə'mjuːzɪŋ/ 美:/ə'mjuzɪŋ/ </td>
                    <td class="export-td">1. adj. 有趣的，好玩的；引人发笑的
    2. v. 逗乐；打发；使…高兴（amuse的ing形式）</td>
                </tr>

                 <tr>
                    <td class="export-td">137</td>
                    <td class="export-td">amusement</td>
                    <td class="export-td">英:/ə'mjuːzm(ə)nt/ 美:/ə'mjuzmənt/ </td>
                    <td class="export-td">娱乐, 消遣</td>
                </tr>

                 <tr>
                    <td class="export-td">138</td>
                    <td class="export-td">amused</td>
                    <td class="export-td">/ə'mju:zd/ </td>
                    <td class="export-td">1. adj. 愉快的，顽皮的；被逗乐的
    2. v. 使欢乐；逗笑（amuse的过去分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">139</td>
                    <td class="export-td">amplifier</td>
                    <td class="export-td">英:/'æmplɪfaɪə/ 美:/'æmplɪfaɪɚ/ </td>
                    <td class="export-td">放大器, 扩音机</td>
                </tr>

                 <tr>
                    <td class="export-td">140</td>
                    <td class="export-td">amp</td>
                    <td class="export-td">英:/ˌeɪemˈpi:/ 美:/ˌeemˈpi/ </td>
                    <td class="export-td">1. abbr. 安培（ampere，电流强度的单位）；放大器（amplifier）
    2. n. [俚]电吉他</td>
                </tr>

                 <tr>
                    <td class="export-td">141</td>
                    <td class="export-td">amazing</td>
                    <td class="export-td">/ə'mezɪŋ/ </td>
                    <td class="export-td">1. adj. 令人惊异的
    2. v. 使吃惊（amaze的ing形式）</td>
                </tr>

                 <tr>
                    <td class="export-td">142</td>
                    <td class="export-td">amazement</td>
                    <td class="export-td">英:/ə'meɪzm(ə)nt/ 美:/ə'mezmənt/ </td>
                    <td class="export-td">惊愕, 惊异</td>
                </tr>

                 <tr>
                    <td class="export-td">143</td>
                    <td class="export-td">amazed</td>
                    <td class="export-td">/ə'meizd/ </td>
                    <td class="export-td">1. adj. 惊奇的，吃惊的
    2. v. 使…吃惊；把…弄糊涂（amaze的过去分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">144</td>
                    <td class="export-td">am</td>
                    <td class="export-td">英:/强 æm/ 美:/æm/ </td>
                    <td class="export-td">1. abbr. 调幅
    2. v. 是</td>
                </tr>

                 <tr>
                    <td class="export-td">145</td>
                    <td class="export-td">airmail</td>
                    <td class="export-td">英:/'eəmeɪl/ 美:/'ɛrmel/ </td>
                    <td class="export-td">航空邮件，航空邮政</td>
                </tr>

                 <tr>
                    <td class="export-td">146</td>
                    <td class="export-td">AIDS</td>
                    <td class="export-td">/edz/ </td>
                    <td class="export-td">abbr. 获得性免疫缺乏综合症；爱滋病（Acquired Immure Deficiency Syndrome）</td>
                </tr>

                 <tr>
                    <td class="export-td">147</td>
                    <td class="export-td">adverd</td>
                    <td class="export-td"></td>
                    <td class="export-td"></td>
                </tr>

                 <tr>
                    <td class="export-td">148</td>
                    <td class="export-td">accommodatometer</td>
                    <td class="export-td"></td>
                    <td class="export-td">调节计</td>
                </tr>

                 <tr>
                    <td class="export-td">149</td>
                    <td class="export-td">accommodationist</td>
                    <td class="export-td">英:/ə,kɑmə'deʃənɪst/ 美:/əˌkɑməˈdeʃənɪst/ </td>
                    <td class="export-td">妥协派</td>
                </tr>

                 <tr>
                    <td class="export-td">150</td>
                    <td class="export-td">accommodation</td>
                    <td class="export-td">英:/əkɒmə'deɪʃ(ə)n/ 美:/ə,kɑmə'deʃən/ </td>
                    <td class="export-td">住处,膳宿</td>
                </tr>

                 <tr>
                    <td class="export-td">151</td>
                    <td class="export-td">absord</td>
                    <td class="export-td"></td>
                    <td class="export-td"></td>
                </tr>

                 <tr>
                    <td class="export-td">152</td>
                    <td class="export-td">absentminded</td>
                    <td class="export-td">/'æbsənt'maindid/ </td>
                    <td class="export-td">恍惚</td>
                </tr>

                 <tr>
                    <td class="export-td">153</td>
                    <td class="export-td">BC</td>
                    <td class="export-td">/ˌbi: 'si:/ </td>
                    <td class="export-td">abbr. 公元前（Before Christ）</td>
                </tr>

                 <tr>
                    <td class="export-td">154</td>
                    <td class="export-td">boar</td>
                    <td class="export-td">英:/bɔː/ 美:/bɔr/ </td>
                    <td class="export-td">n. 野猪；（未阉的）公猪</td>
                </tr>

                 <tr>
                    <td class="export-td">155</td>
                    <td class="export-td">be</td>
                    <td class="export-td">英:/biː/ 美:/bi/ </td>
                    <td class="export-td">prep. 在，存在；是</td>
                </tr>

                 <tr>
                    <td class="export-td">156</td>
                    <td class="export-td">board</td>
                    <td class="export-td">英:/bɔːd/ 美:/bɔrd/ </td>
                    <td class="export-td">1. n. 木板；甲板；膳食；董事会
    2. vt. 用板盖上；上（飞机、车、船等）；给提供膳宿</td>
                </tr>

                 <tr>
                    <td class="export-td">157</td>
                    <td class="export-td">bra</td>
                    <td class="export-td">英:/brɑː/ 美:/brɑ/ </td>
                    <td class="export-td">n. 胸罩</td>
                </tr>

                 <tr>
                    <td class="export-td">158</td>
                    <td class="export-td">boarding</td>
                    <td class="export-td">英:/'bɔːdɪŋ/ 美:/'bɔrdɪŋ/ </td>
                    <td class="export-td">1. n. 木板；寄膳宿；上船
    2. adj. 供膳的</td>
                </tr>

                 <tr>
                    <td class="export-td">159</td>
                    <td class="export-td">black</td>
                    <td class="export-td">英:/blæk/ 美:/blæk/ </td>
                    <td class="export-td">黑色</td>
                </tr>

                 <tr>
                    <td class="export-td">160</td>
                    <td class="export-td">beach</td>
                    <td class="export-td">英:/biːtʃ/ 美:/bitʃ/ </td>
                    <td class="export-td">1. n. 海滩；湖滨
    2. vt. 将…拖上岸</td>
                </tr>

                 <tr>
                    <td class="export-td">161</td>
                    <td class="export-td">bracelet</td>
                    <td class="export-td">英:/'breɪslɪt/ 美:/'breslət/ </td>
                    <td class="export-td">n. 手镯</td>
                </tr>

                 <tr>
                    <td class="export-td">162</td>
                    <td class="export-td">bubble</td>
                    <td class="export-td">英:/'bʌb(ə)l/ 美:/'bʌbl/ </td>
                    <td class="export-td">1. n. 气泡，泡沫，泡状物；透明圆形罩，圆形顶
    2. vi. 沸腾，冒泡；发出气泡声</td>
                </tr>

                 <tr>
                    <td class="export-td">163</td>
                    <td class="export-td">ad</td>
                    <td class="export-td">/əd/ </td>
                    <td class="export-td">广告</td>
                </tr>

                 <tr>
                    <td class="export-td">164</td>
                    <td class="export-td">against</td>
                    <td class="export-td">英:/ə'genst/ 美:/ə'ɡɛnst/ </td>
                    <td class="export-td">1. prep. 反对，违反；靠；倚；防备
    2. adj. 对立的；不利的</td>
                </tr>

                 <tr>
                    <td class="export-td">165</td>
                    <td class="export-td">blackberry</td>
                    <td class="export-td">英:/'blækb(ə)rɪ/ 美:/'blæk'bɛri/ </td>
                    <td class="export-td">黑莓</td>
                </tr>

                 <tr>
                    <td class="export-td">166</td>
                    <td class="export-td">blackbird</td>
                    <td class="export-td">英:/'blækbɜːd/ 美:/'blækbɝd/ </td>
                    <td class="export-td">画眉, 燕八哥</td>
                </tr>

                 <tr>
                    <td class="export-td">167</td>
                    <td class="export-td">academic</td>
                    <td class="export-td">英:/ækə'demɪk/ 美:/ˌækə'dɛmɪk/ </td>
                    <td class="export-td">1. adj. 学院的；学术的；理论的
    2. n. 大学生，大学教师；学者</td>
                </tr>

                 <tr>
                    <td class="export-td">168</td>
                    <td class="export-td">a</td>
                    <td class="export-td">英:/ə/ 美:/e/ </td>
                    <td class="export-td">a   a<br /><br />一</td>
                </tr>

                 <tr>
                    <td class="export-td">169</td>
                    <td class="export-td">boast</td>
                    <td class="export-td">英:/bəʊst/ 美:/bost/ </td>
                    <td class="export-td">1. vt. 以有…而自豪；夸口说，自吹自擂说
    2. n. 自夸；值得夸耀的事物，引以为荣的事物</td>
                </tr>

                 <tr>
                    <td class="export-td">170</td>
                    <td class="export-td">blackcurrant</td>
                    <td class="export-td">/ˌblæk'kɝənt/ </td>
                    <td class="export-td">黑加仑</td>
                </tr>

                 <tr>
                    <td class="export-td">171</td>
                    <td class="export-td">brag</td>
                    <td class="export-td">英:/bræg/ 美:/bræɡ/ </td>
                    <td class="export-td">1. n. 吹牛，自夸
    2. vi. 吹牛，自夸</td>
                </tr>

                 <tr>
                    <td class="export-td">172</td>
                    <td class="export-td">boat</td>
                    <td class="export-td">英:/bəʊt/ 美:/bot/ </td>
                    <td class="export-td">1. n. 小船；轮船
    2. vi. 划船</td>
                </tr>

                 <tr>
                    <td class="export-td">173</td>
                    <td class="export-td">beak</td>
                    <td class="export-td">英:/biːk/ 美:/bik/ </td>
                    <td class="export-td">n. 鸟嘴；鹰钩鼻子；地方执法官；男教师</td>
                </tr>

                 <tr>
                    <td class="export-td">174</td>
                    <td class="export-td">baby</td>
                    <td class="export-td">英:/'beɪbɪ/ 美:/'bebi/ </td>
                    <td class="export-td">1. n. 婴儿，婴孩；孩子气的人
    2. vt. 纵容，娇纵；把……当婴儿般对待</td>
                </tr>

                 <tr>
                    <td class="export-td">175</td>
                    <td class="export-td">bucket</td>
                    <td class="export-td">英:/'bʌkɪt/ 美:/'bʌkɪt/ </td>
                    <td class="export-td">1. n. 铲斗；桶，水桶；一桶的量
    2. v. 倾盆而下；颠簸着行进</td>
                </tr>

                 <tr>
                    <td class="export-td">176</td>
                    <td class="export-td">braid</td>
                    <td class="export-td">英:/breɪd/ 美:/bred/ </td>
                    <td class="export-td">1. vt. 编织
    2. n. 辫子；穗带；发辫</td>
                </tr>

                 <tr>
                    <td class="export-td">177</td>
                    <td class="export-td">Braille</td>
                    <td class="export-td">英:/breil/ 美:/brel/ </td>
                    <td class="export-td">1. vt. 用盲字印
    2. n. 布莱叶（法国盲人教育家）；盲人用点字法</td>
                </tr>

                 <tr>
                    <td class="export-td">178</td>
                    <td class="export-td">beam</td>
                    <td class="export-td">英:/biːm/ 美:/bim/ </td>
                    <td class="export-td">1. n. 横梁；船宽；电波；光线；秤杆
    2. vt. 以梁支撑；用…照射；流露；发送</td>
                </tr>

                 <tr>
                    <td class="export-td">179</td>
                    <td class="export-td">accelerator</td>
                    <td class="export-td">英:/ək'seləreɪtə/ 美:/ək'sɛlə'retɚ/ </td>
                    <td class="export-td">加速器</td>
                </tr>

                 <tr>
                    <td class="export-td">180</td>
                    <td class="export-td">buckle</td>
                    <td class="export-td">英:/ˈbʌkl/ 美:/ˈbʌkəl/ </td>
                    <td class="export-td">1. vi. 扣住；变弯曲
    2. vt. 扣住；使弯曲</td>
                </tr>

                 <tr>
                    <td class="export-td">181</td>
                    <td class="export-td">accent</td>
                    <td class="export-td">英:/'æks(ə)nt/ 美:/'æksɛnt/ </td>
                    <td class="export-td">1. n. 口音；重音；重音符号；强调；特点
    2. vt. 重读；强调；带…口音讲话</td>
                </tr>

                 <tr>
                    <td class="export-td">182</td>
                    <td class="export-td">black hole</td>
                    <td class="export-td"></td>
                    <td class="export-td">黑洞</td>
                </tr>

                 <tr>
                    <td class="export-td">183</td>
                    <td class="export-td">brainy</td>
                    <td class="export-td">英:/'breɪnɪ/ 美:/'breni/ </td>
                    <td class="export-td">adj. 聪明的；脑筋好的；有头脑的</td>
                </tr>

                 <tr>
                    <td class="export-td">184</td>
                    <td class="export-td">bean</td>
                    <td class="export-td">英:/biːn/ 美:/bin/ </td>
                    <td class="export-td">1. n. 豆；[动]嘴峰；[美口]毫无价值的东西
    2. vt. [美口]击…的头部</td>
                </tr>

                 <tr>
                    <td class="export-td">185</td>
                    <td class="export-td">accept</td>
                    <td class="export-td">英:/ək'sept/ 美:/ək'sɛpt/ </td>
                    <td class="export-td">1. vt. 接受；承认；承担；承兑；容纳
    2. vi. 同意；承认；承兑</td>
                </tr>

                 <tr>
                    <td class="export-td">186</td>
                    <td class="export-td">acceptable</td>
                    <td class="export-td">英:/ək'septəb(ə)l/ 美:/ək'sɛptəbl/ </td>
                    <td class="export-td">接受</td>
                </tr>

                 <tr>
                    <td class="export-td">187</td>
                    <td class="export-td">bob</td>
                    <td class="export-td">英:/bɒb/ 美:/bɑb/ </td>
                    <td class="export-td">1. n. 短发；浮子；摆动；轻敲；悬挂的饰品
    2. vt. 剪短；敲击；使上下快速摆动</td>
                </tr>

                 <tr>
                    <td class="export-td">188</td>
                    <td class="export-td">bear</td>
                    <td class="export-td">英:/beə/ 美:/bɛr/ </td>
                    <td class="export-td">1. vi. 结果实；承受
    2. vt. 忍受；具有；支撑</td>
                </tr>

                 <tr>
                    <td class="export-td">189</td>
                    <td class="export-td">addict</td>
                    <td class="export-td">英:/'ædɪkt/ 美:/'ædɪkt/ </td>
                    <td class="export-td">1. n. 有瘾的人；入迷的人
    2. vt. 使沉溺；使上瘾</td>
                </tr>

                 <tr>
                    <td class="export-td">190</td>
                    <td class="export-td">acceptance</td>
                    <td class="export-td">英:/ək'sept(ə)ns/ 美:/ək'sɛptəns/ </td>
                    <td class="export-td">接受 ，同意，认可</td>
                </tr>

                 <tr>
                    <td class="export-td">191</td>
                    <td class="export-td">aback</td>
                    <td class="export-td">英:/ə'bæk/ 美:/ə'bæk/ </td>
                    <td class="export-td">adv. 向后；处于顶风位置；向后地</td>
                </tr>

                 <tr>
                    <td class="export-td">192</td>
                    <td class="export-td">bud</td>
                    <td class="export-td">英:/bʌd/ 美:/bʌd/ </td>
                    <td class="export-td">1. n. 芽，萌芽；蓓蕾
    2. vi. 发芽，萌芽</td>
                </tr>

                 <tr>
                    <td class="export-td">193</td>
                    <td class="export-td">Buddhism</td>
                    <td class="export-td">英:/'bʊdɪz(ə)m/ 美:/'bʊdɪzəm/ </td>
                    <td class="export-td">n. 佛教</td>
                </tr>

                 <tr>
                    <td class="export-td">194</td>
                    <td class="export-td">access</td>
                    <td class="export-td">英:/'ækses/ 美:/'æksɛs/ </td>
                    <td class="export-td">1. vt. 存取；接近；使用
    2. n. 通路；进入；使用权</td>
                </tr>

                 <tr>
                    <td class="export-td">195</td>
                    <td class="export-td">buddhist</td>
                    <td class="export-td">/'budist/ </td>
                    <td class="export-td">1. n. 佛教徒
    2. adj. 佛教的</td>
                </tr>

                 <tr>
                    <td class="export-td">196</td>
                    <td class="export-td">budge</td>
                    <td class="export-td">英:/bʌdʒ/ 美:/bʌdʒ/ </td>
                    <td class="export-td">1. vi. 挪动；微微移动；改变态度或意见；服从
    2. vt. 移动；使改变态度或意见；使让步</td>
                </tr>

                 <tr>
                    <td class="export-td">197</td>
                    <td class="export-td">abandon</td>
                    <td class="export-td">英:/ə'bænd(ə)n/ 美:/ə'bændən/ </td>
                    <td class="export-td">1. n. 狂热，放任
    2. vt. 遗弃，放弃</td>
                </tr>

                 <tr>
                    <td class="export-td">198</td>
                    <td class="export-td">budget</td>
                    <td class="export-td">英:/'bʌdʒɪt/ 美:/'bʌdʒɪt/ </td>
                    <td class="export-td">1. n. 预算，预算费
    2. vt. 安排，预定；把…编入预算</td>
                </tr>

                 <tr>
                    <td class="export-td">199</td>
                    <td class="export-td">brake</td>
                    <td class="export-td">英:/breɪk/ 美:/brek/ </td>
                    <td class="export-td">1. vi. 刹车
    2. n. 闸，刹车；阻碍</td>
                </tr>

                 <tr>
                    <td class="export-td">200</td>
                    <td class="export-td">beard</td>
                    <td class="export-td">英:/bɪəd/ 美:/bɪrd/ </td>
                    <td class="export-td">1. vt. 公然反对；抓…的胡须
    2. n. 胡须；颌毛</td>
                </tr>

                 <tr>
                    <td class="export-td">201</td>
                    <td class="export-td">accident</td>
                    <td class="export-td">英:/'æksɪdənt/ 美:/'æksədənt/ </td>
                    <td class="export-td">n. 事故；机遇；意外事件；意外</td>
                </tr>

                 <tr>
                    <td class="export-td">202</td>
                    <td class="export-td">bachelor</td>
                    <td class="export-td">英:/'bætʃələ/ 美:/'bætʃəlɚ/ </td>
                    <td class="export-td">n. 单身汉；学士；（尚未交配的）小雄兽</td>
                </tr>

                 <tr>
                    <td class="export-td">203</td>
                    <td class="export-td">back</td>
                    <td class="export-td">英:/bæk/ 美:/bæk/ </td>
                    <td class="export-td">1. n. 背部；后面；靠背；足球等的后卫；书报等的末尾
    2. vt. 支持；后退；下赌注；背书</td>
                </tr>

                 <tr>
                    <td class="export-td">204</td>
                    <td class="export-td">accidental</td>
                    <td class="export-td">英:/æksɪ'dent(ə)l/ 美:/ˌæksɪ'dɛntl/ </td>
                    <td class="export-td">偶然</td>
                </tr>

                 <tr>
                    <td class="export-td">205</td>
                    <td class="export-td">beast</td>
                    <td class="export-td">英:/biːst/ 美:/bist/ </td>
                    <td class="export-td">n. 野兽；畜生，人面兽心的人</td>
                </tr>

                 <tr>
                    <td class="export-td">206</td>
                    <td class="export-td">buffalo</td>
                    <td class="export-td">英:/ˈbʌfələu/ 美:/ˈbʌfəˌlo/ </td>
                    <td class="export-td">n. 水牛；野牛（产于北美）；水陆两用坦克</td>
                </tr>

                 <tr>
                    <td class="export-td">207</td>
                    <td class="export-td">accidentally</td>
                    <td class="export-td">英:/ˌæksɪˈdentəlɪ/ 美:/ˌæksə'dɛntli/ </td>
                    <td class="export-td">偶然地, 意外地</td>
                </tr>

                 <tr>
                    <td class="export-td">208</td>
                    <td class="export-td">body</td>
                    <td class="export-td">英:/'bɒdɪ/ 美:/'bɑdi/ </td>
                    <td class="export-td">1. n. 身体；主体；团体；主要部分；大量
    2. vt. 赋以形体</td>
                </tr>

                 <tr>
                    <td class="export-td">209</td>
                    <td class="export-td">backbone</td>
                    <td class="export-td">英:/'bækbəʊn/ 美:/'bæk'bon/ </td>
                    <td class="export-td">n. 决心，毅力；支柱；脊椎；[计]主干网</td>
                </tr>

                 <tr>
                    <td class="export-td">210</td>
                    <td class="export-td">beat</td>
                    <td class="export-td">英:/biːt/ 美:/bit/ </td>
                    <td class="export-td">1. vt. 打；打败
    2. vi. 打；打败；拍打；有节奏地舒张与收缩</td>
                </tr>

                 <tr>
                    <td class="export-td">211</td>
                    <td class="export-td">buffet</td>
                    <td class="export-td">英:/'bʊfeɪ/ 美:/bə'fe/ </td>
                    <td class="export-td">1. n. 打击；小卖部；猛烈冲击；自助餐
    2. vt. 与…搏斗；连续猛击</td>
                </tr>

                 <tr>
                    <td class="export-td">212</td>
                    <td class="export-td">backpack</td>
                    <td class="export-td">英:/'bækpæk/ 美:/'bæk'pæk/ </td>
                    <td class="export-td">1. n. 远足用的背包；双肩背包，背包
    2. vt. 挑运；把…放入背包</td>
                </tr>

                 <tr>
                    <td class="export-td">213</td>
                    <td class="export-td">branch</td>
                    <td class="export-td">英:/brɑːn(t)ʃ/ 美:/bræntʃ/ </td>
                    <td class="export-td">1. vt. 分支；出现分歧
    2. vi. 分支；出现分歧</td>
                </tr>

                 <tr>
                    <td class="export-td">214</td>
                    <td class="export-td">brand</td>
                    <td class="export-td">英:/brænd/ 美:/brænd/ </td>
                    <td class="export-td">1. vt. 打烙印于；印…商标于；铭刻于，铭记
    2. n. 商标，牌子；烙印</td>
                </tr>

                 <tr>
                    <td class="export-td">215</td>
                    <td class="export-td">abbey</td>
                    <td class="export-td">英:/ˈæbi/ 美:/ˈæbi/ </td>
                    <td class="export-td">n. 大修道院，大寺院；修道院中全体修士或修女</td>
                </tr>

                 <tr>
                    <td class="export-td">216</td>
                    <td class="export-td">bug</td>
                    <td class="export-td">英:/bʌg/ 美:/bʌɡ/ </td>
                    <td class="export-td">1. n. 臭虫，小虫；窃听器；故障
    2. vt. 烦扰，打扰；装窃听器</td>
                </tr>

                 <tr>
                    <td class="export-td">217</td>
                    <td class="export-td">brandy</td>
                    <td class="export-td">英:/'brændɪ/ 美:/'brændi/ </td>
                    <td class="export-td">n. 白兰地酒</td>
                </tr>

                 <tr>
                    <td class="export-td">218</td>
                    <td class="export-td">backstroke</td>
                    <td class="export-td">英:/'bækstrəʊk/ 美:/'bæk'strok/ </td>
                    <td class="export-td">仰泳</td>
                </tr>

                 <tr>
                    <td class="export-td">219</td>
                    <td class="export-td">bodyguard</td>
                    <td class="export-td">英:/'bɒdɪgɑːd/ 美:/'bɑdɪɡɑrd/ </td>
                    <td class="export-td">保镖</td>
                </tr>

                 <tr>
                    <td class="export-td">220</td>
                    <td class="export-td">blackmail</td>
                    <td class="export-td">英:/'blækmeɪl/ 美:/'blækmel/ </td>
                    <td class="export-td">勒索; 勒索，讹诈</td>
                </tr>

                 <tr>
                    <td class="export-td">221</td>
                    <td class="export-td">brass</td>
                    <td class="export-td">英:/brɑːs/ 美:/bræs/ </td>
                    <td class="export-td">n. 黄铜；黄铜制品；厚脸皮；铜管乐器</td>
                </tr>

                 <tr>
                    <td class="export-td">222</td>
                    <td class="export-td">buggy</td>
                    <td class="export-td">英:/'bʌgɪ/ 美:/'bʌɡi/ </td>
                    <td class="export-td">1. n. 双轮单座轻马车；童车
    2. adj. 多虫的</td>
                </tr>

                 <tr>
                    <td class="export-td">223</td>
                    <td class="export-td">blacksmith</td>
                    <td class="export-td">英:/'blæksmɪθ/ 美:/'blæksmɪθ/ </td>
                    <td class="export-td">铁匠</td>
                </tr>

                 <tr>
                    <td class="export-td">224</td>
                    <td class="export-td">blade</td>
                    <td class="export-td">英:/bleɪd/ 美:/bled/ </td>
                    <td class="export-td">n. 刀片，刀锋；叶片；剑</td>
                </tr>

                 <tr>
                    <td class="export-td">225</td>
                    <td class="export-td">build</td>
                    <td class="export-td">英:/bɪld/ 美:/bɪld/ </td>
                    <td class="export-td">1. vt. 建筑；建立
    2. vi. 建筑；建造</td>
                </tr>

                 <tr>
                    <td class="export-td">226</td>
                    <td class="export-td">builder</td>
                    <td class="export-td">英:/'bɪldə/ 美:/'bɪldɚ/ </td>
                    <td class="export-td">n. 建筑者；建立者</td>
                </tr>

                 <tr>
                    <td class="export-td">227</td>
                    <td class="export-td">built</td>
                    <td class="export-td">英:/bɪlt/ 美:/bɪlt/ </td>
                    <td class="export-td">1. v. 建造（build的过去分词）
    2. adj. 身段优美的；…建成的</td>
                </tr>

                 <tr>
                    <td class="export-td">228</td>
                    <td class="export-td">blame</td>
                    <td class="export-td">英:/bleɪm/ 美:/blem/ </td>
                    <td class="export-td">1. vt. 责备；归咎于
    2. n. 责备；过失；责任</td>
                </tr>

                 <tr>
                    <td class="export-td">229</td>
                    <td class="export-td">beautician</td>
                    <td class="export-td">英:/bjuː'tɪʃ(ə)n/ 美:/bjuˈtɪʃən/ </td>
                    <td class="export-td">美容师</td>
                </tr>

                 <tr>
                    <td class="export-td">230</td>
                    <td class="export-td">building</td>
                    <td class="export-td">英:/'bɪldɪŋ/ 美:/'bɪldɪŋ/ </td>
                    <td class="export-td">1. n. 建筑；建筑物
    2. v. 建筑；建立；增加（build的ing形式）</td>
                </tr>

                 <tr>
                    <td class="export-td">231</td>
                    <td class="export-td">beautiful</td>
                    <td class="export-td">英:/'bjuːtɪfʊl/ 美:/'bjʊtəfəl/ </td>
                    <td class="export-td">美丽的, 漂亮的</td>
                </tr>

                 <tr>
                    <td class="export-td">232</td>
                    <td class="export-td">backside</td>
                    <td class="export-td">英:/bæk'saɪd/ 美:/'bæksaɪd/ </td>
                    <td class="export-td">n. 背部；后方；臀部</td>
                </tr>

                 <tr>
                    <td class="export-td">233</td>
                    <td class="export-td">bulb</td>
                    <td class="export-td">英:/bʌlb/ 美:/bʌlb/ </td>
                    <td class="export-td">1. n. 电灯泡；球状物；[植]鳞茎
    2. vi. 生球茎；膨胀成球状</td>
                </tr>

                 <tr>
                    <td class="export-td">234</td>
                    <td class="export-td">bland</td>
                    <td class="export-td">英:/blænd/ 美:/blænd/ </td>
                    <td class="export-td">1. adj. 乏味的；冷漠的；温和的
    2. vt. 使…变得淡而无味；除掉…的特性</td>
                </tr>

                 <tr>
                    <td class="export-td">235</td>
                    <td class="export-td">boil</td>
                    <td class="export-td">英:/bɒɪl/ 美:/bɔɪl/ </td>
                    <td class="export-td">1. vi. 煮沸，沸腾；激动，激昂
    2. vt. 煮沸，烧开；使…激动；使…蒸发</td>
                </tr>

                 <tr>
                    <td class="export-td">236</td>
                    <td class="export-td">boiling</td>
                    <td class="export-td">英:/'bɒɪlɪŋ/ 美:/'bɔɪlɪŋ/ </td>
                    <td class="export-td">1. adj. 沸腾的；激昂的
    2. n. 煮沸；沸腾；起泡</td>
                </tr>

                 <tr>
                    <td class="export-td">237</td>
                    <td class="export-td">bulge</td>
                    <td class="export-td">英:/bʌldʒ/ 美:/bʌldʒ/ </td>
                    <td class="export-td">1. n. 胀；膨胀；凸出部分
    2. vt. 使膨胀；使凸起</td>
                </tr>

                 <tr>
                    <td class="export-td">238</td>
                    <td class="export-td">brave</td>
                    <td class="export-td">英:/breɪv/ 美:/brev/ </td>
                    <td class="export-td">1. adj. 勇敢的；华丽的
    2. vt. 勇敢地面对</td>
                </tr>

                 <tr>
                    <td class="export-td">239</td>
                    <td class="export-td">beauty</td>
                    <td class="export-td">英:/'bjuːtɪ/ 美:/'bjuti/ </td>
                    <td class="export-td">n. 美；美人；美好的东西；美丽</td>
                </tr>

                 <tr>
                    <td class="export-td">240</td>
                    <td class="export-td">ability</td>
                    <td class="export-td">英:/ə'bɪlɪtɪ/ 美:/ə'bɪləti/ </td>
                    <td class="export-td">n. 能力，能耐；才能</td>
                </tr>

                 <tr>
                    <td class="export-td">241</td>
                    <td class="export-td">backyard</td>
                    <td class="export-td">英:/bæk'jɑːd/ 美:/ˌbæk'jɑrd/ </td>
                    <td class="export-td">n. 后院；后庭</td>
                </tr>

                 <tr>
                    <td class="export-td">242</td>
                    <td class="export-td">blank</td>
                    <td class="export-td">英:/blæŋk/ 美:/blæŋk/ </td>
                    <td class="export-td">1. adj. 空白的；空虚的；单调的
    2. n. 空白；空白表格；空虚</td>
                </tr>

                 <tr>
                    <td class="export-td">243</td>
                    <td class="export-td">bulky</td>
                    <td class="export-td">英:/'bʌlkɪ/ 美:/'bʌlki/ </td>
                    <td class="export-td">adj. 庞大的；体积大的；笨重的</td>
                </tr>

                 <tr>
                    <td class="export-td">244</td>
                    <td class="export-td">boiler</td>
                    <td class="export-td">英:/'bɒɪlə/ 美:/'bɔɪlɚ/ </td>
                    <td class="export-td">n. 锅炉；盛热水器；烧水壶，热水器</td>
                </tr>

                 <tr>
                    <td class="export-td">245</td>
                    <td class="export-td">bull</td>
                    <td class="export-td">英:/bʊl/ 美:/bʊl/ </td>
                    <td class="export-td">1. n. 公牛；看好股市者；粗壮如牛的人；[俚]胡说八道；印玺
    2. adj. 公牛似的；雄性的；大型的</td>
                </tr>

                 <tr>
                    <td class="export-td">246</td>
                    <td class="export-td">blanket</td>
                    <td class="export-td">英:/'blæŋkɪt/ 美:/'blæŋkɪt/ </td>
                    <td class="export-td">1. n. 毛毯，毯子；毯状物，覆盖层
    2. adj. 总括的，全体的；没有限制的</td>
                </tr>

                 <tr>
                    <td class="export-td">247</td>
                    <td class="export-td">able</td>
                    <td class="export-td">英:/'eɪb(ə)l/ 美:/'ebl/ </td>
                    <td class="export-td">adj. 能干的；有能力的；能</td>
                </tr>

                 <tr>
                    <td class="export-td">248</td>
                    <td class="export-td">bold</td>
                    <td class="export-td">英:/bəʊld/ 美:/bold/ </td>
                    <td class="export-td">adj. 大胆的，英勇的；厚颜无耻的；险峻的；黑体的</td>
                </tr>

                 <tr>
                    <td class="export-td">249</td>
                    <td class="export-td">boldly</td>
                    <td class="export-td">/'bəuldli/ </td>
                    <td class="export-td">adv. 大胆地；冒失地；显眼地</td>
                </tr>

                 <tr>
                    <td class="export-td">250</td>
                    <td class="export-td">because</td>
                    <td class="export-td">英:/bɪ'kɒz/ 美:/bɪ'kɔz/ </td>
                    <td class="export-td">conj. 因为</td>
                </tr>

                 <tr>
                    <td class="export-td">251</td>
                    <td class="export-td">beckon</td>
                    <td class="export-td">英:/'bek(ə)n/ 美:/'bɛkən/ </td>
                    <td class="export-td">1. vt. 召唤；吸引
    2. vi. （招手或点头）示意；吸引</td>
                </tr>

                 <tr>
                    <td class="export-td">252</td>
                    <td class="export-td">administration</td>
                    <td class="export-td">英:/ədmɪnɪ'streɪʃ(ə)n/ 美:/əd,mɪnɪ'streʃən/ </td>
                    <td class="export-td">行政,管理,行政部门</td>
                </tr>

                 <tr>
                    <td class="export-td">253</td>
                    <td class="export-td">bed</td>
                    <td class="export-td">英:/bed/ 美:/bɛd/ </td>
                    <td class="export-td">1. n. 床；基础；河底， 海底
    2. vt. 使睡觉；安置，嵌入；栽种</td>
                </tr>

                 <tr>
                    <td class="export-td">254</td>
                    <td class="export-td">abnormal</td>
                    <td class="export-td">英:/əb'nɔːm(ə)l/ 美:/æb'nɔrml/ </td>
                    <td class="export-td">adj. 反常的，不规则的；变态的</td>
                </tr>

                 <tr>
                    <td class="export-td">255</td>
                    <td class="export-td">blast</td>
                    <td class="export-td">英:/blɑːst/ 美:/blæst/ </td>
                    <td class="export-td">1. n. 爆炸；冲击波；一阵
    2. vi. 猛攻</td>
                </tr>

                 <tr>
                    <td class="export-td">256</td>
                    <td class="export-td">bedclothes</td>
                    <td class="export-td">英:/'bedkləʊðz/ 美:/ˈbɛdˌkloz/ </td>
                    <td class="export-td">铺盖, 床单被褥类</td>
                </tr>

                 <tr>
                    <td class="export-td">257</td>
                    <td class="export-td">bread</td>
                    <td class="export-td">英:/bred/ 美:/brɛd/ </td>
                    <td class="export-td">1. n. 生计；面包
    2. vt. 在…上洒面包屑</td>
                </tr>

                 <tr>
                    <td class="export-td">258</td>
                    <td class="export-td">aboard</td>
                    <td class="export-td">英:/ə'bɔːd/ 美:/ə'bɔrd/ </td>
                    <td class="export-td">1. adv. 在火车上；在飞机上；在船上
    2. prep. 在…上</td>
                </tr>

                 <tr>
                    <td class="export-td">259</td>
                    <td class="export-td">bulldozer</td>
                    <td class="export-td">英:/'bʊldəʊzə/ 美:/'bʊl'dozɚ/ </td>
                    <td class="export-td">推土机; 欺凌者</td>
                </tr>

                 <tr>
                    <td class="export-td">260</td>
                    <td class="export-td">bullet</td>
                    <td class="export-td">英:/'bʊlɪt/ 美:/'bʊlɪt/ </td>
                    <td class="export-td">1. n. 子弹；只选某党全部候选人的投票；[美俚]豆子
    2. vi. 射出；迅速行进</td>
                </tr>

                 <tr>
                    <td class="export-td">261</td>
                    <td class="export-td">abolish</td>
                    <td class="export-td">英:/ə'bɒlɪʃ/ 美:/ə'bɑlɪʃ/ </td>
                    <td class="export-td">vt. 废除，废止；取消，革除</td>
                </tr>

                 <tr>
                    <td class="export-td">262</td>
                    <td class="export-td">background</td>
                    <td class="export-td">英:/ˈbækɡraund/ 美:/'bækɡraʊnd/ </td>
                    <td class="export-td">背景,幕后,配音</td>
                </tr>

                 <tr>
                    <td class="export-td">263</td>
                    <td class="export-td">abolition</td>
                    <td class="export-td">英:/æbə'lɪʃ(ə)n/ 美:/ˌæbə'lɪʃən/ </td>
                    <td class="export-td">废除, 废止</td>
                </tr>

                 <tr>
                    <td class="export-td">264</td>
                    <td class="export-td">bacon</td>
                    <td class="export-td">英:/ˈbeɪkən/ 美:/ˈbekən/ </td>
                    <td class="export-td">n. 熏猪肉；咸肉；腌肉</td>
                </tr>

                 <tr>
                    <td class="export-td">265</td>
                    <td class="export-td">bacteria</td>
                    <td class="export-td">英:/bæk'tɪərɪə/ 美:/bæk'tɪrɪə/ </td>
                    <td class="export-td">n. 细菌</td>
                </tr>

                 <tr>
                    <td class="export-td">266</td>
                    <td class="export-td">bedroom</td>
                    <td class="export-td">英:/'bedruːm/ 美:/'bɛdrum/ </td>
                    <td class="export-td">1. n. 卧室
    2. adj. 两性关系的；城郊住宅区的</td>
                </tr>

                 <tr>
                    <td class="export-td">267</td>
                    <td class="export-td">bolt</td>
                    <td class="export-td">英:/bəʊlt/ 美:/bolt/ </td>
                    <td class="export-td">1. n. 闪电；螺栓；门闩；弩箭
    2. vt. 囫囵吞下；上门闩</td>
                </tr>

                 <tr>
                    <td class="export-td">268</td>
                    <td class="export-td">bedside</td>
                    <td class="export-td">英:/'bedsaɪd/ 美:/'bɛd'saɪd/ </td>
                    <td class="export-td">1. n. 床边，床旁
    2. adj. 床旁的，枕边的</td>
                </tr>

                 <tr>
                    <td class="export-td">269</td>
                    <td class="export-td">blaze</td>
                    <td class="export-td">英:/bleɪz/ 美:/blez/ </td>
                    <td class="export-td">1. vt. 在树皮上刻路标；公开宣布
    2. n. 火焰，烈火；光辉；情感爆发</td>
                </tr>

                 <tr>
                    <td class="export-td">270</td>
                    <td class="export-td">bedspread</td>
                    <td class="export-td">英:/'bedspred/ 美:/'bɛdsprɛd/ </td>
                    <td class="export-td">床单, 床罩</td>
                </tr>

                 <tr>
                    <td class="export-td">271</td>
                    <td class="export-td">bad</td>
                    <td class="export-td">英:/bæd/ 美:/bæd/ </td>
                    <td class="export-td">1. adj. 坏的；严重的；劣质的
    2. n. 坏人；坏事</td>
                </tr>

                 <tr>
                    <td class="export-td">272</td>
                    <td class="export-td">break</td>
                    <td class="export-td">英:/breɪk/ 美:/brek/ </td>
                    <td class="export-td">1. n. 休息，中断；破裂处
    2. vt. 打破，弄破；中断；弄坏；削弱</td>
                </tr>

                 <tr>
                    <td class="export-td">273</td>
                    <td class="export-td">badly</td>
                    <td class="export-td">英:/'bædlɪ/ 美:/'bædli/ </td>
                    <td class="export-td">adv. 严重地，厉害地；恶劣地；非常，很</td>
                </tr>

                 <tr>
                    <td class="export-td">274</td>
                    <td class="export-td">blazer</td>
                    <td class="export-td">英:/'bleɪzə/ 美:/'blezɚ/ </td>
                    <td class="export-td">n. 燃烧体；宣布者；颜色鲜明的运动上衣</td>
                </tr>

                 <tr>
                    <td class="export-td">275</td>
                    <td class="export-td">bedtime</td>
                    <td class="export-td">英:/'bedtaɪm/ 美:/'bɛdtaɪm/ </td>
                    <td class="export-td">1. n. 就寝时间
    2. adj. 适于睡前的</td>
                </tr>

                 <tr>
                    <td class="export-td">276</td>
                    <td class="export-td">bully</td>
                    <td class="export-td">英:/'bʊlɪ/ 美:/'bʊli/ </td>
                    <td class="export-td">1. n. 欺凌弱小者；土霸
    2. adj. [口]第一流的；特好的</td>
                </tr>

                 <tr>
                    <td class="export-td">277</td>
                    <td class="export-td">bum</td>
                    <td class="export-td">英:/bʌm/ 美:/bʌm/ </td>
                    <td class="export-td">1. n. 流浪汉；狂欢作乐；能力差的人；嗡嗡声；屁股；[贬]执达员（等于bumbailiff）
    2. vi. 流浪；靠乞讨过活；发嗡嗡声</td>
                </tr>

                 <tr>
                    <td class="export-td">278</td>
                    <td class="export-td">bad-tempered</td>
                    <td class="export-td">英:/'bæd,tempəd/ 美:/ bædˈtɛmpɚd/ </td>
                    <td class="export-td">易怒的</td>
                </tr>

                 <tr>
                    <td class="export-td">279</td>
                    <td class="export-td">about</td>
                    <td class="export-td">英:/ə'baʊt/ 美:/ə'baʊt/ </td>
                    <td class="export-td">1. prep. 关于；大约
    2. adj. 四处走动的；在起作用的；在附近的</td>
                </tr>

                 <tr>
                    <td class="export-td">280</td>
                    <td class="export-td">bleak</td>
                    <td class="export-td">英:/bliːk/ 美:/blik/ </td>
                    <td class="export-td">adj. 荒凉的，无遮蔽的；阴冷的；黯淡的，无希望的；冷酷的；单调的</td>
                </tr>

                 <tr>
                    <td class="export-td">281</td>
                    <td class="export-td">above</td>
                    <td class="export-td">英:/ə'bʌv/ 美:/ə'bʌv/ </td>
                    <td class="export-td">1. prep. 在……上面；在……之上；超过
    2. adv. 在上面；在上文</td>
                </tr>

                 <tr>
                    <td class="export-td">282</td>
                    <td class="export-td">badge</td>
                    <td class="export-td">英:/bædʒ/ 美:/bædʒ/ </td>
                    <td class="export-td">1. n. 徽章；标记；证章
    2. vt. 授给…徽章</td>
                </tr>

                 <tr>
                    <td class="export-td">283</td>
                    <td class="export-td">baptize</td>
                    <td class="export-td">英:/bæpˈtaɪz/ 美:/bæp'taɪz/ </td>
                    <td class="export-td">baptise<br /><br />1. vt. 给…施浸礼；命名；使经受考验（等于baptise）
    2. vi. 施行洗礼（等于baptise）</td>
                </tr>

                 <tr>
                    <td class="export-td">284</td>
                    <td class="export-td">badger</td>
                    <td class="export-td">英:/'bædʒə/ 美:/'bædʒɚ/ </td>
                    <td class="export-td">n. 獾；獾皮毛</td>
                </tr>

                 <tr>
                    <td class="export-td">285</td>
                    <td class="export-td">bee</td>
                    <td class="export-td">英:/biː/ 美:/bi/ </td>
                    <td class="export-td">n. 蜜蜂，蜂；勤劳的人</td>
                </tr>

                 <tr>
                    <td class="export-td">286</td>
                    <td class="export-td">beehive</td>
                    <td class="export-td">英:/'biːhaɪv/ 美:/'bihaɪv/ </td>
                    <td class="export-td">n. 蜂窝；蜂箱</td>
                </tr>

                 <tr>
                    <td class="export-td">287</td>
                    <td class="export-td">bump</td>
                    <td class="export-td">英:/bʌmp/ 美:/bʌmp/ </td>
                    <td class="export-td">1. n. 肿块，隆起物；撞击
    2. vi. 碰撞，撞击；颠簸而行</td>
                </tr>

                 <tr>
                    <td class="export-td">288</td>
                    <td class="export-td">badminton</td>
                    <td class="export-td">英:/'bædmɪnt(ə)n/ 美:/'bædmɪntən/ </td>
                    <td class="export-td">羽毛球</td>
                </tr>

                 <tr>
                    <td class="export-td">289</td>
                    <td class="export-td">bumpy</td>
                    <td class="export-td">英:/'bʌmpɪ/ 美:/'bʌmpi/ </td>
                    <td class="export-td">adj. 崎岖不平的；颠簸的</td>
                </tr>

                 <tr>
                    <td class="export-td">290</td>
                    <td class="export-td">bleed</td>
                    <td class="export-td">英:/bliːd/ 美:/blid/ </td>
                    <td class="export-td">1. vt. 使出血；榨取
    2. vi. 流血；渗出；悲痛</td>
                </tr>

                 <tr>
                    <td class="export-td">291</td>
                    <td class="export-td">abroad</td>
                    <td class="export-td">英:/ə'brɔːd/ 美:/ə'brɔd/ </td>
                    <td class="export-td">1. adv. 到海外；在国外
    2. adj. 往国外的</td>
                </tr>

                 <tr>
                    <td class="export-td">292</td>
                    <td class="export-td">bumper</td>
                    <td class="export-td">英:/'bʌmpə/ 美:/'bʌmpɚ/ </td>
                    <td class="export-td">1. adj. 丰盛的，丰富的
    2. n. 缓冲器</td>
                </tr>

                 <tr>
                    <td class="export-td">293</td>
                    <td class="export-td">breakdown</td>
                    <td class="export-td">英:/'breɪkdaʊn/ 美:/'brek'daʊn/ </td>
                    <td class="export-td">击穿</td>
                </tr>

                 <tr>
                    <td class="export-td">294</td>
                    <td class="export-td">abrupt</td>
                    <td class="export-td">英:/ə'brʌpt/ 美:/ə'brʌpt/ </td>
                    <td class="export-td">adj. 突然的；唐突的；陡峭的；生硬的</td>
                </tr>

                 <tr>
                    <td class="export-td">295</td>
                    <td class="export-td">beef</td>
                    <td class="export-td">英:/biːf/ 美:/bif/ </td>
                    <td class="export-td">1. n. 牛肉；食用牛；肌肉；牢骚
    2. vi. 抱怨，告发；发牢骚</td>
                </tr>

                 <tr>
                    <td class="export-td">296</td>
                    <td class="export-td">breakfast</td>
                    <td class="export-td">英:/'brekfəst/ 美:/'brɛkfəst/ </td>
                    <td class="export-td">早餐</td>
                </tr>

                 <tr>
                    <td class="export-td">297</td>
                    <td class="export-td">bag</td>
                    <td class="export-td">英:/bæg/ 美:/bæɡ/ </td>
                    <td class="export-td">1. n. 袋；猎获物；（俚）一瓶啤酒
    2. vt. 猎获；把…装入袋中；[口]占据，私吞；使膨大</td>
                </tr>

                 <tr>
                    <td class="export-td">298</td>
                    <td class="export-td">beefburger</td>
                    <td class="export-td">/'bɛdbɝɡɚ/ </td>
                    <td class="export-td">n. 德式牛排,煎牛肉饼</td>
                </tr>

                 <tr>
                    <td class="export-td">299</td>
                    <td class="export-td">bagel</td>
                    <td class="export-td">英:/'beɪg(ə)l/ 美:/'beɡl/ </td>
                    <td class="export-td">n. 百吉饼（先蒸后烤的发面圈）；[俚]（体育比赛中）零蛋</td>
                </tr>

                 <tr>
                    <td class="export-td">300</td>
                    <td class="export-td">bone</td>
                    <td class="export-td">英:/bəʊn/ 美:/bon/ </td>
                    <td class="export-td">1. n. 骨；骨骼；香烟；一首歌
    2. vt. 剔去...的骨；施骨肥于</td>
                </tr>

                 <tr>
                    <td class="export-td">301</td>
                    <td class="export-td">baggage</td>
                    <td class="export-td">英:/'bægɪdʒ/ 美:/'bæɡɪdʒ/ </td>
                    <td class="export-td">n. 辎重（军队的）；行李</td>
                </tr>

                 <tr>
                    <td class="export-td">302</td>
                    <td class="export-td">absence</td>
                    <td class="export-td">英:/'æbs(ə)ns/ 美:/'æbsns/ </td>
                    <td class="export-td">n. 缺席；缺乏；没有；不注意</td>
                </tr>

                 <tr>
                    <td class="export-td">303</td>
                    <td class="export-td">blend</td>
                    <td class="export-td">英:/blend/ 美:/blɛnd/ </td>
                    <td class="export-td">1. vt. 混合
    2. vi. 混合；协调</td>
                </tr>

                 <tr>
                    <td class="export-td">304</td>
                    <td class="export-td">bun</td>
                    <td class="export-td">英:/bʌn/ 美:/bʌn/ </td>
                    <td class="export-td">n. 小圆面包</td>
                </tr>

                 <tr>
                    <td class="export-td">305</td>
                    <td class="export-td">been</td>
                    <td class="export-td">英:/biːn/ 美:/'hæz 'bin/ </td>
                    <td class="export-td">v. 是，有（be的过去分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">306</td>
                    <td class="export-td">absent</td>
                    <td class="export-td">英:/'æbs(ə)nt/ 美:/æb'sɛnt/ </td>
                    <td class="export-td">1. adj. 缺席的；缺少的；心不在焉的；茫然的
    2. vt. 使缺席</td>
                </tr>

                 <tr>
                    <td class="export-td">307</td>
                    <td class="export-td">bless</td>
                    <td class="export-td">英:/bles/ 美:/blɛs/ </td>
                    <td class="export-td">vt. 祝福；保佑；赞美</td>
                </tr>

                 <tr>
                    <td class="export-td">308</td>
                    <td class="export-td">bunch</td>
                    <td class="export-td">英:/bʌn(t)ʃ/ 美:/bʌntʃ/ </td>
                    <td class="export-td">1. n. 串；群；突出物
    2. vi. 隆起；打褶；形成一串</td>
                </tr>

                 <tr>
                    <td class="export-td">309</td>
                    <td class="export-td">baggy</td>
                    <td class="export-td">英:/'bægɪ/ 美:/'bæɡi/ </td>
                    <td class="export-td">adj. 袋状的，膨胀的；宽松而下垂的</td>
                </tr>

                 <tr>
                    <td class="export-td">310</td>
                    <td class="export-td">beer</td>
                    <td class="export-td">英:/bɪə/ 美:/bɪr/ </td>
                    <td class="export-td">1. n. 啤酒
    2. vi. 喝啤酒</td>
                </tr>

                 <tr>
                    <td class="export-td">311</td>
                    <td class="export-td">bagpipes</td>
                    <td class="export-td">/'bæɡpaɪps/ </td>
                    <td class="export-td">(also. 风笛</td>
                </tr>

                 <tr>
                    <td class="export-td">312</td>
                    <td class="export-td">bungalow</td>
                    <td class="export-td">英:/'bʌŋgələʊ/ 美:/'bʌŋɡəlo/ </td>
                    <td class="export-td">n. 平房；小屋</td>
                </tr>

                 <tr>
                    <td class="export-td">313</td>
                    <td class="export-td">breath</td>
                    <td class="export-td">英:/breθ/ 美:/brɛθ/ </td>
                    <td class="export-td">n. 呼吸，气息；一口气，（呼吸的）一次；微风；瞬间，瞬息；迹象；[语]无声音，气音</td>
                </tr>

                 <tr>
                    <td class="export-td">314</td>
                    <td class="export-td">beetle</td>
                    <td class="export-td">英:/'biːt(ə)l/ 美:/ˈbitl/ </td>
                    <td class="export-td">1. vi. 急忙来回；突出
    2. vt. 用槌打</td>
                </tr>

                 <tr>
                    <td class="export-td">315</td>
                    <td class="export-td">bonfire</td>
                    <td class="export-td">英:/'bɒnfaɪə/ 美:/'bɑnfaɪɚ/ </td>
                    <td class="export-td">n. 营火；篝火</td>
                </tr>

                 <tr>
                    <td class="export-td">316</td>
                    <td class="export-td">absolute</td>
                    <td class="export-td">英:/'æbsəluːt/ 美:/'æbsəlut/ </td>
                    <td class="export-td">1. adj. 绝对的；完全的；专制的
    2. n. 绝对事物；绝对</td>
                </tr>

                 <tr>
                    <td class="export-td">317</td>
                    <td class="export-td">beetroot</td>
                    <td class="export-td">英:/'biːtruːt/ 美:/'bitrut/ </td>
                    <td class="export-td">n. 甜菜的根</td>
                </tr>

                 <tr>
                    <td class="export-td">318</td>
                    <td class="export-td">bunk</td>
                    <td class="export-td">英:/bʌŋk/ 美:/bʌŋk/ </td>
                    <td class="export-td">1. n. 铺位；座床；床铺
    2. vi. 睡在铺上；逃跑</td>
                </tr>

                 <tr>
                    <td class="export-td">319</td>
                    <td class="export-td">breathe</td>
                    <td class="export-td">英:/briːð/ 美:/brið/ </td>
                    <td class="export-td">1. vi. 呼吸；低语；松口气；（风）轻拂
    2. vt. 呼吸；流露；使喘息；低声说</td>
                </tr>

                 <tr>
                    <td class="export-td">320</td>
                    <td class="export-td">blew</td>
                    <td class="export-td">英:/bluː/ 美:/blʊ/ </td>
                    <td class="export-td">blow的过去式</td>
                </tr>

                 <tr>
                    <td class="export-td">321</td>
                    <td class="export-td">bunny</td>
                    <td class="export-td">英:/'bʌnɪ/ 美:/'bʌni/ </td>
                    <td class="export-td">n. 兔子（特别是小兔子）；可爱女郎</td>
                </tr>

                 <tr>
                    <td class="export-td">322</td>
                    <td class="export-td">breathless</td>
                    <td class="export-td">英:/'breθlɪs/ 美:/'brɛθləs/ </td>
                    <td class="export-td">喘不过气来的</td>
                </tr>

                 <tr>
                    <td class="export-td">323</td>
                    <td class="export-td">buoy</td>
                    <td class="export-td">英:/bɒɪ/ 美:/'bʊi/ </td>
                    <td class="export-td">1. n. 浮标；浮筒；救生圈；航标
    2. vt. 使浮起；支撑；鼓励</td>
                </tr>

                 <tr>
                    <td class="export-td">324</td>
                    <td class="export-td">before</td>
                    <td class="export-td">英:/bɪ'fɔː/ 美:/bɪ'fɔr/ </td>
                    <td class="export-td">1. prep. 在…之前，先于
    2. adv. 在前；以前</td>
                </tr>

                 <tr>
                    <td class="export-td">325</td>
                    <td class="export-td">beforehand</td>
                    <td class="export-td">英:/bɪ'fɔːhænd/ 美:/bɪ'fɔrhænd/ </td>
                    <td class="export-td">预先, 事先</td>
                </tr>

                 <tr>
                    <td class="export-td">326</td>
                    <td class="export-td">absorbent</td>
                    <td class="export-td">英:/əb'zɔːb(ə)nt/ 美:/əb'sɔrbənt/ </td>
                    <td class="export-td">能吸收的</td>
                </tr>

                 <tr>
                    <td class="export-td">327</td>
                    <td class="export-td">blind</td>
                    <td class="export-td">英:/blaɪnd/ 美:/blaɪnd/ </td>
                    <td class="export-td">1. adj. 瞎的；盲目的
    2. adv. 看不见地；盲目地</td>
                </tr>

                 <tr>
                    <td class="export-td">328</td>
                    <td class="export-td">beg</td>
                    <td class="export-td">英:/beg/ 美:/bɛɡ/ </td>
                    <td class="export-td">1. vt. 恳求；乞讨；回避正题
    2. vi. 请求；乞讨</td>
                </tr>

                 <tr>
                    <td class="export-td">329</td>
                    <td class="export-td">absorbing</td>
                    <td class="export-td">英:/əb'zɔːbɪŋ/ 美:/əb'sɔrbɪŋ/ </td>
                    <td class="export-td">吸收</td>
                </tr>

                 <tr>
                    <td class="export-td">330</td>
                    <td class="export-td">beggar</td>
                    <td class="export-td">英:/'begə/ 美:/'bɛɡɚ/ </td>
                    <td class="export-td">1. n. 乞丐；穷人；[英口]家伙
    2. vt. 使贫穷；使沦为乞丐</td>
                </tr>

                 <tr>
                    <td class="export-td">331</td>
                    <td class="export-td">book</td>
                    <td class="export-td">英:/bʊk/ 美:/bʊk/ </td>
                    <td class="export-td">1. n. 书籍；帐簿；卷；名册；工作簿
    2. vt. 预订；登记</td>
                </tr>

                 <tr>
                    <td class="export-td">332</td>
                    <td class="export-td">breed</td>
                    <td class="export-td">英:/briːd/ 美:/brid/ </td>
                    <td class="export-td">1. vi. 繁殖；饲养；产生
    2. vt. 繁殖；饲养；养育，教育；引起</td>
                </tr>

                 <tr>
                    <td class="export-td">333</td>
                    <td class="export-td">balance</td>
                    <td class="export-td">英:/'bæl(ə)ns/ 美:/'bæləns/ </td>
                    <td class="export-td">1. n. 平衡；匀称；余额
    2. vt. 使平衡；结算；使相称</td>
                </tr>

                 <tr>
                    <td class="export-td">334</td>
                    <td class="export-td">bookcase</td>
                    <td class="export-td">英:/'bʊkkeɪs/ 美:/'bʊkkes/ </td>
                    <td class="export-td">n. 书柜，书架</td>
                </tr>

                 <tr>
                    <td class="export-td">335</td>
                    <td class="export-td">begin</td>
                    <td class="export-td">英:/bɪ'gɪn/ 美:/bɪ'ɡɪn/ </td>
                    <td class="export-td">1. vt. 开始
    2. vi. 开始；首先</td>
                </tr>

                 <tr>
                    <td class="export-td">336</td>
                    <td class="export-td">beginner</td>
                    <td class="export-td">英:/bɪ'gɪnə/ 美:/bɪ'gɪnɚ/ </td>
                    <td class="export-td">n. 初学者；新手；创始人</td>
                </tr>

                 <tr>
                    <td class="export-td">337</td>
                    <td class="export-td">breeze</td>
                    <td class="export-td">英:/briːz/ 美:/briz/ </td>
                    <td class="export-td">1. n. 微风；轻而易举的事；煤屑；焦炭渣；小风波
    2. vi. 吹微风；逃走</td>
                </tr>

                 <tr>
                    <td class="export-td">338</td>
                    <td class="export-td">abstract</td>
                    <td class="export-td">英:/'æbstrækt/ 美:/'æbstrækt/ </td>
                    <td class="export-td">1. n. 抽象；摘要；抽象的概念
    2. adj. 抽象的；深奥的</td>
                </tr>

                 <tr>
                    <td class="export-td">339</td>
                    <td class="export-td">balcony</td>
                    <td class="export-td">英:/'bælkənɪ/ 美:/'bælkəni/ </td>
                    <td class="export-td">n. 阳台；包厢；戏院楼厅</td>
                </tr>

                 <tr>
                    <td class="export-td">340</td>
                    <td class="export-td">across</td>
                    <td class="export-td">英:/ə'krɒs/ 美:/ə'krɔs/ </td>
                    <td class="export-td">1. prep. 穿过；横穿
    2. adv. 在对面；横过</td>
                </tr>

                 <tr>
                    <td class="export-td">341</td>
                    <td class="export-td">bald</td>
                    <td class="export-td">英:/bɔːld/ 美:/bɔld/ </td>
                    <td class="export-td">1. adj. 秃顶的；单调的；光秃的；无装饰的
    2. vi. 变秃</td>
                </tr>

                 <tr>
                    <td class="export-td">342</td>
                    <td class="export-td">blindfold</td>
                    <td class="export-td">英:/'blaɪn(d)fəʊld/ 美:/'blaɪndfold/ </td>
                    <td class="export-td">蒙住...的眼睛</td>
                </tr>

                 <tr>
                    <td class="export-td">343</td>
                    <td class="export-td">blink</td>
                    <td class="export-td">英:/blɪŋk/ 美:/blɪŋk/ </td>
                    <td class="export-td">1. vt. 眨眼；使…闪烁
    2. vi. 眨眼；闪烁</td>
                </tr>

                 <tr>
                    <td class="export-td">344</td>
                    <td class="export-td">absurd</td>
                    <td class="export-td">英:/əb'sɜːd/ 美:/əb'sɝd/ </td>
                    <td class="export-td">1. adj. 荒谬的；可笑的
    2. n. 荒诞；荒诞作品</td>
                </tr>

                 <tr>
                    <td class="export-td">345</td>
                    <td class="export-td">begun</td>
                    <td class="export-td">英:/bɪ'ɡʌn/ 美:/bɪ'ɡʌn/ </td>
                    <td class="export-td">v. 开始（begin的过去分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">346</td>
                    <td class="export-td">blister</td>
                    <td class="export-td">英:/'blɪstə/ 美:/'blɪstɚ/ </td>
                    <td class="export-td">1. n. 水疱；水泡；气泡；砂眼；起泡剂
    2. vt. 使起水泡；痛打；猛烈抨击</td>
                </tr>

                 <tr>
                    <td class="export-td">347</td>
                    <td class="export-td">brewery</td>
                    <td class="export-td">英:/'brʊərɪ/ 美:/'bruəri/ </td>
                    <td class="export-td">n. 啤酒厂</td>
                </tr>

                 <tr>
                    <td class="export-td">348</td>
                    <td class="export-td">booking</td>
                    <td class="export-td">英:/'bʊkɪŋ/ 美:/'bʊkɪŋ/ </td>
                    <td class="export-td">n. 预订；预约；演出契约</td>
                </tr>

                 <tr>
                    <td class="export-td">349</td>
                    <td class="export-td">behave</td>
                    <td class="export-td">英:/bɪ'heɪv/ 美:/bɪ'hev/ </td>
                    <td class="export-td">1. vi. 表现；举止端正；（机器等）运转；（事物）起某种作用
    2. vt. 使守规矩；使表现得…</td>
                </tr>

                 <tr>
                    <td class="export-td">350</td>
                    <td class="export-td">abuse</td>
                    <td class="export-td">英:/ə'bjuːz/ 美:/ə'bjus/ </td>
                    <td class="export-td">1. n. 滥用；辱骂；虐待；弊端；恶习，陋习
    2. vt. 滥用；辱骂；虐待</td>
                </tr>

                 <tr>
                    <td class="export-td">351</td>
                    <td class="export-td">bribe</td>
                    <td class="export-td">英:/braɪb/ 美:/braɪb/ </td>
                    <td class="export-td">1. vt. 贿赂，收买
    2. vi. 行贿</td>
                </tr>

                 <tr>
                    <td class="export-td">352</td>
                    <td class="export-td">brick</td>
                    <td class="export-td">英:/brɪk/ 美:/brɪk/ </td>
                    <td class="export-td">1. n. 砖，砖块；砖形物；[口]心肠好的人
    2. vt. 用砖砌</td>
                </tr>

                 <tr>
                    <td class="export-td">353</td>
                    <td class="export-td">boom</td>
                    <td class="export-td">英:/buːm/ 美:/bʊm/ </td>
                    <td class="export-td">1. vt. 发隆隆声；使兴旺
    2. vi. 发隆隆声；急速发展</td>
                </tr>

                 <tr>
                    <td class="export-td">354</td>
                    <td class="export-td">blizzard</td>
                    <td class="export-td">英:/'blɪzəd/ 美:/'blɪzɚd/ </td>
                    <td class="export-td">1. n. 暴风雪，大风雪；[俚]大打击
    2. vi. 下暴风雪</td>
                </tr>

                 <tr>
                    <td class="export-td">355</td>
                    <td class="export-td">ballerina</td>
                    <td class="export-td">英:/bælə'riːnə/ 美:/ˌbælə'rinə/ </td>
                    <td class="export-td">芭蕾舞女演员</td>
                </tr>

                 <tr>
                    <td class="export-td">356</td>
                    <td class="export-td">behind</td>
                    <td class="export-td">英:/bɪ'haɪnd/ 美:/bɪ'haɪnd/ </td>
                    <td class="export-td">1. prep. 支持；落后于；晚于
    2. adv. 在后地；在原处</td>
                </tr>

                 <tr>
                    <td class="export-td">357</td>
                    <td class="export-td">blob</td>
                    <td class="export-td">英:/blɒb/ 美:/blɑb/ </td>
                    <td class="export-td">1. n. 一滴；一抹；难以名状的一团
    2. vt. 弄脏；[美俚]把…做错</td>
                </tr>

                 <tr>
                    <td class="export-td">358</td>
                    <td class="export-td">ballet</td>
                    <td class="export-td">英:/'bæleɪ/ 美:/'bæle/ </td>
                    <td class="export-td">n. 芭蕾舞剧；芭蕾舞乐曲</td>
                </tr>

                 <tr>
                    <td class="export-td">359</td>
                    <td class="export-td">block</td>
                    <td class="export-td">英:/blɔk/ 美:/blɑk/ </td>
                    <td class="export-td">1. n. 块；街区；障碍物；大厦
    2. vt. 阻塞；阻止；限制</td>
                </tr>

                 <tr>
                    <td class="export-td">360</td>
                    <td class="export-td">bride</td>
                    <td class="export-td">英:/braɪd/ 美:/braɪd/ </td>
                    <td class="export-td">n. 新娘；[英俚]姑娘，女朋友</td>
                </tr>

                 <tr>
                    <td class="export-td">361</td>
                    <td class="export-td">beige</td>
                    <td class="export-td">英:/beɪʒ/ 美:/beʒ/ </td>
                    <td class="export-td">1. n. 米黄色
    2. adj. 浅褐色的；米黄色的</td>
                </tr>

                 <tr>
                    <td class="export-td">362</td>
                    <td class="export-td">boost</td>
                    <td class="export-td">英:/buːst/ 美:/bʊst/ </td>
                    <td class="export-td">1. vt. 促进；增加；支援
    2. vi. 宣扬；偷窃</td>
                </tr>

                 <tr>
                    <td class="export-td">363</td>
                    <td class="export-td">being</td>
                    <td class="export-td">英:/'biːɪŋ/ 美:/'biɪŋ/ </td>
                    <td class="export-td">1. n. 存在；生命；本质；品格
    2. adj. 存在的；现有的</td>
                </tr>

                 <tr>
                    <td class="export-td">364</td>
                    <td class="export-td">bridegroom</td>
                    <td class="export-td">英:/'braɪdgruːm/ 美:/'braɪdɡrum/ </td>
                    <td class="export-td">新郎</td>
                </tr>

                 <tr>
                    <td class="export-td">365</td>
                    <td class="export-td">boot</td>
                    <td class="export-td">英:/buːt/ 美:/bʊt/ </td>
                    <td class="export-td">1. vt. 使穿靴；引导；踢；解雇
    2. n. 靴子；汽车行李箱；踢</td>
                </tr>

                 <tr>
                    <td class="export-td">366</td>
                    <td class="export-td">bridesmaid</td>
                    <td class="export-td">英:/'braɪdzmeɪd/ 美:/'braɪdzmed/ </td>
                    <td class="export-td">女傧相</td>
                </tr>

                 <tr>
                    <td class="export-td">367</td>
                    <td class="export-td">balloon</td>
                    <td class="export-td">英:/bə'luːn/ 美:/bə'lun/ </td>
                    <td class="export-td">1. vi. 激增；膨胀如气球
    2. n. 气球</td>
                </tr>

                 <tr>
                    <td class="export-td">368</td>
                    <td class="export-td">bridge</td>
                    <td class="export-td">英:/brɪdʒ/ 美:/brɪdʒ/ </td>
                    <td class="export-td">1. n. 桥；桥牌；船桥；桥接器
    2. vt. 渡过；架桥</td>
                </tr>

                 <tr>
                    <td class="export-td">369</td>
                    <td class="export-td">ballot</td>
                    <td class="export-td">英:/'bælət/ 美:/'bælət/ </td>
                    <td class="export-td">1. n. 投票；投票用纸；投票总数
    2. vi. 投票；抽签决定</td>
                </tr>

                 <tr>
                    <td class="export-td">370</td>
                    <td class="export-td">brief</td>
                    <td class="export-td">英:/briːf/ 美:/brif/ </td>
                    <td class="export-td">1. adj. 简短的，简洁的；短暂的，草率的
    2. n. 概要，诉书；摘要，简报</td>
                </tr>

                 <tr>
                    <td class="export-td">371</td>
                    <td class="export-td">belief</td>
                    <td class="export-td">英:/bɪ'liːf/ 美:/bɪ'lif/ </td>
                    <td class="export-td">n. 相信，信赖；教义；信仰</td>
                </tr>

                 <tr>
                    <td class="export-td">372</td>
                    <td class="export-td">believe</td>
                    <td class="export-td">英:/bɪ'liːv/ 美:/bɪ'liv/ </td>
                    <td class="export-td">1. vi. 信任；料想；笃信宗教
    2. vt. 相信；认为；信任</td>
                </tr>

                 <tr>
                    <td class="export-td">373</td>
                    <td class="export-td">briefcase</td>
                    <td class="export-td">英:/'briːfkeɪs/ 美:/'brifkes/ </td>
                    <td class="export-td">公文包</td>
                </tr>

                 <tr>
                    <td class="export-td">374</td>
                    <td class="export-td">bloke</td>
                    <td class="export-td">英:/bləʊk/ 美:/blok/ </td>
                    <td class="export-td">n. [俚]家伙；小子</td>
                </tr>

                 <tr>
                    <td class="export-td">375</td>
                    <td class="export-td">blood</td>
                    <td class="export-td">英:/blʌd/ 美:/blʌd/ </td>
                    <td class="export-td">1. n. 血，血液；血统
    2. vt. 从…抽血；使先取得经验</td>
                </tr>

                 <tr>
                    <td class="export-td">376</td>
                    <td class="export-td">bell</td>
                    <td class="export-td">英:/bel/ 美:/bɛl/ </td>
                    <td class="export-td">1. n. 铃，钟；钟声，铃声；钟状物
    2. vt. 装钟于，系铃于</td>
                </tr>

                 <tr>
                    <td class="export-td">377</td>
                    <td class="export-td">bamboo</td>
                    <td class="export-td">英:/bæm'buː/ 美:/ˌbæm'bu/ </td>
                    <td class="export-td">1. n. 竹，竹子
    2. vt. 为…装上篾条</td>
                </tr>

                 <tr>
                    <td class="export-td">378</td>
                    <td class="export-td">brighten</td>
                    <td class="export-td">英:/'braɪt(ə)n/ 美:/'braɪtn/ </td>
                    <td class="export-td">1. vi. 变亮；活跃；明亮；快乐高兴
    2. vt. 使生辉；使闪亮；使快乐高兴</td>
                </tr>

                 <tr>
                    <td class="export-td">379</td>
                    <td class="export-td">border</td>
                    <td class="export-td">英:/'bɔːdə/ 美:/'bɔrdɚ/ </td>
                    <td class="export-td">1. n. 边界；边境；国界
    2. vt. 接近；与…接壤；在…上镶边</td>
                </tr>

                 <tr>
                    <td class="export-td">380</td>
                    <td class="export-td">ban</td>
                    <td class="export-td">英:/bæn/ 美:/bæn/ </td>
                    <td class="export-td">禁令</td>
                </tr>

                 <tr>
                    <td class="export-td">381</td>
                    <td class="export-td">bore</td>
                    <td class="export-td">英:/bɔː/ 美:/bɔr/ </td>
                    <td class="export-td">忍受</td>
                </tr>

                 <tr>
                    <td class="export-td">382</td>
                    <td class="export-td">banana</td>
                    <td class="export-td">英:/bə'nɑːnə/ 美:/bə'nænə/ </td>
                    <td class="export-td">n. 香蕉；喜剧演员；大鹰钩鼻</td>
                </tr>

                 <tr>
                    <td class="export-td">383</td>
                    <td class="export-td">brilliant</td>
                    <td class="export-td">英:/'brɪlj(ə)nt/ 美:/'brɪljənt/ </td>
                    <td class="export-td">辉煌</td>
                </tr>

                 <tr>
                    <td class="export-td">384</td>
                    <td class="export-td">brilliantly</td>
                    <td class="export-td">英:/'briljəntli/ 美:/ˈbrɪljəntlɪ/ </td>
                    <td class="export-td">出色</td>
                </tr>

                 <tr>
                    <td class="export-td">385</td>
                    <td class="export-td">boring</td>
                    <td class="export-td">英:/'bɔːrɪŋ/ 美:/'bɔrɪŋ/ </td>
                    <td class="export-td">1. adj. 令人厌烦的；无聊的
    2. n. 钻孔</td>
                </tr>

                 <tr>
                    <td class="export-td">386</td>
                    <td class="export-td">band</td>
                    <td class="export-td">英:/bænd/ 美:/bænd/ </td>
                    <td class="export-td">1. n. 带；松紧带；传送带；乐队；一帮
    2. vi. 联合；聚焦</td>
                </tr>

                 <tr>
                    <td class="export-td">387</td>
                    <td class="export-td">brim</td>
                    <td class="export-td">英:/brɪm/ 美:/brɪm/ </td>
                    <td class="export-td">1. n. 边；边缘
    2. vi. 满溢；溢出</td>
                </tr>

                 <tr>
                    <td class="export-td">388</td>
                    <td class="export-td">born</td>
                    <td class="export-td">英:/bɔ:n/ 美:/bɔrn/ </td>
                    <td class="export-td">1. v. 出世（bear的过去分词）
    2. adj. 天生的</td>
                </tr>

                 <tr>
                    <td class="export-td">389</td>
                    <td class="export-td">borne</td>
                    <td class="export-td">英:/bɔːn/ 美:/bɔrn/ </td>
                    <td class="export-td">v. 忍受；负荷；结果实；生子女（bear的过去分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">390</td>
                    <td class="export-td">bring</td>
                    <td class="export-td">英:/brɪŋ/ 美:/brɪŋ/ </td>
                    <td class="export-td">vt. 带来；引起；促使；使某人处于某种情况或境地</td>
                </tr>

                 <tr>
                    <td class="export-td">391</td>
                    <td class="export-td">bandage</td>
                    <td class="export-td">英:/'bændɪdʒ/ 美:/'bændɪdʒ/ </td>
                    <td class="export-td">1. n. 绷带
    2. vt. 用绷带包扎</td>
                </tr>

                 <tr>
                    <td class="export-td">392</td>
                    <td class="export-td">belly</td>
                    <td class="export-td">英:/'belɪ/ 美:/'bɛli/ </td>
                    <td class="export-td">1. n. 腹部；胃；食欲
    2. vi. 涨满；鼓起</td>
                </tr>

                 <tr>
                    <td class="export-td">393</td>
                    <td class="export-td">borrow</td>
                    <td class="export-td">英:/'bɒrəʊ/ 美:/'bɑro/ </td>
                    <td class="export-td">1. vi. 借；借用；从其他语言中引入
    2. vt. 借用；借</td>
                </tr>

                 <tr>
                    <td class="export-td">394</td>
                    <td class="export-td">bloodstream</td>
                    <td class="export-td">英:/'blʌdstriːm/ 美:/'blʌdstrim/ </td>
                    <td class="export-td">血流</td>
                </tr>

                 <tr>
                    <td class="export-td">395</td>
                    <td class="export-td">bandit</td>
                    <td class="export-td">英:/'bændɪt/ 美:/'bændɪt/ </td>
                    <td class="export-td">强盗</td>
                </tr>

                 <tr>
                    <td class="export-td">396</td>
                    <td class="export-td">belong</td>
                    <td class="export-td">英:/bɪ'lɒŋ/ 美:/bɪ'lɔŋ/ </td>
                    <td class="export-td">vi. 属于，应归入；适宜；应被放置；居住</td>
                </tr>

                 <tr>
                    <td class="export-td">397</td>
                    <td class="export-td">belongings</td>
                    <td class="export-td">英:/biˈlɔŋiŋz/ 美:/bə'lɔŋɪŋz/ </td>
                    <td class="export-td">财产, 所有物</td>
                </tr>

                 <tr>
                    <td class="export-td">398</td>
                    <td class="export-td">bloody</td>
                    <td class="export-td">英:/'blʌdɪ/ 美:/'blʌdi/ </td>
                    <td class="export-td">1. adj. 嗜杀的，残忍的；血腥的；非常的；血色的
    2. vt. 使流血</td>
                </tr>

                 <tr>
                    <td class="export-td">399</td>
                    <td class="export-td">boss</td>
                    <td class="export-td">英:/bɒs/ 美:/bɔs/ </td>
                    <td class="export-td">1. n. 老板；工头；首领
    2. vt. 指挥，调遣；当…的领导</td>
                </tr>

                 <tr>
                    <td class="export-td">400</td>
                    <td class="export-td">below</td>
                    <td class="export-td">英:/bɪ'ləʊ/ 美:/bɪ'lo/ </td>
                    <td class="export-td">1. adv. 在下面，在较低处；在本页下面
    2. prep. 在…下面</td>
                </tr>

                 <tr>
                    <td class="export-td">401</td>
                    <td class="export-td">belt</td>
                    <td class="export-td">英:/belt/ 美:/bɛlt/ </td>
                    <td class="export-td">1. n. 地带；带；腰带
    2. vt. 用带子系住；用皮带抽打</td>
                </tr>

                 <tr>
                    <td class="export-td">402</td>
                    <td class="export-td">bossy</td>
                    <td class="export-td">英:/'bɒsɪ/ 美:/'bɔsi/ </td>
                    <td class="export-td">1. adj. 专横的；浮雕装饰的；爱指挥他人的
    2. n. 母牛；牛犊</td>
                </tr>

                 <tr>
                    <td class="export-td">403</td>
                    <td class="export-td">bang</td>
                    <td class="export-td">英:/bæŋ/ 美:/bæŋ/ </td>
                    <td class="export-td">砰</td>
                </tr>

                 <tr>
                    <td class="export-td">404</td>
                    <td class="export-td">bloom</td>
                    <td class="export-td">英:/bluːm/ 美:/blum/ </td>
                    <td class="export-td">1. n. 花；青春；旺盛
    2. vt. 使开花；使茂盛</td>
                </tr>

                 <tr>
                    <td class="export-td">405</td>
                    <td class="export-td">bench</td>
                    <td class="export-td">英:/ben(t)ʃ/ 美:/bɛntʃ/ </td>
                    <td class="export-td">1. n. 长凳；工作台；替补队员
    2. vt. 给…以席位；为…设置条凳</td>
                </tr>

                 <tr>
                    <td class="export-td">406</td>
                    <td class="export-td">brisk</td>
                    <td class="export-td">英:/brɪsk/ 美:/brɪsk/ </td>
                    <td class="export-td">1. adj. 敏锐的，活泼的，轻快的；凛冽的
    2. vi. 活跃起来；变得轻快</td>
                </tr>

                 <tr>
                    <td class="export-td">407</td>
                    <td class="export-td">banister</td>
                    <td class="export-td">英:/'bænɪstə/ 美:/'bænɪstɚ/ </td>
                    <td class="export-td">n. 栏杆的支柱；楼梯的扶栏</td>
                </tr>

                 <tr>
                    <td class="export-td">408</td>
                    <td class="export-td">bend</td>
                    <td class="export-td">英:/bend/ 美:/bɛnd/ </td>
                    <td class="export-td">1. vt. 使弯曲；使屈服；使致力；使朝向
    2. vi. 弯曲，转弯；屈服；专心于；倾向</td>
                </tr>

                 <tr>
                    <td class="export-td">409</td>
                    <td class="export-td">bank</td>
                    <td class="export-td">英:/bæŋk/ 美:/bæŋk/ </td>
                    <td class="export-td">1. n. 银行；岸；储库；浅滩
    2. vt. 将…存入银行；倾斜转弯</td>
                </tr>

                 <tr>
                    <td class="export-td">410</td>
                    <td class="export-td">bristle</td>
                    <td class="export-td">英:/'brisl/ 美:/ˈbrɪsəl/ </td>
                    <td class="export-td">1. n. 猪鬃；刚毛
    2. vi. 发怒；竖起</td>
                </tr>

                 <tr>
                    <td class="export-td">411</td>
                    <td class="export-td">both</td>
                    <td class="export-td">英:/bəʊθ/ 美:/boθ/ </td>
                    <td class="export-td">1. adj. 两者的；两个的
    2. adv. 又；并；两者皆</td>
                </tr>

                 <tr>
                    <td class="export-td">412</td>
                    <td class="export-td">blouse</td>
                    <td class="export-td">英:/'blaʊz/ 美:/blaʊs/ </td>
                    <td class="export-td">1. n. 宽松的上衣；女装衬衫
    2. vt. 使…宽松下垂</td>
                </tr>

                 <tr>
                    <td class="export-td">413</td>
                    <td class="export-td">blow</td>
                    <td class="export-td">英:/bləʊ/ 美:/blo/ </td>
                    <td class="export-td">1. n. 吹；殴打；打击
    2. vi. 风吹；喘气</td>
                </tr>

                 <tr>
                    <td class="export-td">414</td>
                    <td class="export-td">beneath</td>
                    <td class="export-td">英:/bɪ'niːθ/ 美:/bɪ'niθ/ </td>
                    <td class="export-td">1. prep. 在…之下
    2. adv. 在下方</td>
                </tr>

                 <tr>
                    <td class="export-td">415</td>
                    <td class="export-td">bottle</td>
                    <td class="export-td">英:/'bɒt(ə)l/ 美:/'bɑtl/ </td>
                    <td class="export-td">1. n. 瓶子；一瓶的容量
    2. vt. 把…装入瓶中；控制</td>
                </tr>

                 <tr>
                    <td class="export-td">416</td>
                    <td class="export-td">banker</td>
                    <td class="export-td">英:/'bæŋkə/ 美:/'bæŋkɚ/ </td>
                    <td class="export-td">n. 银行家；银行业者；掘土工</td>
                </tr>

                 <tr>
                    <td class="export-td">417</td>
                    <td class="export-td">bottom</td>
                    <td class="export-td">英:/'bɒtəm/ 美:/'bɑtəm/ </td>
                    <td class="export-td">1. n. 底部；臀部；末端；尽头
    2. adj. 底部的</td>
                </tr>

                 <tr>
                    <td class="export-td">418</td>
                    <td class="export-td">banking</td>
                    <td class="export-td">英:/'bæŋkɪŋ/ 美:/'bæŋkɪŋ/ </td>
                    <td class="export-td">1. n. 银行业；银行业务；银行家的职业；筑堤
    2. v. 把钱存入银行；做银行家；在…边筑堤（bank的现在分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">419</td>
                    <td class="export-td">bankrupt</td>
                    <td class="export-td">英:/'bæŋkrʌpt/ 美:/'bæŋkrʌpt/ </td>
                    <td class="export-td">1. adj. 破产的
    2. vt. 使破产</td>
                </tr>

                 <tr>
                    <td class="export-td">420</td>
                    <td class="export-td">brittle</td>
                    <td class="export-td">英:/'brɪt(ə)l/ 美:/'brɪtl/ </td>
                    <td class="export-td">adj. 易碎的，脆弱的；易生气的</td>
                </tr>

                 <tr>
                    <td class="export-td">421</td>
                    <td class="export-td">broad</td>
                    <td class="export-td">英:/brɔːd/ 美:/brɔd/ </td>
                    <td class="export-td">1. adj. 宽的，辽阔的；显著的；大概的
    2. n. 宽阔部分</td>
                </tr>

                 <tr>
                    <td class="export-td">422</td>
                    <td class="export-td">banner</td>
                    <td class="export-td">英:/'bænə/ 美:/'bænɚ/ </td>
                    <td class="export-td">n. 旗帜，横幅；标语</td>
                </tr>

                 <tr>
                    <td class="export-td">423</td>
                    <td class="export-td">benefit</td>
                    <td class="export-td">英:/'benɪfɪt/ 美:/'bɛnɪfɪt/ </td>
                    <td class="export-td">1. n. 利益，好处；救济金
    2. vt. 有益于，对…有益</td>
                </tr>

                 <tr>
                    <td class="export-td">424</td>
                    <td class="export-td">bought</td>
                    <td class="export-td">英:/bɔːt/ 美:/bɔt/ </td>
                    <td class="export-td">v. 买（buy的过去式和过去分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">425</td>
                    <td class="export-td">bent</td>
                    <td class="export-td">英:/bent/ 美:/bɛnt/ </td>
                    <td class="export-td">1. n. 爱好，嗜好
    2. adj. 弯曲的；决心的</td>
                </tr>

                 <tr>
                    <td class="export-td">426</td>
                    <td class="export-td">bounce</td>
                    <td class="export-td">英:/baʊns/ 美:/baʊns/ </td>
                    <td class="export-td">1. n. 弹力；活力；跳
    2. vt. 弹跳；使弹起</td>
                </tr>

                 <tr>
                    <td class="export-td">427</td>
                    <td class="export-td">broadcast</td>
                    <td class="export-td">英:/'brɔːdkɑːst/ 美:/'brɔdkæst/ </td>
                    <td class="export-td">n. 广播; 播音; 广播节目; vt. & vi. 广播, 播放; vt. 传播, 乱传时 态: ...</td>
                </tr>

                 <tr>
                    <td class="export-td">428</td>
                    <td class="export-td">baptism</td>
                    <td class="export-td">英:/'bæptɪz(ə)m/ 美:/'bæptɪzəm/ </td>
                    <td class="export-td">n. [宗]洗礼；[喻]严峻考验</td>
                </tr>

                 <tr>
                    <td class="export-td">429</td>
                    <td class="export-td">bound</td>
                    <td class="export-td">英:/baʊnd/ 美:/baʊnd/ </td>
                    <td class="export-td">1. adj. 受约束的；装有封面的；有义务的
    2. vt. 束缚；使跳跃</td>
                </tr>

                 <tr>
                    <td class="export-td">430</td>
                    <td class="export-td">broadcloth</td>
                    <td class="export-td">英:/'brɔːdklɒθ/ 美:/'brɔd,klɔθ/ </td>
                    <td class="export-td">各色细平布</td>
                </tr>

                 <tr>
                    <td class="export-td">431</td>
                    <td class="export-td">bar</td>
                    <td class="export-td">英:/bɑː/ 美:/bɑr/ </td>
                    <td class="export-td">1. n. 酒吧；条，棒；障碍
    2. vt. 禁止；阻拦</td>
                </tr>

                 <tr>
                    <td class="export-td">432</td>
                    <td class="export-td">boundary</td>
                    <td class="export-td">英:/'baʊnd(ə)rɪ/ 美:/'baʊndri/ </td>
                    <td class="export-td">n. 分界线；边界；范围</td>
                </tr>

                 <tr>
                    <td class="export-td">433</td>
                    <td class="export-td">bar code</td>
                    <td class="export-td"></td>
                    <td class="export-td"></td>
                </tr>

                 <tr>
                    <td class="export-td">434</td>
                    <td class="export-td">broccoli</td>
                    <td class="export-td">英:/'brɒkəlɪ/ 美:/'brɑkəli/ </td>
                    <td class="export-td">n. 花椰菜；西兰花</td>
                </tr>

                 <tr>
                    <td class="export-td">435</td>
                    <td class="export-td">barmaid</td>
                    <td class="export-td">英:/'bɑːmeɪd/ 美:/'bɑrmed/ </td>
                    <td class="export-td">n. 酒吧女侍</td>
                </tr>

                 <tr>
                    <td class="export-td">436</td>
                    <td class="export-td">brochure</td>
                    <td class="export-td">英:/'brəʊʃə/ 美:/bro'ʃʊr/ </td>
                    <td class="export-td">n. 手册，小册子</td>
                </tr>

                 <tr>
                    <td class="export-td">437</td>
                    <td class="export-td">barman</td>
                    <td class="export-td">英:/'bɑːmən/ 美:/'bɑrmən/ </td>
                    <td class="export-td">n. 酒吧店主；酒吧间招待员</td>
                </tr>

                 <tr>
                    <td class="export-td">438</td>
                    <td class="export-td">bartender</td>
                    <td class="export-td">英:/'bɑːtendə/ 美:/'bɑrtɛndɚ/ </td>
                    <td class="export-td">酒保</td>
                </tr>

                 <tr>
                    <td class="export-td">439</td>
                    <td class="export-td">beret</td>
                    <td class="export-td">英:/'bereɪ/ 美:/bə're/ </td>
                    <td class="export-td">n. 贝雷帽</td>
                </tr>

                 <tr>
                    <td class="export-td">440</td>
                    <td class="export-td">berry</td>
                    <td class="export-td">英:/'berɪ/ 美:/'bɛri/ </td>
                    <td class="export-td">1. n. 浆果（葡萄，番茄等）
    2. vi. 采集浆果</td>
                </tr>

                 <tr>
                    <td class="export-td">441</td>
                    <td class="export-td">broken</td>
                    <td class="export-td">英:/'brəʊk(ə)n/ 美:/'brokən/ </td>
                    <td class="export-td">1. adj. 坏掉的；破碎的
    2. v. 打碎；折断；损坏（break的过去分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">442</td>
                    <td class="export-td">bouquet</td>
                    <td class="export-td">英:/bʊ'keɪ/ 美:/bu'ke/ </td>
                    <td class="export-td">n. 酒香；花束</td>
                </tr>

                 <tr>
                    <td class="export-td">443</td>
                    <td class="export-td">barbecue</td>
                    <td class="export-td">英:/'bɑːbɪkjuː/ 美:/'bɑrbɪkju/ </td>
                    <td class="export-td">1. n. 烤肉；吃烤肉的野宴
    2. vt. 烤肉；烧烤</td>
                </tr>

                 <tr>
                    <td class="export-td">444</td>
                    <td class="export-td">barber</td>
                    <td class="export-td">英:/ˈbɑ:bə/ 美:/ˈbɑrbɚ/ </td>
                    <td class="export-td">1. vt. 为…理发；修整
    2. n. 理发师</td>
                </tr>

                 <tr>
                    <td class="export-td">445</td>
                    <td class="export-td">blunt</td>
                    <td class="export-td">英:/blʌnt/ 美:/blʌnt/ </td>
                    <td class="export-td">1. adj. 钝的，不锋利的；生硬的；直率的
    2. vt. 使迟钝</td>
                </tr>

                 <tr>
                    <td class="export-td">446</td>
                    <td class="export-td">beside</td>
                    <td class="export-td">英:/bɪ'saɪd/ 美:/bɪ'saɪd/ </td>
                    <td class="export-td">prep. 在旁边；与…相比；和…无关</td>
                </tr>

                 <tr>
                    <td class="export-td">447</td>
                    <td class="export-td">besides</td>
                    <td class="export-td">英:/bɪ'saɪdz/ 美:/bɪ'saɪdz/ </td>
                    <td class="export-td">1. adv. 而且；此外
    2. prep. 除…之外</td>
                </tr>

                 <tr>
                    <td class="export-td">448</td>
                    <td class="export-td">bow</td>
                    <td class="export-td">英:/bəʊ/ 美:/baʊ/ </td>
                    <td class="export-td">1. n. 弓；鞠躬；船首
    2. vi. 鞠躬；弯腰</td>
                </tr>

                 <tr>
                    <td class="export-td">449</td>
                    <td class="export-td">blush</td>
                    <td class="export-td">英:/blʌʃ/ 美:/blʌʃ/ </td>
                    <td class="export-td">1. vi. 脸红；感到惭愧
    2. n. 脸红；红色；羞愧</td>
                </tr>

                 <tr>
                    <td class="export-td">450</td>
                    <td class="export-td">bare</td>
                    <td class="export-td">英:/beə/ 美:/bɛr/ </td>
                    <td class="export-td">1. adj. 空的；赤裸的，无遮蔽的
    2. vt. 露出，使赤裸</td>
                </tr>

                 <tr>
                    <td class="export-td">451</td>
                    <td class="export-td">barely</td>
                    <td class="export-td">英:/'beəlɪ/ 美:/'bɛrli/ </td>
                    <td class="export-td">adv. 仅仅，勉强；几乎不；公开地；贫乏地</td>
                </tr>

                 <tr>
                    <td class="export-td">452</td>
                    <td class="export-td">bronze</td>
                    <td class="export-td">英:/brɒnz/ 美:/brɑnz/ </td>
                    <td class="export-td">1. n. 青铜；青铜制品；古铜色
    2. adj. 青铜色的；青铜制的</td>
                </tr>

                 <tr>
                    <td class="export-td">453</td>
                    <td class="export-td">best</td>
                    <td class="export-td">英:/best/ 美:/bɛst/ </td>
                    <td class="export-td">1. n. 最好的人，最好的事物；最佳状态
    2. adj. 最好的</td>
                </tr>

                 <tr>
                    <td class="export-td">454</td>
                    <td class="export-td">bargain</td>
                    <td class="export-td">英:/'bɑːgɪn/ 美:/'bɑrɡən/ </td>
                    <td class="export-td">1. n. 交易；契约；特价商品
    2. vi. 讨价还价；成交</td>
                </tr>

                 <tr>
                    <td class="export-td">455</td>
                    <td class="export-td">brooch</td>
                    <td class="export-td">英:/brəʊtʃ/ 美:/brotʃ/ </td>
                    <td class="export-td">n. （女用的）胸针，领针</td>
                </tr>

                 <tr>
                    <td class="export-td">456</td>
                    <td class="export-td">bowl</td>
                    <td class="export-td">英:/bəʊl/ 美:/bol/ </td>
                    <td class="export-td">1. n. 碗；木球；大酒杯
    2. vi. 玩保龄球；滑动；平稳快速移动</td>
                </tr>

                 <tr>
                    <td class="export-td">457</td>
                    <td class="export-td">barge</td>
                    <td class="export-td">英:/bɑːdʒ/ 美:/bɑrdʒ/ </td>
                    <td class="export-td">1. vi. 蹒跚；闯入
    2. n. 驳船；游艇</td>
                </tr>

                 <tr>
                    <td class="export-td">458</td>
                    <td class="export-td">bowling</td>
                    <td class="export-td">英:/'bəʊlɪŋ/ 美:/'bolɪŋ/ </td>
                    <td class="export-td">1. n. 滚木球戏；保龄球戏
    2. v. 打保龄球（bowl的现在分词）</td>
                </tr>

                 <tr>
                    <td class="export-td">459</td>
                    <td class="export-td">broom</td>
                    <td class="export-td">英:/bruːm/ 美:/brum/ </td>
                    <td class="export-td">1. n. 金雀花；扫帚
    2. vt. 扫除</td>
                </tr>

                 <tr>
                    <td class="export-td">460</td>
                    <td class="export-td">bet</td>
                    <td class="export-td">英:/bet/ 美:/bɛt/ </td>
                    <td class="export-td">1. n. 打赌，赌注；被打赌的事物
    2. vt. 打赌；敢断定，确信</td>
                </tr>

                 <tr>
                    <td class="export-td">461</td>
                    <td class="export-td">brother</td>
                    <td class="export-td">英:/'brʌðə/ 美:/'brʌðɚ/ </td>
                    <td class="export-td">1. n. 兄弟；战友；同事
    2. int. [俚]我的老兄！</td>
                </tr>

                 <tr>
                    <td class="export-td">462</td>
                    <td class="export-td">bark</td>
                    <td class="export-td">英:/bɑːk/ 美:/bɑrk/ </td>
                    <td class="export-td">1. vt. 咆哮；吠叫；[口]咳嗽
    2. vi. 厉声说出；高声叫卖</td>
                </tr>

                 <tr>
                    <td class="export-td">463</td>
                    <td class="export-td">box</td>
                    <td class="export-td">英:/bɒks/ 美:/bɑks/ </td>
                    <td class="export-td">1. n. 箱，盒子；包厢；一拳
    2. vi. 拳击</td>
                </tr>

                 <tr>
                    <td class="export-td">464</td>
                    <td class="export-td">barley</td>
                    <td class="export-td">英:/'bɑːlɪ/ 美:/'bɑrli/ </td>
                    <td class="export-td">n. [植]大麦</td>
                </tr>

                 <tr>
                    <td class="export-td">465</td>
                    <td class="export-td">betray</td>
                    <td class="export-td">英:/bɪ'treɪ/ 美:/bɪ'tre/ </td>
                    <td class="export-td">vt. 背叛；出卖；泄露（秘密）；露出…迹象</td>
                </tr>

                 <tr>
                    <td class="export-td">466</td>
                    <td class="export-td">barn</td>
                    <td class="export-td">英:/bɑːn/ 美:/bɑrn/ </td>
                    <td class="export-td">1. n. 谷仓；车库；畜棚；靶（核反应截面单位）
    2. vt. 把…贮存入仓</td>
                </tr>

                 <tr>
                    <td class="export-td">467</td>
                    <td class="export-td">brow</td>
                    <td class="export-td">英:/braʊ/ 美:/braʊ/ </td>
                    <td class="export-td">n. 眉，眉毛；表情；额</td>
                </tr>

                 <tr>
                    <td class="export-td">468</td>
                    <td class="export-td">better</td>
                    <td class="export-td">英:/'betə/ 美:/'bɛtɚ/ </td>
                    <td class="export-td">1. n. 较好者；打赌的人（等于bettor）；长辈
    2. adv. 更多的；更好的；较大程度地</td>
                </tr>

                 <tr>
                    <td class="export-td">469</td>
                    <td class="export-td">boxer</td>
                    <td class="export-td">英:/'bɒksə/ 美:/'bɑksɚ/ </td>
                    <td class="export-td">n. 拳师，拳击手</td>
                </tr>

                 <tr>
                    <td class="export-td">470</td>
                    <td class="export-td">boxing</td>
                    <td class="export-td">英:/'bɒksɪŋ/ 美:/'bɑksɪŋ/ </td>
                    <td class="export-td">1. n. 拳击；装箱；围模；做箱的材料
    2. v. 将…装入盒中（box的ing形式）</td>
                </tr>

                 <tr>
                    <td class="export-td">471</td>
                    <td class="export-td">brown</td>
                    <td class="export-td">英:/braun/ 美:/braʊn/ </td>
                    <td class="export-td">1. adj. 棕色的，褐色的；太阳晒黑的
    2. vi. 变成褐色</td>
                </tr>

                 <tr>
                    <td class="export-td">472</td>
                    <td class="export-td">between</td>
                    <td class="export-td">英:/bɪ'twiːn/ 美:/bɪ'twin/ </td>
                    <td class="export-td">1. prep. 在…之间
    2. adv. 在中间</td>
                </tr>

                 <tr>
                    <td class="export-td">473</td>
                    <td class="export-td">beware</td>
                    <td class="export-td">英:/bɪ'weə/ 美:/bɪ'wɛr/ </td>
                    <td class="export-td">1. vi. 当心，小心
    2. vt. 提防；注意，当心</td>
                </tr>

                 <tr>
                    <td class="export-td">474</td>
                    <td class="export-td">bruise</td>
                    <td class="export-td">英:/bruːz/ 美:/bruz/ </td>
                    <td class="export-td">1. n. 擦伤；挫伤；青肿
    2. vt. 使受瘀伤；使受挫伤</td>
                </tr>

                 <tr>
                    <td class="export-td">475</td>
                    <td class="export-td">barracks</td>
                    <td class="export-td">/'bærəks/ </td>
                    <td class="export-td">1. n. 兵营，营房；简陋的房子；警察所（barrack的复数）
    2. v. 使驻扎军营里；住在工房、棚屋里；（澳）大声鼓噪（barrack的三单形式）</td>
                </tr>

                 <tr>
                    <td class="export-td">476</td>
                    <td class="export-td">beyond</td>
                    <td class="export-td">英:/bɪ'jɒnd/ 美:/bɪ'jɑnd/ </td>
                    <td class="export-td">1. prep. 超过；越过；在...较远的一边；那一边
    2. adv. 在更远处；在远处</td>
                </tr>

                 <tr>
                    <td class="export-td">477</td>
                    <td class="export-td">barrel</td>
                    <td class="export-td">英:/'bær(ə)l/ 美:/'bærəl/ </td>
                    <td class="export-td">1. vt. 把……装入桶内
    2. n. 桶；枪管，炮管</td>
                </tr>

                 <tr>
                    <td class="export-td">478</td>
                    <td class="export-td">brush</td>
                    <td class="export-td">英:/brʌʃ/ 美:/brʌʃ/ </td>
                    <td class="export-td">1. n. 刷子；画笔；毛笔；争吵
    2. vt. 刷；画</td>
                </tr>

                 <tr>
                    <td class="export-td">479</td>
                    <td class="export-td">barricade</td>
                    <td class="export-td">英:/ˌbærɪ'keɪd/ 美:/'bærɪ'ked/ </td>
                    <td class="export-td">壅</td>
                </tr>

                 <tr>
                    <td class="export-td">480</td>
                    <td class="export-td">barrier</td>
                    <td class="export-td">英:/'bærɪə/ 美:/'bærɪɚ/ </td>
                    <td class="export-td">1. n. 障碍物，屏障；界线
    2. vt. 把…关入栅栏</td>
                </tr>

                 <tr>
                    <td class="export-td">481</td>
                    <td class="export-td">brutal</td>
                    <td class="export-td">英:/'bruːt(ə)l/ 美:/'brutl/ </td>
                    <td class="export-td">adj. 残忍的；野蛮的，不讲理的</td>
                </tr>

                 <tr>
                    <td class="export-td">482</td>
                    <td class="export-td">base</td>
                    <td class="export-td">英:/beɪs/ 美:/bes/ </td>
                    <td class="export-td">1. n. 底部；垒；基础
    2. adj. 卑鄙的；低劣的</td>
                </tr>

                 <tr>
                    <td class="export-td">483</td>
                    <td class="export-td">baseball</td>
                    <td class="export-td">英:/ˈbeisbɔ:l/ 美:/'besbɔl/ </td>
                    <td class="export-td">n. 棒球运动；棒球</td>
                </tr>

                 <tr>
                    <td class="export-td">484</td>
                    <td class="export-td">basement</td>
                    <td class="export-td">英:/'beɪsm(ə)nt/ 美:/'besmənt/ </td>
                    <td class="export-td">n. 地下室；地窖</td>
                </tr>

                 <tr>
                    <td class="export-td">485</td>
                    <td class="export-td">bases</td>
                    <td class="export-td">英:/'beɪsiːz/ 美:/'besiz/ </td>
                    <td class="export-td">n. 主要成分；根据；基础（base的复数形式）</td>
                </tr>

                 <tr>
                    <td class="export-td">486</td>
                    <td class="export-td">basic</td>
                    <td class="export-td">英:/'beɪsɪk/ 美:/'besɪk/ </td>
                    <td class="export-td">1. adj. 基本的；基础的
    2. n. 基础；要素</td>
                </tr>

                 <tr>
                    <td class="export-td">487</td>
                    <td class="export-td">basically</td>
                    <td class="export-td">英:/ˈbeisikəli/ 美:/'besɪkli/ </td>
                    <td class="export-td">基本上, 主要地</td>
                </tr>

                 <tr>
                    <td class="export-td">488</td>
                    <td class="export-td">basin</td>
                    <td class="export-td">英:/'beɪs(ə)n/ 美:/'besn/ </td>
                    <td class="export-td">n. 盆地；盆；水池；流域</td>
                </tr>

                 <tr>
                    <td class="export-td">489</td>
                    <td class="export-td">basis</td>
                    <td class="export-td">英:/'beɪsɪs/ 美:/'besɪs/ </td>
                    <td class="export-td">n. 底部；基础；主要成分；基本原则或原理</td>
                </tr>

                 <tr>
                    <td class="export-td">490</td>
                    <td class="export-td">basket</td>
                    <td class="export-td">英:/'bɑːskɪt/ 美:/'bæskɪt/ </td>
                    <td class="export-td">1. n. 篮子；（篮球比赛的）得分；一篮之量；篮筐
    2. vt. 装入篮</td>
                </tr>

                 <tr>
                    <td class="export-td">491</td>
                    <td class="export-td">bass</td>
                    <td class="export-td">英:/bæs/ 美:/bæs/ </td>
                    <td class="export-td">1. n. [音]男低音；低音部；[鱼]鲈鱼；[植]椴树
    2. adj. 低音的</td>
                </tr>

                 <tr>
                    <td class="export-td">492</td>
                    <td class="export-td">bat</td>
                    <td class="export-td">英:/bæt/ 美:/bæt/ </td>
                    <td class="export-td">1. n. 蝙蝠；球棒；批处理文件的扩展名
    2. vt. 用球棒击球；击球率达…</td>
                </tr>

                 <tr>
                    <td class="export-td">493</td>
                    <td class="export-td">batch</td>
                    <td class="export-td">英:/bætʃ/ 美:/bætʃ/ </td>
                    <td class="export-td">1. n. 一批；一炉；一次所制之量
    2. vt. 分批处理</td>
                </tr>

                 <tr>
                    <td class="export-td">494</td>
                    <td class="export-td">bathroom</td>
                    <td class="export-td">英:/'bɑːθruːm/ 美:/'bæθrum/ </td>
                    <td class="export-td">n. 浴室；厕所；盥洗室</td>
                </tr>

                 <tr>
                    <td class="export-td">495</td>
                    <td class="export-td">bathe</td>
                    <td class="export-td">英:/beɪð/ 美:/beð/ </td>
                    <td class="export-td">1. vt. 沐浴；用水洗
    2. vi. 洗澡；沐浴</td>
                </tr>

                 <tr>
                    <td class="export-td">496</td>
                    <td class="export-td">battery</td>
                    <td class="export-td">英:/'bæt(ə)rɪ/ 美:/'bætri/ </td>
                    <td class="export-td">n. 电池，蓄电池</td>
                </tr>

                 <tr>
                    <td class="export-td">497</td>
                    <td class="export-td">battle</td>
                    <td class="export-td">英:/'bæt(ə)l/ 美:/'bætl/ </td>
                    <td class="export-td">1. n. 战役；斗争
    2. vi. 作战；斗争</td>
                </tr>

                 <tr>
                    <td class="export-td">498</td>
                    <td class="export-td">bay</td>
                    <td class="export-td">英:/beɪ/ 美:/be/ </td>
                    <td class="export-td">1. n. 海湾；狗吠声
    2. vt. 向…吠叫</td>
                </tr>

                 <tr>
                    <td class="export-td">499</td>
                    <td class="export-td">arouse</td>
                    <td class="export-td">英:/ə'raʊz/ 美:/ə'raʊz/ </td>
                    <td class="export-td">1. vt. 引起；鼓励；唤醒
    2. vi. 醒来；发奋；激发</td>
                </tr>

                 <tr>
                    <td class="export-td">500</td>
                    <td class="export-td">assembly</td>
                    <td class="export-td">英:/ə'semblɪ/ 美:/ə'sɛmbli/ </td>
                    <td class="export-td">n. 装配；集会，集合</td>
                </tr>

                 <tr>
                    <td class="export-td">501</td>
                    <td class="export-td">association</td>
                    <td class="export-td">英:/əsəʊsɪ'eɪʃ(ə)n/ 美:/ə,soʃɪ'eʃən/ </td>
                    <td class="export-td">协会</td>
                </tr>

                 <tr>
                    <td class="export-td">502</td>
                    <td class="export-td">attend</td>
                    <td class="export-td">英:/ə'tend/ 美:/ə'tɛnd/ </td>
                    <td class="export-td">1. vt. 出席；上（大学等）；照料；招待；陪伴
    2. vi. 出席；照料；照顾；致力于</td>
                </tr>

                 <tr>
                    <td class="export-td">503</td>
                    <td class="export-td">become</td>
                    <td class="export-td">英:/bɪ'kʌm/ 美:/bɪ'kʌm/ </td>
                    <td class="export-td">1. vi. 变成；变得；成为
    2. vt. 适合；相称</td>
                </tr>

                 <tr>
                    <td class="export-td">504</td>
                    <td class="export-td">bicycle</td>
                    <td class="export-td">英:/'baɪsɪkl/ 美:/'baɪsɪkl/ </td>
                    <td class="export-td">1. n. 自行车
    2. vi. 骑脚踏车</td>
                </tr>

                 <tr>
                    <td class="export-td">505</td>
                    <td class="export-td">big</td>
                    <td class="export-td">英:/bɪg/ 美:/bɪɡ/ </td>
                    <td class="export-td">1. adj. 大的；重要的；量大的
    2. adv. 大量地；夸大地；顺利</td>
                </tr>

                 <tr>
                    <td class="export-td">506</td>
                    <td class="export-td">bike</td>
                    <td class="export-td">英:/baɪk/ 美:/baɪk/ </td>
                    <td class="export-td">1. n. 自行车；脚踏车
    2. vi. 骑自行车（或摩托车）</td>
                </tr>

                 <tr>
                    <td class="export-td">507</td>
                    <td class="export-td">bill</td>
                    <td class="export-td">英:/bɪl/ 美:/bɪl/ </td>
                    <td class="export-td">1. n. 帐单；法案；广告；钞票；票据；清单
    2. vt. 宣布；开帐单；用海报宣传</td>
                </tr>

                 <tr>
                    <td class="export-td">508</td>
                    <td class="export-td">billion</td>
                    <td class="export-td">英:/'bɪljən/ 美:/'bɪljən/ </td>
                    <td class="export-td">1. n. 十亿；大量
    2. num. 十亿</td>
                </tr>

                 <tr>
                    <td class="export-td">509</td>
                    <td class="export-td">bind</td>
                    <td class="export-td">英:/baɪnd/ 美:/baɪnd/ </td>
                    <td class="export-td">1. vi. 装订；结合；过紧；有约束力
    2. vt. 装订；约束；绑；包扎；凝固</td>
                </tr>

                 <tr>
                    <td class="export-td">510</td>
                    <td class="export-td">biology</td>
                    <td class="export-td">英:/baɪ'ɒlədʒɪ/ 美:/baɪ'ɑlədʒi/ </td>
                    <td class="export-td">n. 生物学；（一个地区全部的）生物</td>
                </tr>

                 <tr>
                    <td class="export-td">511</td>
                    <td class="export-td">bird</td>
                    <td class="export-td">英:/bɜːd/ 美:/bɝd/ </td>
                    <td class="export-td">1. n. 鸟；家伙；羽毛球
    2. vt. 向…喝倒彩；起哄</td>
                </tr>

                 <tr>
                    <td class="export-td">512</td>
                    <td class="export-td">birth</td>
                    <td class="export-td">英:/bɜːθ/ 美:/bɝθ/ </td>
                    <td class="export-td">n. 出生；血统，出身；起源</td>
                </tr>

                 <tr>
                    <td class="export-td">513</td>
                    <td class="export-td">birthday</td>
                    <td class="export-td">英:/'bɜːθdeɪ/ 美:/'bɝθde/ </td>
                    <td class="export-td">n. 生日，诞辰；诞生的日子</td>
                </tr>

                 <tr>
                    <td class="export-td">514</td>
                    <td class="export-td">biscuit</td>
                    <td class="export-td">英:/'bɪskɪt/ 美:/'bɪskɪt/ </td>
                    <td class="export-td">n. 小点心，饼干</td>
                </tr>

                 <tr>
                    <td class="export-td">515</td>
                    <td class="export-td">bit</td>
                    <td class="export-td">英:/bɪt/ 美:/bɪt/ </td>
                    <td class="export-td">1. n. 少量；马嚼子；比特（二进位制信息单位）；辅币；[口]老一套
    2. vt. 控制</td>
                </tr>

                 <tr>
                    <td class="export-td">516</td>
                    <td class="export-td">bite</td>
                    <td class="export-td">英:/baɪt/ 美:/baɪt/ </td>
                    <td class="export-td">咬</td>
                </tr>

                 <tr>
                    <td class="export-td">517</td>
                    <td class="export-td">bitter</td>
                    <td class="export-td">英:/'bɪtə/ 美:/'bɪtɚ/ </td>
                    <td class="export-td">1. adj. 苦的；痛苦的；充满仇恨的；尖刻的
    2. n. 苦味；苦啤酒</td>
                </tr>

                 <tr>
                    <td class="export-td">518</td>
                    <td class="export-td">resistance</td>
                    <td class="export-td">英:/rɪ'zɪst(ə)ns/ 美:/rɪ'zɪstəns/ </td>
                    <td class="export-td">阻力</td>
                </tr>

                 <tr>
                    <td class="export-td">519</td>
                    <td class="export-td">arena</td>
                    <td class="export-td">英:/ə'riːnə/ 美:/ə'rinə/ </td>
                    <td class="export-td">n. 竞技场；舞台</td>
                </tr>

                 <tr>
                    <td class="export-td">520</td>
                    <td class="export-td">bid</td>
                    <td class="export-td">英:/bɪd/ 美:/bɪd/ </td>
                    <td class="export-td">1. vt. 投标；出价；吩咐；表示
    2. vi. 投标；吩咐</td>
                </tr>

                 <tr>
                    <td class="export-td">521</td>
                    <td class="export-td">biography</td>
                    <td class="export-td">英:/baɪ'ɒgrəfɪ/ 美:/baɪ'ɑɡrəfi/ </td>
                    <td class="export-td">传记</td>
                </tr>

                 <tr>
                    <td class="export-td">522</td>
                    <td class="export-td">bizarre</td>
                    <td class="export-td">英:/bɪ'zɑː/ 美:/bɪ'zɑr/ </td>
                    <td class="export-td">adj. 奇异的（指态度，容貌，款式等）</td>
                </tr>

                 <tr>
                    <td class="export-td">523</td>
                    <td class="export-td">bead</td>
                    <td class="export-td">英:/biːd/ 美:/bid/ </td>
                    <td class="export-td">1. n. 珠子；念珠；滴
    2. vi. 形成珠状，起泡</td>
                </tr>

                 <tr>
                    <td class="export-td">524</td>
                    <td class="export-td">bin</td>
                    <td class="export-td">英:/bɪn/ 美:/bɪn/ </td>
                    <td class="export-td">箱柜</td>
                </tr>

                 <tr>
                    <td class="export-td">525</td>
                    <td class="export-td">blonde</td>
                    <td class="export-td">英:/blɒnd/ 美:/blɑnd/ </td>
                    <td class="export-td">1. adj. 亚麻色的；白皙的；白肤金发碧眼的
    2. n. 白肤金发碧眼的女人</td>
                </tr>

                 <tr>
                    <td class="export-td">526</td>
                    <td class="export-td">bilingual</td>
                    <td class="export-td">英:/baɪ'lɪŋgw(ə)l/ 美:/'baɪ'lɪŋgwəl/ </td>
                    <td class="export-td">双语</td>
                </tr>

                 <tr>
                    <td class="export-td">527</td>
                    <td class="export-td">blur</td>
                    <td class="export-td">英:/blɜː/ 美:/blɝ/ </td>
                    <td class="export-td">1. vt. 涂污；使…模糊不清；使暗淡；玷污
    2. vi. 沾上污迹；变模糊</td>
                </tr>

                 <tr>
                    <td class="export-td">528</td>
                    <td class="export-td">bricklayer</td>
                    <td class="export-td">英:/'brɪkleɪə/ 美:/'brɪkleɚ/ </td>
                    <td class="export-td">砖匠</td>
                </tr>

                 <tr>
                    <td class="export-td">529</td>
                    <td class="export-td">prey</td>
                    <td class="export-td">英:/preɪ/ 美:/pre/ </td>
                    <td class="export-td">1. vi. 捕食；掠夺；折磨
    2. n. 牺牲者；被捕食的动物；捕食</td>
                </tr>"""

    items = get_useful_informatin(html)
    for item in items:
        print(item)

if __name__ == "__main__":
    main()