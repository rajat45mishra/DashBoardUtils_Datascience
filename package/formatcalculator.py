from package.keyborddata import *
from typing import Dict, List, Any
import itertools
    

class FormatCalculator:
    
    """FormatCalculator class fetches formets from any type of data input data should be in df or records format and helps us to do \n
     analysis over it to fetch format and itration format and seeds from data then we must able to regenerate that data by having following receipies\n
        --- data formats\n
        --- itration format\n
        --- itration format seeds\n
        --- data format seeds\n
    Format Calculator class have following features\n
       -- regex_formattor (groups regex string and generate optimised regex generated by FormatCalculator inputargs:[cls,str])\n
       -- get_unique_hashes_from_data ( gets uniques hashes from data columns wise  inputargs:[cls,LIST[ANY]])\n
       -- split_all_labels_to_words_with_new_cols ( splits string and create new cols in dataframe inputargs:[cls,Dataframe,exer=[" "]])\n
       -- hash_df_single_df_column ( hashes single df col inputargs:[cls,pd.Series])\n
       -- hash_df_formats ( hashes all data in dataframe ) inputargs:[cls,pd.Dataframe]\n
       -- get_unique_hashes_from_df_columnwise ( column wise hashes generater in records format inputargs:[cls,pd.DataFrame])\n

    """

    @classmethod
    def regex_formattor(cls, value):
        """(groups regex string and generate optimised regex generated by FormatCalculator inputargs:[cls,str])"""
        s = "".join(ch for ch, _ in itertools.groupby(value))
        formats = ["[a-z]{1}", "[A-Z]{1}", "\\d{1}", "\\s"]
        hashs = []
        rowhash = ""
        for x in s:
            rowhash += x
            if len(rowhash) == 8 and rowhash in formats:
                if hashs == []:
                    hashs.append(rowhash)
                else:
                    mat = hashs[-1][0:6] + "1" + hashs[-1][-1]
                    if mat == rowhash:
                        ha = list(hashs[-1])
                        ha[-2] = str(int(hashs[-1][-2]) + 1)
                        hashs[-1] = "".join(ha)
                    else:
                        hashs.append(rowhash)
                rowhash = ""
            elif len(rowhash) == 2 and rowhash in formats:
                hashs.append(rowhash)
                rowhash = ""
            elif len(rowhash) == 5 and rowhash in formats:
                if hashs == []:
                    hashs.append(rowhash)
                else:
                    mat = hashs[-1][0:4] + "1" + hashs[-1][-1]
                    if mat == rowhash:
                        ha = list(hashs[-1])
                        ha[-2] = str(int(hashs[-1][-2]) + 1)
                        hashs[-1] = "".join(ha)
                    else:
                        hashs.append(rowhash)
                rowhash = ""
        return "".join(hashs)

    @classmethod
    def get_unique_hashes_from_data(cls, chuncks: List[Any]):
        """( gets uniques hashes from data columns wise  inputargs:[cls,LIST[ANY]])"""
        import pandas as pd
        df = pd.DataFrame.from_records(chuncks).fillna("0")
        cols = df.columns.to_list()
        df_list = []
        for x in cols:
            d = df[df[x] != "0"]
            df_list.append(d[x])

        series_list = []
        for s in df_list:
            lables = []
            for e in s:
                lables += e["lables"]

            unique_lables = []
            for xsa in lables:
                if xsa not in unique_lables:
                    unique_lables.append(xsa)
            series_list.append(unique_lables)

        hash_list = []
        for x in series_list:
            hash_lables = []
            for q in x:
                datalen = len(q)
                hash = r""
                for xs in range(datalen):
                    if str(q[xs]) in alphabets:
                        hash += "[a-z]{1}"
                    elif str(q[xs]) in alphabets_upper:
                        hash += "[A-Z]{1}"
                    elif str(q[xs]) in simbols:
                        hash += str(q[xs])
                    else:
                        data = None
                        try:
                            data = int(q[xs])
                        except Exception as E:
                            if q[xs] == " ":
                                hash += "\s"
                            else:
                                hash += q[xs]
                        if data is not None:
                            hash += "\d{1}"
                hash_lables.append(hash)
            hash_list.append(hash_lables)

        unique_hashes = []
        for i, x in enumerate(hash_list):
            unique_hashes.append({cols[i]: list(set(x))})
        return unique_hashes

    @classmethod
    def split_all_labels_to_words_with_new_cols(cls, df, exer=[" "]):
        """(splits string and create new cols in dataframe inputargs:[cls,Dataframe,exer=[" "]])"""
        import pandas as pd
        numdata = df
        df = df.select_dtypes(include=["object"])
        cols_to_select = set(numdata.columns.to_list()) - set(df.columns.to_list())
        result = df.to_dict("records")
        cols = df.columns.to_list()
        final_df = []
        for v in result:
            for x in cols:
                val = None
                for s in exer:
                    if type(v[x]) != list:
                        if s in v[x]:
                            val = v[x].split(s)
                        else:
                            val = v[x]
                v[x] = val
            final_df.append(v)
        df_list = []
        for v in final_df:
            cd = {}
            for d, n in v.items():
                if type(n) == list:
                    for i, xs in enumerate(n):
                        if i == 0:
                            cd[d] = xs
                        else:
                            cd["_".join([d, str(i)])] = xs
                else:
                    cd[d] = n
            df_list.append(cd)
        return pd.DataFrame.from_records(df_list).join(numdata[list(cols_to_select)])

    @classmethod
    def hash_df_single_df_column(cls, Series):
        """( hashes single df col inputargs:[cls,pd.Series])"""
        for k, v in Series.items():
            hash = ""
            for x in str(v):
                if str(x) in alphabets:
                    hash += "[a-z]{1}"
                elif str(x) in alphabets_upper:
                    hash += "[A-Z]{1}"
                elif str(x) in simbols:
                    hash += str(x)
                else:
                    data = None
                    try:
                        data = int(x)
                    except Exception as E:
                        if x == " ":
                            hash += "\s"
                        else:
                            hash += x
                    if data is not None:
                        hash += "\d{1}"
            yield k, hash

    @classmethod
    def hash_df_formats(cls, df):
        """( hashes all data in dataframe ) inputargs:[cls,pd.Dataframe]"""
        import pandas as pd
        df_list = []
        for x, s in df.iterrows():
            value = None
            idx = [sa[0] for sa in list(cls.hash_df_single_df_column(s))]
            vals = [sw[1] for sw in list(cls.hash_df_single_df_column(s))]
            value = pd.Series(vals, index=idx)
            df_list.append(value.to_dict())
        return pd.DataFrame.from_records(df_list)

    @classmethod
    def get_unique_hashes_from_df_columnwise(cls, df):
        """( column wise hashes generater in records format inputargs:[cls,pd.DataFrame] )"""
        for x in df.columns.to_list():
            yield (x, df[x].unique().tolist())
