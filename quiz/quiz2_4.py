'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
<입력>
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다
'''

class Mart_card():
    '''마트'''
    def consume(self,consume):
        self.money -= consume*0.9
        print('마트에서 {}원을 사용했습니다.'.format(consume*0.9))
            
class Movie_card():
    '''영화관'''
    def consume(self,consume):
        self.money -= consume*0.8
        print('영화관에서 {}원을 사용했습니다.'.format(consume*0.8))
        
class Trans_card():
    '''교통'''
    def consume(self,consume):
        self.money -= consume*0.9
        print('교통에서 {}원을 사용했습니다.'.format(consume*0.9))
        
class Multi_card(Mart_card,Movie_card,Trans_card):
    def __init__(self):
        self.money = 0
        print('카드가 발급 되었습니다.')
    
    def charge(self,charge):
        self.money += charge
        print('{}원이 충전되었습니다.'.format(charge))
        
    def consume(self,consume,where):
        if self.money > consume:
            if where == '마트':
                Mart_card.consume(self,consume)
            if where == '영화관':
                Movie_card.consume(self,consume)
            if where == '교통':
                Trans_card.consume(self,consume)

    
    def print(self):
        print('잔액이 {}원 입니다.'.format(self.money))
        

multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()            