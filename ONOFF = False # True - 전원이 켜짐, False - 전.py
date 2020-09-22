ONOFF = False # True - 전원이 켜짐, False - 전원이 꺼짐
VOLUMN = 1    # 볼륨 크기 (1~20)
CHANNEL = 1   # 채널 번호 (1~10)
def setVolumnUp (size):
  global VOLUMN
  if VOLUMN+size>20:
    VOLUMN=20
  else:
    VOLUMN+=size

def setVolumnDown (size):
  global VOLUMN
  if VOLUMN+size<1:
    VOLUMN=1
  else:
    VOLUMN+=size

def setChannelUp (size):
  global CHANNEL
  if CHANNEL+size>10:
    CHANNEL=10
  else:
    CHANNEL+=size

def setChannelDown (size):
  global CHANNEL
  if CHANNEL+size<1:
    CHANNEL=1
  else:
    CHANNEL+=size




 
def power ():
  global ONOFF

  if ONOFF==False:
    print("전원을 킵니다.")
    ONOFF=True
  else :
    print("전원을 끕니다.")
    ONOFF=False


while True:
  print("="*50)
  print("1.전원 끄기")
  print("2.전원 켜기")
  print("3.볼륨 조절")
  print("4.채널 조절")
  print("5.현재의 상태 출력")
  print("6.프로그램 종료")
  print("="*50)

  want=int(input("원하는 기능의 번호를 입력하세요>>"))

  
  if want==1:
    if ONOFF==False:
      print("이미 꺼져있습니다.")
    else:
      power()

  elif want==2:
    if ONOFF==True:
      print("이미 켜져있습니다.")
    else:
      power()


  elif want==3:
    if ONOFF==False:
      print("tv가 꺼져있습니다.")
    else:
      volumn_user=int(input("볼륨 조절값을 입력해 주세요>>"))
      if volumn_user>=0:
        setVolumnUp(volumn_user)
      else:
        setVolumnDown(volumn_user)

    





  elif want ==4:
    if ONOFF==False:
      print("TV가 꺼져있습니다.")
    else:
      channel_user=int(input("채널 변동값을 입력해 주세요>>"))
      if channel_user>0:
        setChannelUp(channel_user)
      else:
        setChannelDown(channel_user)


  elif want==5:
    if ONOFF==True:
      print("현재 TV가 켜져있고")
    else:
      print("현재 TV가 꺼져있고")

    print("현재 볼륨은",VOLUMN,"이고")
    print("현재 채널은",CHANNEL,"번 입니다.")
  elif want == 6:
    print("프로그램을 종료합니다.")
    break
  else :
    print("입력할 수 있는 기능은 1~6번까지입니다.")


