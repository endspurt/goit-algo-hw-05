# Vergleich der Suchalgorithmen: Boyer-Moore, Knuth-Morris-Pratt und Rabin-Karp

## Einleitung
Dieser Bericht vergleicht die Effizienz der Suchalgorithmen Boyer-Moore, Knuth-Morris-Pratt und Rabin-Karp anhand zweier Textdateien. Die Algorithmen wurden sowohl auf ein vorhandenes als auch ein nicht vorhandenes Muster getestet. Die Zeitmessung erfolgte mit `timeit`.

### Text 1

| Algorithmus | Vorhandenes Muster (Sek.) | Nicht vorhandenes Muster (Sek.) |
|-------------|---------------------------|----------------------------------|
| Boyer-Moore      | 0.000011                  | 0.000010                         |

### Text 2

| Algorithmus | Vorhandenes Muster (Sek.) | Nicht vorhandenes Muster (Sek.) |
|-------------|---------------------------|----------------------------------|
| Boyer-Moore      | 0.000008                  | 0.000007                         |

### Text 1

| Algorithmus | Vorhandenes Muster (Sek.) | Nicht vorhandenes Muster (Sek.) |
|-------------|---------------------------|----------------------------------|
| Knuth-Morris-Pratt      | 0.000030                  | 0.000031                         |

### Text 2

| Algorithmus | Vorhandenes Muster (Sek.) | Nicht vorhandenes Muster (Sek.) |
|-------------|---------------------------|----------------------------------|
| Knuth-Morris-Pratt      | 0.000031                  | 0.000035                         |

### Text 1

| Algorithmus | Vorhandenes Muster (Sek.) | Nicht vorhandenes Muster (Sek.) |
|-------------|---------------------------|----------------------------------|
| Rabin-Karp      | 0.000037                  | 0.000029                         |

### Text 2

| Algorithmus | Vorhandenes Muster (Sek.) | Nicht vorhandenes Muster (Sek.) |
|-------------|---------------------------|----------------------------------|
| Rabin-Karp      | 0.000029                  | 0.000048                         |

## Zusammenfassung
Die Ergebnisse zeigen, dass alle drei Algorithmen (Boyer-Moore, Knuth-Morris-Pratt und Rabin-Karp) bei den verwendeten Texten nahezu identische Suchgeschwindigkeiten aufwiesen. Dies könnte auf die geringe Textlänge und die Einfachheit der Muster zurückzuführen sein. Weitere Tests mit längeren Texten und komplexeren Mustern könnten Unterschiede in der Effizienz der Algorithmen deutlicher machen.
