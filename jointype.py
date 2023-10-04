"""
JoinType - Classe Wrapper di Pandas per la gestione delle join.

Questa classe fornisce metodi per creare join native in pandas e non native (com ela right outer join e la left outer join).

Created on Mon Sep 28 12:30:00 2023
@author: AlanBimbati
"""

import pandas as pd

class JoinType:
    def __init__(self, df_sx, df_dx, keys):
        self.df_sx = df_sx
        self.df_dx = df_dx
        self.keys = keys

    def right_outer_join(self):
        df_merged_inner = self.df_sx.merge(self.df_dx, how="inner", on=self.keys)
        df_merged_right = pd.merge(self.df_sx, self.df_dx, how='right', on=self.keys)

        # elimino la parte inner della right
        df_merged_right = df_merged_right.merge(df_merged_inner, how='left', on=self.keys, indicator=True)
        df_merged_right = df_merged_right[df_merged_right['_merge'] == 'left_only']
        df_merged_right.drop('_merge', axis=1, inplace=True)

        # elimino le colonne _x e _y, creo una nuova colonna come coalesce(colonna_x,colonna_y)
        for col in df_merged_right.columns:
            if col not in self.keys and '_x' in col:
                col = col.replace('_x','')
                df_merged_right[col] = df_merged_right[col+ '_x'].fillna(df_merged_right[col + '_y'])
                df_merged_right.drop(col + '_x', axis=1, inplace=True)
                df_merged_right.drop(col + '_y', axis=1, inplace=True)

        return df_merged_right

    def left_outer_join(self):
        df_merged_inner = self.df_sx.merge(self.df_dx, how="inner", on=self.keys)
        df_merged_left = pd.merge(self.df_sx, self.df_dx, how='left', on=self.keys)

        # elimino la parte inner della left
        df_merged_left = df_merged_left.merge(df_merged_inner, how='right', on=self.keys, indicator=True)
        df_merged_left = df_merged_left[df_merged_left['_merge'] == 'right_only']
        df_merged_left.drop('_merge', axis=1, inplace=True)

        # elimino le colonne _x e _y, creo una nuova colonna come coalesce(colonna_x,colonna_y)
        for col in df_merged_left.columns:
            if col not in self.keys and '_y' in col:
                col = col.replace('_y','')
                df_merged_left[col] = df_merged_left[col+ '_x'].fillna(df_merged_left[col + '_y'])
                df_merged_left.drop(col + '_x', axis=1, inplace=True)
                df_merged_left.drop(col + '_y', axis=1, inplace=True)

        return df_merged_left

    def left_join(self):
        return pd.merge(self.df_sx, self.df_dx, how='left', on=self.keys)

    def right_join(self):
        return pd.merge(self.df_sx, self.df_dx, how='right', on=self.keys)

    def inner_join(self):
        return self.df_sx.merge(self.df_dx, how="inner", on=self.keys)

    def full_outer_join(self):
        return self.df_sx.merge(self.df_dx, how="outer", on=self.keys)
     
"""
Example of usage:

# Crea i DataFrame df_sx e df_dx
df_sx = pd.DataFrame({'chiave1': [1, 2, 3], 'colonna': ['x1', 'x2', 'x3']})
df_dx = pd.DataFrame({'chiave1': [1, 4, 5], 'colonna': ['y1', 'y2', 'y3']})

# Crea un'istanza della classe JoinType
join_type = JoinType(df_sx, df_dx, ['chiave1'])

# Esegue una right outer join
df_merged_right = join_type.right_outer_join()

   chiave1  colonna
3        4          y2
4        5          y3

"""