# 람다 함수를 활용한 다양한 정렬 예시

print("=== 람다 함수 정렬 완전 정복 ===\n")

# 원본 코드 실행
print("📝 원본 코드:")
a = [(1, 2), (3, 1), (5, 0)]
print(f"정렬 전: {a}")
a.sort(key=lambda x: x[1])  # 튜플의 두 번째 요소 기준 정렬
print(f"정렬 후: {a}")
print()

print("="*50)

# 예시 1: 첫 번째 요소 기준 정렬
print("\n📝 예시 1: 첫 번째 요소 기준 정렬")
b = [(5, 0), (1, 2), (3, 1)]
print(f"정렬 전: {b}")
b.sort(key=lambda x: x[0])  # 첫 번째 요소 기준
print(f"정렬 후: {b}")

# 예시 2: 내림차순 정렬
print("\n📝 예시 2: 두 번째 요소 기준 내림차순")
c = [(1, 2), (3, 1), (5, 0)]
print(f"정렬 전: {c}")
c.sort(key=lambda x: x[1], reverse=True)  # 내림차순
print(f"정렬 후: {c}")

# 예시 3: 문자열 길이 기준 정렬
print("\n📝 예시 3: 문자열 길이 기준 정렬")
words = ["python", "java", "c", "javascript", "go"]
print(f"정렬 전: {words}")
words.sort(key=lambda x: len(x))  # 문자열 길이 기준
print(f"정렬 후: {words}")

# 예시 4: 절댓값 기준 정렬
print("\n📝 예시 4: 절댓값 기준 정렬")
numbers = [-5, 3, -1, 8, -2]
print(f"정렬 전: {numbers}")
numbers.sort(key=lambda x: abs(x))  # 절댓값 기준
print(f"정렬 후: {numbers}")

# 예시 5: 복합 조건 정렬 (우선순위 정렬)
print("\n📝 예시 5: 복합 조건 정렬")
students = [("김철수", 85, 2), ("이영희", 95, 1), ("박민수", 85, 3)]
print("학생 데이터: (이름, 점수, 학번)")
print(f"정렬 전: {students}")

# 점수 내림차순, 점수 같으면 학번 오름차순
students.sort(key=lambda x: (-x[1], x[2]))
print(f"정렬 후: {students}")
print("해석: 점수 높은 순, 점수 같으면 학번 낮은 순")

# 예시 6: 딕셔너리 정렬
print("\n📝 예시 6: 딕셔너리 정렬")
people = [
    {"name": "김철수", "age": 25, "score": 85},
    {"name": "이영희", "age": 23, "score": 95}, 
    {"name": "박민수", "age": 27, "score": 80}
]

print("나이 기준 정렬:")
people_by_age = sorted(people, key=lambda x: x["age"])
for p in people_by_age:
    print(f"  {p['name']}: {p['age']}세")

print("\n점수 기준 내림차순 정렬:")
people_by_score = sorted(people, key=lambda x: x["score"], reverse=True)
for p in people_by_score:
    print(f"  {p['name']}: {p['score']}점")

print("\n" + "="*50)

print("\n🎯 람다 함수 핵심 패턴:")
print("1. 기본: list.sort(key=lambda x: x[인덱스])")
print("2. 내림차순: list.sort(key=lambda x: x[인덱스], reverse=True)")
print("3. 절댓값: list.sort(key=lambda x: abs(x))")
print("4. 길이: list.sort(key=lambda x: len(x))")
print("5. 복합조건: list.sort(key=lambda x: (조건1, 조건2))")
print("6. 딕셔너리: list.sort(key=lambda x: x['키'])")

print("\n💡 실전 팁:")
print("- sort(): 원본 리스트 수정")
print("- sorted(): 새로운 리스트 반환")
print("- 복합조건에서 내림차순: -를 앞에 붙이거나 reverse=True")
print("- 문자열은 사전순, 숫자는 크기순 정렬")

print("\n🔥 코딩테스트 자주 나오는 패턴:")
print("- 좌표 정렬: points.sort(key=lambda x: (x[0], x[1]))")
print("- 구간 정렬: intervals.sort(key=lambda x: x[1])  # 끝점 기준")
print("- 우선순위: tasks.sort(key=lambda x: (-x[0], x[1]))  # 중요도↓, 시간↑")
