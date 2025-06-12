const responses = {
  very_good: [
    "와, 오늘 정말 환한 미소였네요! 그 순간을 오래 기억하세요 😊",
    "행복이 전해져요. 이런 날이 더 많이 찾아오길 바라요!"
  ],
  good: [
    "좋은 하루였군요! 소중한 하루를 보내셨어요 🙂",
    "작은 기쁨이라도 챙길 줄 아는 당신, 멋져요!"
  ],
  neutral: [
    "그냥 그랬다고요? 그런 날도 충분히 가치 있어요.",
    "평범함 속에도 소중함이 숨어 있답니다."
  ],
  bad: [
    "조금 힘들었다니… 오늘 정말 잘 버텼어요. 수고 많으셨어요.",
    "짧은 쉬어감이 필요할 때가 있죠. 따뜻한 차 한 잔 어떠세요?"
  ],
  very_bad: [
    "많이 지쳤나 봐요… 당신의 마음을 꼭 안아드리고 싶어요.",
    "어깨 한번 펴고, 깊게 숨을 쉬어보세요. 괜찮다고, 잘하고 있다고요."
  ]
};

document.querySelectorAll('.buttons button').forEach(btn => {
  btn.addEventListener('click', () => {
    const key = btn.dataset.feeling;
    const msgs = responses[key];
    const reply = msgs[Math.floor(Math.random() * msgs.length)];
    document.getElementById('response').textContent = reply;
  });
});
