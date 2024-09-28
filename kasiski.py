from collections import defaultdict
import math

def kasiski_analysis(ciphertext, sequence_length=5):
    sequences = defaultdict(list)
    
    # Шукаємо повторювані послідовності довжиною sequence_length у шифротексті
    for i in range(len(ciphertext) - sequence_length):
        sequence = ciphertext[i:i + sequence_length]
        for j in range(i + sequence_length, len(ciphertext) - sequence_length):
            if ciphertext[j:j + sequence_length] == sequence:
                sequences[sequence].append(j - i)
    
    distances = []
    # Визначаємо відстані між повторюваними послідовностями
    for positions in sequences.values():
        if len(positions) > 1:
            for i in range(len(positions) - 1):
                distances.append(positions[i + 1] - positions[i])
    
    return distances

def gcd_multiple(numbers):
    return math.gcd(*numbers) if numbers else None

# Приклад використання методу Касіскі
ciphertext = """
KFT OXKIHA KJ IAS TRTHRQI DY HVAJAGHLJ MVOEGH. VF GXJKRL HPV YCW IFNRLYN RWX GITXZR ZQ TFZ'S HGO. 
MVK CGPRKT XL NV LOM TYC HXRNHSYVV XGHU ACVRJVP FOTEEG MT Y GSC MPACTZYA VOJ XTNTVQHBCT OU ZGRSIBTAC IOGPXQ. 
ZYE OGIYCHM, RS AFG JDPSYK, MMTD DY IIIIPAKJK BG R BVBG MU OAKOQPMIIYEAM. 
IOMUV LAC WICK WXJN AKRNXUEU GC PKRUIPDWC IAWTXS HPG ADKFAGT DGVYMJM HVICN EYYGFWTX. AFKJ XL G FPBJV. 
MVUJE DFQ DXGR SEPBRKWSA AKRNXUEU GC PKRUIPDWC IAWTXS HPG RWX ILLIPTCKCS. LFR AFGJC MVKIE PQ YMEX. 
TWLW RPT HNV TSCEK IH CYOB ZGRSIBTAC IOGPXQ FSGE DUJA ZTTIZP. 
RJVPT WY ND QWTF MVOEG HQ R BHFGC DY CE XFAUIAA ZQFI. PUFKH YTV LXZR WGPRVVL, CX BPKJA UGBHZVN. RJRR BG RLA. 
KFT BOEEILCPKF-VSTKUGF FZQABYK OU PGRJXLA ZS AFG PPZS FF JYNZZPG YVEXUE YGH CCE UHAG GC O XLPZQ. 
IAS EICLRGVLIA-IVNIBPA BXLZOBE VD IMBTBZZCXZK ZQ MVK RPNC FD VORZBPU PFR LSKZNV FKJ DPB WARL KE P URRSH. 
KFT AUIAA JKWC HT DAC DQIKH DGIT VD KFT GASJTJR DYIMSX OU RJV PKHOJT, ZWK IAS DOGHJKKW HT RRI AQEQXLHY IC RJV EXFLVCI SUV DY GE XTNGIDTVH DESPSO. 
GC RRIPQV BTLWXVS AM GPDOS RNNAFKEE. SBVN AFKEEH HNRT HPG RGNS TAC ZG NGHJKU. UM RPIBGZ HPZ GKFXVOR SNTNCKFXXG. 
PU GKFXVOR SNTNCKFN WT AC YTKGHM OJ PU WENPKRUEAQSC DYCGSXZSB MH QIRZK. CV CIRXLH ZS LTGI BHFHZD. 
VYC TFZZSI ACE TQDXVSH CXVPNMVOEG. RJFSVAH RNS JCEEJTUK AGL VF IAS RRIPQV GCLHXLMTURU MU OT AGA. 
TXVS RNS TKIRJX GIE AM KFT OXKIHA ORRTKWGCS MMT YC OXK. 
DTFK MVK PDPLV MU JOVW VD WMGF, KHT RAGC HT RLA RJV PKHY IH RJV PKH FF AFG KJLWIZAC. 
WPDF ZYE WMKER HT MITD QW UXSRZNV, VYC TQZFR'Z EIYUM OJ IOC KWEX. 
AAS CIR BG RT VLEV HNFLRCT YPU HRAHFL. RJFQT KNF VV DVLTTHN TWL ULPUTQK DD QQ YI HNVIG NGIGA. 
KHDZC NFD FKRD AFG QNFPUC SV UF PM ZYEXY RVPXE. 
II GU RWX YGERAYVFP, OTU CVR CGUX, KHPA CIR KSGCLN KKIPDKG. 
SPTGIQXMM FF VNKEGDG GSOJA C UDKY FF HPV QWHKY TWHR KFT KUIK PQ ECL, IFMESCZ, KBHGC. 
UJVL VFOKIRZ FZQPZFKV IOC RPIBGZ IH GP YRVCXU LPRJ FXFGKCF. 
YV RTB WOGNGXV P AGE UVP DYZBBM A BQGWSA HNZNV YU JDGU RS OC UMTL TFT HBOZPT WZ. 
AFG MCEM VXRBQG DDK SRKXUE R JLSRVSH RJZLV WY TWHR FLT OJDIGLQ ZR BBZVNHLJA. PEZ RRI GU OJBHK UHLJGJQ.
"""

# Викликаємо метод Касіскі
distances = kasiski_analysis(ciphertext)

# Знаходимо найбільший спільний дільник відстаней
if distances:
    key_length = gcd_multiple(distances)
    print(f"Ймовірна довжина ключа: {key_length}")
else:
    print("Не вдалося знайти повторювані послідовності.")
