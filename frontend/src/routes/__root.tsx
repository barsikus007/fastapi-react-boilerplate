import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import { createRootRoute, Outlet } from '@tanstack/react-router';
import { TanStackRouterDevtools } from '@tanstack/router-devtools';

import Navbar from '~/components/Navbar';

// eslint-disable-next-line import/prefer-default-export
export const Route = createRootRoute({
  component: () => (
    <>
      <Navbar />
      <Outlet />
      <ReactQueryDevtools />
      <TanStackRouterDevtools />
    </>
  ),
  notFoundComponent: () => <>Not Found</>,
});
