# JoinType

**Classe Wrapper di Pandas per la gestione delle join**

Questa classe fornisce metodi per creare join native in pandas e non native (come la right outer join e la left outer join).

**Esempio di utilizzo:**

```python
# Crea i DataFrame df_sx e df_dx
df_sx = pd.DataFrame({'chiave1': [1, 2, 3], 'colonna': ['x1', 'x2', 'x3']})
df_dx = pd.DataFrame({'chiave1': [1, 4, 5], 'colonna': ['y1', 'y2', 'y3']})

# Crea un'istanza della classe JoinType
join_type = JoinType(df_sx, df_dx, ['chiave1'])

# Esegue una right outer join
df_merged_right = join_type.right_outer_join()

print(df_merged_right)
```
  chiave1  colonna
3        4          y2
4        5          y3


**Funzioni disponibili:**

* `right_outer_join()`: esegue una right outer join sui due DataFrame.
* `left_outer_join()`: esegue una left outer join sui due DataFrame.
* `left_join()`: esegue una left join sui due DataFrame.
* `right_join()`: esegue una right join sui due DataFrame.
* `inner_join()`: esegue una inner join sui due DataFrame.
* `full_outer_join()`: esegue una full outer join sui due DataFrame.

**Note:**

* Le join non native (right outer join e left outer join) sono implementate utilizzando join inner e merge multiple.
* Le colonne `_x` e `_y` vengono aggiunte ai DataFrame risultanti dalle join non native. Queste colonne contengono i valori delle colonne corrispondenti dei DataFrame originali.
* Le colonne `_x` e `_y` vengono eliminate dai DataFrame risultanti dalle join non native, insieme a una colonna `_merge` che indica se la riga proviene dalla join inner o dalla merge multiple.
* Le colonne corrispondenti dei DataFrame originali vengono unite utilizzando la funzione `coalesce()` di pandas.

**Spero che questo codice sia utile!**

**Installazione:**

git clone https://github.com/alanbimbati/JoinType

