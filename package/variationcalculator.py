# process veriations calculator
import ast
import pandas as pd
from typing import Optional,List

class VERIATIONS:
    def __init__(self, columnsTable: pd.DataFrame, RowTable: pd.DataFrame,keyboard:Optional[List]=None) -> None:
        """_summary_

        Args:
            columnsTable (pd.DataFrame): _description_
            RowTable (pd.DataFrame): _description_
        """
        self.columnsTable = columnsTable
        self.RowTable     = RowTable
        self.keyboard     = keyboard

    def formats_and_no_of_patterns(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        col = {}
        for i, v in self.columnsTable.iterrows():
            cd = self.columnsTable.columns.to_list()
            for c in cd:
                sw = None
                try:
                    sw = ast.literal_eval(v[c])
                except Exception as E:
                    sw = v[c]
                if isinstance(sw, list):
                    col[c] = len(sw)
                else:
                    col[c] = 1
        return col

    def row_sequance_veriations(self):
        """_summary_

        Returns:
            columns: list of columns seq veriations
        """
        veriations = []
        for i, v in enumerate(self.RowTable.columns.to_list()):
            s, d = v.split("|")
            s = s.split("+")
            d = d.split("+")
            s = [x.split("?") if "?" in x else [x] for x in s]
            d = [x.split("?") if "?" in x else [x] for x in d]
            veriations.append({i: [s, d]})
        return veriations

    def solve_iteration(self,string,filter_params=[]):
        d=string.split("?")
        d=[[x[0]]*int(x.split("(")[-1][0:-1]) for x in d]
        flat_list = []
        for inner_list in d:
            flat_list.extend(inner_list)
        return flat_list

    def add_data_slices(self,datalist):
        rows=[]
        for x in range(len(datalist[0])):
            data=[d[x] for d in datalist]
            rows.append("".join(data))
        return rows

    def get_column_row_pattern(self,formatpattern,patternseq):
        return "|".join([formatpattern,patternseq])[1:]

    def replace_empty_vals(self,rows):
        for x in rows:
            if "*" in x:
                x=x.replace("*","")
            yield x

    def generate_row_patterns(self):
        rowcolslist=[]
        for x in self.RowTable.columns.to_list():
            x=x.split("|")
            x=[z.split("+") for z in x]
            r=[]
            for s in x:
                w=[]
                for q in s:
                    q=self.solve_iteration(q)
                    w.append(q)
                r.append(self.add_data_slices(w))
            x=[list(self.replace_empty_vals(a)) for a in r]
            rowcolslist.append(x)
        return rowcolslist

    def merge(self,list1, list2):
        merged_list = ["|".join((list1[i], list2[i])) for i in range(0, len(list1))]
        return merged_list

    def get_columnswise_rowpatterns(self):
        colrows=self.generate_row_patterns()
        col=[]
        for x in colrows:
            x=self.merge(x[0],x[1])
            col.append(x)
        dataframeconst={x:y for x,y in enumerate(col)}
        return pd.DataFrame.from_dict(dataframeconst)

    def transform_sequences_to_keyboard_values(self):
        for x,y in self.get_columnswise_rowpatterns().iterrows():
            ye=[]
            for z in self.get_columnswise_rowpatterns().columns.to_list():
                val=y[z]
                val=val.split("|")
                data=self.columnsTable.iloc[0,int(val[0])]
                try:
                    data=ast.literal_eval(data)
                except Exception as E:
                    pass
                if isinstance(data,list):
                    data=data[int(val[1])]
                data2=[]
                for p in data.split("+"):
                    p=self.solve_iteration(p)
                    data2.append(p)
                data2=self.add_data_slices(data2)
                ye.append(data2)
            yield ye

    def format_keyboard_values(self):
        rows=[]
        for x in list(self.transform_sequences_to_keyboard_values()):
            wq=[]
            for z in x:
                pds=[]
                for p in z:
                    if "*" in p:
                        p=p.replace("*","")
                        pds.append(p)
                    else:
                        pds.append(p)
                wq.append(pds)
            rows.append(wq)
        return pd.DataFrame(rows,columns=[x for x in range(len(rows[0]))])

    def traform_keybord_seq_to_data(self):
        df=self.format_keyboard_values()
        result=[]
        for k,v in df.iterrows():
            data     = v.values.tolist()
            if data != [] and self.keyboard is not None:
                datas=[]
                for g in data:
                    try:
                        d=ast.literal_eval(g)
                    except Exception as E:
                        d=g
                    da="".join([self.keyboard[int(e)] for e in d])
                    datas.append(da)
            result.append(datas)
        return pd.DataFrame(result,columns=[x for x in range(len(result[0]))])


