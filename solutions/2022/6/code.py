from collections import deque
import typer

queue = deque()

data = "hqhnqhqshhslswsffchfcfbblvlblqlggfwwqfwwqdddbbbhzhjjrqjqbjqjwqjwqwhwrrmcrrjqjjlllcvcrrnpptzpzmmswmmzrzjrrfcrfccpbpzzvrrdndllttwftwwgzzwhwggdvdnnlrnncscbcfcctchcdchdccztzgzjjtdtcdtcchrrgpgzgsgpsggvtvppdccfhcfclfcfdfnddlbbptbtdbtdtjdjgdjjzljlssgbgcgqcqzccfnftfjjsgstggsngsscvssjzjnjtntvnvssrqqhtqtvqtvvjbvvbnvvqvmvrmmdsdvdwwnbnvbnvvcgvcczcfzftfsfrfsfttldtdrrgrgmgbbdvvbqbhqbqlqsqbsbpbgbvgbgwwrswrwrwttvnnzdnzzwggrmrfmmvllzwlwzzlvlbvllgsllpnlnvncvcvqqrwwcmcczhchzczbccdwcwvwzwwvddlwlhljlqjqnncntnctczzmwmlmccpggljlssqswsmmpvmvwvrrcpcrprmprrtdrtdrrsjsmshmmdpdlppbnbvvmmflmmjvjhvhjvjsjbjwjvvblvbvlbbllwlslvljvlvdvdgvgcchnhpnhnvhhtfhhvssczztlzzgvvqqghqgqssdscsnsrsmrmmwgwmgmlmdmggbgzbgzgdzdzccghgfgddtntftddpdrdrmrjmmmzttqmttnwngggtgtqtqnqhnqqpnnntrntrnnshhjtjzzfqqblqqlblslflmlttcwtwzzrlrnrcrrrgtrrftfhthzhggwggvgvvfvddcnddfjddzqzrrvtrvrfrrgpgrgngsgddlmddzgzppdzzjzhjhjhqqbpbvvlrvrsvrvnrrsgsttndnbngnppmlppvgvfggvcvrvnnsnfnnfqfwwppnddrrfqqgbqqfmmlnlnngwgcgjgnjgjsgjgqjjnccdttpqttswwcgcmgmccrppmqmbbfwwvdwdfwfjwfjjblldsdrdvvgcvcwwllfpllcslsvssnvsnvvhnvnvwwcgwccslsbbnlbnbrrrtprptpdpdvdttgsgwswppcdchhqbqcbqbzbgbbstshthsttqgtqtpqqzhhwhghwwmbbdlbbtlltsllbvbnvvmqvqtvqvttlwtltmmrttwgtwwfdddwcchtchhbthbbclczzqbzzpvvwzwswggjddntnrnnwmnnbdbmbccqgqvvsnvvqbvbzvvzmvzzrfrlfrfhhdvddnmnnmhmqhhrhlrldljlbljjgqqvdvhhgmgvgddmmznndmmhssznsswvwdvdzdhhscssntnftfmmrggbmbmgmlltctbtbntnqqscqcscrcrhrlhhdchhzccvvbfvvpfffbwbsbjjmgmwgmgppjnpjphhlmhhpwwhwzhhhzbbzzcbchhpnnptpvphhsdsccffqbqllchlhlwlcljlppnccqsstzstswtwwljwjmmpttvqqspsjjclljqqlhqqtnnbrrsbrbjjllrmrjmjzmmclmclmmcvvbddhnnmhmbbwqqqhrqqtqmqbqdbdtdvvcscshccmffhqffdgdcgddljdjbdbjbdbrrtjjtnntpntpnpmnpmpgghffrnfrnnmdnmnhmmjcjffftrrttfwfvwvcwwrmwmpwmmnvntthmmgmbbcdclcppjhpjhjwwlppgsszqqwggmttfrfqflfsfmmmhchshmmjtjjgdjjnnsvsmsnwcgdfqljmnphlfdrhpggfqnhnszgpndhdqcgfhtdcgbsbtmhvnnrmqzqqcjdqndzbnrhwjvbvcldmnwltgpqbmstntnggtbqjzzqrfdsfttdfrcnsrpwrjrjqbgtjfmlwsrzdbdqvbtczgsjqhtgmctjfmdglfrsvqtgwpbqghzgzdfwzhbdhlmhdvhwjrdhhtjptvwpmjnmfcjdmdczmczvdqwvbgtvlwvwnvdlbqfshmlmvzzcmjbtpwpwgsqhfsgljzhbppcztfjdntzcvllqnzrqjwfjrlgvhmbpvbtqjrdzcsmcjzcdsmvcmhrbhgnscnfrfmscqsqpqplbrzhsrlsvvpmfdtdmtlrtvspmlljmfpshfmstjgnrrwmqlbnwbndcfdstrtqtnzpfqlcgrzmsnmhllljdgtmvftjttbwhqzcqwbwdbshgcqrptfjwbbfsjnvzztlbdchqrlbbrcnsswmhwphfwrbnvrncbrthprmltlwwlfpbqhdfqzwwcwjgqzdnvmhwpzpbtpwwvzcpfcsfqpwjljzzfwzmlfvhsccppzlzjlrvlpdtjpcptnvqjwtdbzrqwnfwmmjndflqqggczrfjlpdfjffctprnmhfdqvnzbfvhszzdmngnlmwzfdrbvlvjnmbllgrczssqcrhbmnpmqlrzgmqmhgsvcdlqnmlhlzvqzhnccbctslzlbcpdvqltqncpcrzwdchrqmwfwlcbcvfnnpjntfrznqdjsdtzqjjttddwvnfqmznhflblzvvtbwdzrrlqlmndzzzwnpbhhlvlbswfjtbnhlccscbnfgjtwbfdlwvzszwnwzhlbcdpvgqjcrpzsvvnfwqcqvrmhzhggvmzwggdpbfrdscjwhsdsbbjcnzldhzcvqtjrhsbfjlrlpvtcqhnnsvslfrdjvjhfhdcfzqchpvvhzbpqglqlrdttrdtndzhnzhtqndghtgmpsnhptprqzhbbdcrgmbvrvqmbptqgnmsccwmhrlpddvmhjntllwrzqwnsjchnblcgndjtmpswwgcstdftqcbhzgttrhnpvrhspjznhhvrlpdqbzzrvzjphcswhljdldvsrdhzltwgrcsvqwnhtqqjjrjgrplzmsnjhzrfbtqgdfgnbpvjrfzrrpdphgzrfbswdhzgbzswqtwwdtrvvswmjvwhqddfzjhgdqsfnwbmlcfwtmpldrdpwjwggbpmncvbghzjmpsqpvnmbhjfzzpsjdgmrtnndhzrphjzdbgrrnthtrfnspdngbdmwbnfjlsndqswfsvfqftqlgqjpfsfpmdbsjfrptvbpvflqgvlmmbchhghhrwmvdlrhlsdtvjjchwglcrwfsfnnbhjbtccbjsfwrbzrvgsbfnvzghhrqblqchjvdtrrbrwwwmfnczzmmrqdggsfrqbldbbfbbcthtsvpcnlbjjztwvhctbrjltqdwbzmrrfslbmjpnqwllbvjzgfsfqqtwbgwgclgdflshfhwggwdqlgbmdmdqglrtfwbddtsltmsvswhgjtqwtnrncpdzhnpfqcjnjzmtbjfzpjwgfbfggmsmfdhfbjctnhchpgfspthdbfpmvrmdbbspvwzqqwnmfwdnnblbcjszbccgflngnjjwsqshfbhjwgzrmvsgnrdbgwfhdvpmznpnvznfcqdclztcptjrrpbmpztwwbvlvtmngfhmfbfmrjbjzlrcvgllrlgthltstnwmffntqrwsrndlzqhztwpcwbdjjztgdzmgtthcvtvnjzzhvstfqhgddddgdsrbcqzqspjrncphhtbnslzphrtfqphffjrrlgwbrwqfzzqvzhnffcwvrncttgplshccglvchvlcbnlthhmzvcrfjvjqfsjjzzgqlpslfwngqnbgcwffpcqhlmlhvwssrpjbrcbftpzbbpptzrdqwpzpdjhtwbvwcqbfnwtflfgzgttglpcwdnzsmjffgfftdnpzlpszmzrrhvlzdfpgbzqlvvfslnndcmjvvpwzwcdzpcttfwbsdswmfqbbhbfbjvbvtspbbhmphzjsjcmmzpvvzhtvzlgwlqqvbnrgtszvghjfmchrwwhpmbsvfmgvqdtmvdtjppchbsgqrtgtnzczqmpgjdbmmflfpjbcdmhldwpgdtdvsbzhztjzfhcsbndfjntbldjnqwdffqspfnlplbtcdjtwdjhldtsdfrnmpfhzghnpcqlhhgblmqjvwhndqfbccvzzlbzbdprvcpwjjhrqnjptwssbjhgvpgtfzqwrzjvbdgwtnmptvdjrffcmbzmzcmrfbjv"


def main(n: int):
    for i, c in enumerate(data):

        queue.append(c)
        print(f"[{i + 1}]: {queue}")

        if len(queue) < n:
            continue

        if len(set(queue)) == n:
            print(f"Result: {i + 1}")
            break

        queue.popleft()


if __name__ == "__main__":
    typer.run(main)