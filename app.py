from flask import Flask, render_template, request
import random

app = Flask(__name__)

# 감정별 응답 메시지 사전 (기존 것 그대로)
responses = {
    'very_good': [
        "기분이 정말 좋으셨군요! 당신이 행복하다는 말에 저도 덩달아 미소가 지어져요. 오늘 밤은 행복한 꿈 꾸시길!",
        "내일도 오늘같이 행복한 하루가 될 거예요!! 남은 하루도 즐겁게 마무리 하세요! "
    ],
    'good': ["나쁘지 않은 하루였다니 다행이에요. 때로는 평범한 하루가 주는 소소한 안정감이 가장 큰 행복이 될 수 있죠. 당신의 오늘을 응원합니다!",
        "그럭저럭 괜찮은 하루였군요. 작은 만족들이 모여 내일을 위한 에너지가 될 거예요. 당신은 오늘도 충분히 잘 해냈어요."

    ],
    'neutral': [
        "오늘은 감흥 없는 하루였나 보네요. 그럴 수도 있죠. 복잡하게 생각하지 않아도 괜찮아요. 그저 숨 쉬고 존재한 것만으로도 당신은 충분해요.",
        "딱히 좋지도 나쁘지도 않았군요. 모든 하루가 드라마 같을 필요는 없어요. 당신의 마음이 고요하게 흘러갔다면 그걸로 충분합니다."
    ],
    'bad': [
        "조금 힘드셨군요... 혼자 힘들어하지 않아도 괜찮아요. 잠시 쉬어가도 좋고, 누군가에게 기대도 괜찮아요. 당신은 충분히 잘하고 있어요.",
        "오늘 하루 어깨에 작은 짐이 올려졌군요. 괜찮아요, 잠시 그 짐을 내려놓고 숨을 깊게 들이쉬세요. 내일은 좀 더 가벼워질 거예요."
    ],
    'very_bad': [
        "많이 지치셨군요... 얼마나 힘드셨을지 감히 헤아릴 수 없을 만큼 마음이 아파요. 오늘은 아무것도 하지 않아도 괜찮아요. 당신의 지친 몸과 마음이 푹 쉴 수 있기를 바라요.",
        "어깨 한번 펴고, 깊게 숨을 쉬어보세요. 괜찮다고, 잘하고 있다고요."
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/response', methods=['POST'])
def response_page():
    feeling = request.form.get('feeling', 'neutral')
    if feeling not in responses:
        feeling = 'neutral'
    message = random.choice(responses[feeling])
    return render_template('response.html',
                           message=message,
                           feeling=feeling)

if __name__ == '__main__':
    app.run(debug=True)
