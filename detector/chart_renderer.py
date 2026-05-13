from detector.chart_renderer import render_chart
from detector.image_detector import detect_image_pattern


closes = [
    100, 98, 96, 94, 95, 97, 99,
    97, 95, 94, 96, 99, 103, 106
]

image_path = render_chart(closes)

result = detect_image_pattern(image_path)

print(result)
