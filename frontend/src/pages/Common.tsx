import { Outlet } from '@tanstack/react-router';

import Navbar from '~/components/Navbar';

function Common() {
  return (
    <>
      <Navbar />
      <Outlet />
    </>
  );
}

export default Common;
