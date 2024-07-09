크게 보면 4가지 단계로 이루어 진것 같다.
- generate(text)
  - process_text(text)
  - generate_from_frequencies(words)
- to_image()
  - Image()
  - ImageDraw()
- to_svg()
- to_file(filename)


## generate(text)

- process_text(text)
  - 텍스트를 처리하여 단어 토큰을 추출하고, 불용어를 제거한 뒤 단어의 빈도를 계산하는 기능을 수행한다

- generate_from_frequencies(words)
  - 입력된 단어의 빈도에 따라 적절한 크기와 위치로 워드클라우드를 생성하는 과정을 보여준다
    -  폰트 사이즈 결정하는 부분 <br>
        ```
        for word, freq in frequencies:
            if freq == 0:
                continue
            rs = self.relative_scaling
            if rs != 0:
                font_size = int(round((rs * (freq / float(last_freq)) + (1 - rs)) * font_size))
        ```
    - 회전 시킬지 말지 결정하는 부분 <br>
        ```
        if random_state.random() < self.prefer_horizontal:
                orientation = None
            else:
                orientation = Image.ROTATE_90
        ```

    - 어디에 위치시킬지 결정하는 부분 <br>
        ```
        result = occupancy.sample_position(box_size[3] + self.margin, box_size[2] + self.margin, random_state)
        ```

    - 폰트의 회전 적용 <br>
        ```
        transposed_font = ImageFont.TransposedFont(font, orientation=orientation)
        ```

## to_image()

워드 클라우드를 이미지 형식으로 변환하는 기능을 수행한다.

- 각 단어를 그리는 부분
    ```
        img = Image.new(self.mode, (int(width * self.scale),
                                    int(height * self.scale)),
                        self.background_color)
        draw = ImageDraw.Draw(img)
        for (word, count), font_size, position, orientation, color in self.layout_:
            font = ImageFont.truetype(self.font_path,
                                      int(font_size * self.scale))
            transposed_font = ImageFont.TransposedFont(
                font, orientation=orientation)
            pos = (int(position[1] * self.scale),
                   int(position[0] * self.scale))
            draw.text(pos, word, fill=color, font=transposed_font)
    ```

## to_svg()

워드 클라우드를 SVG 형식으로 내보내는 기능을 수행한다.

## ro_file(filename)

워드 클라우드를 이미지 파일로 내보내는 기능을 수행한다.