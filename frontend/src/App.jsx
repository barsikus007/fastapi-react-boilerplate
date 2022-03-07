import React from 'react';
import styled from 'styled-components';

const Main = styled.div`
  text-align: center;
`;

const Header = styled.header`
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
`;

function App() {
  return (
    <Main>
      <Header>
        <p>Edit any file in src/ to reload.</p>
      </Header>
    </Main>
  );
}

export default App;
