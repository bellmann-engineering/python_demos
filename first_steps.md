```python
import pandas as pd
```


```python
data = {'First Name': [], 'Last Name': [], 'Country': []}
```


```python
df = pd.DataFrame(data)
```


```python
kai_data = { 'First Name': 'Kai', 'Last Name': 'Bellmann', 'Country': 'Germany' }
df = pd.concat([df, pd.DataFrame( [kai_data] ) ])
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Last Name</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kai</td>
      <td>Bellmann</td>
      <td>Germany</td>
    </tr>
  </tbody>
</table>
</div>




```python
people = [
    {'First Name': 'John', 'Last Name': 'Doe', 'Country': 'USA'},
    {'First Name': 'Emma', 'Last Name': 'Smith', 'Country': 'Canada'},
    {'First Name': 'Maria', 'Last Name': 'Garcia', 'Country': 'Spain'},
    {'First Name': 'Satoshi', 'Last Name': 'Nakamoto', 'Country': 'Japan'},
    {'First Name': 'Luis', 'Last Name': 'Fernandez', 'Country': 'Mexico'},
    {'First Name': 'Elena', 'Last Name': 'Ivanova', 'Country': 'Russia'},
    {'First Name': 'Lucas', 'Last Name': 'Müller', 'Country': 'Germany'},
    {'First Name': 'Isabella', 'Last Name': 'Chen', 'Country': 'China'},
    {'First Name': 'Alessandro', 'Last Name': 'Ricci', 'Country': 'Italy'}
]
```


```python
for person in people:
    df = pd.concat([df, pd.DataFrame( [person] ) ])
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Last Name</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kai</td>
      <td>Bellmann</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>Doe</td>
      <td>USA</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Emma</td>
      <td>Smith</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Maria</td>
      <td>Garcia</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Satoshi</td>
      <td>Nakamoto</td>
      <td>Japan</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Luis</td>
      <td>Fernandez</td>
      <td>Mexico</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Elena</td>
      <td>Ivanova</td>
      <td>Russia</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Lucas</td>
      <td>Müller</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Isabella</td>
      <td>Chen</td>
      <td>China</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Alessandro</td>
      <td>Ricci</td>
      <td>Italy</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Country'] == 'Germany'
```




    0     True
    0    False
    0    False
    0    False
    0    False
    0    False
    0    False
    0     True
    0    False
    0    False
    Name: Country, dtype: bool




```python
df[df['Country'] == 'Germany']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Last Name</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kai</td>
      <td>Bellmann</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Lucas</td>
      <td>Müller</td>
      <td>Germany</td>
    </tr>
  </tbody>
</table>
</div>




```python
mask = df['Country'] == 'Germany'
```


```python
df[mask]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Last Name</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kai</td>
      <td>Bellmann</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Lucas</td>
      <td>Müller</td>
      <td>Germany</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df['First Name'] == 'Emma']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Last Name</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Emma</td>
      <td>Smith</td>
      <td>Canada</td>
    </tr>
  </tbody>
</table>
</div>




```python
mask = (df['First Name'] == 'Emma') & (df['Last Name'] == 'Smith')
```


```python
df[mask]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Last Name</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Emma</td>
      <td>Smith</td>
      <td>Canada</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[(df['First Name'] == 'Emma') & (df['Last Name'] == 'Smith')]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Last Name</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Emma</td>
      <td>Smith</td>
      <td>Canada</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[(df['First Name'] == 'Kai') | (df['First Name'] == 'Kay')]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>First Name</th>
      <th>Last Name</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kai</td>
      <td>Bellmann</td>
      <td>Germany</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
