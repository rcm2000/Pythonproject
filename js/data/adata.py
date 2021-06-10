import json


class Adata:
    def aj011(self):
        data = [
            {'id': 'id01', 'pwd': 'pwd01', 'age': 10},
            {'id': 'id02', 'pwd': 'pwd02', 'age': 20},
            {'id': 'id03', 'pwd': 'pwd03', 'age': 30},
            {'id': 'id04', 'pwd': 'pwd04', 'age': 40},
            {'id': 'id05', 'pwd': 'pwd05', 'age': 50}

        ];
        return data
    def aj02(self,cmd):
        data = [];
        if cmd == 'a':
            data = [{'location':'seoul','datas':[10,20,30,40,50]}];
        else:
            data = [{'location':'busan','datas':[15,25,35,45,55]}];
        return data;

    def aj03(self,cmd):
        data = [];
        if cmd == 't':
            data = [{
                'name': 'Tokyo',
                'data': [7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
            }, ];
        elif cmd == 'l':
            data = [{
                'name': 'London',
                'data': [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
            }];
        elif cmd == 'a':
            data = [{
                'name': 'Tokyo',
                'data': [7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
            },
                {
                    'name': 'London',
                    'data': [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
                }
            ];
        return data;


if __name__ == '__main__':
    result = Adata().aj02('a');
    jresult = json.dumps(result);
    print(jresult);


