"""
https://leetcode.com/problems/two-sum/?envType=study-plan&id=data-structure-i
"""

# Question didn't specify whether you could sort the list
class Solution:
    def twoSum(self, n: list[int], t: int) -> list[int]:
        s_n = [x for x in enumerate(n)]
        s_n.sort(key=lambda x: x[1])
        step = 0
        pull_v = lambda x: s_n[x][1]
        pull_i = lambda x: s_n[x][0]
        l = 0
        h = len(n) - 1

        if t == 0:
            if n.count(0) == 2:
                m = (h - l) // 2
                while True:
                    if 0 < s_n[m][1] != 0:
                        m -= 1
                        if s_n[m][1] == 0:
                            return [s_n[m-1][0], s_n[m][0]]
                    else:
                        m += 1
                        if s_n[m][1] == 0:
                            return [s_n[m+1][0], s_n[m][0]]
            else:
                cv = pull_v(step)
                find = abs(cv) if cv < 0 else cv * -1
                m = ((h - l) // 2) + l
                mv = pull_v(m)
                while mv != find and h - l > 1:
                    if find < mv:
                        h = m
                        m = ((h - l) // 2) + l
                    elif find > mv:
                        l = m
                        m = ((h - l) // 2) + l
                if h - l == 1:
                    if find == pull_v(m + 1):
                        return [pull_i(step), pull_i(m + 1)]
                if mv == find:
                    return [pull_i(step), pull_i(m)]
                else:
                    step += 1
                    l = step
                    h = len(n) - 1
        else:
            while step < len(n):
                cv = pull_v(step)
                find = abs(cv) - abs(t) if cv < 0 > t else abs(cv) + t if cv < 0 < t else cv - t if cv > 0 > t else t - cv if t > 0 < cv else abs(cv) if cv < 0 == t else cv *-1 if cv > 0 == t else 0
                m = ((h - l) // 2) + l
                mv = pull_v(m)
                while mv != find and h-l > 1:
                    mv = pull_v(m)
                    if find < mv:
                        h = m
                        m = ((h - l) // 2) + l
                    elif find > mv:
                        l = m
                        m = ((h - l) // 2) + l
                if h - l == 1:
                    if find == pull_v(m + 1):
                        return [pull_i(step), pull_i(m + 1)]
                if mv == find:
                    return [pull_i(step), pull_i(m)]
                else:
                    step += 1
                    l = step
                    h = len(n) - 1

"""
90 ms - answer vs. mine ... I am going to spend some time analyzing this and doing time testing myself to understand why this is the case.

My logic with my actual accepted attempt was this: Sacrifice O(n) by sorting the list first to allow for binary search.
I believe now, that I basically forced my program to take O(n2) because I was looping through it twice anyway, even if the
second loop could potentially use binary search, it would still be possible for it to take the maximum time.  Here,
Ineed to remember that you can parse through once and because you have to touch each element once anyway, then is the
time to sort and store values while checking for complement.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, x in enumerate(nums):
            complement = target - x
            if complement in dictionary:
                return [i, dictionary[complement]]
            dictionary[x] = i
        return []

I need to remember this well because I caused myself a lot of work for nothing here.  Look at all of the bullshit I was
keeping track of

loop through the enumerated list:
at each iteration, create a new complement variable to check for
Check to see if the new complement is already stored in dictionary
return if so
add element in dictionary by key = index



So things to remember, if you know you are most likely going to be FORCED to loop through an entire array, find a way
to contain it to one simple loop through the elements.  I was trying to save on data usage to a certain extent, but
in the end I was carrying multiple variables through the whole process and maintaining references to all of the elements
There may be additional costs for the pull_v and pull_i that made it easier to type but most likely cost on time/memory
for larger lists.

Anyway, this was another one where the solution was easy if you could think of it.  My first version of the problem 
would have worked but timed out.  It was the brute force option where you have inner/outter loop to check all possible
compilations.

I need to do more actual testing of my algorithms with the timer.py funcitonality and also read the rest of the algorithm book, because I need to start understanding
how much memory is actually utilized for each type of data and container.  I didn't get to that part of the book
on hashmap yet and it is perhaps not as costly to access the hashmap for every item on the loop.

Still learning.

"""




if __name__ == "__main__":
    S = Solution()
    testcase = ([2, 4, 21, 33, 2, 16, 6, 13, 1, 1, 11, 5], 16)
    testcase2 = ([5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5], 10)
    testcase3 = ([9, 9, 9,9, 1, 9, 9, 9, 9, 0], 1)
    testcase4 = ([0, 4, 3, 0], 0)
    testcase5 = ([3, 2, 4], 6)
    testcase6 = ([-10, -1, -18, -19], -19)
    testcase7 = ([-10, 7, 19, 15], 9)
    testcase8 = ([-8525576,2821699,8376865,-9212317,5207750,7142430,4359550,5104325,-8054581,9303446,-3478369,-8348583,6777365,9388417,5911004,8924909,7930494,-2687145,6789728,6140413,3037810,6839110,7613859,-381356,9848108,-3893960,-9260739,-1291602,-4431234,-9505752,-4313632,-6719920,-2615081,5795961,3293382,6411875,-7460292,2968015,6026065,3362676,-4436688,9440912,-8513576,-3159450,-8998433,-4309718,-1987023,210072,-1274570,1024374,-4697294,-3582515,-2732215,850472,-5758747,-9657394,-3957063,-5721156,-9840913,3798442,-1854013,7972446,-3365366,796810,5502180,9851730,-7783084,7138877,4455900,5764296,3230660,6546995,-9100443,-736500,-673663,-8287547,5628134,8925235,-7563102,-9650994,-7925698,2522927,2381245,-7729316,3943295,296501,7393804,-6014735,8078828,1334481,4738427,7557845,2716149,-688559,-2383430,-6362840,-2480316,39696,6400502,2960375,4823357,9206169,3069186,7043284,-7737620,6111430,6481195,-6833906,-7808409,-2520456,-1441273,8312357,1098423,620019,7206181,2559811,4153201,-9987166,4643768,-7267277,1968598,-4387785,-8995279,-3462145,139934,-5065871,-3105906,1073424,-5491921,-8893820,-3308790,1415168,6474889,2477914,-7821473,-6963465,-5038661,-8892789,-322340,7467552,-1650191,-2165286,-1840127,9099481,4672231,-2952557,2538745,-4869459,-8611986,1695017,5587406,-1638557,-9741243,8303637,9555184,-8938516,-5753781,-8495406,-4880080,5039978,-7154802,9017353,2924829,3454971,-3821240,-9791203,-21599,-1951327,-7029101,5115018,-1591411,4662075,-5844339,6058599,-1299646,-5858539,8618193,9602540,1181513,-5160496,-6644134,6534717,5558140,8853890,8395423,-51610,5722960,8205114,8653613,-1774666,7732664,-8883501,-4783769,-1975780,-5940120,-4007489,-9406777,4889483,-7315707,-7426593,3055469,3423448,-8609993,-8326412,4379103,-8267110,-9432734,-114879,-3766165,4779158,547417,9746352,8796956,-7421240,-8323062,2818763,-9937655,2190708,-6150224,2391430,7270317,-1691374,6993405,8388364,-7092092,-3228318,744072,-1847252,1447350,-2127548,-6070501,-734035,-4785694,9822102,2776903,1506289,1812526,-2379670,1707270,-9509152,-6253365,-4982599,9455837,6581402,721376,3881667,8298993,-166709,-1179212,-353220,7537049,5758238,-6262558,3205396,-2991279,-1170936,-5807440,6443338,644818,19920,5394339,-6662867,-9727166,9066255,-5213538,2551041,-2034945,-4619989,-7771121,-1621444,6122601,4625771,9638438,7157430,9345501,-419132,-9494998,-3893011,2683368,8166123,2207847,1987730,-4085018,9878497,6883868,7814352,8103989,5271281,-6989257,2891524,1391179,-121390,4370650,1762431,-7350206,3327644,-4552333,-5582739,4135800,-6469588,8985894,2283798,-4976683,-2122622,-3560088,4581541,688503,1596164,6653622,7532293,2073015,-8012770,1896913,-9791902,6555385,-6872850,-8750543,8455338,-279299,-2770375,1023909,-1076916,-2293185,5812978,4939172,-5046465,1004182,4743763,-6415924,5625775,7131805,-7160873,7218936,-9150014,7548922,-675583,-8385432,-3225402,-772872,-8715530,538414,-5945506,-7737867,-8135344,-4420258,-8067908,-7668874,-6404894,-4392786,4906411,-3632338,1480213,8578242,8615344,-9344965,-9237936,8891393,-426543,2793325,-7740687,8351499,8178662,9690668,5554374,-7955894,-8385818,8815958,-3932346,-2485860,-9964645,-2979727,550711,8114291,-5960488,7966835,-5190445,9208118,-5587368,3716432,1571125,9823037,7035016,9576081,-9201578,4529158,-9771547,7309954,8598580,-8115425,1011316,-9178024,5761459,2509040,817780,-816184,-8314208,-3395592,1519354,-4703043,-9943732,1296837,7036941,-1208061,1539298,-2489250,6781577,1641928,-4669629,-4659636,5199667,7449147,-9714069,-9890687,-9486738,4602590,7582705,6697756,-8158382,8436543,-834490,8213182,7955484,9301788,-3965915,6695106,2958046,4220538,-1732263,4603891,1820413,-2375960,3307322,-6897837,-7328396,3994855,1670457,4802379,9500275,-4973841,6435679,-2508047,-2857945,8787209,5073647,2437445,-6960737,4894269,-6754068,-5951352,-8733915,-9306475,-3069330,-9730016,-2396084,-562708,-6525755,-9193005,-7951496,6972902,7026903,-4227728,5414457,105055,-6495,-1913030,7710220,-9676812,5250131,5255425,7462450,299297,-7023339,1749846,3787409,6276134,8581007,-4863617,5740055,3220065,8119352,-6690522,-6668242,-2705588,-3735505,9854867,-870839,-7533875,4258816,7006651,97611,1484596,447246,8086362,-8195783,7432420,-8064331,4061543,-1759198,827773,-2911087,-1801717,5831302,9632217,-5222985,-2008043,6370734,6393722,6613069,3896613,6447597,7838593,181922,1794796,-7066675,5994105,8366300,-4970686,1035095,8294630,2312342,3694100,7852462,5632072,-2709999,-3497635,-1183085,-7997083,-5122712,5591450,-887282,-4606981,1303153,-7061717,7463870,-1459331,-1519162,-2029137,478053,9781454,-9906134,7536086,7423964,5706854,6318344,4869850,-7066875,2922225,-5129519,-2346798,-4041358,-1514009,-6964030,467859,9051351,-3170573,-5216420,6325498,-4744077,7351510,1190966,-593265,6213598,2081417,-2342377,238271,4005953,-1968475,4736518,1027965,2656156,1916670,2567170,6363095,-9244914,-9646325,1140048,7640988,3951040,3526918,8029098,1242493,1178720,-1638418,1706933,6205313,3897809,1335406,-1759712,1676509,-9310336,-9153936,8964478,-1242689,-4689574,6806603,-8010723,6758905,5870218,-9363421,2346856,-5739262,1861410,-6073926,-3773123,1166233,-8874291,-3854678,-5858916,7232591,-7645941,-6110615,2467538,-590130,4776092,-6075907,2915401,-5496959,7575289,-3095927,-8967252,2822998,-3458667,4203027,2286731,-3600675,9960082,-8925111,5795919,-1263467,8927344,-2190154,-6376786,-9944444,2355972,-3664430,8307464,-5817397,386223,-318487,-4578705,1675925,-4425604,1564198,-8288950,-7045187,-5419862,5124080,5160927,-242688,5010164,-8424165,9195589,7913699,-5070000,3140890,4834001,7363705,937876,-779704,9523987,-1868952,-5439574,-4525253,-4543448,-9243626,152422,5490046,9066345,2574372,-4697965,5197428,9184963,-4007079,9841805,5487268,2291071,-8057088,8098150,2592293,-7707396,-9093563,-1124539,-6606145], -5703877)
    testcase9 = ([-19, -18, -4, 0, 2, 5, 7, 20], -17)
    print(S.twoSum2(*testcase8))