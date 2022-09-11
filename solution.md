# 문제 풀이

```
1.1.1.1;c''at$IFS*flag.txt
```

1.1.1.1로 ping을 보낸 후 ; 로 탈출,
''로 cat 단언 필터링을 우회한 후 $IFS로 공백을 넣어준 후 *flag.txt로 flag.txt를 읽어온다.