import styled from 'styled-components';

const Center = styled.header`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
`;

function Index() {
  return (
    <Center>
      <a href="/docs">
        <img src="https://assets.stickpng.com/thumbs/5c9226c6598da1028f26c5af.png" alt="Doki-Doki!" />
      </a>
      Doki-Doki!
      <br />
      <a href="/docs">(/docs)</a>
    </Center>
  );
}

export default Index;
