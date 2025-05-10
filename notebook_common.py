import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import chardet
import re
from itertools import islice


# 解析书面语正则
pattern_table_written = re.compile(r"<table[\s\S]+?>[\s\S]+?<\/table>")
pattern_td_written = re.compile(r"<td><span class=\"\w+\">(.+?)[\s]?</span></td>")

#解析口头语正则
pattern_table_spoken = re.compile(r"<table[\s\S]+?>[\s\S]+?<\/table>")
pattern_td_spoken = re.compile(r"<td><span class=\"\w+\">(.+?)[\s]?</span></td>")

#解析音频文件正则
pattern_voice = re.compile(r"<table[\s\S]+?>[\s\S]+?<\/table>")


# 2400 word
r_word_2400_xlsx = "D:/05.japanproject/jp/freq/r_word_2400.xlsx"
w_word_2400_csv = "D:/05.japanproject/jp/freq/w_word_2400.csv"
w_word_2400_with_guide_csv = "D:/05.japanproject/jp/freq/w_word_2400_with_guide.csv"
w_word_2400_without_guide_csv = "D:/05.japanproject/jp/freq/w_word_2400_without_guide.csv"
r_final_word_2400_with_freq_csv = "D:/05.japanproject/jp/freq/final/r_final_word_2400_with_freq.csv"
w_final_word_2400_with_freq_and_level_csv = "D:/05.japanproject/jp/freq/final/w_final_word_2400_with_freq_and_level.csv"



# JLPT 难易度词汇
r_jlpt_csv = "D:/05.japanproject/jp/freq/r_jlpt.csv"
w_jlpt_csv = "D:/05.japanproject/jp/freq/w_jlpt.csv"
w_jlpt_word_csv = "D:/05.japanproject/jp/freq/w_jlpt_word.csv"


#---------------------------书面语---------------------------------
#原始解压的nlt书面语词频文件
r_written_freq_nlt_with_enter_txt = "D:/05.japanproject/jp/freq/r_written_freq_nlt_with_enter.txt"
#格式化后的的书面语词频文件
w_written_freq_nlt_with_enter_csv = "D:/05.japanproject/jp/freq/w_written_freq_nlt_with_enter.csv"
#格式化后分组汇总后的书面语词频文件(因为词语有重复)
w_written_freq_nlt_sumed_csv = "D:/05.japanproject/jp/freq/w_written_freq_nlt_sumed.csv"


#---------------------------口语---------------------------------
#原始解压的nlb口语词频文件
r_spoken_freq_nlb_with_enter_txt = "D:/05.japanproject/jp/freq/r_spoken_freq_nlt_with_enter.txt"
#格式化后的的口语词频文件
w_spoken_freq_nlb_with_enter_csv = "D:/05.japanproject/jp/freq/w_spoken_freq_nlb_with_enter.csv"
#过滤后的的口语词频文件
w_spoken_freq_nlb_with_enter_filtered_csv = "D:/05.japanproject/jp/freq/w_spoken_freq_nlb_with_enter_filtered.csv"
#增加headword-reading-type字段后的的口语词频文件
w_spoken_freq_nlb_with_enter_filtered_hrt_csv = "D:/05.japanproject/jp/freq/w_spoken_freq_nlb_with_enter_filtered_hrt.csv"
#对headword, reading字段分组后的语词频文件
w_spoken_freq_nlb_with_enter_filtered_hr_csv = "D:/05.japanproject/jp/freq/w_spoken_freq_nlb_with_enter_filtered_hr.csv"
#格式化后分组汇总后的口语词频文件
w_spoken_freq_nlb_sumed_csv = "D:/05.japanproject/jp/freq/w_spoken_freq_nlb_sumed.csv"

#---------------------------合并书面语和口语---------------------------------
#书面语和口语词汇汇总数据
w_merged_freq_sumed_csv = "D:/05.japanproject/jp/freq/w_merged_freq_sumed.csv"
#原始--书面语和口语词汇汇总数据
w_raw_merged_freq_sumed_csv = "D:/05.japanproject/jp/freq/w_raw_merged_freq_sumed.csv"

# 临时文件
w_tmp_csv = "D:/05.japanproject/jp/freq/w_tmp_csv.csv"
#---------------------------音频文件---------------------------------
r_voice_txt="D:/05.japanproject/jp/freq/Forvo-Japanese.txt"
r_voice_csv="D:/05.japanproject/jp/freq/final/r_voice.csv"





# 将日文字符转换为unicode编码
def get_unicode_codepoints(text):
    """将文本中每个字符转换为4位十六进制Unicode码点字符串（无U+前缀）"""
    return "".join([f"{ord(char):04X}" for char in text])


#检测编码
def check_encoding(file_path):
    with open(file_path, "rb") as f:
        result = chardet.detect(f.read())
        print(f"检测到编码: {result['encoding']}")


def to_csv_sig(df,path,need_index=False):        
    df.to_csv(path, index=need_index, encoding="utf-8-sig")


def read_excel(path,sheet_name):
    return pd.read_excel(path, sheet_name=sheet_name)


def fetch_random_from_set(my_set,n=5):
    print(list(islice(my_set,n)))
    





def p(ob):
    print(ob)
def l(ob="",len_dash=40):
    s = "-" * len_dash
    print(f'{s}{ob}{s}')






