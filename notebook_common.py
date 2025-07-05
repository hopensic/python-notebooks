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

#base_url
base_url="D:/Dropbox/06.wanjuan/02.jp/freq/"
jlpt_url="D:/Dropbox/06.wanjuan/02.jp/pos/"
course_map_url="D:/Dropbox/06.wanjuan/02.jp/course_map/"
article_map_url="D:/Dropbox/06.wanjuan/02.jp/article/"



# 2400 word
r_word_2400_xlsx = base_url+"r_word_2400.xlsx"
r_word_2400_v2_csv = base_url+"r_word_2400_v2.csv"
w_word_2400_csv = base_url+"w_word_2400.csv"
w_word_2400_with_guide_csv = base_url+"w_word_2400_with_guide.csv"
w_word_2400_without_guide_csv = base_url+"w_word_2400_without_guide.csv"
r_final_word_2400_with_freq_csv = base_url+"final/r_final_word_2400_with_freq.csv"
w_final_word_2400_with_freq_and_level_csv = base_url+"final/w_final_word_2400_with_freq_and_level.csv"



# JLPT 难易度词汇
r_jlpt_csv = base_url+"r_jlpt.csv"
r_jlpt_v2_csv = base_url+"r_jlpt_v2.csv"
w_jlpt_csv = base_url+"w_jlpt.csv"
w_jlpt_word_csv = base_url+"w_jlpt_word.csv"
w_jlpt_multiidx_agg_csv = base_url+"w_jlpt_multiidx_agg.csv"

#12000JLPT词汇
r_jlpt_12000_csv = jlpt_url+"r_jlpt_12000.csv"
w_jlpt_12000_csv = jlpt_url+"w_jlpt_12000.csv"

#词性字典表
r_pos_dict_csv = jlpt_url+"r_pos_dict.csv"




#---------------------------书面语---------------------------------
#原始解压的nlt书面语词频文件
r_written_freq_nlt_with_enter_txt = base_url+"r_written_freq_nlt_with_enter.txt"
#格式化后的的书面语词频文件
w_written_freq_nlt_with_enter_csv = base_url+"w_written_freq_nlt_with_enter.csv"
#格式化后分组汇总后的书面语词频文件(因为词语有重复)
w_written_freq_nlt_sumed_csv = base_url+"w_written_freq_nlt_sumed.csv"


#---------------------------口语---------------------------------
#原始解压的nlb口语词频文件
r_spoken_freq_nlb_with_enter_txt = base_url+"r_spoken_freq_nlt_with_enter.txt"
#格式化后的的口语词频文件
w_spoken_freq_nlb_with_enter_csv = base_url+"w_spoken_freq_nlb_with_enter.csv"
#过滤后的的口语词频文件
w_spoken_freq_nlb_with_enter_filtered_csv = base_url+"w_spoken_freq_nlb_with_enter_filtered.csv"
#增加headword-reading-type字段后的的口语词频文件
w_spoken_freq_nlb_with_enter_filtered_hrt_csv = base_url+"w_spoken_freq_nlb_with_enter_filtered_hrt.csv"
#对headword, reading字段分组后的语词频文件
w_spoken_freq_nlb_with_enter_filtered_hr_csv = base_url+"w_spoken_freq_nlb_with_enter_filtered_hr.csv"
#格式化后分组汇总后的口语词频文件
w_spoken_freq_nlb_sumed_csv = base_url+"w_spoken_freq_nlb_sumed.csv"

#---------------------------合并书面语和口语---------------------------------
#书面语和口语词汇汇总数据
w_merged_freq_sumed_csv = base_url+"w_merged_freq_sumed.csv"
#原始--书面语和口语词汇汇总数据
w_raw_merged_freq_sumed_csv = base_url+"w_raw_merged_freq_sumed.csv"
#原始--书面语和口语词汇汇总数据-以word作为分组
w_word_raw_merged_freq_sumed_csv = base_url+"w_word_raw_merged_freq_sumed.csv"


#---------------------------base_structure---------------------------------
#发音词频表
r_pron_freq_csv = base_url+"r_pron_freq.csv"
#基础词频表
r_base_freq_csv = base_url+"r_base_freq.csv"


# 临时文件
w_tmp_csv = base_url+"w_tmp_csv.csv"


#---------------------------course_map(课程地图)---------------------------------
#课程地图单元主表（course_map_unit)
w_course_map_unit_csv=course_map_url+"w_course_map_unit.csv"
#关卡表(course_stage)
w_course_stage_csv=course_map_url+"w_course_stage.csv"
#五十音表(fifty tones)
w_fifty_tones_csv=course_map_url+"w_fifty_tones.csv"
#生词表(new_words)
w_new_words_csv=course_map_url+"w_new_words.csv"
#组句句子表(sentence_formation
w_sentence_formation_csv=course_map_url+"w_sentence_formation.csv"
#组句句子单词表(sentence_word_formation)
w_sentence_word_formation_csv=course_map_url+"w_sentence_word_formation.csv"
#阅读文章表(需要和文章主表关联，通过主键关联)(article_stage_rel)
w_article_stage_rel_csv=course_map_url+"w_article_stage_rel.csv"
#闯关问题关联表(需要和问题主表关联，通过主键关联)(question_stage_rel)
w_question_stage_rel_csv=course_map_url+"w_question_stage_rel.csv"


#---------------------------文章句子问题选项---------------------------------
#日语文章表(article_jap)
w_article_jap_csv=article_map_url+"w_article_jap.csv"
#日语文章句子表(article_sentence_jap)
w_article_sentence_jap_csv=article_map_url+"w_article_sentence_jap.csv"
#问题表(question_jap)
w_question_jap_csv=article_map_url+"w_question_jap.csv"
#问题选项表(article_question_option_jap)
w_article_question_option_jap_csv=article_map_url+"w_article_question_option_jap.csv"


#---------------------------摸底测试问题和选项---------------------------------
#问题表(modi_question)
w_modi_question_csv=article_map_url+"w_modi_question.csv"
#问题选项表(modi_question_option)
w_modi_question_option_csv=article_map_url+"w_modi_question_option.csv"









#---------------------------音频文件---------------------------------
r_voice_txt=base_url+"Forvo-Japanese.txt"
r_voice_csv=base_url+"final/r_voice.csv"





# 将日文字符转换为unicode编码
def get_unicode_codepoints(text):
    """将文本中每个字符转换为4位十六进制Unicode码点字符串（无U+前缀）"""
    return "".join([f"{ord(char):04X}" for char in text])


#检测编码
def check_encoding(file_path):
    with open(file_path, "rb") as f:
        result = chardet.detect(f.read())
        print(f"检测到编码: {result['encoding']}")


def rd_csv_sig(path, index_columns=None):
    return pd.read_csv(
        path,
        encoding="utf-8-sig",
        on_bad_lines="skip",
        engine="python",
        index_col=index_columns,
    )


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






