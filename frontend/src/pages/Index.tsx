import { useState } from 'react'
import styled from '@emotion/styled';

import reactLogo from 'assets/react.svg'
import viteLogo from '/vite.svg'

const Center = styled.header`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
`;

function Index() {
  const [count, setCount] = useState(0)

  return (
    <Center>
      <a href="/docs">
        <img src="https://assets.stickpng.com/thumbs/5c9226c6598da1028f26c5af.png" alt="Doki-Doki!" />
      </a>
      Doki-Doki!
      <br />
      <a href="/docs">(/docs)</a>
      <hr/>
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
          <button onClick={() => setCount((count) => count + 1)}>
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
