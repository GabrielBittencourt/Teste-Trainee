SELECT nomeprof, numhoras
FROM PROFESSOR, HORARIO
WHERE PROFESSOR.codprof = PROFTURMA.codprof and PROFTURMA.coddepto = TURMA.coddepto and TURMA.coddepto = HORARIO.coddepto  