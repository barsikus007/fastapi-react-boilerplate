import { useState } from 'react';
import styled from '@emotion/styled';

import viteLogo from '/favicon.svg';

import reactLogo from '~/assets/react.svg';
import '~/App.css';

const Center = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: 1.5vmin;
`;

function Index() {
  const [count, setCount] = useState(0);

  return (
    <Center>
      <a href="/docs">
        <img
          src="https://static.wikia.nocookie.net/logopedia/images/a/ac/Doki_Doki_Literature_Club_Logo.png"
          alt="Doki-Doki!"
        />
        <div>Doki-Doki!</div>
      </a>
      <hr />
      <div>
        <div>
          <a href="https://vitejs.dev" target="_blank" rel="noreferrer">
            <img src={viteLogo} className="logo" alt="Vite logo" />
          </a>
          <a href="https://react.dev" target="_blank" rel="noreferrer">
            <img src={reactLogo} className="logo react" alt="React logo" />
          </a>
        </div>
        <h1>Vite + React</h1>
        <div className="card">
          <button type="button" onClick={() => setCount((cnt) => cnt + 1)}>
            count is {count}
          </button>
          <p>
            Edit <code>src/App.tsx</code> and save to test HMR
          </p>
        </div>
        <p className="read-the-docs">
          Click on the Vite and React logos to learn more
        </p>
      </div>
    </Center>
  );
}

export default Index;
