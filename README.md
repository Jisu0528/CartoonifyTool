## CartoonifyTool
CartoonifyTool은 OpenCV를 사용하여 이미지를 카툰 스타일로 변환하는 간단한 프로그램입니다.

- `cv2.Canny()`를 이용하여 edge를 검출한다.
- `cv2.bilateralFliter()`를 이용하여 이미지의 노이즈를 제거하면서 edge를 보존한다.
- `cv2.bitwise_and()`를 이용하여 edge 이미지와 카툰 스타일로 필터링된 이미지를 합성한다. 

### 적용 예
**잘된 예시**
<table>
  <th>원본</th>
  <th>변환 후</th>
  <tr>
    <td><img src="/image/good_sample1.jpg" height="200"/></td>
    <td><img src="https://github.com/Jisu0528/CartoonifyTool/assets/71203375/c27c1f31-5afa-4b28-a3e3-32c1d5d629bb" height="200"/></td>
  </tr>
    <tr>
    <td><img src="/image/good_sample2.jpg" height="200"/></td>
    <td><img src="https://github.com/Jisu0528/CartoonifyTool/assets/71203375/27655aaf-4d2f-428f-b70a-9f42510dc058" height="200"/></td>
  </tr>
    <tr>
    <td><img src="https://github.com/Jisu0528/CartoonifyTool/assets/71203375/60cb5218-8f48-4580-be13-0bc6d09ddf16" height="200"/></td>
    <td><img src="https://github.com/Jisu0528/CartoonifyTool/assets/71203375/7d798941-b415-43de-a20f-c9774f0557f7" height="200"/></td>
  </tr>
</table>

**잘 안된 예시**
<table>
  <th>원본</th>
  <th>변환 후</th>
  <tr>
    <td><img src="/image/bad_sample1.jpg" height="200"/></td>
    <td><img src="https://github.com/Jisu0528/CartoonifyTool/assets/71203375/1f20e25a-0c90-4325-ba35-a9135b3254e3" height="200"/></td>
  </tr>
    <tr>
    <td><img src="/image/bad_sample2.jpg" height="200"/></td>
    <td><img src="https://github.com/Jisu0528/CartoonifyTool/assets/71203375/b98a1f0c-f3e5-47aa-8123-b973ca8330c6" height="200"/></td>
  </tr>
    <tr>
    <td><img src="https://github.com/Jisu0528/CartoonifyTool/assets/71203375/de78ea5b-a4a4-460b-9217-786f2207679a" height="200"/></td>
    <td><img src="https://github.com/Jisu0528/CartoonifyTool/assets/71203375/0b211542-c650-4f74-8e13-97001d3a341e" height="200"/></td>
  </tr>
</table>

### 한계
- 배경이나 이미지의 안의 요소가 큰 것은 필터 적용이 잘된다.
- 하지만, 동물의 털 표현이나 얇은 글씨, 주변과 색 차이가 크지 않은 이미지는 필터가 잘 적용되지 않는다.
- 물가의 윤슬이나 자잘한 패턴들은 너무 자세히 표현되어 오히려 알아보기 힘들다.
