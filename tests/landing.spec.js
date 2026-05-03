import { test, expect } from '@playwright/test';

test.describe('FC Global Group Landing Page', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('has correct title', async ({ page }) => {
    await expect(page).toHaveTitle(/FC Global Group/);
  });

  test('navigation links are visible', async ({ page }) => {
    await expect(page.getByRole('link', { name: /About/i })).toBeVisible();
    await expect(page.getByRole('link', { name: /Process/i })).toBeVisible();
    await expect(page.getByRole('link', { name: /Become a Supplier/i })).toBeVisible();
  });

  test('logo is visible', async ({ page }) => {
    await expect(page.locator('.nav-logo')).toBeVisible();
  });

  test('page loads without console errors', async ({ page }) => {
    const errors = [];
    page.on('console', msg => {
      if (msg.type() === 'error') errors.push(msg.text());
    });
    await page.goto('/');
    expect(errors).toHaveLength(0);
  });

  test('is responsive on mobile', async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 812 });
    await expect(page.locator('.nav')).toBeVisible();
  });

  test('screenshot of landing page', async ({ page }) => {
    await expect(page).toHaveScreenshot('landing-full.png', { fullPage: true });
  });
});
